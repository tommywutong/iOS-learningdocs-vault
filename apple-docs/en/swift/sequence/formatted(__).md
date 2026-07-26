---
title: 'formatted(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/formatted%28_%3A%29.json'
content_hash: 'sha256:dafea1f9bc073b69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# formatted(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ style: S) -> S.FormatOutput where Self == S.FormatInput, S : FormatStyle
```

## See Also

### Formatting a Sequence

- [formatted()](<formatted().md>)
- [ListFormatStyle](../../foundation/listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.
