---
title: last post in this mini-series
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-10-26-fourier-transforms-and-ffts.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:90acbcc272f726cd'
translated: false
---

> 原文：[last post in this mini-series](https://www.mikeash.com/pyblog/friday-qa-2012-10-26-fourier-transforms-and-ffts.html)　·　mikeash.com Friday Q&A

Posted at 2012-10-26 13:25 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-11-02: Building the FFT](https://www.mikeash.com/pyblog/friday-qa-2012-11-02-building-the-fft.html)  
Previous article: [Friday Q&A 2012-10-12: Obtaining and Interpreting Audio Data](https://www.mikeash.com/pyblog/friday-qa-2012-10-12-obtaining-and-interpreting-audio-data.html)  
Tags: [audio](https://www.mikeash.com/pyblog/?tag=audio) [coreaudio](https://www.mikeash.com/pyblog/?tag=coreaudio) [fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa)

Friday Q&A 2012-10-26: Fourier Transforms and FFTs

by [Mike Ash](https://www.mikeash.com/)

**Theory**  
Humans largely experience audio in the frequency domain. If you plot the waveform of a guitar chord, it's a messy thing, yet we experience it as a combination of individual notes, or frequencies. Analyzing audio by frequencies is tremendously useful, not in the least because it matches up much better with how we experience sound. Computers generally consider audio to be a collection of individual samples, while people consider it to be a collection of individual frequencies. Going from individual samples to frequencies is, essentially, the Fourier transform.

Imagine that you have an audio waveform that you think has a 200Hz frequency component in it. However, you're not sure, and you don't know how loud it is. How can you check?

First, let's slow the audio down by a factor of 1000 so this 200Hz frequency is on a more human timescale. With that factor of 1000 slowdown, a 200Hz frequency is a waveform that goes up, down, and back to the starting point every five seconds. The frequency is now far too low to hear, but easy to see, and convenient to analyze. This is a bit like how computers deal with audio, since they're fast and can devote a lot of attention to every individual audio sample.

The mystery audio has a complex waveform which goes up and down in what seems like a nearly random fashion. But you suspect this 200Hz pattern, or a consistent up and down every five seconds, embedded in the rest of the action.

You could check for this by just tapping out a beat once every five seconds, and checking where the waveform is at each beat. If it's consistently up, even after you've done this for a couple of minutes, then there's clearly some consistent once-every-five-seconds signal in there.

There's a problem with this, though. The 200Hz frequency crosses zero on its way between the hills and valleys of the wave. What if your beat happens to line up with those zero crossings? You'll get nothing, even though the signal is present. You'd have to repeat this simple analysis several times to make sure you didn't end up out of phase with the signal.

It would be better to have a single analysis that works with any phase, and has no chance of consistently hitting zero crossings. You want something that lines up with this once-every-five-seconds period, but still operates constantly. In short, you want a circle.

Get the waveform going so you can see it. It's moving up, down, back up, etc. Now, imagine you stand up and start turning in place. Make one complete turn once every five seconds.

Now start walking. Adjust your speed to match the waveform at any particular moment. If the wave is high, walk forward quickly. If it's near zero, walk slowly. If it's at zero, stop. When it's below zero, walk backwards. And keep turning at a rate of one complete turn every five seconds.

If you keep this up for a couple of minutes, you'll end up with a solid analysis of the 200Hz signal, or lack thereof, in the audio you're analyzing. Because you're turning at a rate that exactly matches the frequency you're looking for, any audio at that frequency will consistently move you in a single direction. As you turn, the 200Hz wave will crest at exactly the same point around the turn each time, and you'll begin to wander away from where you started.

All the parts of the sound that aren't at 200Hz will move you around too, of course. But because they don't match the speed at which you turn, they end up getting spread out all along the circle, and the net result is to bring you back to the center. Only the 200Hz component will consistently move you away. How far away you get tells you how strong that component is. The direction you move in tells you where the wave started, or its phase.

Do this over and over again, and you can characterize the whole sound. For example, you might do this at 20Hz, 40Hz, 60Hz, 80Hz, 100Hz, etc., all the way up to 20,000Hz or so. At the end, you'll have completely mapped out the strength and phase of all of the frequency components of the sound. A sound can be thought of as a sum of various sine waves, or pure tones. Any sound, or indeed any signal at all, can be represented as a collection of sine waves with the right frequency and phase. By mapping out the frequencies in the sound, you build up the fundamental component sine waves it contains.

This map is the Fourier transform of the sound. You spin the sound around in a circle at different frequences and come up with all of its components, and get the Fourier transform. You've now gone from a collection of individual samples, which tell you very little, to a comprehensive map of the fundamental components of the audio, which tell you a lot. The Fourier transform is, essentially, what your ear does with incoming sound, and we fundamentally hear sound by frequencies, not samples, so it's a much better match for human perception.

You can also take the Fourier transform and reverse it to obtain the original audio. If you modify the transformed frequency components, that modification shows up in the original audio. This can be used to reduce or increase the volume of certain frequency components, or perform other interesting changes on the original audio.

The Fast Fourier Transform, or FFT, is pretty much what it implies. It's an algorithm for quickly computing the Fourier transform of a sequence of values. While FFT just refers to the algorithm, and Fourier transform is the actual result that it produces, FFT is often used pretty much interchangeably for both.

**Basic Implementation**  
Let's build a basic Fourier transform. The fundamental operation is the rotation procedure I described above, so let's build a function to perform that:

```
    COMPLEX Rotate(float *buf, int samples, float hz, float rate)
    {
```

`COMPLEX` is a data type defined in Apple's `vDSP` library that simply has two components, `real` and `imag`. The output of a Fourier transform is actually a sequence of complex numbers, which correspond to the two-dimensional result of the rotation procedure. The Fourier transform is actually defined in terms of [complex number exponents](http://en.wikipedia.org/wiki/Exponentiation#Complex_exponents_with_positive_real_bases), which conceptually maps to rotation in two dimensions.

The goal is to add all of the various impulses together, so we want `COMPLEX` variable to serve as an accumulator:

```
        COMPLEX result = { 0, 0 };
```

Then loop over all of the samples:

```
        for(int i = 0; i < samples; i++)
        {
```

We want to rotate to make a complete circle once every `rate / hz` samples. The following line computes the appropriate angle (in radians) for the current sample:

```
            float angle = i * hz * 2 * M_PI / rate;
```

Now we use that angle to compute the step to take. This is simply the value of `buf[i]`, rotated by `angle`, which is a simple bit of trigonometry:

```
            float real = buf[i] * cos(angle);
            float imag = buf[i] * sin(angle);
```

We then add that step into the accumulator, and continue with the loop:

```
            result.real += real;
            result.imag += imag;
        }
```

Once the loop is done, just return the accumulated result:

```
        return result;
    }
```

Note that, for reasons I don't fully understand, the results of this function are off by a factor of two and sometimes with inverted components compared to a reference FFT function's output. However, this still does fine in illustrating the principle and getting usable data out.

To perform a Fourier transform, we then just call `Rotate` repeatedly with different frequencies. Which frequencies? The lowest frequency the Fourier transform can extract (aside from zero) is equal to the sample rate divided by the number of samples, which is the frequency where one complete waveform can fit within the samples given. The transform produces `samples / 2` bins of output, where each bin is a complex number. (Technically, it produces `samples` bins of output, but with real-valued input, the output is symmetric and half of it can be neglected.) The first bin (bin `0`) corresponds to a frequency of 0Hz, also called the DC offset. The second bin corresponds to `rate / samples`Hz. The third bin corresponds to `2 * rate / samples`Hz, and so on like that, with each bin's frequency equal to `i * rate / samples`.

Given that, here is a quick routine to compute the Fourier transform of a collection of samples:

```
    int samples = ...;
    float *buf = ...;

    COMPLEX result[samples / 2];
    for(int i = 0; i < samples / 2; i++)
        result[i] = Rotate(buf, samples, i * rate / samples, rate);
```

This is great code to play with and makes it a lot easier to understand what's happening when you generate a Fourier transform. However, it's impractical for any real use, as it's _far_ too slow. For speed, we want an FFT implementation, and Apple has a good one.

**vDSP FFT**  
Apple's vDSP provides optimized digital signal processing routines, including a full suite of FFT functions. For those wondering, "DSP" stands for digital signal processing, and the "v" stands for vector, indicating that it will use your CPU's vector unit whenever possible for best speed.

The FFT functions need some initial setup done which can be reused across multiple calls. To reduce overhead, you perform the setup separately, then use the resulting data as many times as you want before destroying it. The `vDSP_create_fftsetup` function handles this. It takes the maximum amount of data you want to work with, and a radix. The data is specified as a power of two, so to specify that you want to work with `1024` samples at a time, pass in `10`. For the radix, pass `kFFTRadix2`. vDSP supports radix values of `3` and `5`, which allows it to work with data whose length is a multiple of `3` or `5`, but this is not generally useful. Powers of two are convenient in programming, so we'll stick with that. Here is the code to set up the vDSP FFT for `1024` samples:

```
    int bufferFrames = 1024;
    int bufferlog2 = round(log2(bufferFrames));
    FFTSetup fftSetup = vDSP_create_fftsetup(bufferlog2, kFFTRadix2);
```

Next, the input data has to be transformed into the arrangement that vDSP expects. The output is provided as two distinct arrays, one for the real parts and one for the imaginary parts. To keep things simple (for vDSP, not for us), the input is also split into two arrays, and the FFT performed in place. Here are the two arrays, plus a little structure to hold them:

```
    float outReal[bufferFrames / 2];
    float outImaginary[bufferFrames / 2];
    COMPLEX_SPLIT out = { .realp = outReal, .imagp = outImaginary };
```

The input buffer needs to be transformed so that all of the even-numbered elements go into `outReal`, and all of the odd-numbered elements go into `outImaginary`. vDSP provides a convenient function to do this for us:

```
    vDSP_ctoz((COMPLEX *)data, 2, &out, 1, bufferFrames / 2);
```

This function is intended to take an array of complex numbers as the input (thus the cast to `COMPLEX *`) and produce a split array of the output. By squinting and pretending that the input data is actually complex numbers, this accomplishes the even/odd split that we wanted.

Performing the FFT itself is actually pretty simple. Just call `vDSP_fft_zrip`, give it the `fftSetup` object, the array to work on, the stride (how many elements to move forward for each iteration, usually `1`) the data length (as a power of two), and specify that you want a forward FFT:

```
    vDSP_fft_zrip(fftSetup, &out, 1, bufferlog2, FFT_FORWARD);
```

The same function can do both forward (from standard PCM audio to frequencies) and inverse (from frequencies back to raw audio) transforms, which is why this call has to specify `FFT_FORWARD`.

At this point, outReal and outImaginary contain the real and imaginary components of the FFT output. Their magnitude (`sqrt(real * real + imag * imag)`) tells you how much energy is in a particular frequency bin. Note that the magnitude can be quite high even when the input is restricted to a range of [-1, 1], since very pure tones will deposit all of their energy into a single bin.

Analyzing the magnitudes can produce for interesting visualizations. Since human hearing works similar to the FFT, the result corresponds much more with how we hear audio than a simple waveform generated from the PCM data.

The output has one odd feature. Index `0` in the output would normally contain the DC offset, which is always a pure real value with a zero imaginary component. Index `bufferFrames / 2` contains the Nyquist frequency, which _also_ is a pure real value with zero imaginary component. To save a bit of space, vDSP squashes these two together at index `0`. `outReal[0]` contains the DC offset, and `outImaginary[0]` contains the Nyquist component.

The FFT output can be altered to, for example, reduce or increase the strength of certain frequencies. You can then transform the result back into raw audio data, which will reflect the alterations. The alterations are just a matter of twiddling around with `outReal` and `outImaginary`. For example, if you go through and set the first 1/4th of each array to`0`, you'll remove all of the low frequency components from the sound.

To reverse the transform, just call `vDSP_fft_zrip` again with `FFT_INVERSE`:

```
    vDSP_fft_zrip(fftSetup, &out, 1, bufferlog2, FFT_INVERSE);
```

Then de-interleave the data, using `vDSP_ztoc` which just does the opposite of the `vDSP_ctoz` call useb previously:

```
    float outData[bufferFrames];
    vDSP_ztoc(&out, 1, (COMPLEX *)outData, 2, bufferFrames / 2);
```

The result of this inverse transformation, for reasons I don't fully understand, comes out multiplied by a factor of `bufferFrames * 2`. This needs to be removed before treating the result as audio data, unless you like frightening everybody in the restaurant with the sudden blast of sound from your MacBook (ask me how I know this).

A simple `for` loop would do for this, but the `cblas_sscal` function will do it faster and nearly as easily. This function is found in `Accelerate.framework`, the umbrella framework which also contains vDSP and a bunch of other nifty functionality that I highly recommend you check out. This code simply multiplies every element in the output data by `1 / (bufferFrames * 2)` to renormalize it:

```
    cblas_sscal(bufferFrames, 1.0 / (bufferFrames * 2), outData, 1);
```

At this point, `outData` now contains the audio that was originally in `data`, except with whatever modifications made to the FFT data in between.

**Conclusion**  
Fourier transforms are a deep and complicated subject, and this article barely scratches the surface. The interpretation and modification of the resulting data can get about as complex as you care to go. Just performing and understanding the basics of an FFT can be tough, though, and I hope I've jumped you over that initial hurdle today.

It's time for everybody to go home now. But before you go, please don't forget to visit the suggestion box. Friday Q&A is driven by reader suggestions, in case you haven't already picked that up, so please [let me know](mailto:mike@mikeash.com) if you have an idea for a topic that you'd like to see covered in a future article.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
