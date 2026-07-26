---
title: 'CFAttributedStringGetString(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringgetstring(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringgetstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringgetstring%28_%3A%29.json'
content_hash: 'sha256:ba3016f0182ef43b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringGetString(_:)

<sub>Function</sub>

Returns the string for an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringGetString(_ aStr: CFAttributedString!) -> CFString!
```

## Parameters

- `aStr` — The attributed string to examine.

## Return Value

An immutable string containing the characters from `aStr`, or `NULL` if there was a problem creating the object. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

For performance reasons, the string returned will often be the backing store of the attributed string, and it might therefore change if the attributed string is edited. However, this is an implementation detail, and you should not rely on this behavior.

## See Also

### Creating a CFAttributedString

- [CFAttributedStringCreate](<cfattributedstringcreate(______).md>) — Creates an attributed string with specified string and attributes.
- [CFAttributedStringCreateCopy](<cfattributedstringcreatecopy(____).md>) — Creates an immutable copy of an attributed string.
- [CFAttributedStringCreateWithSubstring](<cfattributedstringcreatewithsubstring(______).md>) — Creates a sub-attributed string from the specified range.
- [CFAttributedStringGetLength](<cfattributedstringgetlength(__).md>) — Returns the length of the attributed string in characters.
