---
title: CGColorSpaceRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorspaceretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorspaceretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorspaceretain.json'
content_hash: 'sha256:00cc646a423fa076'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorSpaceRetain

<sub>Function</sub>

Increments the retain count of a color space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGColorSpaceRefCGColorSpaceRetain(CGColorSpaceRef space);
```

## Parameters

- `space` — The Quartz color space to retain.

## Return Value

The same color space you passed in as the `space` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `cs` parameter is `NULL`.

## See Also

### Retaining and Releasing Color Spaces

- [CGColorSpaceRelease](cgcolorspacerelease.md) — Decrements the retain count of a color space.
