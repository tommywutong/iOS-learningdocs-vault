---
title: CGColorRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcolorretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcolorretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcolorretain.json'
content_hash: 'sha256:4a4edf87ae788163'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGColorRetain

<sub>Function</sub>

Increments the retain count of a color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGColorRefCGColorRetain(CGColorRef color);
```

## Parameters

- `color` — The color to retain.

## Return Value

The same color you passed in as the `color` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `color` parameter is `NULL`.

## See Also

### Retaining and Releasing Color Objects

- [CGColorRelease](cgcolorrelease.md) — Decrements the retain count of a color.
