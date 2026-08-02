---
title: AirPlay Overview
apple_id: TP40011045
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/AirPlayGuide/EnrichYourAppforAirPlay/EnrichYourAppforAirPlay.html
archived_at: '2026-07-15T05:21:01.377109Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [AirPlay Overview](About%20AirPlay.md)


[Next](Encryption%20and%20Authentication.md)[Previous](Opting%20Into%20or%20Out%20of%20AirPlay.md)

# Enriching the AirPlay Experience in Your App

There are several ways you can provide a richer experience for your users when they are using AirPlay with your app:

- Provide an AirPlay picker in your app.
- Make sure that all of your app audio goes to the AirPlay output device, and that user interface sounds stay on the host device.
- Provide audio metadata that can be displayed on the AirPlay output device.
- Respond to remote events from the AirPlay output device.
- Take advantage of an external display by providing separate content for the iOS-based device display and the external display (to learn how to do this, see _[Multiple Display Programming Guide for iOS](../../Windows%20Views/Multiple%20Display%20Programming%20Guide%20for%20iOS/Using%20Windows%20to%20Present%20Content%20on%20Multiple%20Displays.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdknjv)_).
- Provide alternate data streams with high-definition video and AC3 audio (for more information, see [Providing AC3 Audio and High-Definition Video](Preparing%20Your%20Media%20and%20Server%20for%20AirPlay.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytanbvfvbuqnbnknlte)).

The user can go to the system AirPlay picker in the iOS multitasking interface to select an AirPlay output, as illustrated in Figure 3-1. If an AirPlay output device is available, an AirPlay button appears next to the volume slider; tapping the button displays a list of available devices.

__Figure 3-1__  System AirPlay picker

!

If your app plays media, you might want to provide an AirPlay output picker within your app so that the user doesn’t have to change focus. You can add an AirPlay picker to your media playback controls by using `MPVolumeView`, as shown in the following code snippet:

```
MPVolumeView *volumeView = [ [MPVolumeView alloc] init] ;
[view addSubview:volumeView];
```

If you have a custom media controller and don’t want to use the standard volume controller, you can add just the AirPlay picker using the following code snippet:

```
MPVolumeView *volumeView = [ [MPVolumeView alloc] init] ;
[volumeView setShowsVolumeSlider:NO];
[volumeView sizeToFit];
[view addSubview:volumeView];
```

The picker is visible only when there is an AirPlay output device available.

Apps typically use two types of sound—app audio (such as ambient sounds, background music, and incidental noises) and system sounds (such as key clicks and alert sounds). AirPlay attempts to deliver the app audio to a remote sound system while keeping system sounds on the host, so that feedback sounds remain local to the input device.

If your app uses system sound APIs for app audio, AirPlay does not redirect them to the AirPlay-enabled sound system. The result is a less-than-optimum user experience. It is important to use system sound APIs _only_ for system sounds. For app audio, use APIs such as `AVAudioPlayer`.

Your audio might be playing on a big-screen home theater system or on a sound system with an LCD display. Your app gives a better user experience if you provide metadata that can be shown on the AirPlay device’s display, such as the artist name, song title, and album art.

Add metadata by passing a dictionary into the `setNowPlayingInfo` method of `MPNowPlayingInfoCenter`. The `MPNowPlayingInfoCenter` class is part of the `MediaPlayer` framework, but works with all playback frameworks, including `MediaPlayer`, `AVFoundation`, and `AudioQueue`.

In addition to providing the usual song information strings, you should also pass in the playback rate, elapsed time, and media item duration. The playback device can use the duration and playback rate to create a progress bar. Update the elapsed time and playback rate whenever the playback rate changes.

When AirPlay is in use, your media might be playing in another room from your host device. The AirPlay output device might have its own controls or respond to an Apple remote control. For the best user experience, your app should listen for and respond to remote events, such as play, pause, and fast-forward requests. Enabling remote events also allows your app to respond to the controls on headphones or earbuds that are plugged into the host device.

Use the following code snippet to receive remote events:

```objc
- (BOOL) canBecomeFirstResponder {return YES;}
- (void) viewDidAppear: (BOOL) animated {
    [super viewDidAppear:animated];
    [ [UIApplication sharedApplication] beginReceivingRemoteControlEvents];
    [self becomeFirstResponder];
}
```

When your app is finished playing media, let the system know that you are no longer the receiver for remote events by using the following code snippet:

```objc
- (void) viewWillDisappear: (BOOL) animated {
    [super viewWillDisappear:animated];
    [ [UIApplication sharedApplication] endReceivingRemoteControlEvents];
    [self resignFirstResponder];
}
```

Respond to events of the type `UIEventTypeRemoteControl` and the subtypes appropriate for your app. The following code snippet gives an example:

```objc
- (void) remoteControlReceivedWithEvent: (UIEvent *) receivedEvent {
    if (receivedEvent.type == UIEventTypeRemoteControl) {
        switch (receivedEvent.subtype) {
            case UIEventSubtypeRemoteControlTogglePlayPause:
                [self playPauseToggle: nil]
                break;
            case UIEventSubtypeRemoteControlNextTrack:
                [self nextTrack: nil]
                break;
...
```

See `UIEvent.h` for an enumeration of event subtypes.

[Next](Encryption%20and%20Authentication.md)[Previous](Opting%20Into%20or%20Out%20of%20AirPlay.md)

