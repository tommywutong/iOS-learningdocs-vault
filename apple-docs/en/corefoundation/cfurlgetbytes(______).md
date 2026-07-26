---
title: 'CFURLGetBytes(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlgetbytes(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlgetbytes(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlgetbytes%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:72e66cca7140b143'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLGetBytes(_:_:_:)

<sub>Function</sub>

Returns by reference the byte representation of a URL object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLGetBytes(_ url: CFURL!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferLength: CFIndex) -> CFIndex
```

## Parameters

- `url` — The URL object to convert to a byte representation.

- `buffer` — The buffer where you want the bytes to be placed. If the buffer is of insufficient size, returns `-1` and no bytes are placed in buffer. If `NULL` the needed length is computed and returned. The returned bytes are the original bytes from which the URL was created (_not_ including the base URL). If the URL was created from a string, the bytes are the bytes of the string encoded via UTF-8.

- `bufferLength` — The number of bytes in `buffer`.

## Return Value

Returns the number of bytes in `buffer` that were filled. If the buffer is of insufficient size, returns `-1`.

## See Also

### Getting URL Properties

- [CFURLGetBaseURL](<cfurlgetbaseurl(__).md>) — Returns the base URL of a given URL if it exists.
- [CFURLGetByteRangeForComponent](<cfurlgetbyterangeforcomponent(______).md>) — Returns the range of the specified component in the bytes of a URL.
- [CFURLGetTypeID](<cfurlgettypeid().md>) — Returns the type identifier for the `CFURL` opaque type.
- [CFURLResourceIsReachable](<cfurlresourceisreachable(____).md>) — Returns whether the resource pointed to by a file URL can be reached.
