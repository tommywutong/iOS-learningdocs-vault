---
title: CGFunctionRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgfunctionretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgfunctionretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgfunctionretain.json'
content_hash: 'sha256:40c28b8395477d8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGFunctionRetain

<sub>Function</sub>

Increments the retain count of a function object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGFunctionRefCGFunctionRetain(CGFunctionRef function);
```

## Parameters

- `function` — The function object to retain.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `function` parameter is `nil`.

## See Also

### Retaining and Releasing CGFunction Objects

- [CGFunctionRelease](cgfunctionrelease.md) — Decrements the retain count of a function object.
