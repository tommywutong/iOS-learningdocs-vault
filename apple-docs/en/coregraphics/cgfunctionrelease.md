---
title: CGFunctionRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfunctionrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfunctionrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfunctionrelease.json'
content_hash: 'sha256:b9e4f9e75c445953'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFunctionRelease

<sub>Function</sub>

Decrements the retain count of a function object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGFunctionRelease(CGFunctionRef function);
```

## Parameters

- `function` — The function object to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `function` parameter is `nil`.

## See Also

### Retaining and Releasing CGFunction Objects

- [CGFunctionRetain](cgfunctionretain.md) — Increments the retain count of a function object.
