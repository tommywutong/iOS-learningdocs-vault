---
title: Saving Power During Audio I/O - The kAudioHardwarePropertyPowerHint Property
apple_id: DTS40013499
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2013-07-30'
source_url: https://developer.apple.com/library/archive/technotes/tn2321/_index.html
archived_at: '2026-07-26T19:54:10.698626Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2321

# Saving Power During Audio I/O - The kAudioHardwarePropertyPowerHint Property

This technical note discusses the `kAudioHardwarePropertyPowerHint` property available beginning in OS X 10.9 Mavericks. Developers can set this property to save power when performing audio I/O.

[Background](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbzhewugsbrfvbecq2li5je6vkoiq)[The Audio Power Hint](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbzhewugsbrfvkeqrk7ifkuiskpl5ie6v2fkjpuqskokq)[Save Power With Configuration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbzhewugsbrfvjucvsfl5ie6v2fkjpvoskujbpugt2oizeuovksifkest2o)[The I/O Buffer Size](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbzhewugsbrfvkeqrk7jfpu6x2ckvdemrksl5juswsf)[I/O Buffer Size and I/O Latency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbzhewugsbrfvke4vcbi42a)[Summary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbzhewugsbrfvjvktknifjfs)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbzhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Background

Fast performance and long battery life are two critical elements contributing to an overall positive experience users have with the Mac. But while users have become more dependent on battery life, the applications they use have at the same time become more and more hungry for power. Therefore, it has become very important in the evolution of OS X to look for ways to save power while also maintaining system responsiveness and fast performance.

OS X makes sure power is saved in many ways using advanced technologies like Timer Coalescing, App Nap and so on. However, to save power when performing audio input and output, OS X needs information from the application itself.

In order to save power, OS X has to make decisions that will increase the latency of the audio I/O subsystem thereby directly affecting an application. For some applications, the trade off between latency and battery life is absolutely fine and results in no perceived performance loss. For other applications, this can be disastrous. Therefore, OS X needs the application's assistance to know when this type of trade off is ok and when it is not.

