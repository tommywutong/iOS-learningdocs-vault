---
title: 'encode(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainerprotocol/encode(_:forkey:)-8gl89'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/encode(_:forkey:)-8gl89'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainerprotocol/encode%28_%3Aforkey%3A%29-8gl89.json'
content_hash: 'sha256:a5209c4075eb873d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainerProtocol](../keyedencodingcontainerprotocol.md)

# encode(_:forKey:)

<sub>Instance Method</sub>

Encodes the given value for the given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encode<T>(_ value: T, forKey key: Self.Key) throws where T : Encodable
```

## Parameters

- `value` — The value to encode.

- `key` — The key to associate the value with.

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Default Implementations

### KeyedEncodingContainerProtocol Implementations

- [encode(_:forKey:)](<encode(__forkey_)-5igzg.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<encode(__forkey_)-7lntx.md>) — Encodes the given value for the given key.
