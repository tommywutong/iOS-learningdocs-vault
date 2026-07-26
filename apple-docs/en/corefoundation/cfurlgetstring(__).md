---
title: 'CFURLGetString(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlgetstring(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlgetstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlgetstring%28_%3A%29.json'
content_hash: 'sha256:a58e7d759b5bd6f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLGetString(_:)

<sub>Function</sub>

Returns the URL as a `CFString` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLGetString(_ anURL: CFURL!) -> CFString!
```

## Parameters

- `anURL` — The `CFURL` object to convert into a `CFString` object.

## Return Value

A string representation of `anURL`. Ownership follows the get rule. See [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## See Also

### Converting URLs to Other Representations

- [CFURLCreateData](<cfurlcreatedata(________).md>) — Creates a `CFData` object containing the content of a given URL.
- [CFURLCreateStringByAddingPercentEscapes](<cfurlcreatestringbyaddingpercentescapes(__________).md>) — Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding. _(deprecated)_
- [CFURLCreateStringByReplacingPercentEscapes](<cfurlcreatestringbyreplacingpercentescapes(______).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent.
- [CFURLCreateStringByReplacingPercentEscapesUsingEncoding](<cfurlcreatestringbyreplacingpercentescapesusingencoding(________).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent. _(deprecated)_
- [CFURLGetFileSystemRepresentation](<cfurlgetfilesystemrepresentation(________).md>) — Fills a buffer with the file system’s native string representation of a given URL’s path.
- [CFURLGetFSRef](<cfurlgetfsref(____).md>) — Converts a given URL to a file or directory object. _(deprecated)_
