---
title: 'encodeIfPresent(_:forKey:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-d7xg'
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol/encodeifpresent(_:forkey:)-d7xg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainerprotocol/encodeifpresent%28_%3Aforkey%3A%29-d7xg.json'
content_hash: 'sha256:76cdeb1e85749460'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [KeyedEncodingContainerProtocol](../keyedencodingcontainerprotocol.md)

# encodeIfPresent(_:forKey:)

<sub>Instance Method</sub>

Encodes the given value for the given key if it is not `nil`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func encodeIfPresent(_ value: Int128?, forKey key: Self.Key) throws
```

## Parameters

- `value` — The value to encode.

- `key` — The key to associate the value with.

## Discussion

> [!danger] Throws
> `EncodingError.invalidValue` if the given value is invalid in the current context for this format.

## Default Implementations

### KeyedEncodingContainerProtocol Implementations

- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-1g1z4.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-1lv6o.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-1lz0j.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-1r6ai.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-2dwj5.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-3lhrl.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-4a2u7.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-4d89n.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-4kvt4.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-4p5p4.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-5jh2r.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-6xbjj.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-7rynx.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-8i0us.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-8m92m.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-9sui2.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<encodeifpresent(__forkey_)-yaxk.md>) — Encodes the given value for the given key if it is not `nil`.
