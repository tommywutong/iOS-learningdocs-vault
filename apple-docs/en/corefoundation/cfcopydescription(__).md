---
title: 'CFCopyDescription(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcopydescription(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcopydescription(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcopydescription%28_%3A%29.json'
content_hash: 'sha256:7cea048bff13c9c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCopyDescription(_:)

<sub>Function</sub>

Returns a textual description of a Core Foundation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCopyDescription(_ cf: CFTypeRef!) -> CFString!
```

## Parameters

- `cf` — The CFType object (a generic reference of type [CFTypeRef](cftyperef.md)) from which to derive a description.

## Return Value

A string that contains a description of `cf`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The nature of the description differs by object. For example, a description of a CFArray object would include descriptions of each of the elements in the collection.

You can use this function for debugging Core Foundation objects in your code. Note, however, that the description for a given object may be different in different releases of the operating system. Do _not_  create dependencies in your code on the content or format of the information returned by this function.

## See Also

### Miscellaneous Functions

- [CFCopyTypeIDDescription](<cfcopytypeiddescription(__).md>) — Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.
- [CFGetTypeID](<cfgettypeid(__).md>) — Returns the unique identifier of an opaque type to which a Core Foundation object belongs.
- [CFShow](<cfshow(__).md>) — Prints a description of a Core Foundation object to stderr.
