---
title: CGContextRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgcontextretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgcontextretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgcontextretain.json'
content_hash: 'sha256:21a8ff074e80eaa1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGContextRetain

<sub>Function</sub>

Increments the retain count of a graphics context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGContextRefCGContextRetain(CGContextRef c);
```

## Parameters

- `c` — The graphics context to retain.

## Return Value

The same graphics context you passed in as the `context` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except it does not cause an error if `c` is `NULL`.

## See Also

### Retaining and Releasing Graphics Contexts

- [CGContextRelease](cgcontextrelease.md) — Decrements the retain count of a graphics context.
