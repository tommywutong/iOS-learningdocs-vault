---
title: 'values(forAttributes:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmetadataitem/values(forattributes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataitem/values(forattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataitem/values%28forattributes%3A%29.json'
content_hash: 'sha256:231d51a997d83a07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataItem](../nsmetadataitem.md)

# values(forAttributes:)

<sub>Instance Method</sub>

Returns a dictionary containing the key-value pairs for the attribute names specified by a given array of keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func values(forAttributes keys: [String]) -> [String : Any]?
```

## Parameters

- `keys` — An array containing `NSString` objects that specify the names of a metadata attributes. See the “Constants” section for a list of possible keys.

## Return Value

A dictionary containing the key-value pairs for the attribute names specified by `keys`.

## See Also

### Getting Item Attributes

- [attributes](attributes.md) — An array containing the attribute keys for the metadata item’s values.
- [- valueForAttribute:](<value(forattribute_).md>) — Returns the receiver’s metadata attribute name specified by a given key.
