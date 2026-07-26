---
title: CGGradientRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cggradientretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cggradientretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggradientretain.json'
content_hash: 'sha256:8858f08d9e3ddc26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGradientRetain

<sub>Function</sub>

Increments the retain count of a CGGradient object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGGradientRefCGGradientRetain(CGGradientRef gradient);
```

## Parameters

- `gradient` — The gradient object to retain.

## Return Value

The same gradient object that you passed in as the `gradient` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md), except that it does not cause an error if the `gradient` parameter is `NULL`.

## See Also

### Retaining and Releasing a Gradient

- [CGGradientRelease](cggradientrelease.md) — Decrements the retain count of a CGGradient object.
