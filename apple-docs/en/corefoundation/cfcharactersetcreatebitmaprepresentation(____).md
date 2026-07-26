---
title: 'CFCharacterSetCreateBitmapRepresentation(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetcreatebitmaprepresentation(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatebitmaprepresentation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetcreatebitmaprepresentation%28_%3A_%3A%29.json'
content_hash: 'sha256:40b329783a2c45af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetCreateBitmapRepresentation(_:_:)

<sub>Function</sub>

Creates a new immutable data with the bitmap representation from the given character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetCreateBitmapRepresentation(_ alloc: CFAllocator!, _ theSet: CFCharacterSet!) -> CFData!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `theSet` — The set from which to create a bitmap representation. Refer to the comments for [CFCharacterSetCreateWithBitmapRepresentation](<cfcharactersetcreatewithbitmaprepresentation(____).md>) for the detailed discussion of the bitmap representation format.

## Return Value

A new CFData object containing a bitmap representation of `theSet`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Querying Character Sets

- [CFCharacterSetHasMemberInPlane](<cfcharactersethasmemberinplane(____).md>) — Reports whether or not a character set contains at least one member character in the specified plane.
- [CFCharacterSetIsCharacterMember](<cfcharactersetischaractermember(____).md>) — Reports whether or not a given Unicode character is in a character set.
- [CFCharacterSetIsLongCharacterMember](<cfcharactersetislongcharactermember(____).md>) — Reports whether or not a given UTF-32 character is in a character set.
- [CFCharacterSetIsSupersetOfSet](<cfcharactersetissupersetofset(____).md>) — Reports whether or not a character set is a superset of another set.
