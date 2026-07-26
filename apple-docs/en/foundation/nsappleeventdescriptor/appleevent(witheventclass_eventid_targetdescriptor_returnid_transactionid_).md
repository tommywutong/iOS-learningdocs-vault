---
title: 'appleEvent(withEventClass:eventID:targetDescriptor:returnID:transactionID:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsappleeventdescriptor/appleevent(witheventclass:eventid:targetdescriptor:returnid:transactionid:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor/appleevent(witheventclass:eventid:targetdescriptor:returnid:transactionid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor/appleevent%28witheventclass%3Aeventid%3Atargetdescriptor%3Areturnid%3Atransactionid%3A%29.json'
content_hash: 'sha256:8f16bb3b49b40370'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAppleEventDescriptor](../nsappleeventdescriptor.md)

# appleEvent(withEventClass:eventID:targetDescriptor:returnID:transactionID:)

<sub>Type Method</sub>

Creates a descriptor that represents an Apple event, initialized according to the specified information.

<sub>Mac Catalyst, macOS</sub>

```swift
class func appleEvent(withEventClass eventClass: AEEventClass, eventID: AEEventID, targetDescriptor: NSAppleEventDescriptor?, returnID: AEReturnID, transactionID: AETransactionID) -> NSAppleEventDescriptor
```

## Parameters

- `eventClass` — The event class to be set in the returned descriptor.

- `eventID` — The event ID to be set in the returned descriptor.

- `targetDescriptor` — A pointer to a descriptor that identifies the target application for the Apple event. Passing `nil` results in an Apple event descriptor that has no `keyAddressAttr` attribute (it is valid for an Apple event to have no target address attribute).

- `returnID` — The return ID to be set in the returned descriptor. If you pass a value of `kAutoGenerateReturnID`, the Apple Event Manager assigns the created Apple event a return ID that is unique to the current session. If you pass any other value, the Apple Event Manager assigns that value for the ID.

- `transactionID` — The transaction ID to be set in the returned descriptor. A transaction is a sequence of Apple events that are sent back and forth between client and server applications, beginning with the client’s initial request for a service. All Apple events that are part of a transaction must have the same transaction ID. You can specify `kAnyTransactionID` if the Apple event is not one of a series of interdependent Apple events.

## Return Value

A descriptor for an Apple event, initialized according to the specified parameter values, or `nil` if an error occurs.

## Discussion

Constants such as `kAutoGenerateReturnID` and `kAnyTransactionID` are defined in `AE.framework`, a subframework of `ApplicationServices.framework`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### Creating and Initializing Descriptors

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
- [- initWithDescriptorType:bytes:length:](<init(descriptortype_bytes_length_).md>) — Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an arbitrary sequence of bytes and a length count).
- [- initWithDescriptorType:data:](<init(descriptortype_data_).md>) — Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an instance of `NSData`).
- [- initWithEventClass:eventID:targetDescriptor:returnID:transactionID:](<init(eventclass_eventid_targetdescriptor_returnid_transactionid_).md>) — Initializes a newly allocated instance as a descriptor for an Apple event, initialized with the specified values.
