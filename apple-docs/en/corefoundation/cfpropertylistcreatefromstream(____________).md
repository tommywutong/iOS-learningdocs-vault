---
title: 'CFPropertyListCreateFromStream(_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.2+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfpropertylistcreatefromstream(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatefromstream(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistcreatefromstream%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cf99443925dc8450'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListCreateFromStream(_:_:_:_:_:_:)

<sub>Function</sub>

Creates a property list using data from a stream.

> [!warning] Deprecated
> Use CFPropertyListCreateWithStream instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListCreateFromStream(_ allocator: CFAllocator!, _ stream: CFReadStream!, _ streamLength: CFIndex, _ mutabilityOption: CFOptionFlags, _ format: UnsafeMutablePointer<CFPropertyListFormat>!, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new property list. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `stream` — The stream whose data contains the content. The stream must be opened and configured—this function simply reads bytes from the stream. The stream may contain any supported property list type (see [CFPropertyListFormat](cfpropertylistformat.md)).

- `streamLength` — The number of bytes to read. If `0`, this function will read to the end of the stream.

- `mutabilityOption` — A constant that specifies the degree of mutability for the returned property list. See [Property List Mutability Options](property_list_mutability_options.md) for descriptions of possible values.

- `format` — A constant that specifies the format of the property list. See [CFPropertyListFormat](cfpropertylistformat.md) for possible values.

- `errorString` — On return, `NULL` if the conversion is successful, otherwise a string that describes the nature of the error. Error messages are not localized, but may be in the future, so they are not suitable for comparison. Pass `NULL` if you do not wish to receive an error string. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Return Value

A new property list initialized with the data contained in `stream`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function simply reads bytes from `stream` starting at the current location to the end, which is expected to be the end of the property list, or up to the number of bytes specified by `streamLength` if it is not `0`.

### Special Considerations

> [!warning] Warning
> This function is obsolete and will be deprecated soon. Use [CFPropertyListCreateWithStream](<cfpropertylistcreatewithstream(____________).md>) instead.

## See Also

### Creating a Property List

- [CFPropertyListCreateWithData](<cfpropertylistcreatewithdata(__________).md>) — Creates a property list from a given CFData object.
- [CFPropertyListCreateWithStream](<cfpropertylistcreatewithstream(____________).md>) — Create and return a property list with a CFReadStream input.
- [CFPropertyListCreateDeepCopy](<cfpropertylistcreatedeepcopy(______).md>) — Recursively creates a copy of a given property list.
- [CFPropertyListCreateFromXMLData](<cfpropertylistcreatefromxmldata(________).md>) — Creates a property list using the specified XML or binary property list data. _(deprecated)_
