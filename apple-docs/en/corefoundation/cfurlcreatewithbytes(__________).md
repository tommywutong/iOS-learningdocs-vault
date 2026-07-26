---
title: 'CFURLCreateWithBytes(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreatewithbytes(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatewithbytes(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatewithbytes%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fd9f8e3be5e27d40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateWithBytes(_:_:_:_:_:)

<sub>Function</sub>

Creates a `CFURL` object using a given character bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateWithBytes(_ allocator: CFAllocator!, _ URLBytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!) -> CFURL!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `URLBytes` — The character bytes to convert into a `CFURL` object.

- `length` — The number of bytes in `URLBytes`.

- `encoding` — The string encoding of the `URLBytes` string. This encoding is also used to interpret percent escape sequences.

- `baseURL` — The URL to which `URLBytes` is relative. Pass `NULL` if `URLBytes` contains an absolute URL or if you want to create a relative URL. If `URLBytes` contains an absolute URL, this parameter is ignored.

## Return Value

A new `CFURL` object. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The specified string encoding will be used both to interpret `URLBytes`, and to interpret any percent-escapes within the string.

> [!note] Note
> This function does not support string encoding which isn’t a superset of ASCII encoding. Both [CFURLGetBytes](<cfurlgetbytes(______).md>) and [CFURLGetByteRangeForComponent](<cfurlgetbyterangeforcomponent(______).md>) require 7-bit ASCII characters to be stored in a single 8-bit byte. The following [CFStringEncodings](cfstringencodings.md) can be used: [kCFStringEncodingMacRoman](cfstringbuiltinencodings/macroman.md), [kCFStringEncodingWindowsLatin1](cfstringbuiltinencodings/windowslatin1.md), [kCFStringEncodingISOLatin1](cfstringbuiltinencodings/isolatin1.md), [kCFStringEncodingNextStepLatin](cfstringbuiltinencodings/nextsteplatin.md), [kCFStringEncodingASCII](cfstringbuiltinencodings/ascii.md) and [kCFStringEncodingUTF8](cfstringbuiltinencodings/utf8.md).

## See Also

### Creating a CFURL

- [CFURLCopyAbsoluteURL](<cfurlcopyabsoluteurl(__).md>) — Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
- [CFURLCreateAbsoluteURLWithBytes](<cfurlcreateabsoluteurlwithbytes(____________).md>) — Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.
- [CFURLCreateByResolvingBookmarkData](<cfurlcreatebyresolvingbookmarkdata(______________).md>) — Returns a new URL made by resolving bookmark data.
- [CFURLCreateCopyAppendingPathComponent](<cfurlcreatecopyappendingpathcomponent(________).md>) — Creates a copy of a given URL and appends a path component.
- [CFURLCreateCopyAppendingPathExtension](<cfurlcreatecopyappendingpathextension(______).md>) — Creates a copy of a given URL and appends a path extension.
- [CFURLCreateCopyDeletingLastPathComponent](<cfurlcreatecopydeletinglastpathcomponent(____).md>) — Creates a copy of a given URL with the last path component deleted.
- [CFURLCreateCopyDeletingPathExtension](<cfurlcreatecopydeletingpathextension(____).md>) — Creates a copy of a given URL with its last path extension removed.
- [CFURLCreateFilePathURL](<cfurlcreatefilepathurl(______).md>) — Returns a new file path URL that refers to the same resource as a specified URL.
- [CFURLCreateFileReferenceURL](<cfurlcreatefilereferenceurl(______).md>) — Returns a new file reference URL that points to the same resource as a specified URL.
- [CFURLCreateFromFileSystemRepresentation](<cfurlcreatefromfilesystemrepresentation(________).md>) — Creates a new `CFURL` object for a file system entity using the native representation.
- [CFURLCreateFromFileSystemRepresentationRelativeToBase](<cfurlcreatefromfilesystemrepresentationrelativetobase(__________).md>) — Creates a `CFURL` object from a native character string path relative to a base URL.
- [CFURLCreateFromFSRef](<cfurlcreatefromfsref(____).md>) — Creates a URL from a given directory or file. _(deprecated)_
- [CFURLCreateWithFileSystemPath](<cfurlcreatewithfilesystempath(________).md>) — Creates a `CFURL` object using a local file system path string.
- [CFURLCreateWithFileSystemPathRelativeToBase](<cfurlcreatewithfilesystempathrelativetobase(__________).md>) — Creates a `CFURL` object using a local file system path string relative to a base URL.
- [CFURLCreateWithString](<cfurlcreatewithstring(______).md>) — Creates a `CFURL` object using a given `CFString` object.
