---
title: CGImageRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgimageretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgimageretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgimageretain.json'
content_hash: 'sha256:57d13b7c5fc75c51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGImageRetain

<sub>Function</sub>

Increments the retain count of a bitmap image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGImageRefCGImageRetain(CGImageRef image);
```

## Parameters

- `image` — The image to retain.

## Return Value

The same image you passed in as the `image` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `image` parameter is `NULL`.

## See Also

### Retaining and releasing images

- [CGImageRelease](cgimagerelease.md) — Decrements the retain count of a bitmap image.
