---
title: kCTFrameClippingPathsAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctframeclippingpathsattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctframeclippingpathsattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctframeclippingpathsattributename.json'
content_hash: 'sha256:67dc2508e42db3fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFrameClippingPathsAttributeName

<sub>Global Variable</sub>

Specifies array of paths to clip frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFrameClippingPathsAttributeName: CFString
```

## Discussion

The value must be a `CFArrayRef` containing `CFDictionaryRef`s. Each dictionary should have a `kCTFramePathClippingPathAttributeName` key-value pair, and can have a `kCTFramePathFillRuleAttributeName` key-value pair and `kCTFramePathFillRuleAttributeName` key-value pair as optional parameters.

## See Also

### Constants

- [CTFrameProgression](ctframeprogression.md) — Constants that specify frame progression types.
- [kCTFrameProgressionAttributeName](kctframeprogressionattributename.md) — Specifies progression for a frame.
- [kCTFramePathFillRuleAttributeName](kctframepathfillruleattributename.md) — The key used to specify the fill rule for a frame.
- [kCTFramePathWidthAttributeName](kctframepathwidthattributename.md) — The key used to specify the frame width.
- [kCTFramePathClippingPathAttributeName](kctframepathclippingpathattributename.md) — Specifies clipping path.
