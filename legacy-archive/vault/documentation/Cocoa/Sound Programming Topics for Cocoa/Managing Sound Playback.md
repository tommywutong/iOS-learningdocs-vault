---
title: Sound Programming Topics for Cocoa
apple_id: 10000104i
resource_type: Guide
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AppKit
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Sound/Tasks/PlayingAudioData.html
archived_at: '2026-07-15T07:19:16.845023Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Sound Programming Topics for Cocoa](Introduction%20to%20Sound%20Programming%20Topics%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Loading%20Audio%20Data.md)

# Managing Sound Playback

This article describes how to manage the playback of a sound using the `NSSound` class.

Playing audio data using the `NSSound` class is very simple; instance methods provide transport control. Listing 1 shows several action methods that control the playback of a sound.

__Listing 1__  Controlling sound playback

```objc
- (IBAction) playSound:(id)sender
{
    if (loaded && ![sound isPlaying]) {
        [sound play];
        [infoTextField setStringValue:@"Playback in progress"];
    }
}

- (IBAction) pauseSound:(id)sender
{
    [sound pause];
    [infoTextField setStringValue:@"Playback paused"];
}

- (IBAction) resumeSound:(id)sender
{
    [sound resume];
    [infoTextField setStringValue:@"Playback resumed"];
}

- (IBAction) stopSound:(id)sender
{
    [sound stop]
    [infoTextField setStringValue:@"Playback canceled"];
}
```


The `isPlaying` method tells you whether a sound is playing, as shown in Listing 2.

__Listing 2__  Determining whether a sound is playing

```objc
- (IBAction) isSoundPlaying:(id)sender
{
    if ([sound isPlaying])
        [infoTextField setStringValue:@"The sound is playing"];
    else
        [infoTextField setStringValue:@"The sound is not playing"];
}
```


Listing 3 shows an example implementation of the `sound:didFinishPlaying:` delegate method, which is called when a sound finishes playing.

__Listing 3__  Performing an action when a sound finishes playing

```objc
- (void) sound:(NSSound *)sound didFinishPlaying:(BOOL)playbackSuccessful
{
    if (playbackSuccessful) {
        [infoTextField setStringValue:@"Playback ended successfully"];
    }
    else {
        [infoTextField setStringValue:@"Playback ended abnormally"];
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](Loading%20Audio%20Data.md)

