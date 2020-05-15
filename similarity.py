import sys
import scipy.io.wavfile
import numpy as np

def cos_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def exec_fft(filename):
    # 参考ページ
    # https://jorublog.site/python-voice-analysis/

    # ファイル読み込み
    rate, data = scipy.io.wavfile.read(filename)
    # ステレオはモノラルに変換
    if (data.ndim == 2):
        data = data[:, 0]

    #（振幅）の配列を作成
    data = data / 32768

    ##### 周波数成分を表示する #####
    #縦軸：dataを高速フーリエ変換する（時間領域から周波数領域に変換する）
    return np.abs(np.fft.fft(data))

args = sys.argv

if args[1] == 'none' or args[2] == 'none':
    print('command usage: `make sample TRAINING=$1 SAMPLE=$2` $1 and $2 are media filename without csv')
    print('sample: `make sample TRAINING=nansu SAMPLE=myvoice` -> calculate similarity nansu, your voice')
    exit(-1)

training = exec_fft('./media/' + args[1] + '.wav')
sample = exec_fft('./media/' + args[2] + '.wav')
target_len = min(len(training), len(sample))

similarity = cos_similarity(training[0:target_len - 1], sample[0:target_len - 1])
result = round(similarity * 100)

print(args[1] + 'さんと' + args[2] + 'さんの声の類似度は' + str(result) + '%です')
