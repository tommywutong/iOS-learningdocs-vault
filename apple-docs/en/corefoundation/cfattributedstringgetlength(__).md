---
title: 'CFAttributedStringGetLength(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringgetlength(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringgetlength(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringgetlength%28_%3A%29.json'
content_hash: 'sha256:4afae7634d30eab7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringGetLength(_:)

<sub>Function</sub>

Returns the length of the attributed string in characters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringGetLength(_ aStr: CFAttributedString!) -> CFIndex
```

## Parameters

- `aStr` — The attributed string to examine.

## Return Value

The length of the attributed string in characters; this is the same as `CFStringGetLength(CFAttributedStringGetString(aStr))`.

## See Also

### Creating a CFAttributedString

- [CFAttributedStringCreate](<cfattributedstringcreate(______).md>) — Creates an attributed string with specified string and attributes.
- [CFAttributedStringCreateCopy](<cfattributedstringcreatecopy(____).md>) — Creates an immutable copy of an attributed string.
- [CFAttributedStringCreateWithSubstring](<cfattributedstringcreatewithsubstring(______).md>) — Creates a sub-attributed string from the specified range.
- [CFAttributedStringGetString](<cfattributedstringgetstring(__).md>) — Returns the string for an attributed string.
