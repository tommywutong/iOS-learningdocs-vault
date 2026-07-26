---
title: 'findCompatibleTrack(for:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avurlasset/findcompatibletrack(for:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avurlasset/findcompatibletrack(for:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avurlasset/findcompatibletrack%28for%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:85047ce2f6b9cc19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVURLAsset](../avurlasset.md)

# findCompatibleTrack(for:completionHandler:)

<sub>Instance Method</sub>

Loads an asset track from which you can insert any time range into the composition track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func findCompatibleTrack(for compositionTrack: AVCompositionTrack, completionHandler: @escaping @Sendable (AVAssetTrack?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func findCompatibleTrack(for compositionTrack: AVCompositionTrack) async throws -> AVAssetTrack?
```

## Parameters

- `compositionTrack` — A composition track to request an asset track for.

- `completionHandler` — A callback the system invokes after it finishes the request. The system calls the completion handler with the following arguments: - **track** — The compatible asset track, or `nil` if there isn’t one or an error occurs. - **error** — An error object if the request fails; otherwise, `nil`.

## Discussion

This method is the logical complement of [- mutableTrackCompatibleWithTrack:](<../avmutablecomposition/mutabletrack(compatiblewith_).md>).

## See Also

### Loading tracks

- [tracks](../avpartialasyncproperty/tracks-44ptx.md) — The tracks an asset contains.
