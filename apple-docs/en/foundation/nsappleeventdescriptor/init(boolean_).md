---
title: 'init(boolean:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/init(boolean:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/init(boolean:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/init%28boolean%3A%29.json'
content_hash: 'sha256:47eb9f85003a9df7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# init(boolean:)

<sub>Initializer</sub>

Creates a descriptor initialized with type `typeBoolean` that stores the specified Boolean value.

<sub>Mac Catalyst, macOS</sub>

```swift
init(boolean: Bool)
```

## Parameters

- `boolean` — The Boolean value to be set in the returned descriptor.

## Return Value

A descriptor with the specified Boolean value, or `nil` if an error occurs.

## See Also

### Creating and Initializing Descriptors

- [+ appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:](<appleevent(witheventclass_eventid_targetdescriptor_returnid_transactionid_).md>) — Creates a descriptor that represents an Apple event, initialized according to the specified information.
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
- [- initWithDescriptorType:bytes:length:](<init(descriptortype_bytes_length_).md>) — Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an arbitrary sequence of bytes and a length count).
- [- initWithDescriptorType:data:](<init(descriptortype_data_).md>) — Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an instance of `NSData`).
- [- initWithEventClass:eventID:targetDescriptor:returnID:transactionID:](<init(eventclass_eventid_targetdescriptor_returnid_transactionid_).md>) — Initializes a newly allocated instance as a descriptor for an Apple event, initialized with the specified values.
