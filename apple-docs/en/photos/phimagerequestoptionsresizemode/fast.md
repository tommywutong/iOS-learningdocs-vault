---
title: PHImageRequestOptionsResizeMode.fast
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptionsresizemode/fast
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptionsresizemode/fast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptionsresizemode/fast.json'
content_hash: 'sha256:504f77df58d3fa8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHImageRequestOptionsResizeMode](../phimagerequestoptionsresizemode.md)

# PHImageRequestOptionsResizeMode.fast

<sub>Case</sub>

Photos efficiently resizes the image to a size similar to, or slightly larger than, the target size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case fast
```

## Discussion

With this option, Photos can use image subsampling to quickly provide an image at a size roughly matching the target size.

## See Also

### Constants

- [PHImageRequestOptionsResizeModeNone](none.md) — Photos does not resize the image asset.
- [PHImageRequestOptionsResizeModeExact](exact.md) — Photos resizes the image to match the target size exactly.
