---
title: NSAppleEventDescriptor
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsappleeventdescriptor
source_url: 'https://developer.apple.com/documentation/foundation/nsappleeventdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsappleeventdescriptor.json'
content_hash: 'sha256:3464bb79625d6476'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSAppleEventDescriptor

<sub>Class</sub>

A wrapper for the Apple event descriptor data type.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSAppleEventDescriptor
```

## Overview

An instance of [NSAppleEventDescriptor](nsappleeventdescriptor.md) represents a descriptor—the basic building block for Apple events. This class is a wrapper for the underlying Apple event descriptor data type, [AEDesc](../coreservices/aedesc.md). Scriptable Cocoa applications frequently work with instances of [NSAppleEventDescriptor](nsappleeventdescriptor.md), but should rarely need to work directly with the [AEDesc](../coreservices/aedesc.md) data structure.

A _descriptor_ is a data structure that stores data and an accompanying four-character code. A descriptor can store a value, or it can store a list of other descriptors (which may also be lists). All the information in an Apple event is stored in descriptors and lists of descriptors, and every Apple event is itself a descriptor list that matches certain criteria.

> [!important] Important
> An instance of `NSAppleEventDescriptor` can represent any kind of descriptor, from a simple value descriptor, to a descriptor list, to a full-fledged Apple event.

Descriptors can be used to build arbitrarily complex containers, so that one Apple event can represent a script statement such as `tell application "TextEdit" to get word 3 of paragraph 6 of document 3`.

In working with Apple event descriptors, it can be useful to understand some of the underlying data types. You’ll find terms such as descriptor, descriptor list, Apple event record, and Apple event defined in Building an Apple Event in Apple Events Programming Guide. You’ll also find information on the four-character codes used to identify information within a descriptor. Apple event data types are defined in [Apple Event Manager](../applicationservices/apple_event_manager.md). The values of many four-character codes used by Apple (and in some cases reused by developers) can be found in [AppleScript Terminology and Apple Event Codes](http://developer.apple.com/releasenotes/AppleScript/ASTerminology_AppleEventCodes/TermsAndCodes.html).

The most common reason to construct an Apple event with an instance of `NSAppleEventDescriptor` is to supply information in a return Apple event. The most common situation where you might need to extract information from an Apple event (as an instance of `NSAppleEventDescriptor`) is when an Apple event handler installed by your application is invoked, as described in “Installing an Apple Event Handler” in [How Cocoa Applications Handle Apple Events](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_handle_AEs/SAppsHandleAEs.html#//apple_ref/doc/uid/20001239). In addition, if you execute an AppleScript script using the `NSAppleScript` class, you get an instance of `NSAppleEventDescriptor` as the return value, from which you can extract any required information.

When you work with an instance of `NSAppleEventDescriptor`, you can access the underlying descriptor directly, if necessary, with the [aeDesc](nsappleeventdescriptor/aedesc.md) method. Other methods, including [descriptorWithDescriptorType:bytes:length:](nsappleeventdescriptor/descriptorwithdescriptortype_bytes_length_.md) make it possible to create and initialize instances of `NSAppleEventDescriptor` without creating temporary instances of `NSData`.

The designated initializer for `NSAppleEventDescriptor` is [- initWithAEDescNoCopy:](<nsappleeventdescriptor/init(aedescnocopy_)-5cioa.md>). However, it is unlikely that you will need to create a subclass of `NSAppleEventDescriptor`.

Cocoa doesn’t currently provide a mechanism for applications to directly send raw Apple events (though compiling and executing an AppleScript script with `NSAppleScript` may result in Apple events being sent). However, Cocoa applications have full access to the Apple Event Manager C APIs for working with Apple events. So, for example, you might use an instance of  `NSAppleEventDescriptor` to assemble an Apple event and call the Apple Event Manager function `AESend(_:_:_:_:_:_:_:)` to send it.

If you need to send Apple events, or if you need more information on some of the Apple event concepts described here, see Apple Events Programming Guide and [Apple Event Manager](../applicationservices/apple_event_manager.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating and Initializing Descriptors

- [+ appleEventWithEventClass:eventID:targetDescriptor:returnID:transactionID:](<nsappleeventdescriptor/appleevent(witheventclass_eventid_targetdescriptor_returnid_transactionid_).md>) — Creates a descriptor that represents an Apple event, initialized according to the specified information.
- [+ descriptorWithBoolean:](<nsappleeventdescriptor/init(boolean_).md>) — Creates a descriptor initialized with type `typeBoolean` that stores the specified Boolean value.
- [+ descriptorWithEnumCode:](<nsappleeventdescriptor/init(enumcode_).md>) — Creates a descriptor initialized with type `typeEnumerated` that stores the specified enumerator data type value.
- [+ descriptorWithInt32:](<nsappleeventdescriptor/init(int32_).md>) — Creates a descriptor initialized with Apple event type `typeSInt32` that stores the specified integer value.
- [+ descriptorWithString:](<nsappleeventdescriptor/init(string_).md>) — Creates a descriptor initialized with type `typeUnicodeText` that stores the text from the specified string.
- [+ descriptorWithTypeCode:](<nsappleeventdescriptor/init(typecode_).md>) — Creates a descriptor initialized with type `typeType` that stores the specified type value.
- [+ listDescriptor](<nsappleeventdescriptor/list().md>) — Creates and initializes an empty list descriptor.
- [+ nullDescriptor](<nsappleeventdescriptor/null().md>) — Creates and initializes a descriptor with no parameter or attribute values set.
- [+ recordDescriptor](<nsappleeventdescriptor/record().md>) — Creates and initializes a descriptor for an Apple event record whose data has yet to be set.
- [- initListDescriptor](<nsappleeventdescriptor/init(listdescriptor_).md>) — Initializes a newly allocated instance as an empty list descriptor.
- [- initRecordDescriptor](<nsappleeventdescriptor/init(recorddescriptor_).md>) — Initializes a newly allocated instance as a descriptor that is an Apple event record.
- [- initWithAEDescNoCopy:](<nsappleeventdescriptor/init(aedescnocopy_)-5cioa.md>) — Initializes a newly allocated instance as a descriptor for the specified Carbon `AEDesc` structure.
- [- initWithDescriptorType:bytes:length:](<nsappleeventdescriptor/init(descriptortype_bytes_length_).md>) — Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an arbitrary sequence of bytes and a length count).
- [- initWithDescriptorType:data:](<nsappleeventdescriptor/init(descriptortype_data_).md>) — Initializes a newly allocated instance as a descriptor with the specified descriptor type and data (from an instance of `NSData`).
- [- initWithEventClass:eventID:targetDescriptor:returnID:transactionID:](<nsappleeventdescriptor/init(eventclass_eventid_targetdescriptor_returnid_transactionid_).md>) — Initializes a newly allocated instance as a descriptor for an Apple event, initialized with the specified values.

### Getting Information About a Descriptor

- [aeDesc](nsappleeventdescriptor/aedesc.md) — The `AEDesc` structure encapsulated by the receiver, if it has one.
- [booleanValue](nsappleeventdescriptor/booleanvalue.md) — The contents of the receiver as a Boolean value, coercing (to `typeBoolean`) if necessary.
- [- coerceToDescriptorType:](<nsappleeventdescriptor/coerce(todescriptortype_).md>) — Returns a descriptor obtained by coercing the receiver to the specified type.
- [data](nsappleeventdescriptor/data.md) — The receiver’s data.
- [descriptorType](nsappleeventdescriptor/descriptortype.md) — The descriptor type of the receiver.
- [enumCodeValue](nsappleeventdescriptor/enumcodevalue.md) — The contents of the receiver as an enumeration type, coercing to `typeEnumerated` if necessary.
- [int32Value](nsappleeventdescriptor/int32value.md) — The contents of the receiver as an integer, coercing (to `typeSInt32`) if necessary.
- [numberOfItems](nsappleeventdescriptor/numberofitems.md) — The number of descriptors in the receiver’s descriptor list.
- [stringValue](nsappleeventdescriptor/stringvalue.md) — The contents of the receiver as a Unicode text string, coercing to `typeUnicodeText` if necessary.
- [typeCodeValue](nsappleeventdescriptor/typecodevalue.md) — The contents of the receiver as a type, coercing to `typeType` if necessary.

### Working With List Descriptors

- [- descriptorAtIndex:](<nsappleeventdescriptor/atindex(__).md>) — Returns the descriptor at the specified (one-based) position in the receiving descriptor list.
- [- insertDescriptor:atIndex:](<nsappleeventdescriptor/insert(__at_).md>) — Inserts a descriptor at the specified (one-based) position in the receiving descriptor list, replacing the existing descriptor, if any, at that position.
- [- removeDescriptorAtIndex:](<nsappleeventdescriptor/remove(at_).md>) — Removes the descriptor at the specified (one-based) position in the receiving descriptor list.

### Working With Record Descriptors

- [- descriptorForKeyword:](<nsappleeventdescriptor/forkeyword(__).md>) — Returns the receiver’s descriptor for the specified keyword.
- [- keywordForDescriptorAtIndex:](<nsappleeventdescriptor/keywordfordescriptor(at_).md>) — Returns the keyword for the descriptor at the specified (one-based) position in the receiver.
- [- removeDescriptorWithKeyword:](<nsappleeventdescriptor/remove(withkeyword_).md>) — Removes the receiver’s descriptor identified by the specified keyword.
- [- setDescriptor:forKeyword:](<nsappleeventdescriptor/setdescriptor(__forkeyword_).md>) — Adds a descriptor, identified by a keyword, to the receiver.

### Working With Apple Event Descriptors

- [- attributeDescriptorForKeyword:](<nsappleeventdescriptor/attributedescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event attribute identified by the specified keyword.
- [eventClass](nsappleeventdescriptor/eventclass.md) — The event class for the receiver.
- [eventID](nsappleeventdescriptor/eventid.md) — The event ID for the receiver.
- [- paramDescriptorForKeyword:](<nsappleeventdescriptor/paramdescriptor(forkeyword_).md>) — Returns a descriptor for the receiver’s Apple event parameter identified by the specified keyword.
- [- removeParamDescriptorWithKeyword:](<nsappleeventdescriptor/removeparamdescriptor(withkeyword_).md>) — Removes the receiver’s parameter descriptor identified by the specified keyword.
- [returnID](nsappleeventdescriptor/returnid.md) — The receiver’s return ID (the ID for a reply Apple event).
- [- setAttributeDescriptor:forKeyword:](<nsappleeventdescriptor/setattribute(__forkeyword_).md>) — Adds a descriptor to the receiver as an attribute identified by the specified keyword.
- [- setParamDescriptor:forKeyword:](<nsappleeventdescriptor/setparam(__forkeyword_).md>) — Adds a descriptor to the receiver as an Apple event parameter identified by the specified keyword.
- [transactionID](nsappleeventdescriptor/transactionid.md) — The receiver’s transaction ID, if any.

### Supporting Types

- [SendOptions](nsappleeventdescriptor/sendoptions.md)

### Initializers

- [init(AEDescNoCopy:)](<nsappleeventdescriptor/init(aedescnocopy_)-236vs.md>)
- [+ descriptorWithApplicationURL:](<nsappleeventdescriptor/init(applicationurl_).md>) — Creates and returns an application address descriptor using the specified application URL.
- [+ descriptorWithBundleIdentifier:](<nsappleeventdescriptor/init(bundleidentifier_).md>) — Creates and returns an application address descriptor using the specified bundle identifier.
- [init(coder:)](<nsappleeventdescriptor/init(coder_).md>)
- [+ descriptorWithDate:](<nsappleeventdescriptor/init(date_).md>) — Creates a descriptor that stores the specified date value.
- [+ descriptorWithDouble:](<nsappleeventdescriptor/init(double_).md>) — Creates a descriptor initialized with Apple event type `typeIEEE64BitFloatingPoint` that stores the specified double value.
- [+ descriptorWithFileURL:](<nsappleeventdescriptor/init(fileurl_).md>) — Creates a descriptor that stores the specified file URL.
- [+ descriptorWithProcessIdentifier:](<nsappleeventdescriptor/init(processidentifier_).md>) — Creates and returns an application address descriptor using the specified process identifier.

### Instance Properties

- [dateValue](nsappleeventdescriptor/datevalue.md) — The contents of the receiver as a date, coercing if necessary.
- [doubleValue](nsappleeventdescriptor/doublevalue.md) — The contents of the receiver as a double value, coercing (to `typeIEEE64BitFloatingPoint`) if necessary.
- [fileURLValue](nsappleeventdescriptor/fileurlvalue.md) — The contents of the receiver as a file URL, coercing if necessary.
- [isRecordDescriptor](nsappleeventdescriptor/isrecorddescriptor.md) — Returns whether or not the receiver is a record-like descriptor.

### Instance Methods

- [- sendEventWithOptions:timeout:error:](<nsappleeventdescriptor/sendevent(options_timeout_).md>) — Sends an Apple event.

### Type Methods

- [+ currentProcessDescriptor](<nsappleeventdescriptor/currentprocess().md>) — Creates and returns an application address descriptor using the current process.

## See Also

### Apple Event Handling

- [NSAppleEventManager](nsappleeventmanager.md) — A mechanism for registering handler routines for specific types of Apple events and dispatching events to those handlers.
