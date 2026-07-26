---
title: 'setDisconnectedFromSystemAudio(_:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/setdisconnectedfromsystemaudio(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/setdisconnectedfromsystemaudio(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/setdisconnectedfromsystemaudio%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:90f731fc2c19b2b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# setDisconnectedFromSystemAudio(_:completionHandler:)

<sub>Instance Method</sub>

Changes whether the player is disconnected from system audio. This method allows you to dynamically change the player’s system audio connection. The operation is asynchronous. Each call to this method will invoke its own completion handler when the operation completes. When changing from `false` to `true`, you should typically call this method first, then deactivate the `AVAudioSession` to allow other audio to resume.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func setDisconnectedFromSystemAudio(_ disconnected: Bool, completionHandler: (@Sendable () -> Void)? = nil)
```

## Parameters

- `disconnected` — `true` to disconnect from system audio, `false` to connect to it.

- `completionHandler` — A block that is called when the connection state change is complete. This block is called on an arbitrary queue. Defaults to `nil`.

## Using the completion handler

In a scenario where changing the value from `false` to `true` should also allow other system audio to resume, you should only deactivate the audio session once the player has disconnected from system audio.

```swift
// Disconnect from system audio and let other audio resume
player.setDisconnectedFromSystemAudio(true) {
	try AVAudioSession.sharedInstance().setActive(false, options: .notifyOthersOnDeactivation)
}
```
