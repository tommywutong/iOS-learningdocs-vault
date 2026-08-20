---
title: How do I set the volume of audio media for playback with AVPlayer on iOS?
apple_id: DTS40010276
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2014-05-21'
source_url: https://developer.apple.com/library/archive/qa/qa1716/_index.html
archived_at: '2026-07-18T02:34:27.292969Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1716

# How do I set the volume of audio media for playback with AVPlayer on iOS?

## Q:  How do I set the volume of audio media for playback with `AVPlayer` on iOS?

A: `AVPlayer` uses the system volume (controlled by the hardware volume switch) for media playback.

Use the `MPVolumeView` class to present the user with a slider control in your application for setting the system audio output volume. See the [MPVolumeView Class Reference](https://developer.apple.com/iphone/library/documentation/MediaPlayer/Reference/MPVolumeView_Class/Reference/Reference.html) for more information.

On iOS 7, you can mute the playback of audio (local or streamed) with the `AVPlayer` `muted` property:

__Listing 1__  Muting the playback of audio for an `AVPlayer` object using the muted property.

```objc
#import <AVFoundation/AVFoundation.h>

AVPlayer *player = <#A properly configured AVPlayer object#>;
player.muted = YES; // mute the audio
```

On iOS 6 and earlier, you can mute the playback of audio with `AVPlayer` by creating an `AVAudioMix` with a volume ramp to set the volume to 0 as shown in Listing 2:

__Listing 2__  Muting the playback of audio with `AVPlayer` by creating an `AVAudioMix` with zero volume ramp.

```objc
#import <AVFoundation/AVFoundation.h>

AVURLAsset *asset = [AVURLAsset URLAssetWithURL:[self myAssetURL] options:nil];
NSArray *audioTracks = [asset tracksWithMediaType:AVMediaTypeAudio];

// Mute all the audio tracks
NSMutableArray *allAudioParams = [NSMutableArray array];
for (AVAssetTrack *track in audioTracks) {
    AVMutableAudioMixInputParameters *audioInputParams =[AVMutableAudioMixInputParameters audioMixInputParameters];
    [audioInputParams setVolume:0.0 atTime:kCMTimeZero];
    [audioInputParams setTrackID:[track trackID]];
    [allAudioParams addObject:audioInputParams];
}
AVMutableAudioMix *audioZeroMix = [AVMutableAudioMix audioMix];
[audioZeroMix setInputParameters:allAudioParams];

// Create a player item
AVPlayerItem *playerItem = [AVPlayerItem playerItemWithAsset:asset];
[playerItem setAudioMix:audioZeroMix]; // Mute the player item

// Create a new Player, and set the player to use the player item
// with the muted audio mix
AVPlayer *player = [AVPlayer playerWithPlayerItem:playerItem];

// assign player object to an instance variable
self.mPlayer = player;

// play the muted audio
[mPlayer play];
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-05-21 | Added information about the AVPlayer muted property for iOS 7 |
| 2010-08-27 | New document that demonstrates how to set the volume of audio media for playback with AVPlayer on iOS |

