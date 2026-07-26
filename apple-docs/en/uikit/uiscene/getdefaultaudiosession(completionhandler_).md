---
title: 'getDefaultAudioSession(completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscene/getdefaultaudiosession(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/getdefaultaudiosession(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/getdefaultaudiosession%28completionhandler%3A%29.json'
content_hash: 'sha256:e22dff10551eaf82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# getDefaultAudioSession(completionHandler:)

<sub>Instance Method</sub>

Retrieves the audio session that contains all sounds that implicitly belong to this scene.

<sub>visionOS</sub>

```swift
nonisolated func getDefaultAudioSession(completionHandler handler: @escaping @Sendable (AVAudioSession?) -> Void)
```

<sub>visionOS</sub>

```swift
nonisolated var defaultAudioSession: AVAudioSession? { get async }
```

## Discussion

In visionOS, the default [AVAudioSession](../../avfaudio/avaudiosession.md) for a [UIScene](../uiscene.md) contains all of the RealityKit sounds from any [RealityView](../../realitykit/realityview.md) in the scene’s view hierarchy.

The default audio session’s initial configuration is mixable, with [isNowPlayingCandidate](../../avfaudio/avaudiosession/isnowplayingcandidate.md) set to [false](../../swift/false.md). This configuration ensures that the scene’s default audio session doesn’t interfere with existing behavior of the app’s primary audio session, [sharedInstance()](<../../avfaudio/avaudiosession/sharedinstance().md>). However, you can modify the default audio session’s properties as needed.

You can safely call this method on a non-main thread. It’s recommended to get a scene’s default audio session from a non-main thread to avoid calling resource-intensive [AVAudioSession](../../avfaudio/avaudiosession.md) interfaces from the main thread, which can have a negative impact on the responsiveness of the user experience.
