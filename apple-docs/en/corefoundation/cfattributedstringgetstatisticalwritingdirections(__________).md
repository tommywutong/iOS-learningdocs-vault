---
title: 'CFAttributedStringGetStatisticalWritingDirections(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringgetstatisticalwritingdirections(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringgetstatisticalwritingdirections(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringgetstatisticalwritingdirections%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c3d897177096aa1d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringGetStatisticalWritingDirections(_:_:_:_:_:)

<sub>Function</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringGetStatisticalWritingDirections(_ attributedString: CFAttributedString!, _ range: CFRange, _ baseDirection: Int8, _ bidiLevels: UnsafeMutablePointer<UInt8>!, _ baseDirections: UnsafeMutablePointer<UInt8>!) -> Bool
```

## Discussion

If baseDirection is not NSWritingDirectionNatural, result comes from CFAttributedStringGetBidiLevelsAndResolvedDirections; otherwise, it fills bidiLevels by applying a statistical approach (a paragraph is RTL if 40% or more of its words are RTL) to the characters in range. Returns true if the result is not uni-level LTR (in other words, needing further Bidi processing). baseDirection is NSWritingDirection (NSWritingDirectionNatural, NSWritingDirectionLeftToRight, and NSWritingDirectionRightToLeft).  Understands NSWritingDirectionAttributeName values.
