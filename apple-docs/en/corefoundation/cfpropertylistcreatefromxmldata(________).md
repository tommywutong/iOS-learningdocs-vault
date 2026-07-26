---
title: 'CFPropertyListCreateFromXMLData(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（8.0 起废弃）, iPadOS 2.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.0+（10.10 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfpropertylistcreatefromxmldata(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatefromxmldata(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistcreatefromxmldata%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:329a179bf08bb3f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListCreateFromXMLData(_:_:_:_:)

<sub>Function</sub>

Creates a property list using the specified XML or binary property list data.

> [!warning] Deprecated
> Use CFPropertyListCreateWithData instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListCreateFromXMLData(_ allocator: CFAllocator!, _ xmlData: CFData!, _ mutabilityOption: CFOptionFlags, _ errorString: UnsafeMutablePointer<Unmanaged<CFString>?>!) -> Unmanaged<CFPropertyList>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new property list. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `xmlData` — The raw bytes to convert into a property list. The bytes may be the content of an XML file or of a binary property list (see [CFPropertyListFormat](cfpropertylistformat.md)).

- `mutabilityOption` — A constant that specifies the degree of mutability for the returned property list. See [Property List Mutability Options](property_list_mutability_options.md) for descriptions of possible values.

- `errorString` — On return, `NULL` if the conversion is successful, otherwise a string that describes the nature of the error. Error messages are not localized, but may be in the future, so they are not currently suitable for comparison. Pass `NULL` if you do not wish to receive an error string. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Return Value

A new property list if the conversion is successful, otherwise `NULL`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

> [!warning] Warning
> This function is obsolete and will be deprecated soon. Use [CFPropertyListCreateWithData](<cfpropertylistcreatewithdata(__________).md>) instead.

## See Also

### Creating a Property List

- [CFPropertyListCreateWithData](<cfpropertylistcreatewithdata(__________).md>) — Creates a property list from a given CFData object.
- [CFPropertyListCreateWithStream](<cfpropertylistcreatewithstream(____________).md>) — Create and return a property list with a CFReadStream input.
- [CFPropertyListCreateDeepCopy](<cfpropertylistcreatedeepcopy(______).md>) — Recursively creates a copy of a given property list.
- [CFPropertyListCreateFromStream](<cfpropertylistcreatefromstream(____________).md>) — Creates a property list using data from a stream. _(deprecated)_
