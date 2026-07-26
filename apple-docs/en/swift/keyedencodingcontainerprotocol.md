---
title: KeyedEncodingContainerProtocol
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/keyedencodingcontainerprotocol
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainerprotocol.json'
content_hash: 'sha256:8550866ca42b4fc2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# KeyedEncodingContainerProtocol

<sub>Protocol</sub>

A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol KeyedEncodingContainerProtocol
```

## Overview

Encoders should provide types conforming to `KeyedEncodingContainerProtocol` for their format.

## Relationships

- **Conforming Types**: [KeyedEncodingContainer](keyedencodingcontainer.md)

## Topics

### Associated Types

- [Key](keyedencodingcontainerprotocol/key.md)

### Instance Properties

- [codingPath](keyedencodingcontainerprotocol/codingpath.md) — The path of coding keys taken to get to this point in encoding.

### Instance Methods

- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-389ei.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-44xki.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-45mw2.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-4lg54.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-4xpm2.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-53bkq.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-73p1b.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-74l0h.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-75dqb.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-7d8l.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-86s3y.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-887jx.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-8gl89.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-8mwtj.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-8xq4c.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-9hxpb.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainerprotocol/encode(__forkey_)-qjna.md>) — Encodes the given value for the given key.
- [encodeConditional(_:forKey:)](<keyedencodingcontainerprotocol/encodeconditional(__forkey_).md>) — Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-1d9dk.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-1f6sg.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-1iqzh.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-1r22b.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-2xq5p.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-35mgj.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-3j1kl.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-4axra.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-5ig1w.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-5uiig.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-5xhse.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-68f89.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-6xotr.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-7b7eu.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-837jy.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-d7xg.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainerprotocol/encodeifpresent(__forkey_)-luij.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeNil(forKey:)](<keyedencodingcontainerprotocol/encodenil(forkey_).md>) — Encodes a null value for the given key.
- [nestedContainer(keyedBy:forKey:)](<keyedencodingcontainerprotocol/nestedcontainer(keyedby_forkey_).md>) — Stores a keyed encoding container for the given key and returns it.
- [nestedUnkeyedContainer(forKey:)](<keyedencodingcontainerprotocol/nestedunkeyedcontainer(forkey_).md>) — Stores an unkeyed encoding container for the given key and returns it.
- [superEncoder()](<keyedencodingcontainerprotocol/superencoder().md>) — Stores a new nested container for the default `super` key and returns a new encoder instance for encoding `super` into that container.
- [superEncoder(forKey:)](<keyedencodingcontainerprotocol/superencoder(forkey_).md>) — Stores a new nested container for the given key and returns a new encoder instance for encoding `super` into that container.

## See Also

### Encoding Containers

- [SingleValueEncodingContainer](singlevalueencodingcontainer.md) — A container that can support the storage and direct encoding of a single non-keyed value.
- [KeyedEncodingContainer](keyedencodingcontainer.md) — A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.
- [UnkeyedEncodingContainer](unkeyedencodingcontainer.md) — A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.
