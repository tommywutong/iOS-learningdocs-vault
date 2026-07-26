---
title: 'CFAttributedStringCreateCopy(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringcreatecopy(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringcreatecopy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringcreatecopy%28_%3A_%3A%29.json'
content_hash: 'sha256:19d6c35e1306b9f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringCreateCopy(_:_:)

<sub>Function</sub>

Creates an immutable copy of an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringCreateCopy(_ alloc: CFAllocator!, _ aStr: CFAttributedString!) -> CFAttributedString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new attributed string. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `aStr` — The attributed string to copy.

## Return Value

An immutable attributed string with characters and attributes identical to those of `aStr`. Returns `NULL` if there was a problem copying the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating a CFAttributedString

- [CFAttributedStringCreate](<cfattributedstringcreate(______).md>) — Creates an attributed string with specified string and attributes.
- [CFAttributedStringCreateWithSubstring](<cfattributedstringcreatewithsubstring(______).md>) — Creates a sub-attributed string from the specified range.
- [CFAttributedStringGetLength](<cfattributedstringgetlength(__).md>) — Returns the length of the attributed string in characters.
- [CFAttributedStringGetString](<cfattributedstringgetstring(__).md>) — Returns the string for an attributed string.
