---
title: 'CFCopyTypeIDDescription(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcopytypeiddescription(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcopytypeiddescription(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcopytypeiddescription%28_%3A%29.json'
content_hash: 'sha256:2ac3598cc6bdae7b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCopyTypeIDDescription(_:)

<sub>Function</sub>

Returns a textual description of a Core Foundation type, as identified by its type ID, which can be used when debugging.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCopyTypeIDDescription(_ type_id: CFTypeID) -> CFString!
```

## Parameters

- `type_id` — An integer of type [CFTypeID](cftypeid.md) that uniquely identifies a Core Foundation opaque type.

## Return Value

A string containing a type description. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You can use this function for debugging Core Foundation objects in your code. Note, however, that the description for a given object may be different in different releases of the operating system. Do _not_  create dependencies in your code on the content or format of the information returned by this function.

## See Also

### Miscellaneous Functions

- [CFCopyDescription](<cfcopydescription(__).md>) — Returns a textual description of a Core Foundation object.
- [CFGetTypeID](<cfgettypeid(__).md>) — Returns the unique identifier of an opaque type to which a Core Foundation object belongs.
- [CFShow](<cfshow(__).md>) — Prints a description of a Core Foundation object to stderr.
