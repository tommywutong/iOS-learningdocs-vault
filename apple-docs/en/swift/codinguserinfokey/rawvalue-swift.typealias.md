---
title: CodingUserInfoKey.RawValue
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/codinguserinfokey/rawvalue-swift.typealias
source_url: 'https://developer.apple.com/documentation/swift/codinguserinfokey/rawvalue-swift.typealias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/codinguserinfokey/rawvalue-swift.typealias.json'
content_hash: 'sha256:bf62c04e2c30c930'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CodingUserInfoKey](../codinguserinfokey.md)

# CodingUserInfoKey.RawValue

<sub>Type Alias</sub>

The raw type that can be used to represent all values of the conforming type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias RawValue = String
```

## Discussion

Every distinct value of the conforming type has a corresponding unique value of the `RawValue` type, but there may be values of the `RawValue` type that don’t have a corresponding value of the conforming type.
