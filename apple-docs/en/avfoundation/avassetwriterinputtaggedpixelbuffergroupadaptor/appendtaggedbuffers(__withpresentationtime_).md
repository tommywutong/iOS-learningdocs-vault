---
title: 'appendTaggedBuffers(_:withPresentationTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+（26.0 起废弃）, iPadOS 17.0+（26.0 起废弃）, Mac Catalyst 17.0+（26.0 起废弃）, macOS 14.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedbuffers(_:withpresentationtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedbuffers(_:withpresentationtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedbuffers%28_%3Awithpresentationtime%3A%29.json'
content_hash: 'sha256:b66e8b7d4b6e44b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](../avassetwriterinputtaggedpixelbuffergroupadaptor.md)

# appendTaggedBuffers(_:withPresentationTime:)

<sub>Instance Method</sub>

Appends a tagged buffer group to the adaptor.

> [!warning] Deprecated
> Use AVAssetWriterInput.TaggedPixelBufferGroupReceiver.append(_:with:isolation:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func appendTaggedBuffers(_ taggedBuffers: [CMTaggedBuffer], withPresentationTime: CMTime) -> Bool
```

## See Also

### Appending pixel buffers

- [- appendTaggedPixelBufferGroup:withPresentationTime:](<appendtaggedpixelbuffergroup(__withpresentationtime_).md>) — Appends a tagged buffer group to the adaptor. _(deprecated)_
