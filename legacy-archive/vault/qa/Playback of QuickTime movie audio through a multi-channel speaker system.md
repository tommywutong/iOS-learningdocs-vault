---
title: Playback of QuickTime movie audio through a multi-channel speaker system
apple_id: DTS40008071
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2008-11-05'
source_url: https://developer.apple.com/library/archive/qa/qa1627/_index.html
archived_at: '2026-07-18T02:33:00.619469Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1627

# Playback of QuickTime movie audio through a multi-channel speaker system

## Q:  How can we specify a specific pair of channels (speakers) to use for playback of a QuickTime audio movie through a multi-channel speaker system?

A: How can we specify a specific pair of channels (speakers) to use for playback of a QuickTime audio movie through a multi-channel speaker system?

For a given QuickTime movie audio track, use the `QTSetTrackProperty` function along with the `kQTAudioPropertyID_ChannelLayout` attribute to describe the channel layout of the track.

The channel layout describes the playback roles for the channels in an audio recording. For example, in a stereo recording, channel 1 has the role of “left front” and channel 2 has the role of “right front.”

When using `QTSetTrackProperty` with the `kQTAudioPropertyID_ChannelLayout` attribute you must pass an `AudioChannelLayout` structure as the property value. The `AudioChannelLayout` is used to specify the channel arrangements of the audio track.

Here's the `AudioChannelLayout` structure:


```
typedef struct AudioChannelLayout {     AudioChannelLayoutTag mChannelLayoutTag;     UInt32 mChannelBitmap;     UInt32 mNumberChannelDescriptions;     AudioChannelDescription mChannelDescriptions[1]; } AudioChannelLayout;
```

A “Channel Layout Tags” value, stored in `mChannelLayoutTag`, signifies which layout scheme is in use, or, if the scheme is not available there, `mChannelBitmap` may contain a bitmap describing the layout. The bitmap is formed using “Channel Bitmaps.”

A value of `kAudioChannelLayoutTag_UseChannelDescriptions` (== 0) indicates there is no standard description for the ordering or use of channels in the file, so that channel descriptions are used instead. In this case, the number of channel descriptions (`mNumberChannelDescriptions`) must equal the number of channels contained in the file. The channel descriptions follow the `mNumberChannelDescriptions` field.

A value of `kAudioChannelLayoutTag_UseChannelBitmap` (== 0x10000) indicates that the Channel Layout chunk uses a bitmap (in the `mChannelBitmap` field) to describe which channels are present.

A value greater than 0x10000 indicates one of the pre-defined layout tags such as `kAudioChannelLayoutTag_Mono`, `kAudioChannelLayoutTag_Stereo`, and so on. Each channel layout tag has two parts:

- The low 16 bits represents the number of channels described by the tag.
- The high 16 bits indicates a specific ordering of the channels.

For example, the tag `kCAFChannelLayoutTag_Stereo` is defined as ((101<<16) | 2 ) and indicates a two-channel stereo, ordered left as the first channel, right as the second.

Each `AudioChannelDescription` contains information describing a single channel:


```
typedef struct AudioChannelDescription {     AudioChannelLabel mChannelLabel;     UInt32 mChannelFlags;     Float32 mCoordinates[3]; } AudioChannelDescription;
```

The `AudioChannelDescription` is used by `AudioChannelLayout` to describe the position of a speaker.

The `mChannelLabel` data member contains a “Channel Labels” value, a tag identifying how the channel is to be used (left, right, center and so on), while `mChannelFlags` marks which coordinate system is in use (cartesian, spherical, and so on). The position of the speaker is kept in `mCoordinates`, as per the “Channel Flags” and “Channel Coordinates.”

The code in Listing 1 shows how to use the `QTSetTrackProperty` function with the `kQTAudioPropertyID_ChannelLayout` attribute to specify the channel layout of the movie audio for playback to the device. In this example, we assume a movie with a single stereo stream (two channels) of audio. The first channel of audio is set to play to LeftSurround, and the second channel of audio is set to play to RightSurround.

__Listing 1__  Setting the audio channel layout using defined layouts.

