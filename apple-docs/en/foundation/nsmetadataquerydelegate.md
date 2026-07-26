---
title: NSMetadataQueryDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataquerydelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquerydelegate.json'
content_hash: 'sha256:e54917456757efd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataQueryDelegate

<sub>Protocol</sub>

An interface that enables the delegate of a metadata query to provide substitute results or attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol NSMetadataQueryDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting Query Results

- [- metadataQuery:replacementObjectForResultObject:](<nsmetadataquerydelegate/metadataquery(__replacementobjectforresultobject_).md>) — Returns a different object for a given query result object.
- [- metadataQuery:replacementValueForAttribute:value:](<nsmetadataquerydelegate/metadataquery(__replacementvalueforattribute_value_).md>) — Returns a different value for a given attribute and value.

## See Also

### File Search

- [NSMetadataQuery](nsmetadataquery.md) — A query that you perform against Spotlight metadata.
- [NSMetadataItem](nsmetadataitem.md) — The metadata associated with a file.
