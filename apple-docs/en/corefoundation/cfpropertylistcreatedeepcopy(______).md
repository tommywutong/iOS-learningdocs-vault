---
title: 'CFPropertyListCreateDeepCopy(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfpropertylistcreatedeepcopy(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpropertylistcreatedeepcopy(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpropertylistcreatedeepcopy%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:7daa75c7058bbaa8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPropertyListCreateDeepCopy(_:_:_:)

<sub>Function</sub>

Recursively creates a copy of a given property list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPropertyListCreateDeepCopy(_ allocator: CFAllocator!, _ propertyList: CFPropertyList!, _ mutabilityOption: CFOptionFlags) -> CFPropertyList!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new property list. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `propertyList` — The property list to copy. This may be any of the standard property list objects, for example a CFArray or a CFDictionary object.

- `mutabilityOption` — A constant that specifies the degree of mutability of the returned property list. See [Property List Mutability Options](property_list_mutability_options.md) for descriptions of possible values.

## Return Value

A new property list that is a copy of `propertyList`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Recursively creates a copy of the given property list so nested arrays and dictionaries are copied as well as the top-most container.

## See Also

### Creating a Property List

- [CFPropertyListCreateWithData](<cfpropertylistcreatewithdata(__________).md>) — Creates a property list from a given CFData object.
- [CFPropertyListCreateWithStream](<cfpropertylistcreatewithstream(____________).md>) — Create and return a property list with a CFReadStream input.
- [CFPropertyListCreateFromXMLData](<cfpropertylistcreatefromxmldata(________).md>) — Creates a property list using the specified XML or binary property list data. _(deprecated)_
- [CFPropertyListCreateFromStream](<cfpropertylistcreatefromstream(____________).md>) — Creates a property list using data from a stream. _(deprecated)_
