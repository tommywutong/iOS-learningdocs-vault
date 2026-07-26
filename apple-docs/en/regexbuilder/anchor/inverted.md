---
title: inverted
framework: RegexBuilder
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/anchor/inverted
source_url: 'https://developer.apple.com/documentation/regexbuilder/anchor/inverted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/anchor/inverted.json'
content_hash: 'sha256:4bb2cd91993fef26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [RegexBuilder](../../regexbuilder.md) · [Anchor](../anchor.md)

# inverted

<sub>Instance Property</sub>

The inverse of this anchor, which matches at every position that this anchor does not.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var inverted: Anchor { get }
```

## Discussion

For the [wordBoundary](wordboundary.md) and [textSegmentBoundary](textsegmentboundary.md) anchors, the inverted version corresponds to `\B` and `\Y`, respectively.
