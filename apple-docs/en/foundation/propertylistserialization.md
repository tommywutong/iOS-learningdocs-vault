---
title: PropertyListSerialization
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/propertylistserialization
source_url: 'https://developer.apple.com/documentation/foundation/propertylistserialization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistserialization.json'
content_hash: 'sha256:5a5728cc55e534eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PropertyListSerialization

<sub>Class</sub>

An object that converts between a property list and one of several serialized representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class PropertyListSerialization
```

## Overview

The [PropertyListSerialization](propertylistserialization.md) class provides methods that convert a property list to and from several serialized formats. A property list is itself an array or dictionary that contains only [NSData](nsdata.md), [NSString](nsstring.md), [NSArray](nsarray.md), [NSDictionary](nsdictionary.md), [NSDate](nsdate.md), and [NSNumber](nsnumber.md) objects.

Property list objects are toll-free bridged with their respective Core Foundation types ([CFData](../corefoundation/cfdata.md), [CFString](../corefoundation/cfstring.md), and so on). See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2)  for more information on toll-free bridging.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Serializing a Property List

- [+ dataWithPropertyList:format:options:error:](<propertylistserialization/data(frompropertylist_format_options_).md>) — Returns an `NSData` object containing a given property list in a specified format.
- [+ writePropertyList:toStream:format:options:error:](<propertylistserialization/writepropertylist(__to_format_options_error_).md>) — Writes a property list to the specified stream.
- [WriteOptions](propertylistserialization/writeoptions.md)

### Deserializing a Property List

- [+ propertyListWithData:options:format:error:](<propertylistserialization/propertylist(from_options_format_).md>) — Creates and returns a property list from the specified data.
- [+ propertyListWithStream:options:format:error:](<propertylistserialization/propertylist(with_options_format_).md>) — Creates and returns a property list by reading from the specified stream.

### Validating a Property List

- [+ propertyList:isValidForFormat:](<propertylistserialization/propertylist(__isvalidfor_).md>) — Returns a Boolean value that indicates whether a given property list is valid for a given format.

### Obsolete Methods

- [+ dataFromPropertyList:format:errorDescription:](<propertylistserialization/datafrompropertylist(__format_errordescription_).md>) — This method is obsolete and will be deprecated soon. _(deprecated)_
- [+ propertyListFromData:mutabilityOption:format:errorDescription:](<propertylistserialization/propertylistfromdata(__mutabilityoption_format_errordescription_).md>) — This method is deprecated. Use [+ dataWithPropertyList:format:options:error:](<propertylistserialization/data(frompropertylist_format_options_).md>) instead. _(deprecated)_

### Constants

- [MutabilityOptions](propertylistserialization/mutabilityoptions.md) — These constants specify mutability options in property lists.
- [PropertyListFormat](propertylistserialization/propertylistformat.md) — These constants are used to specify a property list serialization format.
- [ReadOptions](propertylistserialization/readoptions.md) — The only read options supported are described in [MutabilityOptions](propertylistserialization/mutabilityoptions.md).

### Error Codes

- [NSPropertyListReadCorruptError](nspropertylistreadcorrupterror-swift.var.md) — Parsing of the property list failed.
- [NSPropertyListReadUnknownVersionError](nspropertylistreadunknownversionerror-swift.var.md) — The version number of the property list cannot be determined.
- [NSPropertyListReadStreamError](nspropertylistreadstreamerror-swift.var.md) — Reading of the property list failed.
- [NSPropertyListWriteStreamError](nspropertylistwritestreamerror-swift.var.md) — Writing to the property list failed.
- [NSPropertyListWriteInvalidError](nspropertylistwriteinvaliderror-swift.var.md) — Writing failed because of an invalid property list object, or an invalid property list type was specified.
- [NSPropertyListErrorMinimum](nspropertylisterrorminimum-swift.var.md) — The start of the range of error codes reserved for property list errors.
- [NSPropertyListErrorMaximum](nspropertylisterrormaximum-swift.var.md) — The end of the range of error codes reserved for property list errors.

## See Also

### Property Lists

- [PropertyListEncoder](propertylistencoder.md) — An object that encodes instances of data types to a property list.
- [PropertyListDecoder](propertylistdecoder.md) — An object that decodes instances of data types from a property list.
