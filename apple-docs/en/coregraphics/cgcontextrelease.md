---
title: CGContextRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextrelease.json'
content_hash: 'sha256:17ebb22769b49f27'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextRelease

<sub>Function</sub>

Decrements the retain count of a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGContextRelease(CGContextRef c);
```

## Parameters

- `c` — The graphics context to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except it does not cause an error if `c` is `NULL`.

## See Also

### Retaining and Releasing Graphics Contexts

- [CGContextRetain](cgcontextretain.md) — Increments the retain count of a graphics context.
