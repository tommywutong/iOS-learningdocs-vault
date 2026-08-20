---
title: QuickTime Audio - Easy Frequency Level Metering with MovieAudio APIs
apple_id: DTS10003833
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2009-01-29'
source_url: https://developer.apple.com/library/archive/qa/qa1459/_index.html
archived_at: '2026-07-18T02:30:52.511900Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1459

# QuickTime Audio - Easy Frequency Level Metering with MovieAudio APIs

## Q:  How can I retrieve the frequency levels of an audio file or a QuickTime Movie and display them like iTunes or QuickTime Player does?

A: QuickTime 7 introduced a number of 'MovieAudio' APIs that now make performing tasks such as volume and frequency metering, adjusting gain, setting audio balance and mute very easy. While some of these APIs may duplicate existing functionality, the 'MovieAudio' APIs present a simpler, more consistent programmer interface and are now the preferred way to perform these tasks.

For example, to monitor frequency levels it is no longer necessary to drop down to the media handler level and use `MediaSetSoundEqualizerBands` and `MediaGetSoundEqualizerBandLevels`.

Given a QuickTime Movie, it's easy to perform frequency metering using two 'MovieAudio' APIs. First call `SetMovieAudioFrequencyMeteringNumBands` to configure frequency metering for a particular audio mix (see the [References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobtgmwugsbrfvke4vcbi4zq) section for a description of the available mixes), then call `GetMovieAudioFrequencyLevels` to retrieve the current frequency meter levels whenever you want them. The values are returned in a `QTAudioFrequencyLevels` structure you allocate according to the number of bands you would like to monitor.

`GetMovieAudioFrequencyLevels` is performing FFTs ([Fast Fourier Transform](http://mathworld.wolfram.com/FastFourierTransform.html)) to calculate the meter levels. The FFT window is proportional to the number of spectral bands you are interested in viewing:

- 1-4 bands -> 256-pt FFT
- 5-15 bands -> 512-pt FFT
- 16-128 bands -> 1024-pt FFT

__Listing 1__  Setting up frequency metering.

```swift
UInt32 numberOfBandLevels = 7; // increase this number for more frequency bands
UInt32 numberOfChannels = 2; // for StereoMix - if using DeviceMix,
                                 // you need to get the channel count of the device

QTAudioFrequencyLevels *freqResults = NULL;

...

// call this once per movie to establish metering
err = SetMovieAudioFrequencyMeteringNumBands(myMovie,
                                             kQTAudioMeter_StereoMix,
                                             &numberOfBandLevels);
if (err) goto bail;

freqResults = malloc(offsetof(QTAudioFrequencyLevels,
                              level[numberOfBandLevels * numberOfChannels]));
if (freqResults == NULL) {
    err = memFullErr;
    goto bail:
}

freqResults->numChannels = numberOfChannels;
freqResults->numFrequencyBands = numberOfBandLevels;

...
```


__Listing 2__  Getting the metered levels.

```swift
...

// call each time you are ready to display meter levels
if (freqResults != NULL) {
    err = GetMovieAudioFrequencyLevels(myMovie, kQTAudioMeter_StereoMix, freqResults);
    if (err) goto bail;

    for (i = 0; i < freqResults->numChannels; i++) {
        for (j = 0; j < freqResults->numFrequencyBands; j++) {
            // the frequency levels are Float32 values between 0. and 1.
            Float32 value = freqResults->level[(i *
                                                freqResults->numFrequencyBands) + j];

            // do something with the value
            ...
        }
    }
}

...
```


__Listing 3__  Retrieving the channel count when using `kQTAudioMeter_DeviceMix`.

```swift
 AudioChannelLayout *layout = NULL;
    UInt32 size = 0;
    UInt32 numChannels = 0;
    OSStatus err;

...

    // get the size of the device layout
    err = QTGetMoviePropertyInfo(theMovie, kQTPropertyClass_Audio,
                                 kQTAudioPropertyID_DeviceChannelLayout,
                                 NULL, &size, NULL);

    if (err || (0 == size)) goto bail;

    // allocate memory for the device layout
    layout = (AudioChannelLayout*)calloc(1, size);
    if (NULL == layout) {
        err = memFullErr;
        goto bail;
    }

    // get the device layout from the movie
    err = QTGetMovieProperty(theMovie, kQTPropertyClass_Audio,
                             kQTAudioPropertyID_DeviceChannelLayout,
                             size,
                             layout,
                             NULL);
    if (err) goto bail;

    // now get the number of channels
    numChannels = (layout->mChannelLayoutTag ==
                   kAudioChannelLayoutTag_UseChannelDescriptions) ?
                   layout->mNumberChannelDescriptions :
                   AudioChannelLayoutTag_GetNumberOfChannels(layout->mChannelLayoutTag);

    free(layout);

...
```



```
Movie Audio Mixes

Three constants define the mix of audio channels for frequency metering:

kQTAudioMeter_StereoMix - Meter a stereo (two-channel) mix of the enabled sound tracks in the movie.

kQTAudioMeter_MonoMix - Meter the movie as if it had been mixed to monaural.

kQTAudioMeter_DeviceMix - Meter the movie’s mix to the AudioChannelLayout of the device the
movie is playing to.
```

- [QuickTime 7 Audio Enhancements](https://developer.apple.com/documentation/QuickTime/Conceptual/QT7UpdateGuide/Chapter02/chapter_2_section_6.html#//apple_ref/doc/uid/TP40001163-CH313-784529)
- [SillyFrequencyLevels](https://developer.apple.com/samplecode/SillyFrequencyLevels/index.htmll)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-01-29 | Editorial |
| 2006-01-26 | New document that describes how to perform frequency band level metering using MovieAudio metering APIs. |

