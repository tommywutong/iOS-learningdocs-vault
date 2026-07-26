---
title: UTTypeReference
framework: Uniform Type Identifiers
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypereference
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference.json'
content_hash: 'sha256:44aa35d579ce7307'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeReference

<sub>Class</sub>

An object that represents a type of data to load, send, or receive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UTTypeReference
```

## Overview

The [UTTypeReference](uttypereference.md) object may represent files on disk, abstract data types with no on-disk representation, or entirely unrelated hierarchical classification systems, such as hardware. Each instance has a unique [identifier](uttype-swift.struct/identifier.md), and helpful properties, [preferredFilenameExtension](uttype-swift.struct/preferredfilenameextension.md) and [preferredMIMEType](uttype-swift.struct/preferredmimetype.md).

> [!note] Note
> The system includes static declarations for many common types, which you can look up by identifier, filename extension, or MIME type.

The [UTTypeReference](uttypereference.md) object may provide additional information related to the type. For example, it may include a localized user-facing description, a reference URL to technical documentation about the type, or its version number. You can look up types by their conformance to get either a type or a list of types that are relevant to your use case.

To define your own types in your app’s `Info.plist`, see [Defining file and data types for your app](defining-file-and-data-types-for-your-app.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Looking up a type

- [+ typesWithTag:tagClass:conformingToType:](<uttypereference/types(tag_tagclass_conformingto_).md>) — Returns an array of types from the provided tag and tag class.

### Creating a type

- [+ typeWithIdentifier:](<uttypereference/init(__).md>) — Creates a type based on an identifier.
- [+ typeWithMIMEType:](<uttypereference/init(mimetype_)-1txq0.md>) — Creates a type based on a MIME type.
- [+ typeWithMIMEType:conformingToType:](<uttypereference/init(mimetype_conformingto_).md>) — Creates a type based on a MIME type and a supertype that it conforms to.
- [+ typeWithFilenameExtension:](<uttypereference/init(filenameextension_).md>) — Creates a type that represents the specified filename extension.
- [+ typeWithFilenameExtension:conformingToType:](<uttypereference/init(filenameextension_conformingto_).md>) — Creates a type that represents the specified filename extension and conforms to an existing type.
- [init(tag:tagClass:conformingToType:)](<uttypereference/init(tag_tagclass_conformingtotype_).md>) — Creates a type that represents the specified tag and tag class and which conforms to an existing type.
- [+ exportedTypeWithIdentifier:](<uttypereference/init(exportedas_).md>) — Creates a type your app owns based on an identifier.
- [+ exportedTypeWithIdentifier:conformingToType:](<uttypereference/init(exportedas_conformingto_).md>) — Creates a type your app owns based on an identifier and a supertype that it conforms to.
- [+ importedTypeWithIdentifier:](<uttypereference/init(importedas_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier.
- [+ importedTypeWithIdentifier:conformingToType:](<uttypereference/init(importedas_conformingto_).md>) — Creates a type your app uses, but doesn’t own, based on an identifier and a supertype that it conforms to.

### Identifying a type

- [identifier](uttype-swift.struct/identifier.md) — The string that represents the type.

### Obtaining tags

- [preferredFilenameExtension](uttype-swift.struct/preferredfilenameextension.md) — The preferred filename extension for the type.
- [preferredMIMEType](uttype-swift.struct/preferredmimetype.md) — The preferred MIME type for the type.
- [tags](uttype-swift.struct/tags.md) — The tag specification dictionary of the type.

### Obtaining additional type information

- [declared](uttypereference/isdeclared.md) — A Boolean value that indicates whether the system declares the type.
- [dynamic](uttypereference/isdynamic.md) — A Boolean value that indicates whether the system generates the type.
- [publicType](uttypereference/ispublic.md) — A Boolean value that indicates whether the type is in the public domain.
- [referenceURL](uttype-swift.struct/referenceurl.md) — The reference URL for the type.
- [version](uttype-swift.struct/version.md) — The type’s version, if available.

### Checking a type’s relationship to another type

- [supertypes](uttype-swift.struct/supertypes.md) — The set of types the type directly or indirectly conforms to.
- [- conformsToType:](<uttypereference/conforms(to_).md>) — Returns a Boolean value that indicates whether a type conforms to the type.
- [- isSubtypeOfType:](<uttypereference/issubtype(of_).md>) — Returns a Boolean value that indicates whether a type is higher in a hierarchy than the type.
- [- isSupertypeOfType:](<uttypereference/issupertype(of_).md>) — Returns a Boolean value that indicates whether a type is lower in a hierarchy than the type.

### Describing a type

- [localizedDescription](uttype-swift.struct/localizeddescription.md) — A localized description of the type.

### Type Properties

- [shazamCustomCatalog](uttype-swift.struct/shazamcustomcatalog.md) — A type that represents a custom catalog.
- [shazamSignature](uttype-swift.struct/shazamsignature.md) — A type that represents a signature.

### Initializers

- [init(MIMEType:)](<uttypereference/init(mimetype_)-7gu84.md>)
- [init(MIMEType:conformingToType:)](<uttypereference/init(mimetype_conformingtotype_).md>)
- [init(coder:)](<uttypereference/init(coder_).md>)
- [init(filenameExtension:conformingToType:)](<uttypereference/init(filenameextension_conformingtotype_).md>)
- [init(identifier:)](<uttypereference/init(identifier_).md>)
- [+ typeWithIdentifier:allowUndeclared:](<uttypereference/init(identifier_allowundeclared_).md>) _(beta)_
- [+ typeWithTag:tagClass:conformingToType:](<uttypereference/init(tag_tagclass_conformingto_).md>)

### Default Implementations

- [UTTypeReference Implementations](uttypereference/uttypereference-implementations.md)

## See Also

### Uniform type identifiers

- [UTType](uttype-swift.struct.md) — A structure that represents a type of data to load, send, or receive.
- [UTTagClass](uttagclass.md) — A type that represents tag classes.
