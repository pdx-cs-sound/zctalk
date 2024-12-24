import argparse, sys
import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wave

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--wavout")
ap.add_argument("wavfile")
args = ap.parse_args()

rate, data = wave.read(args.wavfile)
was_unsigned = data.dtype == np.uint8
data = data.astype(np.float32) / np.iinfo(data.dtype).max
if was_unsigned:
    data -= 0.5
    
if data.ndim == 2:
    data = data.dot(np.array([0.5, 0.5]))
elif data.ndim > 2:
    print("too many channels", file=sys.stderr)
    exit(1)
assert data.ndim == 1

zc = np.sign(data)
for i in range(len(zc)):
    if zc[i] == 0.0:
        zc[i] = 1.0

if args.wavout:
    wave.write(args.wavout, rate, zc)
else:
    sd.play(zc, samplerate=rate, blocking=True)
