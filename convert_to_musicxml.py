import re
import music21

def convert_abc_to_musicxml(abc_filename, output_filename, force_treble=True):
    with open(abc_filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 独自テンションカッコ表記 (+F,C) の除去
    clean_content = re.sub(r'"([^"]*?)\(.*?\)"', r'"\1"', content)
    
    s = music21.converter.parse(clean_content, format='abc')
    
    if force_treble:
        for p in s.parts:
            # ト音記号に明示指定
            p.insert(0, music21.clef.TrebleClef())
            for m in p.getElementsByClass('Measure'):
                clefs = list(m.getElementsByClass('Clef'))
                for c in clefs:
                    m.replace(c, music21.clef.TrebleClef())
    
    s.write('musicxml', fp=output_filename)
    print(f"Successfully generated {output_filename}")

if __name__ == '__main__':
    convert_abc_to_musicxml('jazz_16m.abc', 'jazz_16m.musicxml', force_treble=True)
    convert_abc_to_musicxml('jazz.abc', 'jazz.musicxml', force_treble=True)
    convert_abc_to_musicxml('original.abc', 'original.musicxml', force_treble=True)
