---
title: 'CFURLGetFSRef(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfurlgetfsref(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlgetfsref(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlgetfsref%28_%3A_%3A%29.json'
content_hash: 'sha256:af326992cca0ccd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLGetFSRef(_:_:)

<sub>Function</sub>

Converts a given URL to a file or directory object.

> [!warning] Deprecated
> Not supported

<sub>tvOS, visionOS, watchOS</sub>

```swift
func CFURLGetFSRef(_ url: CFURL!, _ fsRef: OpaquePointer!) -> Bool
```

## Parameters

- `url` — The `CFURL` object to convert to a file or directory object.

- `fsRef` — Upon return, contains the file or directory object representing `url`.

## Return Value

`true` if the conversion was successful, otherwise `false`.

## Discussion

The function cannot create an `FSRef` object if any of the leading path parts specified by `url` is an alias. The function can, however, traverse symbolic links.

## See Also

### Converting URLs to Other Representations

- [CFURLCreateData](<cfurlcreatedata(________).md>) — Creates a `CFData` object containing the content of a given URL.
- [CFURLCreateStringByAddingPercentEscapes](<cfurlcreatestringbyaddingpercentescapes(__________).md>) — Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding. _(deprecated)_
- [CFURLCreateStringByReplacingPercentEscapes](<cfurlcreatestringbyreplacingpercentescapes(______).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent.
- [CFURLCreateStringByReplacingPercentEscapesUsingEncoding](<cfurlcreatestringbyreplacingpercentescapesusingencoding(________).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent. _(deprecated)_
- [CFURLGetFileSystemRepresentation](<cfurlgetfilesystemrepresentation(________).md>) — Fills a buffer with the file system’s native string representation of a given URL’s path.
- [CFURLGetString](<cfurlgetstring(__).md>) — Returns the URL as a `CFString` object.
