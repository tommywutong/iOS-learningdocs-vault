---
title: 'appendTaggedPixelBufferGroup(_:withPresentationTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedpixelbuffergroup(_:withpresentationtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedpixelbuffergroup(_:withpresentationtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/appendtaggedpixelbuffergroup%28_%3Awithpresentationtime%3A%29.json'
content_hash: 'sha256:1dffee7eb993ea81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](../avassetwriterinputtaggedpixelbuffergroupadaptor.md)

# appendTaggedPixelBufferGroup(_:withPresentationTime:)

<sub>Instance Method</sub>

Appends a tagged buffer group to the adaptor.

> [!warning] Deprecated
> Use AVAssetWriter.inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func appendTaggedPixelBufferGroup(_ taggedPixelBufferGroup: __CMTaggedBufferGroup, withPresentationTime presentationTime: CMTime) -> Bool
```

## See Also

### Appending pixel buffers

- [appendTaggedBuffers(_:withPresentationTime:)](<appendtaggedbuffers(__withpresentationtime_).md>) — Appends a tagged buffer group to the adaptor. _(deprecated)_
