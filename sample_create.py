import sys
import soundfile as sf
import librosa
from librosa.core import istft
import csv

args = sys.argv

if args[1] == 'none':
    print('command usage: `make sample SAMPLE_FILE=$1` $1 is media filename without csv')
    print('sample: `make sample SAMPLE_FILE=nansu` -> create sample nansu.wav')
    exit(-1)

print(args[1] + 'mfcc start')

x, fs = sf.read('./media/' + args[1] + '.wav')
mfccs = librosa.feature.mfcc(istft(x), sr=fs)

# 具体的に何をしているかはこのあたりが詳しいです
# https://qiita.com/martin-d28jp-love/items/34161f2facb80edd999f
# https://qiita.com/tmtakashi_dist/items/eecb705ea48260db0b62#librosa%E3%81%A7mfcc%E3%82%92%E6%B1%82%E3%82%81%E3%82%8B
# やらんとしていることは入力された音声ファイルをメル尺度に落とし込み, 1フレームずつの特徴量を取得する, ということです

# DCT したあとで取得する係数の次元(デフォルト20), サンプリングレートxオーディオファイルの長さ（= 全フレーム数）/ STFTスライドサイズ(デフォルト512)
print(mfccs.shape)

with open('sample/' + args[1] +'.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(mfccs)
