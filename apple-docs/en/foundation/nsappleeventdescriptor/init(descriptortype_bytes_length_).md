---
title: 'init(descriptorType:bytes:length:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/init(descriptortype:bytes:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/init(descriptortype:bytes:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/init%28descriptortype%3Abytes%3Alength%3A%29.json'
content_hash: 'sha256:0a5ec577ae8bf0d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# init(descriptorType:bytes:length:)

<sub>Initializer</sub>

Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an arbitrary sequence of bytes and a length count).

<sub>Mac Catalyst, macOS</sub>

```swift
convenience init?(descriptorType: DescType, bytes: UnsafeRawPointer?, length byteCount: Int)
```

## Parameters

- `descriptorType` — The descriptor type to be set in the returned descriptor.

- `bytes` — The data, as a sequence of bytes, to be set in the returned descriptor.

- `byteCount` — The length, in bytes, of the data to be set in the returned descriptor.

## Return Value

An instance of `NSAppleEventDescriptor` with the specified type and data. Returns `nil` if an error occurs.

## See Also

### Creating and Initializing Descriptors

- [+ appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:](<appleevent(witheventclass_eventid_targetdescriptor_returnid_transactionid_).md>) — Creates a descriptor that represents an Apple event, initialized according to the specified information.
- [+ descriptorWithBoolean:](<init(boolean_).md>) — Creates a descriptor initialized with type `typeBoolean` that stores the specified Boolean value.
- [+ descriptorWithEnumCode:](<init(enumcode_).md>) — Creates a descriptor initialized with type `typeEnumerated` that stores the specified enumerator data type value.
- [+ descriptorWithInt32:](<init(int32_).md>) — Creates a descriptor initialized with Apple event type `typeSInt32` that stores the specified integer value.
- [+ descriptorWithString:](<init(string_).md>) — Creates a descriptor initialized with type `typeUnicodeText` that stores the text from the specified string.
- [+ descriptorWithTypeCode:](<init(typecode_).md>) — Creates a descriptor initialized with type `typeType` that stores the specified type value.
- [+ listDescriptor](<list().md>) — Creates and initializes an empty list descriptor.
- [+ nullDescriptor](<null().md>) — Creates and initializes a descriptor with no parameter or attribute values set.
- [+ recordDescriptor](<record().md>) — Creates and initializes a descriptor for an Apple event record whose data has yet to be set.
- [- initListDescriptor](<init(listdescriptor_).md>) — Initializes a newly allocated instance as an empty list descriptor.
- [- initRecordDescriptor](<init(recorddescriptor_).md>) — Initializes a newly allocated instance as a descriptor that is an Apple event record.
- [- initWithAEDescNoCopy:](<init(aedescnocopy_)-5cioa.md>) — Initializes a newly allocated instance as a descriptor for the specified Carbon `AEDesc` structure.
- [- initWithDescriptorType:data:](<init(descriptortype_data_).md>) — Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an instance of `NSData`).
- [- initWithEventClass:eventID:targetDescriptor:returnID:transactionID:](<init(eventclass_eventid_targetdescriptor_returnid_transactionid_).md>) — Initializes a newly allocated instance as a descriptor for an Apple event, initialized with the specified values.
