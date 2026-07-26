---
title: CFPropertyListFormat
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfpropertylistformat
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistformat.json'
content_hash: 'sha256:28326d45fb28bc69'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListFormat

<sub>Enumeration</sub>

Specifies the format of a property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFPropertyListFormat
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFPropertyListOpenStepFormat](cfpropertylistformat/openstepformat.md) — OpenStep format (use of this format is discouraged).
- [kCFPropertyListXMLFormat_v1_0](cfpropertylistformat/xmlformat_v1_0.md) — XML format version 1.0.
- [kCFPropertyListBinaryFormat_v1_0](cfpropertylistformat/binaryformat_v1_0.md) — Binary format version 1.0.

### Initializers

- [init(rawValue:)](<cfpropertylistformat/init(rawvalue_).md>)

## See Also

### Constants

- [Property List Mutability Options](property_list_mutability_options.md) — Option flags that determine the degree of mutability of newly created property lists.
- [Reading and Writing Error Codes](1429999-reading-and-writing-error-codes.md) — Error codes for property list reading and writing functions such as [CFPropertyListCreateWithData](<cfpropertylistcreatewithdata(__________).md>).
