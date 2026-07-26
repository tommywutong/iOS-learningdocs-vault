---
title: CGPathRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathretain.json'
content_hash: 'sha256:0cd094390bbd7ef6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPathRetain

<sub>Function</sub>

Increments the retain count of a graphics path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGPathRefCGPathRetain(CGPathRef path);
```

## Parameters

- `path` — The graphics path to retain.

## Return Value

The same path you passed in as the `path` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `path` parameter is `NULL`.

## See Also

### Retaining and Releasing a Path

- [CGPathRelease](cgpathrelease.md) — Decrements the retain count of a graphics path.
