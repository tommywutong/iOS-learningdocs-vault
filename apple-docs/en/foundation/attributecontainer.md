---
title: AttributeContainer
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributecontainer
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer.json'
content_hash: 'sha256:84da1ec274a454ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# AttributeContainer

<sub>Structure</sub>

A container for attribute keys and values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct AttributeContainer
```

## Overview

[AttributeContainer](attributecontainer.md) provides a way to store attributes and their values outside of an attributed string. You use this type to initialize an instance of [AttributedString](attributedstring.md) with preset attributes, and to set, merge, or replace attributes in existing attributed strings.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomStringConvertible](../swift/customstringconvertible.md), [DecodableWithConfiguration](decodablewithconfiguration.md), [EncodableWithConfiguration](encodablewithconfiguration.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an Attribute Container

- [init()](<attributecontainer/init().md>) — Creates an empty attribute container.
- [init(_:including:)](<attributecontainer/init(__including_)-2mw0o.md>) — Creates an attribute container from a dictionary and an attribute scope.
- [init(_:including:)](<attributecontainer/init(__including_)-28n0g.md>) — Creates an attribute container from a dictionary and an attribute scope that a key path identifies.
- [init(_:)](<attributecontainer/init(__).md>) — Creates an attribute container from a dictionary, using default attribute scopes.

### Accessing Attributes

- [subscript(_:)](<attributecontainer/subscript(__).md>) — Returns the attribute that corresponds to a specified key.
- [subscript(dynamicMember:)](<attributecontainer/subscript(dynamicmember_)-657oj.md>) — Returns the attribute that corresponds to a specified key path.
- [subscript(dynamicMember:)](<attributecontainer/subscript(dynamicmember_)-3jcvx.md>) — Returns the attribute container that corresponds to a specified key path.
- [subscript(dynamicMember:)](<attributecontainer/subscript(dynamicmember_)-60ps5.md>) — Returns a modified attribute container as part of building a chain of attributes.
- [subscript(dynamicMember:)](<attributecontainer/subscript(dynamicmember_)-swift.type.subscript.md>) — Returns a modified attribute container as part of building a chain of attributes, for use as a static method.
- [AttributedStringKey](attributedstringkey.md) — A type that defines an attribute’s name and type.
- [Builder](attributecontainer/builder.md) — A type that iteratively builds attribute containers by setting attribute values.

### Modifying Attributes

- [merge(_:mergePolicy:)](<attributecontainer/merge(__mergepolicy_).md>) — Merges the container’s attributes with those in another attribute container.
- [merging(_:mergePolicy:)](<attributecontainer/merging(__mergepolicy_).md>) — Returns an attribute container by merging the container’s attributes with those in another attribute container.
- [AttributeMergePolicy](attributedstring/attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.

### Interoperating with Objective-C Attributes

- [ObjectiveCConvertibleAttributedStringKey](objectivecconvertibleattributedstringkey.md) — A protocol that defines Objective-C interoperability with an attribute key’s value type.

### Instance Methods

- [filter(inheritedByAddedText:)](<attributecontainer/filter(inheritedbyaddedtext_).md>) — Returns a copy of the attribute container with only attributes that specify the provided inheritance behavior.
- [filter(runBoundaries:)](<attributecontainer/filter(runboundaries_).md>) — Returns a copy of the attribute container with only attributes that have the provided run boundaries.

## See Also

### Creating an Attributed String

- [init()](<attributedstring/init().md>) — Creates an empty attributed string.
- [init(_:)](<attributedstring/init(__)-8tnoq.md>) — Creates an attributed string from an attributed substring.
- [init(_:attributes:)](<attributedstring/init(__attributes_)-2a45h.md>) — Creates an attributed string from a string and an attribute container.
- [init(_:attributes:)](<attributedstring/init(__attributes_)-8jqhp.md>) — Creates an attributed string from a substring and an attribute container.
- [init(_:attributes:)](<attributedstring/init(__attributes_)-8l0iq.md>) — Creates an attributed string from a character sequence and an attribute container.
