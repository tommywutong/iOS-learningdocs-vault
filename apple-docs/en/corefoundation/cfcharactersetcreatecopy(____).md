---
title: 'CFCharacterSetCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetcreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetcreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:f36b437899ecf855'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetCreateCopy(_:_:)

<sub>Function</sub>

Creates a new character set with the values from a given character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetCreateCopy(_ alloc: CFAllocator!, _ theSet: CFCharacterSet!) -> CFCharacterSet!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `theSet` — The character set to copy.

## Return Value

A new character set that is a copy of `theSet`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function tries to compact the backing store where applicable.

## See Also

### Creating Character Sets

- [CFCharacterSetCreateInvertedSet](<cfcharactersetcreateinvertedset(____).md>) — Creates a new immutable character set that is the invert of the specified character set.
- [CFCharacterSetCreateWithCharactersInRange](<cfcharactersetcreatewithcharactersinrange(____).md>) — Creates a new character set with the values from the given range of Unicode characters.
- [CFCharacterSetCreateWithCharactersInString](<cfcharactersetcreatewithcharactersinstring(____).md>) — Creates a new character set with the values in the given string.
- [CFCharacterSetCreateWithBitmapRepresentation](<cfcharactersetcreatewithbitmaprepresentation(____).md>) — Creates a new immutable character set with the bitmap representation specified by given data.
