---
title: kCTFrameProgressionAttributeName
framework: Core Text
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coretext/kctframeprogressionattributename
source_url: 'https://developer.apple.com/documentation/coretext/kctframeprogressionattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/kctframeprogressionattributename.json'
content_hash: 'sha256:3801b8d5a52688e0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# kCTFrameProgressionAttributeName

<sub>Global Variable</sub>

Specifies progression for a frame.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCTFrameProgressionAttributeName: CFString
```

## Discussion

A [CFNumber](../corefoundation/cfnumber.md) object containing a [CTFrameProgression](ctframeprogression.md) constant. The default is `kCTFrameProgressionTopToBottom`.

This value determines the line-stacking behavior for a frame and does not affect the appearance of the glyphs within that frame.

## See Also

### Constants

- [CTFrameProgression](ctframeprogression.md) — Constants that specify frame progression types.
- [kCTFramePathFillRuleAttributeName](kctframepathfillruleattributename.md) — The key used to specify the fill rule for a frame.
- [kCTFramePathWidthAttributeName](kctframepathwidthattributename.md) — The key used to specify the frame width.
- [kCTFrameClippingPathsAttributeName](kctframeclippingpathsattributename.md) — Specifies array of paths to clip frame.
- [kCTFramePathClippingPathAttributeName](kctframepathclippingpathattributename.md) — Specifies clipping path.
