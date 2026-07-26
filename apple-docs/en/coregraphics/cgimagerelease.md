---
title: CGImageRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgimagerelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimagerelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimagerelease.json'
content_hash: 'sha256:a2be3d3ef1e83f74'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGImageRelease

<sub>Function</sub>

Decrements the retain count of a bitmap image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGImageRelease(CGImageRef image);
```

## Parameters

- `image` — The image to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `image` parameter is `NULL`.

## See Also

### Retaining and releasing images

- [CGImageRetain](cgimageretain.md) — Increments the retain count of a bitmap image.
