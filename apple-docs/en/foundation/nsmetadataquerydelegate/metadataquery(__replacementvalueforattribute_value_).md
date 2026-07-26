---
title: 'metadataQuery(_:replacementValueForAttribute:value:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmetadataquerydelegate/metadataquery(_:replacementvalueforattribute:value:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/metadataquery(_:replacementvalueforattribute:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquerydelegate/metadataquery%28_%3Areplacementvalueforattribute%3Avalue%3A%29.json'
content_hash: 'sha256:9eeccc9a4c7ca91b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQueryDelegate](../nsmetadataquerydelegate.md)

# metadataQuery(_:replacementValueForAttribute:value:)

<sub>Instance Method</sub>

Returns a different value for a given attribute and value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func metadataQuery(_ query: NSMetadataQuery, replacementValueForAttribute attrName: String, value attrValue: Any) -> Any
```

## Parameters

- `query` — The query that produced the result object with `attrName`.

- `attrName` — The attribute in question.

- `attrValue` — The attribute value to replace.

## Return Value

Object that replaces the value of `attrName` in the result object

## Discussion

The delegate implementation of this method could convert specific query attribute values to other attribute values, for example, converting date object values to formatted strings for display.

## See Also

### Getting Query Results

- [- metadataQuery:replacementObjectForResultObject:](<metadataquery(__replacementobjectforresultobject_).md>) — Returns a different object for a given query result object.
