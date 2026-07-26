---
title: CGPathFillRule.winding
framework: Core Graphics
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 7.0+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgpathfillrule/winding
source_url: 'https://developer.apple.com/documentation/coregraphics/cgpathfillrule/winding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgpathfillrule/winding.json'
content_hash: 'sha256:f0b35600cf2fd80e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Graphics](../../coregraphics.md) · [CGPathFillRule](../cgpathfillrule.md)

# CGPathFillRule.winding

<sub>Case</sub>

A rule that considers a region to be interior to a path if the winding number for that region is nonzero.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case winding
```

## Discussion

This rule plots a ray from any region to be evaluated toward the bounds of the drawing, then counts the closed path elements that the ray crosses: +1 for counterclockwise paths, -1 for clockwise. The rule defines interior regions as those where the sum of crossings is nonzero, and exterior regions as those where the sum of crossings is zero.

## See Also

### Enumeration Cases

- [CGPathFillRule.evenOdd](evenodd.md) — A rule that considers a region to be interior to a path based on the number of times it is enclosed by path elements.
