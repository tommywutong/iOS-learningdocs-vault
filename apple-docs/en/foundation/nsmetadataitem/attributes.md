---
title: attributes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataitem/attributes
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataitem/attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataitem/attributes.json'
content_hash: 'sha256:a9aa65f5f9532124'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataItem](../nsmetadataitem.md)

# attributes

<sub>Instance Property</sub>

An array containing the attribute keys for the metadata item’s values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var attributes: [String] { get }
```

## Discussion

This property contains an array of attribute keys, representing the values available from this metadata item. For a list of possible keys, see `Attribute Keys`.

## See Also

### Getting Item Attributes

- [- valueForAttribute:](<value(forattribute_).md>) — Returns the receiver’s metadata attribute name specified by a given key.
- [- valuesForAttributes:](<values(forattributes_).md>) — Returns a dictionary containing the key-value pairs for the attribute names specified by a given array of keys.