[Back to Top](#)

## The Audio Power Hint

In order to facilitate a way for applications to let OS X know how to handle the power save/performance trade off, the CoreAudio framework provides a property called `kAudioHardwarePropertyPowerHint`.

Applications can set this property to the value `kAudioHardwarePowerHintFavorSavingPower` to indicate that OS X should take actions to save power including actions that can increase the latency of the I/O system. With OS X 10.9, setting this hint will increase the default I/O buffer size from `512` sample frames to `4096` sample frames. The interaction between buffer size and latency is discussed in the [I/O Buffer Size and I/O Latency](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytgnbzhewugsbrfvke4vcbi42a) section of this document.

Applications have two ways to set the power hint:

- By including a key named "`AudioHardwarePowerHint`" in its `info.plist`. The value of this key can be "`Favor Saving Power`" which tells OS X that the application is __opting in__ to all power savings measures. The value can also be "`None`" indicating to OS X that the application __does not want__ the system to make any I/O changes to save power.
- By using the `AudioObjectSetPropertyData` API. Note that the application is allowed to set the value of this hint as many times as it likes thereby opting into power savings measures initially only to opt out at a later time as the user's needs change. See Listing 1.

__Note:__ An application can use both of the above methods to manage power savings. For example, an application may want to set the "`AudioHardwarePowerHint`" key to "`Favor Saving Power`" by default, then later use `AudioObjectSetPropertyData` to stop favoring power saving by setting the  `kAudioHardwarePropertyPowerHint` property to `kAudioHardwarePowerHintNone`.

__Listing 1__  Setting the Audio Power Hint.

```c
#include <CoreAudio/CoreAudio.h>

static OSStatus SetAudioPowerHintToFavorSavingPower()
{
    AudioObjectPropertyAddress theAddress = { kAudioHardwarePropertyPowerHint,
                                              kAudioObjectPropertyScopeGlobal,
                                              kAudioObjectPropertyElementMaster };

    UInt32 thePowerHint = kAudioHardwarePowerHintFavorSavingPower;
    return AudioObjectSetPropertyData(kAudioObjectSystemObject,
                                      &theAddress,
                                      0,
                                      NULL,
                                      sizeof(UInt32), &thePowerHint);
}

static OSStatus SetAudioPowerHintToNone()
{
    AudioObjectPropertyAddress theAddress = { kAudioHardwarePropertyPowerHint,
                                              kAudioObjectPropertyScopeGlobal,
                                              kAudioObjectPropertyElementMaster };

    UInt32 thePowerHint = kAudioHardwarePowerHintNone;
    return AudioObjectSetPropertyData(kAudioObjectSystemObject,
                                      &theAddress,
                                      0,
                                      NULL,
                                      sizeof(UInt32), &thePowerHint);
}
```

[Back to Top](#)

## Save Power With Configuration

Saving power in general terms is the process of finding ways to accomplish the same tasks while using less CPU and other system resources. This can often take the form of batching up the work to be done all at once so that the CPU can drop into deeper sleep states for longer periods of time. This principle shows up in a couple of places throughout the audio software stack.

Many Core Audio APIs have parameters and properties allowing the developer to control the algorithmic complexity of a signal processing chain. For example, the `AudioConverter` has several properties for controlling the quality of various stages during the conversion process such as the sample rate converter (`kAudioConverterSampleRateConverterQuality`) and audio codec (`kAudioConverterCodecQuality`). Another example is the 3D mixer with its property to control rendering quality by choosing different spatialization algorithms as discussed in [TN2112 Using the 3DMixer Audio Unit](https://developer.apple.com/library/mac/#technotes/tn2112/_index.html). Still another is the system provided audio units that implement various algorithms for doing time and pitch conversions. These audio units provide for different trade-offs between the kind and quality of the signal processing done and the amount of CPU used to do the processing. By using these facilities applications can control the amount of work being done thereby saving power when it is appropriate to do so.

It is the applications responsibility to look at the type of signal processing being done and understand where it can turn down the quality or use alternative algorithms to achieve the same result. This may require some experimentation. It is always a good idea to reserve some time in a development schedule to concentrate on performance tuning. For audio, analyze the signal processing being done by the application to see where things can be scaled back without affecting the user experience.

[Back to Top](#)

## The I/O Buffer Size

Using the properties and parameters of audio units to lower the amount of work done processing audio data is very helpful, but the level of power savings that can be achieved that way is limited. The most influential setting an application has at its disposal to control the amount of power being used during rendering is the size of the I/O buffer it chooses. The size of the I/O buffer controls the rate at which the audio stack will wake the CPU in order to perform I/O. Therefore, the I/O buffer size will nearly always be the dominant factor affecting audio stack power usage.

An application has complete control over the size of the I/O buffer it uses. This control is expressed by telling the audio system what I/O buffer size to use via the `kAudioDevicePropertyBufferFrameSize` property that can be set either with the `AudioObjectSetPropertyData` API or with the AUHAL Audio Unit `AudioUnitSetProperty` API.

The legal range for the buffer frame size property can be queried by using the `kAudioDevicePropertyBufferFrameSizeRange` property. See Listings 2 and 3.

__Listing 2__  Setting the I/O Buffer Size for the HAL.

```c
#include <CoreAudio/CoreAudio.h>

static OSStatus GetIOBufferFrameSizeRange(AudioObjectID inDeviceID,
                                          UInt32* outMinimum,
                                          UInt32* outMaximum)
{
    AudioObjectPropertyAddress theAddress = { kAudioDevicePropertyBufferFrameSizeRange,
                                              kAudioObjectPropertyScopeGlobal,
                                              kAudioObjectPropertyElementMaster };

    AudioValueRange theRange = { 0, 0 };
    UInt32 theDataSize = sizeof(AudioValueRange);
    OSStatus theError = AudioObjectGetPropertyData(inDeviceID,
                                                   &theAddress,
                                                   0,
                                                   NULL,
                                                   &theDataSize,
                                                   &theRange);
    if(theError == 0)
    {
        *outMinimum = theRange.mMinimum;
        *outMaximum = theRange.mMaximum;
    }
    return theError;
}

static OSStatus SetCurrentIOBufferFrameSize(AudioObjectID inDeviceID,
                                            UInt32 inIOBufferFrameSize)
{
    AudioObjectPropertyAddress theAddress = { kAudioDevicePropertyBufferFrameSize,
                                              kAudioObjectPropertyScopeGlobal,
                                              kAudioObjectPropertyElementMaster };

    return AudioObjectSetPropertyData(inDeviceID,
                                      &theAddress,
                                      0,
                                      NULL,
                                      sizeof(UInt32), &inIOBufferFrameSize);
}

static OSStatus GetCurrentIOBufferFrameSize(AudioObjectID inDeviceID,
                                            UInt32* outIOBufferFrameSize)
{
    AudioObjectPropertyAddress theAddress = { kAudioDevicePropertyBufferFrameSize,
                                              kAudioObjectPropertyScopeGlobal,
                                              kAudioObjectPropertyElementMaster };

    UInt32 theDataSize = sizeof(UInt32);
    return AudioObjectGetPropertyData(inDeviceID,
                                      &theAddress,
                                      0,
                                      NULL,
                                      &theDataSize,
                                      outIOBufferFrameSize);
}
```

__Listing 3__  Setting the I/O buffer size for the AUHAL.

```c
#include <AudioToolbox/AudioToolbox.h>
#include <AudioUnit/AudioUnit.h>

static OSStatus GetIOBufferFrameSizeRange(AudioUnit inAUHAL,
                                          UInt32* outMinimum,
                                          UInt32* outMaximum)
{
    AudioValueRange theRange = { 0, 0 };
    UInt32 theDataSize = sizeof(AudioValueRange);
    OSStatus theError = AudioUnitGetProperty(inAUHAL,
                                             kAudioDevicePropertyBufferFrameSizeRange,
                                             kAudioUnitScope_Global,
                                             0,
                                             &theRange, &theDataSize);

    if(theError == 0)
    {
        *outMinimum = theRange.mMinimum;
        *outMaximum = theRange.mMaximum;
    }
    return theError;
}

static OSStatus SetCurrentIOBufferFrameSize(AudioUnit inAUHAL,
                                            UInt32 inIOBufferFrameSize)
{
    return AudioUnitSetProperty(inAUHAL,
                                kAudioDevicePropertyBufferFrameSize,
                                kAudioUnitScope_Global,
                                0,
                                &inIOBufferFrameSize, sizeof(UInt32));
}

static OSStatus GetCurrentIOBufferFrameSize(AudioUnit inAUHAL,
                                            UInt32* outIOBufferFrameSize)
{
    UInt32 theDataSize = sizeof(UInt32);
    return AudioUnitGetProperty(inAUHAL,
                                kAudioDevicePropertyBufferFrameSize,
                                kAudioUnitScope_Global,
                                0,
                                outIOBufferFrameSize, &theDataSize);
}
```

[Back to Top](#)

## I/O Buffer Size and I/O Latency

The size of the I/O buffer is directly related to the latency of the I/O system. It is a one to one relationship. For each sample frame the I/O buffer size is increased there is a corresponding increase of one sample frame more latency. For applications that are sensitive to latency changes this means that any change to the I/O buffer size can dramatically affect the user experience.

Applications sensitive to changes in latency are generally those that need to provide an interactive user experience. Digital audio workstation applications like GarageBand or Logic Pro X are obvious examples of applications sensitive to latency as well as games where sound effects need to be played immediately in response to game events, and even teleconferencing applications where the performance of echo cancellation and noise suppression is directly affected by the amount of latency in the system.

For this class of application the I/O buffer size used should be the largest buffer possible without breaking the specific use case requirements for the application. Experimenting with the buffer size is encouraged to achieve this goal.

__Note:__ For many (but not all) such applications, even a modest increase in the I/O buffer size from the `512` sample frames default to `1024` sample frames can result in measurable power savings without materially affecting behavior. Again, experimentation is encouraged.

Applications not sensitive to latency changes would be media players, for example applications like QuickTime Player or iTunes. This class of application is generally more concerned with playing audio in sync with other media (such as video) than it is with playing the audio as quickly as possible in response to a user event.

This class of application should use the largest I/O buffer size possible and set the audio power hint to favor saving power. Simply setting the "`AudioHardwarePowerHint`" key in the `info.plist` file may be all that is required as doing so will allow OS X to automatically increase the I/O buffer size by default and save power.

__Important:__ If you are using an I/O buffer size that is __larger__ than the default, be aware that audio units have a separate upper bound that controls how large a buffer they can use. This size limitation is expressed by the property `kAudioUnitProperty_MaximumFramesPerSlice`. If an application has set the I/O buffer size to be larger than the default, it is vital that the application also set the value of `kAudioUnitProperty_MaximumFramesPerSlice` for each audio unit instance it is using. The value to set for this property can be the same as the new larger I/O buffer size.

Failure to update the `kAudioUnitProperty_MaximumFramesPerSlice` property will cause audio units to not perform any processing (this included not pulling on any inputs) and return the error `kAudioUnitErr_TooManyFramesToProcess`.

[Back to Top](#)

## Summary

Power usage is fast becoming a key metric by which the quality of an application is judged. When it comes to the audio system, OS X provides many options to increase an applications power efficiency. This includes setting the Audio Power Hint, paying attention to the I/O buffer size as well as using the available audio unit parameters and properties to ensure your application has set up the audio system in a way that not only sounds good but also power efficient.

It is __up to the application itself__ to take advantage of these audio system features. Developers are encouraged to experiment with I/O buffer sizes to figure out the largest size they can use without affecting the user experience and to favor power saving where appropriate.

For certain applications simply setting the "AudioHardwarePowerHint" key to "`Favor Saving Power`" in the applications `info.plist` file may be all that is required as doing so will allow OS X to automatically manage the audio system to favor saving power.

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-07-30 | New document that provides information that developers can use to save power while doing audio I/O. |

