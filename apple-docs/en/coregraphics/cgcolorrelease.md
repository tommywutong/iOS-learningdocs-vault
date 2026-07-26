---
title: CGColorRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorrelease.json'
content_hash: 'sha256:ffffdc7bd35a7ffb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorRelease

<sub>Function</sub>

Decrements the retain count of a color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGColorRelease(CGColorRef color);
```

## Parameters

- `color` — The color to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `color` parameter is `NULL`.

## See Also

### Retaining and Releasing Color Objects

- [CGColorRetain](cgcolorretain.md) — Increments the retain count of a color.
