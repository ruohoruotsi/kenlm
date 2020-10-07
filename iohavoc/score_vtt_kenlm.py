import re
import sys
import kenlm


def test_kenlm(model):
    text = 'in the beginning was the word'
    print(model.score(text), model.perplexity(text))
    text = 'this is a sentence'
    print(model.score(text), model.perplexity(text))
    

def parse_vtt(vtt_filepath):

    tt_segments = []
    webvtt = open(vtt_filepath, 'r', encoding='utf-8')  # opens WebVTT file forcing UTF-8 encoding
    text_buffer = webvtt.read()

    regex = re.compile(r"""(^[0-9]{2}[:][0-9]{2}[:][0-9]{2}[.,][0-9]{3})  # match TC-IN in group1
                           [ ]-->[ ]                                       # VTT/SRT style TC-IN--TC-OUT separator
                           ([0-9]{2}[:][0-9]{2}[:][0-9]{2}[.,][0-9]{3})    # match TC-OUT n group2
                           (.*)\r?\n                                       # additional VTT info (like) alignment
                           ([\s\S]*?)\s*(?:(?:\r?\n){2}|\Z)                # subtitle_content """,
                       re.MULTILINE|re.VERBOSE)

    subtitle_match_count = 0
    for match in regex.finditer(text_buffer):
        subtitle_match_count += 1
        group1, group2, group3, group4 = match.groups()
        tc_in = group1.strip()
        tc_out = group2.strip()
        vtt_extra_info = group3
        subtitle_content = group4

        # print("Subtitle match count: %d" % subtitle_match_count)
        # print("TIMECODE IN".ljust(20), tc_in)
        # print("TIMECODE OUT".ljust(20), tc_out)
        # print("ALIGN".ljust(20), vtt_extra_info.strip())
        # print("SUBTITLE CONTENT".ljust(20), subtitle_content)
        tt_segments.append(subtitle_content.lower())

    return tt_segments



if __name__ == '__main__':
    
    if(len(sys.argv) < 2):
        print("Usage: python score_vtt_kenlm.py [path-to-a-VTT-file]\n")
        exit(1)

    vtt = sys.argv[1]
    model = kenlm.LanguageModel('bible.arpa')

    subtitles = parse_vtt(vtt)
    for sub in subtitles:    
        # print(str(model.perplexity(sub)) + "\t" + "\t" + sub )
        # print("{:.2f}".format(model.perplexity(sub)) + "\t" + "\t" + sub )
        print(sub + "\t" + "\t" + "{:.2f}".format(model.perplexity(sub)))
        # print(model.score(sub, bos=True, eos=True), model.perplexity(sub))

    print("\n\n")
    test_kenlm(model)
