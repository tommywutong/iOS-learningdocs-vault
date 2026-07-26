---
title: 'value(forAttribute:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmetadataitem/value(forattribute:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataitem/value(forattribute:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataitem/value%28forattribute%3A%29.json'
content_hash: 'sha256:3d8145187b9447fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataItem](../nsmetadataitem.md)

# value(forAttribute:)

<sub>Instance Method</sub>

Returns the receiver’s metadata attribute name specified by a given key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func value(forAttribute key: String) -> Any?
```

## Parameters

- `key` — The name of a metadata attribute. See the “Constants” section for a list of possible keys.

## Return Value

The receiver’s metadata attribute name specified by `key`.

## See Also

### Getting Item Attributes

- [attributes](attributes.md) — An array containing the attribute keys for the metadata item’s values.
- [- valuesForAttributes:](<values(forattributes_).md>) — Returns a dictionary containing the key-value pairs for the attribute names specified by a given array of keys.
