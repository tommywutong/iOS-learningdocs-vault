---
title: 'CFPropertyListCreateXMLData(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfpropertylistcreatexmldata(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatexmldata(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistcreatexmldata%28_%3A_%3A%29.json'
content_hash: 'sha256:fee5960632dbcda5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListCreateXMLData(_:_:)

<sub>Function</sub>

Creates an XML representation of the specified property list.

> [!warning] Deprecated
> Use CFPropertyListCreateData instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListCreateXMLData(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!) -> Unmanaged<CFData>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new data object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `propertyList` — The property list to convert. This may be any of the standard property list objects, for example a CFArray or a CFDictionary object.

## Return Value

A CFData object containing the XML data. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

> [!warning] Warning
> This function is obsolete and will be deprecated soon. Use [CFPropertyListCreateData](<cfpropertylistcreatedata(__________).md>) instead.

## See Also

### Exporting a Property List

- [CFPropertyListCreateData](<cfpropertylistcreatedata(__________).md>) — Returns a CFData object containing a serialized representation of a given property list in a specified format.
- [CFPropertyListWrite](<cfpropertylistwrite(__________).md>) — Write the bytes of a serialized property list out to a stream.
- [CFPropertyListWriteToStream](<cfpropertylistwritetostream(________).md>) — Writes the bytes of a property list serialization out to a stream. _(deprecated)_
