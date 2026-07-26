---
title: 'CFPropertyListCreateWithStream(_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpropertylistcreatewithstream(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatewithstream(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistcreatewithstream%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:921acbf5d697d031'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListCreateWithStream(_:_:_:_:_:_:)

<sub>Function</sub>

Create and return a property list with a CFReadStream input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListCreateWithStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ options: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFPropertyList>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new property list object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `stream` — A CFReadStream that contains a serialized representation of a property list.

- `streamLength` — The number of bytes to read from the stream. Pass `0` to read until the end of the stream is detected.

- `options` — A [CFPropertyListMutabilityOptions](cfpropertylistmutabilityoptions.md) constant to specify the mutability of the returned property list—see [Property List Mutability Options](property_list_mutability_options.md) for possible values.

- `format` — If this parameter is non-`NULL`, on return it will be set to the format of the data. See [CFPropertyListFormat](cfpropertylistformat.md) for possible values.

- `error` — If this parameter is non-`NULL`, if an error occurs, on return this will contain a CFError error describing the problem. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Return Value

A new property list created from the data in `stream`. If an error occurs while parsing the data, returns `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a Property List

- [CFPropertyListCreateWithData](<cfpropertylistcreatewithdata(__________).md>) — Creates a property list from a given CFData object.
- [CFPropertyListCreateDeepCopy](<cfpropertylistcreatedeepcopy(______).md>) — Recursively creates a copy of a given property list.
- [CFPropertyListCreateFromXMLData](<cfpropertylistcreatefromxmldata(________).md>) — Creates a property list using the specified XML or binary property list data. _(deprecated)_
- [CFPropertyListCreateFromStream](<cfpropertylistcreatefromstream(____________).md>) — Creates a property list using data from a stream. _(deprecated)_
