---
title: CGColorSpaceRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspacerelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspacerelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspacerelease.json'
content_hash: 'sha256:38df274215e354af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorSpaceRelease

<sub>Function</sub>

Decrements the retain count of a color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGColorSpaceRelease(CGColorSpaceRef space);
```

## Parameters

- `space` — The Quartz color space to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `cs` parameter is `NULL`.

## See Also

### Retaining and Releasing Color Spaces

- [CGColorSpaceRetain](cgcolorspaceretain.md) — Increments the retain count of a color space.
