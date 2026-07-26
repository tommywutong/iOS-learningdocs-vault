---
title: 'CFURLCreateCopyAppendingPathComponent(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreatecopyappendingpathcomponent(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatecopyappendingpathcomponent(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatecopyappendingpathcomponent%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2610d82bc190f73b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateCopyAppendingPathComponent(_:_:_:_:)

<sub>Function</sub>

Creates a copy of a given URL and appends a path component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateCopyAppendingPathComponent(_ allocator: CFAllocator!, _ url: CFURL!, _ pathComponent: CFString!, _ isDirectory: Bool) -> CFURL!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `url` — The `CFURL` object to which to append a path component.

- `pathComponent` — The path component to append to `url`.

- `isDirectory` — A Boolean value that specifies whether the string is treated as a directory path when resolving against relative path components. Pass `true` if the new component indicates a directory, `false` otherwise.

## Return Value

A copy of `url` appended with `pathComponent`. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The `isDirectory` argument specifies whether or not the new path component points to a file or a to directory. Note that the URL syntax for a directory and for a file at otherwise the same location are slightly different—directory URLs must end in “/”. If you have the URL `http://www.apple.com/foo/` and you append the path component `bar`, then if `isDirectory` is [true](../swift/true.md) then the resulting URL is `http://www.apple.com/foo/bar/`, whereas if `isDirectory` is [false](../swift/false.md) then the resulting URL is `http://www.apple.com/foo/bar`. This difference is particularly important if you resolve another URL against this new URL. `file.html` relative to `http://www.apple.com/foo/bar` is `http://www.apple.com/foo/file.html`, whereas `file.html` relative to `http://www.apple.com/foo/bar/` is `http://www.apple.com/foo/bar/file.html`.

## See Also

### Creating a CFURL

- [CFURLCopyAbsoluteURL](<cfurlcopyabsoluteurl(__).md>) — Creates a new `CFURL` object by resolving the relative portion of a URL against its base.
- [CFURLCreateAbsoluteURLWithBytes](<cfurlcreateabsoluteurlwithbytes(____________).md>) — Creates a new `CFURL` object by resolving the relative portion of a URL, specified as bytes, against its given base URL.
- [CFURLCreateByResolvingBookmarkData](<cfurlcreatebyresolvingbookmarkdata(______________).md>) — Returns a new URL made by resolving bookmark data.
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
