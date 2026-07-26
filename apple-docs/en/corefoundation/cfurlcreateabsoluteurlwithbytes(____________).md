---
title: 'CFURLCreateAbsoluteURLWithBytes(_:_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreateabsoluteurlwithbytes(_:_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreateabsoluteurlwithbytes(_:_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreateabsoluteurlwithbytes%28_%3A_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:49f3bcf5e7eadb1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateAbsoluteURLWithBytes(_:_:_:_:_:_:)

<sub>Function</sub>

Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateAbsoluteURLWithBytes(_ alloc: CFAllocator!, _ relativeURLBytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ encoding: CFStringEncoding, _ baseURL: CFURL!, _ useCompatibilityMode: Bool) -> CFURL!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `relativeURLBytes` — The character bytes that represent a relative URL to convert into a `CFURL` object.

- `length` — The number of bytes in `relativeURLBytes`.

- `encoding` — The string encoding of the `relativeURLBytes` string. This encoding is also used to interpret percent escape sequences.

- `baseURL` — The URL to which `relativeURLBytes` is relative.

- `useCompatibilityMode` — If `true`, the rules historically used on the web are used to resolve the string specified by the `relativeURLBytes` parameter against `baseURL`. These rules are generally listed in the RFC as optional or alternate interpretations. Otherwise, the strict rules from the RFC are used.

## Return Value

A new `CFURL` object, or `NULL` if `relativeURLBytes` cannot be made absolute. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

This function interprets the provided bytes using the specified string encoding to create the relative portion of the URL’s address.

> [!note] Note
> This function does not support string encoding which isn’t a superset of ASCII encoding. Both [CFURLGetBytes](<cfurlgetbytes(______).md>) and [CFURLGetByteRangeForComponent](<cfurlgetbyterangeforcomponent(______).md>) require 7-bit ASCII characters to be stored in a single 8-bit byte. The following [CFStringEncodings](cfstringencodings.md) can be used: [kCFStringEncodingMacRoman](cfstringbuiltinencodings/macroman.md), [kCFStringEncodingWindowsLatin1](cfstringbuiltinencodings/windowslatin1.md), [kCFStringEncodingISOLatin1](cfstringbuiltinencodings/isolatin1.md), [kCFStringEncodingNextStepLatin](cfstringbuiltinencodings/nextsteplatin.md), [kCFStringEncodingASCII](cfstringbuiltinencodings/ascii.md) and [kCFStringEncodingUTF8](cfstringbuiltinencodings/utf8.md).

## See Also

### Creating a CFURL

- [CFURLCopyAbsoluteURL](<cfurlcopyabsoluteurl(__).md>) — Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
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
- [CFURLCreateWithBytes](<cfurlcreatewithbytes(__________).md>) — Creates a `CFURL` object using a given character bytes.
- [CFURLCreateWithFileSystemPath](<cfurlcreatewithfilesystempath(________).md>) — Creates a `CFURL` object using a local file system path string.
- [CFURLCreateWithFileSystemPathRelativeToBase](<cfurlcreatewithfilesystempathrelativetobase(__________).md>) — Creates a `CFURL` object using a local file system path string relative to a base URL.
- [CFURLCreateWithString](<cfurlcreatewithstring(______).md>) — Creates a `CFURL` object using a given `CFString` object.
