---
title: NSMutableDictionary
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutabledictionary
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledictionary.json'
content_hash: 'sha256:25d08f65a0134101'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMutableDictionary

<sub>Class</sub>

A dynamic collection of objects associated with unique keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSMutableDictionary
```

## Overview

In Swift, you can use this type instead of a [Dictionary](../swift/dictionary.md) variable in cases that require reference semantics.

The `NSMutableDictionary` class declares the programmatic interface to objects that manage mutable associations of keys and values. It adds modification operations to the basic operations it inherits from [NSDictionary](nsdictionary.md).

`NSMutableDictionary` is “toll-free bridged” with its Core Foundation counterpart, [CFMutableDictionary](../corefoundation/cfmutabledictionary.md). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

### Setting Values Using Subscripting

In addition to the provided instance methods, such as [- setObject:forKey:](<nsmutabledictionary/setobject(__forkey_).md>), you can access `NSDictionary` values by their keys using _subscripting_.

**Swift**

```swift
let value = "someValue"
mutableDictionary["someKey"] = value
```

**Objective-C**

```objc
id value = @"someValue";
mutableDictionary[@"someKey"] = value;
```

### Subclassing Notes

There should typically be little need to subclass `NSMutableDictionary`. If you do need to customize behavior, it is often better to consider composition rather than subclassing.

#### Methods to Override

In a subclass, you must override both of its primitive methods:

- [- setObject:forKey:](<nsmutabledictionary/setobject(__forkey_).md>)
- [- removeObjectForKey:](<nsmutabledictionary/removeobject(forkey_).md>)

You must also override the primitive methods of the [NSDictionary](nsdictionary.md) class.

## Relationships

- **Inherits From**: [NSDictionary](nsdictionary.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomReflectable](../swift/customreflectable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [ExpressibleByDictionaryLiteral](../swift/expressiblebydictionaryliteral.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSFastEnumeration](nsfastenumeration.md), [NSMutableCopying](nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating and Initializing a Mutable Dictionary

- [- initWithCapacity:](<nsmutabledictionary/init(capacity_).md>) — Initializes a newly allocated mutable dictionary, allocating enough memory to hold `numItems` entries.
- [- init](<nsmutabledictionary/init().md>) — Initializes a newly allocated mutable dictionary.
- [+ dictionaryWithSharedKeySet:](<nsmutabledictionary/init(sharedkeyset_).md>) — Creates a mutable dictionary which is optimized for dealing with a known set of keys.

### Adding Entries to a Mutable Dictionary

- [- setObject:forKey:](<nsmutabledictionary/setobject(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- setValue:forKey:](<nsmutabledictionary/setvalue(__forkey_).md>) — Adds a given key-value pair to the dictionary.
- [- addEntriesFromDictionary:](<nsmutabledictionary/addentries(from_).md>) — Adds to the receiving dictionary the entries from another dictionary.
- [- setDictionary:](<nsmutabledictionary/setdictionary(__).md>) — Sets the contents of the receiving dictionary to entries in a given dictionary.

### Removing Entries From a Mutable Dictionary

- [- removeObjectForKey:](<nsmutabledictionary/removeobject(forkey_).md>) — Removes a given key and its associated value from the dictionary.
- [- removeAllObjects](<nsmutabledictionary/removeallobjects().md>) — Empties the dictionary of its entries.
- [- removeObjectsForKeys:](<nsmutabledictionary/removeobjects(forkeys_).md>) — Removes from the dictionary entries specified by elements in a given array.

### Initializers

- [+ dictionaryWithOBEXHeadersData:](<nsmutabledictionary/init(obexheadersdata_).md>)
- [+ dictionaryWithOBEXHeadersData:headersDataSize:](<nsmutabledictionary/init(obexheadersdata_headersdatasize_).md>)
- [- initWithCoder:](<nsmutabledictionary/init(coder_).md>)

### Instance Methods

- [- addApplicationParameterHeader:length:](<nsmutabledictionary/addapplicationparameterheader(__length_).md>)
- [- addAuthorizationChallengeHeader:length:](<nsmutabledictionary/addauthorizationchallengeheader(__length_).md>)
- [- addAuthorizationResponseHeader:length:](<nsmutabledictionary/addauthorizationresponseheader(__length_).md>)
- [- addBodyHeader:length:endOfBody:](<nsmutabledictionary/addbodyheader(__length_endofbody_).md>)
- [- addByteSequenceHeader:length:](<nsmutabledictionary/addbytesequenceheader(__length_).md>)
- [- addConnectionIDHeader:length:](<nsmutabledictionary/addconnectionidheader(__length_).md>)
- [- addCountHeader:](<nsmutabledictionary/addcountheader(__).md>)
- [- addDescriptionHeader:](<nsmutabledictionary/adddescriptionheader(__).md>)
- [- addHTTPHeader:length:](<nsmutabledictionary/addhttpheader(__length_).md>)
- [- addImageDescriptorHeader:length:](<nsmutabledictionary/addimagedescriptorheader(__length_).md>)
- [- addImageHandleHeader:](<nsmutabledictionary/addimagehandleheader(__).md>)
- [- addLengthHeader:](<nsmutabledictionary/addlengthheader(__).md>)
- [- addNameHeader:](<nsmutabledictionary/addnameheader(__).md>)
- [- addObjectClassHeader:length:](<nsmutabledictionary/addobjectclassheader(__length_).md>)
- [- addTargetHeader:length:](<nsmutabledictionary/addtargetheader(__length_).md>)
- [- addTime4ByteHeader:](<nsmutabledictionary/addtime4byteheader(__).md>)
- [- addTimeISOHeader:length:](<nsmutabledictionary/addtimeisoheader(__length_).md>)
- [- addTypeHeader:](<nsmutabledictionary/addtypeheader(__).md>)
- [- addUserDefinedHeader:length:](<nsmutabledictionary/adduserdefinedheader(__length_).md>)
- [- addWhoHeader:length:](<nsmutabledictionary/addwhoheader(__length_).md>)
- [- getHeaderBytes](<nsmutabledictionary/getheaderbytes().md>)

### Default Implementations

- [NSDictionary Implementations](nsmutabledictionary/nsdictionary-implementations.md)
- [NSMutableDictionary Implementations](nsmutabledictionary/nsmutabledictionary-implementations.md)
