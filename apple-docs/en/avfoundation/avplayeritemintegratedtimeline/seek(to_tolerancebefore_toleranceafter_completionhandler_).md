---
title: 'seek(to:toleranceBefore:toleranceAfter:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemintegratedtimeline/seek(to:tolerancebefore:toleranceafter:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimeline/seek(to:tolerancebefore:toleranceafter:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimeline/seek%28to%3Atolerancebefore%3Atoleranceafter%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:b5610313bbd22506'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimeline](../avplayeritemintegratedtimeline.md)

# seek(to:toleranceBefore:toleranceAfter:completionHandler:)

<sub>Instance Method</sub>

Seeks to a particular time in the integrated time domain.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (@Sendable (Bool) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func seek(to time: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime) async -> Bool
```

## Parameters

- `time` — A time represented in the integrated time domain.

- `toleranceBefore` — A tolerance before the target time to allow.

- `toleranceAfter` — A tolerance after the target time to allow.

- `completionHandler` — A callback the system invokes after the seek completes. It passes a Boolean value of `true` if the playhead moved to the new time.

## See Also

### Seeking

- [- seekToDate:completionHandler:](<seek(to_completionhandler_).md>) — Seeks to a particular date in the integrated time domain.
