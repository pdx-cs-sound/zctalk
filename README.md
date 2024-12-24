# zctalk: Zero-Crossing Sound
Bart Massey 2024

This code demonstrates generating barely legible sound on
"bang-bang" speakers — speakers that are always either
full-forward or full-back. The technique is to clip the heck
out of the sound, so that the zero-crossings hit where they
should. This turns out to preserve the frequency content but
not its amplitude (whatever that means). The result is audio
that is so full of noise as to be painful, but in which the
original content can still be heard to an extent.

This is an old trick from the Apple II days in the 1970s: I
first heard it used for speech generation in the original
Castle Wolfenstein. It sounds better in German.

There are several parameters that can be played with to
perhaps slightly improve the quality: see the code for
details.

## License

This work is made available under the "MIT License". See the
file `LICENSE.txt` in this distribution for license terms.
