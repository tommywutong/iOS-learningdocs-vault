---
title: Changing the volume of audio devices
apple_id: DTS10003929
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: CoreAudio
published: '2013-04-04'
source_url: https://developer.apple.com/library/archive/qa/qa1016/_index.html
archived_at: '2026-07-18T02:29:54.728467Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1016

# Changing the volume of audio devices

## Q:  How do I change the volume of an audio device?

A: To change the volume of audio hardware you must first obtain an AudioDevice and determine if the device has volume control that is settable. You can get the default output device or the system output device by using the method AudioHardwareGetProperty and the constants `kAudioHardwarePropertyDefaultOutputDevice` and `kAudioHardwarePropertyDefaultSystemOutputDevice` .

__Listing 1__  Getting the default output device

```
 UInt32 size;
    AudioDeviceID outputDevice;
    AudioHardwareGetProperty(kAudioHardwarePropertyDefaultOutputDevice,
                                              &size,
                                              &outputDevice);
```

After obtaining the device, you must check if it has volume control and if this property is writeable.

__Listing 2__  Getting the device capabilities

```
bool CAAudioHardwareDevice::HasProperty(
    UInt32 inChannel,
    CAAudioHardwareDeviceSectionID inSection,
    AudioHardwarePropertyID inPropertyID) const
{
    OSStatus theError = AudioDeviceGetPropertyInfo(mAudioDeviceID,
            inChannel, inSection, inPropertyID, NULL, NULL);
    return theError == 0;
}

bool CAAudioHardwareDevice::PropertyIsSettable(
    UInt32 inChannel,
    CAAudioHardwareDeviceSectionID inSection,
    AudioHardwarePropertyID inPropertyID) const
{
    Boolean isWritable = false;
    OSStatus theError = AudioDeviceGetPropertyInfo(mAudioDeviceID, inChannel,
        inSection, inPropertyID, NULL, &isWritable);
    ThrowIfError(theError, CAException(theError),
        "CAAudioHardwareDevice::PropertyIsSettable: got "
        "an error getting info about a property");
    return isWritable != 0;
}

bool CAAudioHardwareDevice::HasVolumeControl(
    UInt32 inChannel,
    CAAudioHardwareDeviceSectionID inSection) const
{
    return HasProperty(inChannel, inSection, kAudioDevicePropertyVolumeScalar);
}

bool CAAudioHardwareDevice::VolumeControlIsSettable(
    UInt32 inChannel,
    CAAudioHardwareDeviceSectionID inSection) const
{
    return PropertyIsSettable(inChannel, inSection, kAudioDevicePropertyVolumeScalar);
}
```

Then you can set the volume of the device by using the constant `kAudioDevicePropertyVolumeScalar` within AudioDeviceSetProperty. You must specify a Float32 value between 0 and 1 that will scale the volume of the device.

__Listing 3__  Setting the volume on master channel

```
AudioDeviceSetProperty(theDevice,
                         NULL, //time stamp not needed
                         0, //channel 0 is master channel
                         false,  //for an output device
                         kAudioDevicePropertyVolumeScalar,
                         sizeof(Float32),
                         &theValue );
```


- [CoreAudio Documentation](https://developer.apple.com/documentation/MusicAudio/CoreAudio-date.html)
- [CoreAudio Mailing List](http://lists.apple.com/mailman/listinfo/coreaudio-api)
- CAAudioHardwareDevice - /Developer/Examples/CoreAudio/PublicUtility/CAAudioHardwareDevice
- PublicUtility - /Developer/Examples/CoreAudio/PublicUtility/

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-04-04 | Editorial |
| 2006-05-02 | New document that demonstrates volume controls for audio devices |

