---
title: CGGradientRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cggradientrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cggradientrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cggradientrelease.json'
content_hash: 'sha256:30ca329714506b51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGGradientRelease

<sub>Function</sub>

Decrements the retain count of a CGGradient object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGGradientRelease(CGGradientRef gradient);
```

## Parameters

- `gradient` — The gradient object to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `gradient` parameter is `NULL`.

## See Also

### Retaining and Releasing a Gradient

- [CGGradientRetain](cggradientretain.md) — Increments the retain count of a CGGradient object.
