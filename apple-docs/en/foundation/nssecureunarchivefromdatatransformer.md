---
title: NSSecureUnarchiveFromDataTransformer
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssecureunarchivefromdatatransformer
source_url: 'https://developer.apple.com/documentation/foundation/nssecureunarchivefromdatatransformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssecureunarchivefromdatatransformer.json'
content_hash: 'sha256:8fc639571d8acf80'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSecureUnarchiveFromDataTransformer

<sub>Class</sub>

A value transformer that converts data to and from classes that support secure coding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSSecureUnarchiveFromDataTransformer
```

## Overview

This class provides a default [ValueTransformer](valuetransformer.md) implementation for secure decoding. This class attempts to decode data into the classes listed within [allowedTopLevelClasses](nssecureunarchivefromdatatransformer/allowedtoplevelclasses.md), which includes [NSArray](nsarray.md), [NSDictionary](nsdictionary.md), [NSSet](nsset.md), [NSString](nsstring.md), [NSNumber](nsnumber.md), [NSDate](nsdate.md), [NSData](nsdata.md), [NSURL](nsurl.md), [NSUUID](nsuuid.md), and [NSNull](nsnull.md).

To archive or unarchive other classes that support [NSSecureCoding](nssecurecoding.md), create a subclass and override [allowedTopLevelClasses](nssecureunarchivefromdatatransformer/allowedtoplevelclasses.md) to list the classes to transform.

To use [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md) with [Core Data](../coredata.md), use the name of this class, or the name of a subclass you implement, as the name of the transformer for an entity’s attribute within a Core Data Model. If you use your own transformer subclass, register it with your app before intializing your persistent container with Core Data.

For an example of subclassing [NSSecureUnarchiveFromDataTransformer](nssecureunarchivefromdatatransformer.md), see [Handling Different Data Types in Core Data](../coredata/handling-different-data-types-in-core-data.md), which has a `ColorToDataTransformer` class that transforms [UIColor](../uikit/uicolor.md) to [NSData](nsdata.md) and the reverse, to support archiving instances of [UIColor](../uikit/uicolor.md).

## Relationships

- **Inherits From**: [ValueTransformer](valuetransformer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Information About a Transformer

- [allowedTopLevelClasses](nssecureunarchivefromdatatransformer/allowedtoplevelclasses.md) — A list of allowed classes the top-level object in an archive must conform to, for encoding and decoding.

## See Also

### Keyed Archivers

- [NSKeyedArchiver](nskeyedarchiver.md) — An encoder that stores an object’s data to an archive referenced by keys.
- [NSKeyedArchiverDelegate](nskeyedarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed archiver.
- [NSKeyedUnarchiver](nskeyedunarchiver.md) — A decoder that restores data from an archive referenced by keys.
- [NSKeyedUnarchiverDelegate](nskeyedunarchiverdelegate.md) — The optional methods implemented by the delegate of a keyed unarchiver.
- [NSCoder](nscoder.md) — An abstract class that serves as the basis for objects that enable archiving and distribution of other objects.