```swift
#define fieldOffset(type, field) ((size_t) &((type *) 0)->field)  const int kNumChannelDescriptions = 2;  #include <Carbon/Carbon.h> #include <QuickTime/QuickTime.h> #include <AudioToolbox/AudioToolbox.h> #include <assert>  // Set the channel layout of the movie audio for playback to the device.  // We assume a movie with a single stereo stream (two channels) of audio.  // The first channel of audio is set to play to LeftSurround, and the  // second channel of audio is set to play to RightSurround.  void setAudioTrackChannelLayout(Track inTrack) {     UInt32 trackChannelLayoutSize;     AudioChannelLayout* trackChannelLayout = NULL;      // Allocate a layout of the required size.     trackChannelLayoutSize = fieldOffset(AudioChannelLayout,          mChannelDescriptions[kNumChannelDescriptions]);     // Allocate buffer to hold the layout, initialize all bits to 0.     trackChannelLayout = (AudioChannelLayout*)calloc(1, trackChannelLayoutSize);     assert(trackChannelLayout != nil);      // A tag that indicates the type of layout used.     // Our channel layout is described using audio channel descriptions -- see      // AudioChannelLayout.mChannelDescriptions below.     trackChannelLayout->mChannelLayoutTag = kAudioChannelLayoutTag_UseChannelDescriptions ;      // A bitmap that describes which channels are present.     // We are not using channel bitmaps to describe our layout, we are using     // the array of AudioChannelDescriptions to define the mapping.     trackChannelLayout->mChannelBitmap = 0;      // The number of channel descriptions in the mChannelDescriptionsarray.      // We are using 2 channel descriptions -- one description for Left Surround,      // the other for Right Surround.     trackChannelLayout->mNumberChannelDescriptions = kNumChannelDescriptions ;      // A label that describes the role of the channel. In common cases, such as      // “Left” or “Right,” role implies location. In such cases, mChannelFlags      // and mCoordinates can be set to 0.     // In this example, we set the first channel to play to Left Surround, and     // the second channel to play to Right Surround.     trackChannelLayout->mChannelDescriptions[0].mChannelLabel =          kAudioChannelLabel_LeftSurround ;     trackChannelLayout->mChannelDescriptions[1].mChannelLabel =          kAudioChannelLabel_RightSurround ;      // Flags that indicate how to interpret the data in the mCoordinates field.      // If the audio channel does not require this information, set this field to 0.     trackChannelLayout->mChannelDescriptions[0].mChannelFlags = kAudioChannelFlags_AllOff ;      trackChannelLayout->mChannelDescriptions[1].mChannelFlags = kAudioChannelFlags_AllOff ;      // A set of three coordinates that specify the placement of the sound source for the      // channel in three dimensions, according to the mChannelFlags information.      // If the audio channel does not require this information, set this field to 0.     trackChannelLayout->mChannelDescriptions[0].mCoordinates[0] = 0;     trackChannelLayout->mChannelDescriptions[0].mCoordinates[1] = 0;     trackChannelLayout->mChannelDescriptions[0].mCoordinates[2] = 0;      trackChannelLayout->mChannelDescriptions[1].mCoordinates[0] = 0;     trackChannelLayout->mChannelDescriptions[1].mCoordinates[1] = 0;     trackChannelLayout->mChannelDescriptions[1].mCoordinates[2] = 0;      // Set the channel layout properties on the audio track     OSErr err = QTSetTrackProperty(inTrack,                                     kQTPropertyClass_Audio,                                    kQTAudioPropertyID_ChannelLayout,                                     trackChannelLayoutSize,                                     trackChannelLayout );     assert(err == noErr);      free((void *)trackChannelLayout); }
```


Another option for setting the channel layout is to use discrete channels, meaning channels without any layout imposed on them.

Discrete channels remove any kind of confusion by eliminating the spatial assignments on the speakers, so instead of using one of the standard layouts you mark your content with discrete layouts. For example, given a 2-channel audio source you can assign the first channel to play out to the first speaker, and the second channel to play out to the second speaker.

The code in Listing 2 demonstrates the use of discrete channels. In this example, the first stereo stream (first 2 channels) is marked as discrete-0, discrete-1, so that it will play to the first two speakers, and the second stereo stream is marked discrete-2, discrete-3, to play to the third and fourth speakers.

__Listing 2__  Use Discrete channels to set the channel layout.

