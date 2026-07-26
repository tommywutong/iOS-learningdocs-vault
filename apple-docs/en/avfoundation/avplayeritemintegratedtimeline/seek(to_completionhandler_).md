---
title: 'seek(to:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemintegratedtimeline/seek(to:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/seek(to:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/seek%28to%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:e721e5b5d07c9fab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# seek(to:completionHandler:)

<sub>Instance Method</sub>

Seeks to a particular date in the integrated time domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func seek(to date: Date, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func seek(to date: Date) async -> Bool
```

## Parameters

- `date` — A date represented in the integrated time domain.

- `completionHandler` — A callback the system invokes after the seek completes. It passes a Boolean value of `true` if the playhead moved to the new date.

## See Also

### Seeking

- [- seekToTime:toleranceBefore:toleranceAfter:completionHandler:](<seek(to_tolerancebefore_toleranceafter_completionhandler_).md>) — Seeks to a particular time in the integrated time domain.
