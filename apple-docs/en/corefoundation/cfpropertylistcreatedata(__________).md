---
title: 'CFPropertyListCreateData(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpropertylistcreatedata(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatedata(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistcreatedata%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:981576e64fe564da'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListCreateData(_:_:_:_:_:)

<sub>Function</sub>

Returns a CFData object containing a serialized representation of a given property list in a specified format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListCreateData(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!, _ format: CFPropertyListFormat, _ options: CFOptionFlags, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFData>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new data object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `propertyList` — The property list to write out.

- `format` — A CFPropertyListFormat constant to specify the data format. See [CFPropertyListFormat](cfpropertylistformat.md) for possible values.

- `options` — This parameter is currently unused and should be set to `0`.

- `error` — If this parameter is non-NULL, if an error occurs, on return this will contain a CFError error describing the problem. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Return Value

A CFData object containing a serialized representation of `propertyList` in a the format specified by `format`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

## See Also

### Exporting a Property List

- [CFPropertyListWrite](<cfpropertylistwrite(__________).md>) — Write the bytes of a serialized property list out to a stream.
- [CFPropertyListCreateXMLData](<cfpropertylistcreatexmldata(____).md>) — Creates an XML representation of the specified property list. _(deprecated)_
- [CFPropertyListWriteToStream](<cfpropertylistwritetostream(________).md>) — Writes the bytes of a property list serialization out to a stream. _(deprecated)_
