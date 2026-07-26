---
title: 'memberByName(_:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlstructtype/memberbyname(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlstructtype/memberbyname(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructtype/memberbyname%28_%3A%29.json'
content_hash: 'sha256:f5a73c2cf2acf3bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStructType](../mtlstructtype.md)

# memberByName(_:)

<sub>Instance Method</sub>

Provides a representation of a struct member.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func memberByName(_ name: String) -> MTLStructMember?
```

## Parameters

- `name` — The name of a member in the struct.

## Return Value

An object that represents the named struct member. If `name` does not match a member name, `nil` is returned.

## See Also

### Obtaining information about struct members

- [members](members.md) — An array of instances that describe the fields in the struct.
