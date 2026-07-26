---
title: CTFramePathFillRule.evenOdd
framework: Core Text
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/ctframepathfillrule/evenodd
source_url: 'https://developer.apple.com/documentation/coretext/ctframepathfillrule/evenodd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/ctframepathfillrule/evenodd.json'
content_hash: 'sha256:230ff8afc8b4be9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Text](../../coretext.md) · [CTFramePathFillRule](../ctframepathfillrule.md)

# CTFramePathFillRule.evenOdd

<sub>Case</sub>

Paints the area using the even-odd fill rule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case evenOdd
```

## Discussion

Text is filled in the area that would be painted if the path were given to [CGContextEOFillPath](../../coregraphics/cgcontexteofillpath.md).

## See Also

### Enumeration Cases

- [kCTFramePathFillWindingNumber](windingnumber.md) — Paints the area using the nonzero winding number rule.
