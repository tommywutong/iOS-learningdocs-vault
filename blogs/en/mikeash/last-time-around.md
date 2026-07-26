---
title: Last time around
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2012-10-12-obtaining-and-interpreting-audio-data.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d0b2d6a41b53cf54'
translated: false
---

> 原文：[Last time around](https://www.mikeash.com/pyblog/friday-qa-2012-10-12-obtaining-and-interpreting-audio-data.html)　·　mikeash.com Friday Q&A

Posted at 2012-10-12 13:20 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2012-10-26: Fourier Transforms and FFTs](https://www.mikeash.com/pyblog/friday-qa-2012-10-26-fourier-transforms-and-ffts.html)  
Previous article: [Friday Q&A 2012-09-28: Optimizing Flood Fill](https://www.mikeash.com/pyblog/friday-qa-2012-09-28-optimizing-flood-fill.html)  
Tags: [audio](https://www.mikeash.com/pyblog/?tag=audio) [coreaudio](https://www.mikeash.com/pyblog/?tag=coreaudio) [fridayqa](https://www.mikeash.com/pyblog/?tag=fridayqa)

Friday Q&A 2012-10-12: Obtaining and Interpreting Audio Data

by [Mike Ash](https://www.mikeash.com/)

**Theory**  
Before we even get to the question of how computers represent sound, we first need to have an idea of just what sound _is_, physically. Ultimately, sound is variation in pressure in a medium, usually air, over time.

That variation can be represented as a function of pressure over time. However, the variations are small. If the function represents absolute pressure, then the variations made by the sound are nearly indistinguishable. If you graphed the function, you'd just see a flat line.

Better, then, to represent the sound as a function of pressure over time relative to the normal, undisturbed pressure. The range of the function will vary a lot depending on many different factors, so while we're at it, let's just normalize it to be between -1 and 1. Do this, and you get a nice waveform, as can be seen in just about any audio editor.

Computers can't represent arbitrary continuous functions, so it has to be discretized somehow. Rather than try to represent every point on the function, the computer simply samples it occasionally. How frequently it gathers those samples is called the _sample rate_. The [Nyquist sampling theorem](http://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem) says that a signal sampled at a given rate can represent frequencies up to one half that rate. For example, sampling sound at a rate of 44100 samples/second, or 44.1kHz, allows representing sounds with frequencies up to 22.05kHz, near the top end of the range of human hearing. Because of this, the 44.1kHz sample rate is probably the most common audio sample rate out there.

The value of each sample also has to be discretized, since computers can't represent arbitrary real numbers with infinite precision. Typically, each sample is stored as a signed, 16-bit integer, where the 16-bit integer range of [-32768, 32767] is mapped onto the conceptual sample range of [-1, 1]. For more fidelity, 24-bit values can be used, or for more compact storage, 8-bit values can be used.

Floating point is also a common format. This allows direct use of the normalized [1, -1] range, and good precision. Modern CPUs are fast with floating point, so performance is good, and the data is convenient to work with in code.

This system of representing audio using a series of samples taken at intervals is called pulse-code modulation, or PCM. "PCM" is often used to refer to this representation of "raw" audio, in contrast to various encodings like MP3 or AAC.

Probably the most common digital audio representation out there is 44.1kHz, 16-bit audio. This is what CDs hold, and most digital music files. 44.1kHz is enough to represent sounds up to the maximum frequency most people can hear, and 16 bits is generally granular enough to not produce audible noise or distortion, at least for most situations.

On Apple devices, 32-bit floats are the most common in-memory format for audio, since they can faithfully represent the full range of 24-bit integers, and are convenient to work with.

**A Quick Note on Floating Point**  
Using a floating-point number to represent only values between -1 and 1 may sound wasteful. After all, a 32-bit `float` can represent values between -3.4×1038 and 3.4×1038. Audio uses only a tiny fraction of that range.

It turns out, however, that restricting the range to [-1, 1] only wastes one bit out of the 32 available. In effect, it's being used as a 31-bit number stored in 32 bits of memory, which doesn't sound so bad at all. This is because of how floating point numbers are stored.

The short version is that `float`s are represented in the form m×2e, where `m` and `e` are stored in the number, along with one bit to indicate the sign. For a 32-bit `float`, the exponent (`e`) can range from -128 to 127. Values with exponents in the range [-128, -1] represent the range between -1 and 1. That range restriction simply cuts the exponent's range in half, which equates to restricting only a single bit from its value.

For more details on the floating-point representation, see [my previous article on floating point arithmetic](https://www.mikeash.com/pyblog/friday-qa-2011-01-04-practical-floating-point.html).

**Stereo**  
You may have noticed that most people have two ears. Because of this, sound recorded as two separate streams sounds nicer to most people than a single stream. Conceptually, this audio can be thought of as two separate functions of pressure over time.

To represent stereo sound in data, those two functions have to be represented simultaneously. The most common way is to simply interleave the two channels, so that the first value in a buffer would be the left channel, the second value the right channel, then left again, etc. In memory, it would look like:

```
    LRLRLRLRLRLRLRLRLR
```

It's also possible to simply use two completely different buffers, which just looks like:

```
    buffer 1: LLLLLLLLLL
    buffer 2: RRRRRRRRRR
```

Deinterleaved data like this can be more convenient to work with, but the interleaved representation is more commonly used simply because it keeps everything in one place.

**Obtaining Audio Data**  
There is no audio equivalent to Cocoa's `NSImage` class. The `NSSound` class may seem promising, but it's _extremely_ limited and provides no way to extract the underlying audio data.

Instead, I'll drop down to Core Audio, which excels at this kind of thing. It's not the nicest API in the world, but it's entirely capable. I believe the newer AV Foundation APIs are also capable of extracting raw audio data, but for a basic task like this, Core Audio does just fine.

The [Extended Audio File Services API](https://developer.apple.com/library/mac/#documentation/MusicAudio/Reference/ExtendedAudioFileServicesReference/Reference/reference.html) does exactly this. Given a file, it produces the raw audio data contained within.

The first thing to do is to create an `ExtAudioFileRef` pointing at the file we're interested in. The `ExtAudioFileOpenURL` function takes a `CFURLRef` and creates an audio file object for it. It returns an error value, with the audio file object returned by reference in one of the parameters:

```
    NSURL *urlToFile = ...;
    ExtAudioFileRef af = NULL;
    OSStatus err = ExtAudioFileOpenURL((__bridge CFURLRef)urlToFile, &af);
    if(err != noErr)
        // Handle the error here
```

It's important to check errors! Code like this is really easy to mess up, and if you write code that ignores errors, it can add hours to your debugging for no good reason. Always check the error from any function that returns them.

The next step is to tell the audio file object what kind of in-memory format we want for the audio. This is done using an `AudioStreamBasicDescription`, or ASBD. This is a structure which contains fields for the sample rate, number of channels, etc. Here is an ASBD that asks for 44.1kHz, mono, PCM audio using `float` to store the samples:

```
    AudioStreamBasicDescription clientASBD = {
        .mSampleRate = 44100,
        .mFormatID = kAudioFormatLinearPCM,
        .mFormatFlags = kAudioFormatFlagsNativeFloatPacked,
        .mBitsPerChannel = sizeof(float) * CHAR_BIT,
        .mChannelsPerFrame = 1,
        .mFramesPerPacket = 1,
        .mBytesPerFrame = sizeof(float),
        .mBytesPerPacket = sizeof(float)
    };
```

This structure contains what appears to be redundant information, in the form of the channels and bytes per frame/packet. These fields exist for the benefit of non-PCM formats, and because the ASBD `struct` is used in many different situations. To understand the meaning of these fields, here are some quick definitions:

- a single number representing the value of one audio channel at one point in time.
- a group of one or more samples, with one sample for each channel, representing the audio on all channels at a single point on time.
- a group of one or more frames, representing the audio format's smallest encoding unit, and the audio for all channels across a short amount of time.

Many audio formats use packets that are considerably longer than a single frame. MP3, for example, uses packets of 1152 frames, which are the basic atomic unit of an MP3 stream. PCM audio is just a series of samples, so it can be divided down to the individual frame, and it really has no packet size at all. For the ASBD's purpose, the packet size is equal to the frame size.

Note that the above definitions are a bit loose, and people often use these terms in different ways. However, these definitions are how Core Audio uses the words, which is what counts when we're writing code for that API!

With the structure filled out, the code uses it to tell the audio file object what kind of data we want:

```
    err = ExtAudioFileSetProperty(af, kExtAudioFileProperty_ClientDataFormat, sizeof(clientASBD), &clientASBD);
    if(err != noErr)
        // Handle the error
```

Once again, error handling is important. It's easy to build an ASBD that Core Audio doesn't like, and catching that error early will save a lot of pain.

You won't always want to specify every detail of the audio format like this. For many purposes, you'll want to use the sample rate of the data in the file rather than specifying one and having Core Audio resample the audio if necessary. Likewise, you'll often want to use the number of channels present in the file rather than simply requesting or forcing a certain number of channels. This can be done simply by calling `ExtAudioFileGetProperty` and getting the `kExtAudioFileProperty_FileDataFormat` property. This will return an ASBD describing the file's format, and the file's sample rate and number of channels can easily be extracted from that.

**Reading**  
With the audio file object set up, it's time to start reading data from it.

Since audio data is a stream, and audio files can be huge, it's common to read from them only a piece at a time and move on, rather than trying to read the entire thing into memory at once. Audio data can be pretty big, especially once decoded into memory. A typical 1MB MP3 will decode to about 10MB in memory using the audio format specified in this code, and twice that for stereo.

To that end, we'll define a fixed-size buffer to read audio data into:

```
    int bufferFrames = 4096;
    float data[bufferFrames];
```

For multi-channel audio, the array size needs to be multiplied by the number of channels. We're just reading mono, though, so the array size is equal to the number of frames.

The function to actually read an audio file takes an `AudioBufferList`, which is just a structure of `AudioBuffer` structures. This code constructs an `AudioBuffer` for the above array, and an `AudioBufferList` containing a single entry for that buffer:

```
    AudioBuffer buffer = {
        .mNumberChannels = 1,
        .mDataByteSize = sizeof(data),
        .mData = data
    };

    AudioBufferList bufferList;
    bufferList.mNumberBuffers = 1;
    bufferList.mBuffers[0] = buffer;
```

With that in place, it's time to actually read the data. The read function takes an odd shortcut, where it takes a pointer to a number of frames to read, and then sets that variable to the number of frames actually read. It returns an error just like the rest of these functions:

```
    UInt32 ioFrames = bufferFrames; /* Request reading 4096 frames. */
    err = ExtAudioFileRead(af, &ioFrames, &bufferList);
    if(err != noErr)
        // Handle the error here
```

At this point, `ioFrames` contains the number of frames actually read. The data itself can be found in `data[0]`, `data[1]`, ..., `data[ioFrames - 1]`.

To read the entire file, simply run the above in a loop until `ioFrames` comes out `0`, signaling the end of the file.

Once you're done, don't forget to clean up the audio file object:

```
    if(af)
    {
        err = ExtAudioFileDispose(af);
        if(err != noErr)
            // How do you handle an error from a dispose function?
    }
```

**Interpreting the Data**  
With the audio data in a buffer, the program can read elements out of the buffer to get audio samples. However, interpreting that data can get tricky. Unlike images, where a single pixel has meaning, a single audio sample has essentially no meaning on its own. Audio is fundamentally a result of change over time, so looking at a single sample of, say, `0.5` doesn't tell us anything. Contrast this with an image, where a single pixel with an RGB value of `(255, 0, 0)` tells us that this pixel is red, even if it doesn't tell us anything about the rest of the image.

Interpreting audio data can get extremely difficult, but we can at least cover some basics here.

The sample values are simply deviations from the center. If you wanted to render a visual representation of the waveform, for example, you could simply transform the sample values to vertical offsets from the centerline of your waveform view. [There can be a lot more to it](http://supermegaultragroovy.com/2009/10/06/drawing-waveforms/), but for the basic idea, you can simply generate `(x, y)` values like so:

```
    x = sampleNumber;
    y = data[sampleNumber] * viewHeight / 2 + viewHeight / 2;
```

It can be interesting and useful to figure out how loud a particular piece of audio is. Loudness is typically measured in decibels, which is a logarithmic scale. It's calculated using the base 10 logarithm of a ratio of the audio's power with a reference power level. The pure logarithm produces a value in _bels_, and to obtain decibels, simply multiply that number by 10. The power level of a piece of audio is proportional to the square of the amplitude, and the amplitude is exactly what the individual audio samples describe.

To compute the total power level of a piece of audio, simply average the squares of all the samples:

```
    float accumulator = 0;
    for(int i = 0; i < frames; i++)
        accumulator += data[i] * data[i];
    float power = accumulator / frames;
```

For computer audio, the reference power level is typically `1.0`, which is the loudest possible. To compute decibels, take the base-10 logarithm of the computed power divided by the reference power then multiply the result by 10. Dividing by `1.0` does nothing, so it's ommitted from the calculation:

```
    float decibels = 10 * log10f(power);
```

Mathematically astute readers will notice that squaring the amplitude when calculating the power is equivalent so simply calculating `20 * log10f(averageAmplitude)`, which can simply things slightly. However, don't forget to take the absolute value of the amplitudes when calculating the averages, because otherwise the samples are likely to cancel each other out.

The resulting decibel value is _negative_, which may be confusing if you're used to seeing decibels written as a positive value. It's important to understand that decibels are a _relative_ measure, and need some sort of reference power or amplitude to be meaningful. When audible sound levels are expressed in decibels, the reference level is a standard number which is roughly the quietest sound that a normal human can hear. If a sound is described as 10dB, that means that it's 10 times more powerful than the quietest perceptible sound. 20dB means that it's 100 times more powerful, etc.

For computer audio, the maximum possible output power is typically used as the reference level, because there is no meaningful minimum level to compare with. An audio file filled with zeros has zero output power, and attempting to compute a ratio with that would divide by zero. The result is that, when talking about computer audio, 0dB is the maximum level possible, and negative values are quieter. If audio is described as being at a level of -30dB, that means that it's 1000 times less powerful than this reference maximum value.

To adjust the volume of audio, simply multiply each sample by a fixed gain. The gain can be calculated from a desired change in decibels by reversing the formula above. For example, to achieve a volume increase of 30dB, multiply the power by `1000`, which is equivalent to a gain of `sqrt(1000)`:

```
    float decibelsAdjust = ...;
    float gain = pow(10, decibelsAdjust / 20);
    for(int i = 0; i < frames; i++)
        data[i] *= gain;
```

Note that this works equally well for negative values, which cause a decrease in volume by the specified number of decibels.

**Writing Audio Out**  
You've done a volume adjustment or maybe some other manipulation to the audio data, and you want to get audio back out of your program. The `ExtAudioFile` APIs make this easy.

The first thing to do is to create a new audio file and a new audio file object all at once. This is done by calling `ExtAudioFileCreateWithURL`:

```
        ExtAudioFileRef outAF = NULL;
        err = ExtAudioFileCreateWithURL((__bridge CFURLRef)outURL, kAudioFileCAFType, &clientASBD, NULL, kAudioFileFlags_EraseFile, &outAF);
        if(err != noErr)
            // You should know what to do here by now
```

This function takes several more parameters than `ExtAudioFileOpenURL`. The first parameter is a URL to the file to create. The second one is the file type to create. `ExtAudioFile` [supports many different formats](https://developer.apple.com/library/mac/#documentation/MusicAudio/Reference/AudioFileConvertRef/Reference/reference.html#//apple_ref/c/tdef/AudioFileTypeID). I chose CAF, as it's a simple format that stores raw PCM samples with a minimum of fuss, and was designed specifically to be nice to use with Core Audio.

The third parameter is the format that will be used for audio within the file. By default, it's also used as the in-memory audio format. For convenience, I'm using the same format as the in-memory format specified earlier. In more realistic situations, you'd likely want to specify an in-file format that's more compact or useful (e.g. 16-bit integer), then use the `kExtAudioFileProperty_ClientDataFormat` property to specify the in-memory format, just as we did when reading.

The fourth parameter is an audio channel layout struct, which is optional and only needed for more advanced uses. For this, I leave it NULl.

The fifth parameter tells the system what to do if the file already exists. I want it to erase any existing file and make a new one, so I pass `kAudioFileFlags_EraseFile`. The last parameter is a pointer to where the newly created audio file object will be stored.

Writing audio to this file is almost exactly the same as reading it. You need a buffer of data, an `AudioBuffer` struct, and an `AudioBufferList`. Then simply call `ExtAudioFileWrite`:

```
    err = ExtAudioFileWrite(outAF, ioFrames, &bufferList);
    if(err != noErr)
        // Guess what
```

If you stick this into the same loop as the audio reading code from above, you'll get a program that creates a new CAF audio file using the contents from an existing audio file. If you modify the contents of the `data` buffer before writing, the new audio file will contain your modified contents.

**Conclusion**  
The world of audio can be strange and mysterious, but the basics are pretty simple. The `ExtAudioFile` APIs make it easy, relatively speaking, to get at the audio data of a file. That audio data is represented as a series of samples in memory between -1 and 1. If you want to make changes and build a new file, `ExtAudioFile` makes it easy to write the new audio back out to disk.

That's it for today. You probably know by now that Friday Q&A is driven by reader submissions, so as always, please [send in your ideas for topics](mailto:mike@mikeash.com) if you have a subject you'd like to see covered here.

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
