---
title: 'linguisticTags(in:scheme:options:orthography:tokenRanges:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/linguistictags(in:scheme:options:orthography:tokenranges:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/linguistictags(in:scheme:options:orthography:tokenranges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/linguistictags%28in%3Ascheme%3Aoptions%3Aorthography%3Atokenranges%3A%29.json'
content_hash: 'sha256:c2df66f0d2dcc370'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# linguisticTags(in:scheme:options:orthography:tokenRanges:)

<sub>Instance Method</sub>

Returns an array of linguistic tags for the specified range and requested tags within the receiving string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func linguisticTags<T, R>(in range: R, scheme tagScheme: T, options opts: NSLinguisticTagger.Options = [], orthography: NSOrthography? = nil, tokenRanges: UnsafeMutablePointer<[Range<Self.Index>]>? = nil) -> [String] where T : StringProtocol, R : RangeExpression, R.Bound == String.Index
```
