---
title: 'insert(charactersIn:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/characterset/insert(charactersin:)-7urdg'
source_url: 'https://developer.apple.com/documentation/foundation/characterset/insert(charactersin:)-7urdg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset/insert%28charactersin%3A%29-7urdg.json'
content_hash: 'sha256:929ab869905e862f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CharacterSet](../characterset.md)

# insert(charactersIn:)

<sub>Instance Method</sub>

Insert a range of integer values in the `CharacterSet`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func insert(charactersIn range: Range<Unicode.Scalar>)
```

## Discussion

It is the caller’s responsibility to ensure that the values represent valid `Unicode.Scalar` values, if that is what is desired.
