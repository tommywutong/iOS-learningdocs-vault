---
title: 'CFAttributedStringCreateWithSubstring(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringcreatewithsubstring(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatewithsubstring(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringcreatewithsubstring%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:939c7c5217894b6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringCreateWithSubstring(_:_:_:)

<sub>Function</sub>

Creates a sub-attributed string from the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringCreateWithSubstring(_ alloc: CFAllocator!, _ aStr: CFAttributedString!, _ range: CFRange) -> CFAttributedString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new attributed string. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `aStr` — The attributed string to copy.

- `range` — The range of the attributed string to copy. `range` must not exceed the bounds of `aStr`.

## Return Value

A new attributed string whose string and attributes are copied from the specified range of the supplied attributed string. Returns `NULL` if there was a problem copying the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a CFAttributedString

- [CFAttributedStringCreate](<cfattributedstringcreate(______).md>) — Creates an attributed string with specified string and attributes.
- [CFAttributedStringCreateCopy](<cfattributedstringcreatecopy(____).md>) — Creates an immutable copy of an attributed string.
- [CFAttributedStringGetLength](<cfattributedstringgetlength(__).md>) — Returns the length of the attributed string in characters.
- [CFAttributedStringGetString](<cfattributedstringgetstring(__).md>) — Returns the string for an attributed string.
