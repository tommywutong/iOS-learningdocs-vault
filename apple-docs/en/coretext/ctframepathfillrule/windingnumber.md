---
title: CTFramePathFillRule.windingNumber
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctframepathfillrule/windingnumber
source_url: 'https://developer.apple.com/documentation/coretext/ctframepathfillrule/windingnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframepathfillrule/windingnumber.json'
content_hash: 'sha256:adfc0cf7b8bbc611'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFramePathFillRule](../ctframepathfillrule.md)

# CTFramePathFillRule.windingNumber

<sub>Case</sub>

Paints the area using the nonzero winding number rule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case windingNumber
```

## Discussion

Text is filled in the area that would be painted if the path were given to [CGContextFillPath](../../coregraphics/cgcontextfillpath.md).

## See Also

### Enumeration Cases

- [kCTFramePathFillEvenOdd](evenodd.md) — Paints the area using the even-odd fill rule.
