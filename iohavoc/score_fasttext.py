import sys
import fasttext


PRETRAINED_MODEL_PATH = './lid.176.bin'

if __name__ == '__main__':

    if(len(sys.argv) < 2):
        print("Usage: python score_fasttext.py [a-sentence]\n")
        exit(1)

    model = fasttext.load_model(PRETRAINED_MODEL_PATH)
    sentence = sys.argv[1]
    
    sentences = [sentence]
    predictions = model.predict(sentences)
    print(predictions)
