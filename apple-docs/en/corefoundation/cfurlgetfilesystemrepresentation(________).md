---
title: 'CFURLGetFileSystemRepresentation(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlgetfilesystemrepresentation(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlgetfilesystemrepresentation(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlgetfilesystemrepresentation%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1f2b31306a66f583'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLGetFileSystemRepresentation(_:_:_:_:)

<sub>Function</sub>

Fills a buffer with the file system’s native string representation of a given URL’s path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLGetFileSystemRepresentation(_ url: CFURL!, _ resolveAgainstBase: Bool, _ buffer: UnsafeMutablePointer<UInt8>!, _ maxBufLen: CFIndex) -> Bool
```

## Parameters

- `url` — The `CFURL` object whose native file system representation you want to obtain.

- `resolveAgainstBase` — Pass `true` to return an absolute path name.

- `buffer` — A pointer to a character buffer. On return, the buffer holds the native file system’s representation of `url`. The buffer is null-terminated. This parameter must be at least `maxBufLen` in size for the file system in question to avoid failures for insufficiently large buffers.

- `maxBufLen` — The maximum number of characters that can be written to `buffer`.

## Return Value

`true` if successful, `false` if an error occurred.

## Discussion

No more than `maxBufLen` bytes are written to `buffer`. If `url` requires more than `maxBufLen` bytes to represent itself, including the terminating null byte, this function returns `false`. To avoid this possible failure, you should pass a buffer with size of at least the maximum path length for the file system in question.

## See Also

### Converting URLs to Other Representations

- [CFURLCreateData](<cfurlcreatedata(________).md>) — Creates a `CFData` object containing the content of a given URL.
- [CFURLCreateStringByAddingPercentEscapes](<cfurlcreatestringbyaddingpercentescapes(__________).md>) — Creates a copy of a string, replacing certain characters with the equivalent percent escape sequence based on the specified encoding. _(deprecated)_
- [CFURLCreateStringByReplacingPercentEscapes](<cfurlcreatestringbyreplacingpercentescapes(______).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent.
- [CFURLCreateStringByReplacingPercentEscapesUsingEncoding](<cfurlcreatestringbyreplacingpercentescapesusingencoding(________).md>) — Creates a new string by replacing any percent escape sequences with their character equivalent. _(deprecated)_
- [CFURLGetFSRef](<cfurlgetfsref(____).md>) — Converts a given URL to a file or directory object. _(deprecated)_
- [CFURLGetString](<cfurlgetstring(__).md>) — Returns the URL as a `CFString` object.
