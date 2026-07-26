---
title: CGPatternRelease
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatternrelease
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatternrelease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatternrelease.json'
content_hash: 'sha256:9a21ec693addfa3a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPatternRelease

<sub>Function</sub>

Decrements the retain count of a Core Graphics pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void CGPatternRelease(CGPatternRef pattern);
```

## Parameters

- `pattern` — The pattern to release.

## Discussion

This function is equivalent to [CFRelease](../corefoundation/cfrelease.md), except that it does not cause an error if the `pattern` parameteris `NULL`.

## See Also

### Retaining and Releasing a Pattern

- [CGPatternRetain](cgpatternretain.md) — Increments the retain count of a Core Graphics pattern.
