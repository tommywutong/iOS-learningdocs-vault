---
title: 'descriptorWithDescriptorType:data:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/descriptorwithdescriptortype:data:'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/descriptorwithdescriptortype:data:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/descriptorwithdescriptortype%3Adata%3A.json'
content_hash: 'sha256:18d6d2b88d777ec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# descriptorWithDescriptorType:data:

<sub>Type Method</sub>

Creates a descriptor initialized with the specified event type that stores the specified data (from an instance of `NSData`).

<sub>Mac Catalyst, macOS</sub>

```objc
+ (NSAppleEventDescriptor *) descriptorWithDescriptorType:(DescType) descriptorType data:(NSData *) data;
```

## Parameters

- `descriptorType` — The descriptor type to be set in the returned descriptor.

- `data` — The data, as an instance of `NSData`, to be set in the returned descriptor.

## Return Value

A descriptor with the specified type and data, or `nil` if an error occurs.

## Discussion

You can use this method to create a descriptor that you can build into a complete Apple event by calling methods such as [- setAttributeDescriptor:forKeyword:](<setattribute(__forkeyword_).md>), [- setDescriptor:forKeyword:](<setdescriptor(__forkeyword_).md>), and [- setParamDescriptor:forKeyword:](<setparam(__forkeyword_).md>).

## See Also

### Creating and Initializing Descriptors

- [+ appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:](<appleevent(witheventclass_eventid_targetdescriptor_returnid_transactionid_).md>) — Creates a descriptor that represents an Apple event, initialized according to the specified information.
- [+ descriptorWithBoolean:](<init(boolean_).md>) — Creates a descriptor initialized with type `typeBoolean` that stores the specified Boolean value.
- [descriptorWithDescriptorType:bytes:length:](descriptorwithdescriptortype_bytes_length_.md) — Creates a descriptor initialized with the specified event type that stores the specified data (from a series of bytes).
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
