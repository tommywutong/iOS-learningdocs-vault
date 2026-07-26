---
title: 'CFURLCreateWithFileSystemPath(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreatewithfilesystempath(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatewithfilesystempath(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatewithfilesystempath%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:981dd159fd8f088e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateWithFileSystemPath(_:_:_:_:)

<sub>Function</sub>

Creates a `CFURL` object using a local file system path string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateWithFileSystemPath(_ allocator: CFAllocator!, _ filePath: CFString!, _ pathStyle: CFURLPathStyle, _ isDirectory: Bool) -> CFURL!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `filePath` — The path string to convert to a `CFURL` object.

- `pathStyle` — The operating system path style used in `filePath`. See [CFURLPathStyle](cfurlpathstyle.md) for a list of possible values.

- `isDirectory` — A Boolean value that specifies whether `filePath` is treated as a directory path when resolving against relative path components. Pass `true` if the pathname indicates a directory, `false` otherwise.

## Return Value

A new `CFURL` object. Ownership follows the create rule. See [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

If `filePath` is not absolute, the resulting URL will be considered relative to the current working directory (evaluated when this function is being invoked).

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
- [CFURLCreateWithBytes](<cfurlcreatewithbytes(__________).md>) — Creates a `CFURL` object using a given character bytes.
- [CFURLCreateWithFileSystemPathRelativeToBase](<cfurlcreatewithfilesystempathrelativetobase(__________).md>) — Creates a `CFURL` object using a local file system path string relative to a base URL.
- [CFURLCreateWithString](<cfurlcreatewithstring(______).md>) — Creates a `CFURL` object using a given `CFString` object.
