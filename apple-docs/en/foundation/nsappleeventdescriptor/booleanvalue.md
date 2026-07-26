---
title: booleanValue
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor/booleanvalue
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/booleanvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/booleanvalue.json'
content_hash: 'sha256:13039edf49989baf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# booleanValue

<sub>Instance Property</sub>

The contents of the receiver as a Boolean value, coercing (to `typeBoolean`) if necessary.

<sub>Mac Catalyst, macOS</sub>

```swift
var booleanValue: Bool { get }
```

## Discussion

The contents of the descriptor, as a Boolean value, or `false` if an error occurs.

## See Also

### Getting Information About a Descriptor

- [aeDesc](aedesc.md) — The `AEDesc` structure encapsulated by the receiver, if it has one.
- [- coerceToDescriptorType:](<coerce(todescriptortype_).md>) — Returns a descriptor obtained by coercing the receiver to the specified type.
- [data](data.md) — The receiver’s data.
- [descriptorType](descriptortype.md) — The descriptor type of the receiver.
- [enumCodeValue](enumcodevalue.md) — The contents of the receiver as an enumeration type, coercing to `typeEnumerated` if necessary.
- [int32Value](int32value.md) — The contents of the receiver as an integer, coercing (to `typeSInt32`) if necessary.
- [numberOfItems](numberofitems.md) — The number of descriptors in the receiver’s descriptor list.
- [stringValue](stringvalue.md) — The contents of the receiver as a Unicode text string, coercing to `typeUnicodeText` if necessary.
- [typeCodeValue](typecodevalue.md) — The contents of the receiver as a type, coercing to `typeType` if necessary.
