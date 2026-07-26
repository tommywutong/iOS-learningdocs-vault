---
title: hashValue
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/asyncstream/continuation/termination/hashvalue
source_url: 'https://developer.apple.com/documentation/swift/asyncstream/continuation/termination/hashvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/asyncstream/continuation/termination/hashvalue.json'
content_hash: 'sha256:43042bae05abd7c0'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [AsyncStream](../../../asyncstream.md) · [Continuation](../../continuation.md) · [Termination](../termination.md)

# hashValue

<sub>Instance Property</sub>

The hash value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var hashValue: Int { get }
```

## Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> [!important] Important
> `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

### Hashing

- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
