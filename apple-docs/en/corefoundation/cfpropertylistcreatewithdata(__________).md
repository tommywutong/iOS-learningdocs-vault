---
title: 'CFPropertyListCreateWithData(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpropertylistcreatewithdata(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatewithdata(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistcreatewithdata%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:84ef27f6ac2f6407'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListCreateWithData(_:_:_:_:_:)

<sub>Function</sub>

Creates a property list from a given CFData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListCreateWithData(_ allocator: CFAllocator!, _ data: CFData!, _ options: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new property list object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `data` — A CFData object containing a serialized representation of a property list.

- `options` — A [CFPropertyListMutabilityOptions](cfpropertylistmutabilityoptions.md) constant to specify the mutability of the returned property list—see [Property List Mutability Options](property_list_mutability_options.md) for possible values.

- `format` — If this parameter is non-`NULL`, on return it will be set to the format of the data. See [CFPropertyListFormat](cfpropertylistformat.md) for possible values.

- `error` — If this parameter is non-`NULL`, if an error occurs, on return this will contain a CFError error describing the problem. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Return Value

A new property list created from the data in `data`. If an error occurs while parsing the data, returns `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Property List

- [CFPropertyListCreateWithStream](<cfpropertylistcreatewithstream(____________).md>) — Create and return a property list with a CFReadStream input.
- [CFPropertyListCreateDeepCopy](<cfpropertylistcreatedeepcopy(______).md>) — Recursively creates a copy of a given property list.
- [CFPropertyListCreateFromXMLData](<cfpropertylistcreatefromxmldata(________).md>) — Creates a property list using the specified XML or binary property list data. _(deprecated)_
- [CFPropertyListCreateFromStream](<cfpropertylistcreatefromstream(____________).md>) — Creates a property list using data from a stream. _(deprecated)_
