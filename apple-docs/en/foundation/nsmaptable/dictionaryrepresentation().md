---
title: dictionaryRepresentation()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmaptable/dictionaryrepresentation()
source_url: 'https://developer.apple.com/documentation/foundation/nsmaptable/dictionaryrepresentation()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmaptable/dictionaryrepresentation%28%29.json'
content_hash: 'sha256:382254109bd667bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMapTable](../nsmaptable.md)

# dictionaryRepresentation()

<sub>Instance Method</sub>

Returns a dictionary representation of the map table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dictionaryRepresentation() -> [AnyHashable : ObjectType]
```

## Return Value

A dictionary representation of the map table.

## Discussion

The map table’s values and keys must conform to all the requirements specified in [- setObject:forKey:](<../nsmutabledictionary/setobject(__forkey_).md>) in [NSMutableDictionary](../nsmutabledictionary.md).
