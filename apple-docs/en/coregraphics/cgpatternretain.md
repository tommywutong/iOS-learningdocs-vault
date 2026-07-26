---
title: CGPatternRetain
framework: Core Graphics
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpatternretain
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpatternretain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpatternretain.json'
content_hash: 'sha256:0a008d1bcc5deafc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGPatternRetain

<sub>Function</sub>

Increments the retain count of a Core Graphics pattern.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern CGPatternRefCGPatternRetain(CGPatternRef pattern);
```

## Parameters

- `pattern` — The pattern to retain.

## Return Value

The same pattern youpassed in as the `pattern` parameter.

## Discussion

This function is equivalent to [CFRetain](../corefoundation/cfretain.md),except that it does not cause an error if the `pattern` parameteris `NULL`.

## See Also

### Retaining and Releasing a Pattern

- [CGPatternRelease](cgpatternrelease.md) — Decrements the retain count of a Core Graphics pattern.
