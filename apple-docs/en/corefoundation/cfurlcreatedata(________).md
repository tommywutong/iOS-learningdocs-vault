---
title: 'CFURLCreateData(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreatedata(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatedata(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatedata%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a049c7f5dabcde76'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateData(_:_:_:_:)

<sub>Function</sub>

Creates a `CFData` object containing the content of a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateData(_ allocator: CFAllocator!, _ url: CFURL!, _ encoding: CFStringEncoding, _ escapeWhitespace: Bool) -> CFData!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFData` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `url` — The URL to convert into a `CFData` object.

- `encoding` — The string encoding to use when converting `url` into a `CFData` object.

- `escapeWhitespace` — `true` if you want to escape whitespace characters in the URL, `false` otherwise.

## Return Value

A new `CFData` object containing the content of `url`. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function escapes any character that is not 7-bit ASCII with the byte-code for the given encoding. If `escapeWhitespace` is `true`, whitespace characters (’ ’, ‘\\t’, ‘\\r’, ‘\\n’) will be escaped as well. This is desirable if you want to embed the URL into a larger text stream like HTML.

## See Also

### Converting URLs to Other Representations

- [CFURLCreateStringByAddingPercentEscapes](<cfurlcreatestringbyaddingpercentescapes(__________).md>) — Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding. _(deprecated)_
- [CFURLCreateStringByReplacingPercentEscapes](<cfurlcreatestringbyreplacingpercentescapes(______).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent.
- [CFURLCreateStringByReplacingPercentEscapesUsingEncoding](<cfurlcreatestringbyreplacingpercentescapesusingencoding(________).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent. _(deprecated)_
- [CFURLGetFileSystemRepresentation](<cfurlgetfilesystemrepresentation(________).md>) — Fills a buffer with the file system’s native string representation of a given URL’s path.
- [CFURLGetFSRef](<cfurlgetfsref(____).md>) — Converts a given URL to a file or directory object. _(deprecated)_
- [CFURLGetString](<cfurlgetstring(__).md>) — Returns the URL as a `CFString` object.
