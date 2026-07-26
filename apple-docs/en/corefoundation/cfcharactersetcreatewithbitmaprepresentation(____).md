---
title: 'CFCharacterSetCreateWithBitmapRepresentation(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfcharactersetcreatewithbitmaprepresentation(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfcharactersetcreatewithbitmaprepresentation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfcharactersetcreatewithbitmaprepresentation%28_%3A_%3A%29.json'
content_hash: 'sha256:bfdc29646ed33f13'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFCharacterSetCreateWithBitmapRepresentation(_:_:)

<sub>Function</sub>

Creates a new immutable character set with the bitmap representation specified by given data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFCharacterSetCreateWithBitmapRepresentation(_ alloc: CFAllocator!, _ theData: CFData!) -> CFCharacterSet!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `theData` — A CFData object that specifies the bitmap representation of the Unicode character points the for the new character set. The bitmap representation could contain all the Unicode character range starting from BMP to Plane 16. The first 8KiB (8192 bytes) of the data represent the BMP range. The BMP range 8KiB can be followed by zero to sixteen 8KiB bitmaps, each prepended with the plane index byte. For example, the bitmap representing the BMP and Plane 2 has the size of 16385 bytes (8KiB for BMP, 1 byte index, and a 8KiB bitmap for Plane 2). The plane index byte, in this case, contains the integer value two. If the data contains a Plane index byte outside of the valid Plane range (1 to 16), the behavior is undefined.

## Return Value

A new character set containing the indicated characters from `theData`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating Character Sets

- [CFCharacterSetCreateCopy](<cfcharactersetcreatecopy(____).md>) — Creates a new character set with the values from a given character set.
- [CFCharacterSetCreateInvertedSet](<cfcharactersetcreateinvertedset(____).md>) — Creates a new immutable character set that is the invert of the specified character set.
- [CFCharacterSetCreateWithCharactersInRange](<cfcharactersetcreatewithcharactersinrange(____).md>) — Creates a new character set with the values from the given range of Unicode characters.
- [CFCharacterSetCreateWithCharactersInString](<cfcharactersetcreatewithcharactersinstring(____).md>) — Creates a new character set with the values in the given string.
