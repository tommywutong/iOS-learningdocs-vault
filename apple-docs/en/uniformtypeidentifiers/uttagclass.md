---
title: UTTagClass
framework: Uniform Type Identifiers
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttagclass
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttagclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttagclass.json'
content_hash: 'sha256:dc51a459e82e08a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTagClass

<sub>Structure</sub>

A type that represents tag classes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct UTTagClass
```

## Overview

A tag class is a label that represents the mapping of a [UTType](uttype-swift.struct.md) to another type system; for example, a MIME type or a file system extension.

A tag is a specific instance of a tag class. For example, the tag `txt` is an instance of the tag class [UTTagClassFilenameExtension](uttagclassfilenameextension.md) and represents the type [UTTypePlainText](uttypeplaintext.md).

[UTTagClass](uttagclass.md) uses an untyped `String` or [CFString](../corefoundation/cfstring.md) to refer to a tag class as a string. To get the string representation of a tag class, use its `rawValue-swift.property` property.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md)

## Topics

### Getting a declared types mapping

- [filenameExtension](uttagclass/filenameextension.md) — A type property that returns the tag class used to map a type to a filename extension.
- [mimeType](uttagclass/mimetype.md) — A type property that returns the tag class used to map a type to a MIME type.

## See Also

### Uniform type identifiers

- [UTType](uttype-swift.struct.md) — A structure that represents a type of data to load, send, or receive.
- [UTTypeReference](uttypereference.md) — An object that represents a type of data to load, send, or receive.
