---
title: 'enumerateLinguisticTags(in:scheme:options:orthography:invoking:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/enumeratelinguistictags(in:scheme:options:orthography:invoking:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/enumeratelinguistictags(in:scheme:options:orthography:invoking:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/enumeratelinguistictags%28in%3Ascheme%3Aoptions%3Aorthography%3Ainvoking%3A%29.json'
content_hash: 'sha256:1a967bfa4fc3c1c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# enumerateLinguisticTags(in:scheme:options:orthography:invoking:)

<sub>Instance Method</sub>

Performs linguistic analysis on the specified string by enumerating the specific range of the string, providing the Block with the located tags.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateLinguisticTags<T, R>(in range: R, scheme tagScheme: T, options opts: NSLinguisticTagger.Options = [], orthography: NSOrthography? = nil, invoking body: (String, Range<Self.Index>, Range<Self.Index>, inout Bool) -> Void) where T : StringProtocol, R : RangeExpression, R.Bound == String.Index
```
