---
title: 'CFCharacterSetCreateWithCharactersInRange(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetcreatewithcharactersinrange(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatewithcharactersinrange(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetcreatewithcharactersinrange%28_%3A_%3A%29.json'
content_hash: 'sha256:45a4dcf5b6eb6e9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetCreateWithCharactersInRange(_:_:)

<sub>Function</sub>

Creates a new character set with the values from the given range of Unicode characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetCreateWithCharactersInRange(_ alloc: CFAllocator!, _ theRange: CFRange) -> CFCharacterSet!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `theRange` — The Unicode range of characters of the new character set. The function accepts the range in 32-bit in the UTF-32 format. The valid character point range is from 0x00000 to 0x10FFFF.

## Return Value

A new character set that contains a contiguous range of Unicode characters. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating Character Sets

- [CFCharacterSetCreateCopy](<cfcharactersetcreatecopy(____).md>) — Creates a new character set with the values from a given character set.
- [CFCharacterSetCreateInvertedSet](<cfcharactersetcreateinvertedset(____).md>) — Creates a new immutable character set that is the invert of the specified character set.
- [CFCharacterSetCreateWithCharactersInString](<cfcharactersetcreatewithcharactersinstring(____).md>) — Creates a new character set with the values in the given string.
- [CFCharacterSetCreateWithBitmapRepresentation](<cfcharactersetcreatewithbitmaprepresentation(____).md>) — Creates a new immutable character set with the bitmap representation specified by given data.
