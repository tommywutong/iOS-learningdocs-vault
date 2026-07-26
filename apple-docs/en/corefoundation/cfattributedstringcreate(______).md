---
title: 'CFAttributedStringCreate(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringcreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringcreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringcreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c9d17c7a47e7f5fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringCreate(_:_:_:)

<sub>Function</sub>

Creates an attributed string with specified string and attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringCreate(_ alloc: CFAllocator!, _ str: CFString!, _ attributes: CFDictionary!) -> CFAttributedString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new attributed string. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `str` — A string that specifies the characters to use in the new attributed string. This value is copied.

- `attributes` — A dictionary that contains the attributes to apply to the new attributed string. This value is copied.

## Return Value

An attributed string that contains the characters from `str` and the attributes specified by `attributes`. The result is `NULL` if there was a problem in creating the attributed string. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

Note that both the string and the attributes dictionary are copied. The specified attributes are applied to the whole string. If you want to apply different attributes to different ranges of the string, you should use a mutable attributed string.

## See Also

### Creating a CFAttributedString

- [CFAttributedStringCreateCopy](<cfattributedstringcreatecopy(____).md>) — Creates an immutable copy of an attributed string.
- [CFAttributedStringCreateWithSubstring](<cfattributedstringcreatewithsubstring(______).md>) — Creates a sub-attributed string from the specified range.
- [CFAttributedStringGetLength](<cfattributedstringgetlength(__).md>) — Returns the length of the attributed string in characters.
- [CFAttributedStringGetString](<cfattributedstringgetstring(__).md>) — Returns the string for an attributed string.
