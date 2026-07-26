---
title: CGPathRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathrelease.json'
content_hash: 'sha256:297a7b61a37fd0f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPathRelease

<sub>Function</sub>

Decrements the retain count of a graphics path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGPathRelease(CGPathRef path);
```

## Parameters

- `path` — The graphics path to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `path` parameter is `NULL`.

## See Also

### Retaining and Releasing a Path

- [CGPathRetain](cgpathretain.md) — Increments the retain count of a graphics path.
