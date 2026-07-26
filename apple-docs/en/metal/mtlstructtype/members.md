---
title: members
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlstructtype/members
source_url: 'https://developer.apple.com/documentation/metal/mtlstructtype/members'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlstructtype/members.json'
content_hash: 'sha256:0c5b88779372587c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLStructType](../mtlstructtype.md)

# members

<sub>Instance Property</sub>

An array of instances that describe the fields in the struct.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var members: [MTLStructMember] { get }
```

## Discussion

Each array element in [members](members.md) is an [MTLStructMember](../mtlstructmember.md) instance that corresponds to one of the fields in the struct.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Obtaining information about struct members

- [- memberByName:](<memberbyname(__).md>) — Provides a representation of a struct member.
