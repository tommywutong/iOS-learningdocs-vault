---
title: KeyedEncodingContainer
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/keyedencodingcontainer
source_url: 'https://developer.apple.com/documentation/swift/keyedencodingcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/keyedencodingcontainer.json'
content_hash: 'sha256:5c7e3cfe9c064b69'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# KeyedEncodingContainer

<sub>Structure</sub>

A concrete container that provides a view into an encoder’s storage, making the encoded properties of an encodable type accessible by keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct KeyedEncodingContainer<K> where K : CodingKey
```

## Relationships

- **Conforms To**: [KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md)

## Topics

### Initializers

- [init(_:)](<keyedencodingcontainer/init(__).md>) — Creates a new instance with the given container.

### Instance Properties

- [codingPath](keyedencodingcontainer/codingpath.md) — The path of coding keys taken to get to this point in encoding.

### Instance Methods

- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-11ktw.md>)
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-1m6rk.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-3a74m.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-3xzi8.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-4qaju.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-5bc5p.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-78vtz.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-7a0m.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-7ch7a.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-85f3r.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-8hung.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-8ik7d.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-8qhuv.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-8y5p6.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-92a4.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-99z4.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-9c512.md>) — Encodes the given value for the given key.
- [encode(_:forKey:)](<keyedencodingcontainer/encode(__forkey_)-9mh8u.md>) — Encodes the given value for the given key.
- [encode(_:forKey:configuration:)](<keyedencodingcontainer/encode(__forkey_configuration_)-3i2wq.md>)
- [encode(_:forKey:configuration:)](<keyedencodingcontainer/encode(__forkey_configuration_)-4va3q.md>)
- [encodeConditional(_:forKey:)](<keyedencodingcontainer/encodeconditional(__forkey_).md>) — Encodes a reference to the given object only if it is encoded unconditionally elsewhere in the payload (previously, or in the future).
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-11yvf.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-250z5.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-2b1yb.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-2rzgp.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-3rw9e.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-45la3.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-4c8zy.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-6cflq.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-70fw4.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-70vk4.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-7c6zc.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-7cikn.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-7wqtl.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-87bds.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-9vbxv.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-9ydxr.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:)](<keyedencodingcontainer/encodeifpresent(__forkey_)-ikpq.md>) — Encodes the given value for the given key if it is not `nil`.
- [encodeIfPresent(_:forKey:configuration:)](<keyedencodingcontainer/encodeifpresent(__forkey_configuration_)-7bzb4.md>)
- [encodeIfPresent(_:forKey:configuration:)](<keyedencodingcontainer/encodeifpresent(__forkey_configuration_)-7x1yj.md>)
- [encodeNil(forKey:)](<keyedencodingcontainer/encodenil(forkey_).md>) — Encodes a null value for the given key.
- [encodePredicateExpression(_:forKey:variable:predicateConfiguration:)](<keyedencodingcontainer/encodepredicateexpression(__forkey_variable_predicateconfiguration_)-4hhm9.md>)
- [encodePredicateExpression(_:forKey:variable:predicateConfiguration:)](<keyedencodingcontainer/encodepredicateexpression(__forkey_variable_predicateconfiguration_)-92gv8.md>)
- [encodePredicateExpressionIfPresent(_:forKey:variable:predicateConfiguration:)](<keyedencodingcontainer/encodepredicateexpressionifpresent(__forkey_variable_predicateconfiguration_)-858hy.md>)
- [encodePredicateExpressionIfPresent(_:forKey:variable:predicateConfiguration:)](<keyedencodingcontainer/encodepredicateexpressionifpresent(__forkey_variable_predicateconfiguration_)-ivzi.md>)
- [nestedContainer(keyedBy:forKey:)](<keyedencodingcontainer/nestedcontainer(keyedby_forkey_).md>) — Stores a keyed encoding container for the given key and returns it.
- [nestedUnkeyedContainer(forKey:)](<keyedencodingcontainer/nestedunkeyedcontainer(forkey_).md>) — Stores an unkeyed encoding container for the given key and returns it.
- [superEncoder()](<keyedencodingcontainer/superencoder().md>) — Stores a new nested container for the default `super` key and returns a new encoder instance for encoding `super` into that container.
- [superEncoder(forKey:)](<keyedencodingcontainer/superencoder(forkey_).md>) — Stores a new nested container for the given key and returns a new encoder instance for encoding `super` into that container.

### Type Aliases

- [Key](keyedencodingcontainer/key.md)

### Default Implementations

- [KeyedEncodingContainerProtocol Implementations](keyedencodingcontainer/keyedencodingcontainerprotocol-implementations.md)

## See Also

### Encoding Containers

- [SingleValueEncodingContainer](singlevalueencodingcontainer.md) — A container that can support the storage and direct encoding of a single non-keyed value.
- [KeyedEncodingContainerProtocol](keyedencodingcontainerprotocol.md) — A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type in a keyed manner.
- [UnkeyedEncodingContainer](unkeyedencodingcontainer.md) — A type that provides a view into an encoder’s storage and is used to hold the encoded properties of an encodable type sequentially, without keys.
