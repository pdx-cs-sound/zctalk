# zero-crossing sound stuff
# Bart Massey 2024

import argparse, sys
import numpy as np
import scipy.io.wavfile as wave
import scipy.signal as ss
import sounddevice as sd

ap = argparse.ArgumentParser()
ap.add_argument("-w", "--wavout")
ap.add_argument("--lowpass", type=float)
ap.add_argument("--highpass", type=float)
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

if args.lowpass:
    crit = args.lowpass * 2 / rate
    filt = ss.cheby2(16, 60, crit, output='sos')
    data = ss.sosfilt(filt, data)

if args.highpass:
    crit = args.highpass * 2 / rate
    filt = ss.cheby2(16, 60, crit, btype='highpass', output='sos')
    data = ss.sosfilt(filt, data)

zc = (data >= 0.0).astype(np.float32) - 0.5

if args.wavout:
    wave.write(args.wavout, rate, zc)
else:
    sd.play(zc, samplerate=rate, blocking=True)
