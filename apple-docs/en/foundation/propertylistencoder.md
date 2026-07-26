---
title: PropertyListEncoder
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/propertylistencoder
source_url: 'https://developer.apple.com/documentation/foundation/propertylistencoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistencoder.json'
content_hash: 'sha256:dbe14298f7e46372'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PropertyListEncoder

<sub>Class</sub>

An object that encodes instances of data types to a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class PropertyListEncoder
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [NetworkEncoder](../network/networkencoder.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TopLevelEncoder](../combine/toplevelencoder.md)

## Topics

### Encoding

- [init()](<propertylistencoder/init().md>) — Creates a new, reusable property list encoder with the default formatting settings.
- [encode(_:)](<propertylistencoder/encode(__).md>) — Returns a property list that represents an encoded version of the value you supply.
- [encode(_:configuration:)](<propertylistencoder/encode(__configuration_)-4biuh.md>)
- [encode(_:configuration:)](<propertylistencoder/encode(__configuration_)-5ee8q.md>)

### Customizing Encoding

- [outputFormat](propertylistencoder/outputformat.md) — A value that determines which property list format is used during encoding.
- [userInfo](propertylistencoder/userinfo.md) — A dictionary you use to customize the encoding process by providing contextual information.

## See Also

### Property Lists

- [PropertyListDecoder](propertylistdecoder.md) — An object that decodes instances of data types from a property list.
- [PropertyListSerialization](propertylistserialization.md) — An object that converts between a property list and one of several serialized representations.
