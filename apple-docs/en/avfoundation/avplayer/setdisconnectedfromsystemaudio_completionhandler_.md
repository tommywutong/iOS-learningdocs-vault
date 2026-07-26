---
title: 'setDisconnectedFromSystemAudio:completionHandler:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/setdisconnectedfromsystemaudio:completionhandler:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/setdisconnectedfromsystemaudio:completionhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/setdisconnectedfromsystemaudio%3Acompletionhandler%3A.json'
content_hash: 'sha256:7208b249e3b53f10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# setDisconnectedFromSystemAudio:completionHandler:

<sub>Instance Method</sub>

Changes whether the player is disconnected from system audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) setDisconnectedFromSystemAudio:(BOOL) disconnected completionHandler:(void (^)()) completionHandler;
```

## Parameters

- `disconnected` — YES to disconnect from system audio, NO to connect to it.

- `completionHandler` — A block that is called when the connection state change is complete. This block is called on an arbitrary queue. The completion handler may be nil.

## Discussion

This method allows you to dynamically change the player’s system audio connection. The operation is asynchronous. Each call to this method will invoke its own completion handler when the operation completes. When changing from NO to YES, you should typically call this method first, then deactivate the AVAudioSession in the completion handler to allow other audio to resume.

## Using the completion handler

In a scenario where changing the value from NO to YES should also allow other system audio to resume, you should only deactivate the audio session once the player has disconnected from system audio.

```objective-c
// Disconnect from system audio and let other audio resume
[player setDisconnectedFromSystemAudio:YES completionHandler:^{
    [[AVAudioSession sharedInstance] setActive:NO withOptions:AVAudioSessionSetActiveOptionNotifyOthersOnDeactivation error:nil];
}];
```
