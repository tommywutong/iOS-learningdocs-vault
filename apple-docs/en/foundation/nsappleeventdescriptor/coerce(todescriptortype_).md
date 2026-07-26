---
title: 'coerce(toDescriptorType:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/coerce(todescriptortype:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/coerce(todescriptortype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/coerce%28todescriptortype%3A%29.json'
content_hash: 'sha256:ca021beb25a4ed73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# coerce(toDescriptorType:)

<sub>Instance Method</sub>

Returns a descriptor obtained by coercing the receiver to the specified type.

<sub>Mac Catalyst, macOS</sub>

```swift
func coerce(toDescriptorType descriptorType: DescType) -> NSAppleEventDescriptor?
```

## Parameters

- `descriptorType` — The descriptor type to coerce the receiver to.

## Return Value

A descriptor of the specified type, or `nil` if an error occurs.

## See Also

### Getting Information About a Descriptor

- [aeDesc](aedesc.md) — The `AEDesc` structure encapsulated by the receiver, if it has one.
- [booleanValue](booleanvalue.md) — The contents of the receiver as a Boolean value, coercing (to `typeBoolean`) if necessary.
- [data](data.md) — The receiver’s data.
- [descriptorType](descriptortype.md) — The descriptor type of the receiver.
- [enumCodeValue](enumcodevalue.md) — The contents of the receiver as an enumeration type, coercing to `typeEnumerated` if necessary.
- [int32Value](int32value.md) — The contents of the receiver as an integer, coercing (to `typeSInt32`) if necessary.
- [numberOfItems](numberofitems.md) — The number of descriptors in the receiver’s descriptor list.
- [stringValue](stringvalue.md) — The contents of the receiver as a Unicode text string, coercing to `typeUnicodeText` if necessary.
- [typeCodeValue](typecodevalue.md) — The contents of the receiver as a type, coercing to `typeType` if necessary.
