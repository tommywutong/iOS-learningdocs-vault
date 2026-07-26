---
title: 'metadataQuery(_:replacementObjectForResultObject:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmetadataquerydelegate/metadataquery(_:replacementobjectforresultobject:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataquerydelegate/metadataquery(_:replacementobjectforresultobject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataquerydelegate/metadataquery%28_%3Areplacementobjectforresultobject%3A%29.json'
content_hash: 'sha256:3d00a9f4ac7a485e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMetadataQueryDelegate](../nsmetadataquerydelegate.md)

# metadataQuery(_:replacementObjectForResultObject:)

<sub>Instance Method</sub>

Returns a different object for a given query result object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func metadataQuery(_ query: NSMetadataQuery, replacementObjectForResultObject result: NSMetadataItem) -> Any
```

## Parameters

- `query` — The query that produced the result object to replace.

- `result` — The query result object to replace.

## Return Value

Object that replaces the query result object.

## Discussion

By default query result objects are instances of the [NSMetadataItem](../nsmetadataitem.md) class. By implementing this method, you can return an object of a different class type for the specified result object.

## See Also

### Related Documentation

- [File Metadata Search Programming Guide](https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/SpotlightQuery/Concepts/Introduction.html#//apple_ref/doc/uid/TP40001841)

### Getting Query Results

- [- metadataQuery:replacementValueForAttribute:value:](<metadataquery(__replacementvalueforattribute_value_).md>) — Returns a different value for a given attribute and value.
