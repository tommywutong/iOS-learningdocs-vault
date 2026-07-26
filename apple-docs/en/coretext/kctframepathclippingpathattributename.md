---
title: kCTFramePathClippingPathAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctframepathclippingpathattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctframepathclippingpathattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctframepathclippingpathattributename.json'
content_hash: 'sha256:3e1e870dfa531456'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFramePathClippingPathAttributeName

<sub>Global Variable</sub>

Specifies clipping path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFramePathClippingPathAttributeName: CFString
```

## Discussion

Specifies clipping path.  This attribute is valid only in a dictionary contained in an array specified by `kCTFrameClippingPathsAttributeName`.

The value must be a `CGPathRef` specifying a clipping path. See [kCTFrameClippingPathsAttributeName](kctframeclippingpathsattributename.md).

## See Also

### Constants

- [CTFrameProgression](ctframeprogression.md) — Constants that specify frame progression types.
- [kCTFrameProgressionAttributeName](kctframeprogressionattributename.md) — Specifies progression for a frame.
- [kCTFramePathFillRuleAttributeName](kctframepathfillruleattributename.md) — The key used to specify the fill rule for a frame.
- [kCTFramePathWidthAttributeName](kctframepathwidthattributename.md) — The key used to specify the frame width.
- [kCTFrameClippingPathsAttributeName](kctframeclippingpathsattributename.md) — Specifies array of paths to clip frame.
