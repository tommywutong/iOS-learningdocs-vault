---
title: PropertyListDecoder
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/propertylistdecoder
source_url: 'https://developer.apple.com/documentation/foundation/propertylistdecoder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistdecoder.json'
content_hash: 'sha256:536ecbf233b5cc56'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PropertyListDecoder

<sub>Class</sub>

An object that decodes instances of data types from a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class PropertyListDecoder
```

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [NetworkDecoder](../network/networkdecoder.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [TopLevelDecoder](../combine/topleveldecoder.md)

## Topics

### Decoding

- [init()](<propertylistdecoder/init().md>) — Creates a new, reusable property list decoder.
- [decode(_:from:)](<propertylistdecoder/decode(__from_).md>) — Returns a value of the specified type by decoding a property list using the default property list format.

### Customizing Decoding

- [decode(_:from:format:)](<propertylistdecoder/decode(__from_format_).md>) — Returns a value of the specified type by decoding a property list using the supplied format.
- [userInfo](propertylistdecoder/userinfo.md) — A dictionary you use to customize decoding by providing contextual information.

### Instance Methods

- [decode(_:from:configuration:)](<propertylistdecoder/decode(__from_configuration_)-1m1ya.md>)
- [decode(_:from:configuration:)](<propertylistdecoder/decode(__from_configuration_)-62fzt.md>)
- [decode(_:from:format:configuration:)](<propertylistdecoder/decode(__from_format_configuration_)-1frbk.md>)
- [decode(_:from:format:configuration:)](<propertylistdecoder/decode(__from_format_configuration_)-2epy4.md>)

### Type Aliases

- [PropertyListFormat](propertylistdecoder/propertylistformat.md)

## See Also

### Property Lists

- [PropertyListEncoder](propertylistencoder.md) — An object that encodes instances of data types to a property list.
- [PropertyListSerialization](propertylistserialization.md) — An object that converts between a property list and one of several serialized representations.
