---
title: 'CFCharacterSetCreateInvertedSet(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetcreateinvertedset(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetcreateinvertedset(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetcreateinvertedset%28_%3A_%3A%29.json'
content_hash: 'sha256:b567f086a481715e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetCreateInvertedSet(_:_:)

<sub>Function</sub>

Creates a new immutable character set that is the invert of the specified character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetCreateInvertedSet(_ alloc: CFAllocator!, _ theSet: CFCharacterSet!) -> CFCharacterSet!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `theSet` — The character set from which to create an inverted set.

## Return Value

A new character set that is the invert of `theSet`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating Character Sets

- [CFCharacterSetCreateCopy](<cfcharactersetcreatecopy(____).md>) — Creates a new character set with the values from a given character set.
- [CFCharacterSetCreateWithCharactersInRange](<cfcharactersetcreatewithcharactersinrange(____).md>) — Creates a new character set with the values from the given range of Unicode characters.
- [CFCharacterSetCreateWithCharactersInString](<cfcharactersetcreatewithcharactersinstring(____).md>) — Creates a new character set with the values in the given string.
- [CFCharacterSetCreateWithBitmapRepresentation](<cfcharactersetcreatewithbitmaprepresentation(____).md>) — Creates a new immutable character set with the bitmap representation specified by given data.
