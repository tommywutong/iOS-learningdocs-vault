---
title: 'init(charactersIn:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/characterset/init(charactersin:)-87iva'
source_url: 'https://developer.apple.com/documentation/foundation/characterset/init(charactersin:)-87iva'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset/init%28charactersin%3A%29-87iva.json'
content_hash: 'sha256:f6d08ab8ba5af6e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CharacterSet](../characterset.md)

# init(charactersIn:)

<sub>Initializer</sub>

Initialize with a closed range of integers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(charactersIn range: ClosedRange<Unicode.Scalar>)
```

## Discussion

It is the caller’s responsibility to ensure that the values represent valid `Unicode.Scalar` values, if that is what is desired.
