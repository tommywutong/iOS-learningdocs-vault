---
title: kCTFramePathFillRuleAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.2+, iPadOS 4.2+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctframepathfillruleattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctframepathfillruleattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctframepathfillruleattributename.json'
content_hash: 'sha256:76538f5b57aef5fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFramePathFillRuleAttributeName

<sub>Global Variable</sub>

The key used to specify the fill rule for a frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFramePathFillRuleAttributeName: CFString
```

## Discussion

The value must be a [CFNumber](../corefoundation/cfnumber.md) object containing a [CTFramePathFillRule](ctframepathfillrule.md) constant. The default value is [kCTFramePathFillEvenOdd](ctframepathfillrule/evenodd.md).

## See Also

### Constants

- [CTFrameProgression](ctframeprogression.md) — Constants that specify frame progression types.
- [kCTFrameProgressionAttributeName](kctframeprogressionattributename.md) — Specifies progression for a frame.
- [kCTFramePathWidthAttributeName](kctframepathwidthattributename.md) — The key used to specify the frame width.
- [kCTFrameClippingPathsAttributeName](kctframeclippingpathsattributename.md) — Specifies array of paths to clip frame.
- [kCTFramePathClippingPathAttributeName](kctframepathclippingpathattributename.md) — Specifies clipping path.
