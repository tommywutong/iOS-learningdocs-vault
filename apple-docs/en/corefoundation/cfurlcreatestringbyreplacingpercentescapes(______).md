---
title: 'CFURLCreateStringByReplacingPercentEscapes(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreatestringbyreplacingpercentescapes(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatestringbyreplacingpercentescapes(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatestringbyreplacingpercentescapes%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f7cbd4c9478116a0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateStringByReplacingPercentEscapes(_:_:_:)

<sub>Function</sub>

Creates a new string by replacing any percent escape sequences with their character equivalent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateStringByReplacingPercentEscapes(_ allocator: CFAllocator!, _ originalString: CFString!, _ charactersToLeaveEscaped: CFString!) -> CFString!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFString` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `originalString` — The `CFString` object to be copied and modified.

- `charactersToLeaveEscaped` — Characters whose percent escape sequences, such as `%20` for a space character, you want to leave intact. Pass `NULL` to specify that no percent escapes be replaced, or the empty string (`CFSTR("")`) to specify that all be replaced.

## Return Value

A new `CFString` object, or `NULL` if the percent escapes cannot be converted to characters, assuming UTF-8 encoding. If no characters need to be replaced, this function returns the original string with its reference count incremented. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Converting URLs to Other Representations

- [CFURLCreateData](<cfurlcreatedata(________).md>) — Creates a `CFData` object containing the content of a given URL.
- [CFURLCreateStringByAddingPercentEscapes](<cfurlcreatestringbyaddingpercentescapes(__________).md>) — Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding. _(deprecated)_
- [CFURLCreateStringByReplacingPercentEscapesUsingEncoding](<cfurlcreatestringbyreplacingpercentescapesusingencoding(________).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent. _(deprecated)_
- [CFURLGetFileSystemRepresentation](<cfurlgetfilesystemrepresentation(________).md>) — Fills a buffer with the file system’s native string representation of a given URL’s path.
- [CFURLGetFSRef](<cfurlgetfsref(____).md>) — Converts a given URL to a file or directory object. _(deprecated)_
- [CFURLGetString](<cfurlgetstring(__).md>) — Returns the URL as a `CFString` object.