```swift
#define fieldOffset(type, field) ((size_t) &((type *) 0)->field)  const int kNumChannelDescr = 4;  #include <Carbon/Carbon.h> #include <QuickTime/QuickTime.h> #include <AudioToolbox/AudioToolbox.h> #include <assert>  // Set the channel layout of the movie audio for playback to the device.  // We assume a movie with 2 stereo streams (four channels) of audio.  // The first stereo stream is set to play out the first two speakers, and // the second stereo stream is set to play out the third and fourth speakers.  void setAudioTrackChannelLayoutDiscrete(Track inTrack) {     UInt32 trackChannelLayoutSize;     AudioChannelLayout* trackChannelLayout = NULL;      // Allocate a layout of the required size     trackChannelLayoutSize = fieldOffset(AudioChannelLayout,          mChannelDescriptions[kNumChannelDescr]);     // Allocate buffer to hold the layout, initialize all bits to 0     trackChannelLayout = (AudioChannelLayout*)calloc(1, trackChannelLayoutSize);     assert(trackChannelLayout != nil);      // A tag that indicates the type of layout used.     // Our channel layout is described using audio channel descriptions -- see      // AudioChannelLayout.mChannelDescriptions below.     trackChannelLayout->mChannelLayoutTag = kAudioChannelLayoutTag_UseChannelDescriptions;      // A bitmap that describes which channels are present.     // We are not using channel bitmaps to describe our layout, we are using     // the array of AudioChannelDescriptions to define the mapping.     trackChannelLayout->mChannelBitmap =  0 ;      // The number of channel descriptions in the mChannelDescriptionsarray.      // We are using 4 channel descriptions, one each for: Discrete 0, Discrete 1,      // Discrete 2 and Discrete 3.     trackChannelLayout->mNumberChannelDescriptions = kNumChannelDescr ;      // mChannelLabel = A label that describes the role of the channel. In common cases,      // such as “Left” or “Right,” role implies location. In such cases, mChannelFlags      // and mCoordinates can be set to 0.     //     // This example sets the following channel roles:     //     // first channel -> play to the first speaker     trackChannelLayout->mChannelDescriptions[0].mChannelLabel = kAudioChannelLabel_Discrete_0;     // second channel -> play to the second speaker     trackChannelLayout->mChannelDescriptions[1].mChannelLabel = kAudioChannelLabel_Discrete_1;      // third channel -> play to the third speaker     trackChannelLayout->mChannelDescriptions[2].mChannelLabel = kAudioChannelLabel_Discrete_2;     // fourth channel -> play to the fourth speaker     trackChannelLayout->mChannelDescriptions[3].mChannelLabel = kAudioChannelLabel_Discrete_3;       // Flags that indicate how to interpret the data in the mCoordinates field.      // If the audio channel does not require this information, set this field to 0.     trackChannelLayout->mChannelDescriptions[0].mChannelFlags =          trackChannelLayout->mChannelDescriptions[1].mChannelFlags =              trackChannelLayout->mChannelDescriptions[2].mChannelFlags =                  trackChannelLayout->mChannelDescriptions[3].mChannelFlags =                                                                 kAudioChannelFlags_AllOff ;      // Set the channel layout properties on the track     OSErr err = QTSetTrackProperty(inTrack,                                 kQTPropertyClass_Audio,                                 kQTAudioPropertyID_ChannelLayout,                                  trackChannelLayoutSize,                                 trackChannelLayout );     assert(err == noErr);      free((void *)trackChannelLayout); }
```


If you've followed the above steps but your channel & speaker assignments still do not work correctly you should verify the actual speaker assignments on your computer. For example, if you have a 5.1 audio speaker system check to see that your audio device is set up such that the speaker assignments are really L, R, C, LFE, Ls, Rs.

To configure audio input and output devices on Macintosh, use the Audio Midi Setup application (see /Applications/Utilities/Audio MIDI Setup).

To configure audio input and output devices on Windows, use the Sounds and Audio Devices Control Panel.

[Core Audio Data Types Reference](https://developer.apple.com/documentation/MusicAudio/Reference/CoreAudioDataTypesRef/CoreAudioDataTypesRef.pdf)

[QTAudioExtractionPanel sample code](https://developer.apple.com/samplecode/QTAudioExtractionPanel/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-11-05 | New document that specify a specific pair of channels for QuickTime audio movie playback through a multi-channel speaker system |

