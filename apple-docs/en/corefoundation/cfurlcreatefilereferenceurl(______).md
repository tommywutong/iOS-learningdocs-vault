---
title: 'CFURLCreateFileReferenceURL(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfurlcreatefilereferenceurl(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcreatefilereferenceurl(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcreatefilereferenceurl%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:74b311d343c0e20e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLCreateFileReferenceURL(_:_:_:)

<sub>Function</sub>

Returns a new file reference URL that points to the same resource as a specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFURLCreateFileReferenceURL(_ allocator: CFAllocator!, _ url: CFURL!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Unmanaged<CFURL>!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new `CFURL` object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `url` — The URL.

- `error` — The error that occurred if the URL could not be created.

## Return Value

The new file reference URL, or `NULL` if an error occurs.

## Discussion

File reference URLs use a URL path syntax that identifies a file system object by reference, not by path. This form of file URL remains valid when the file system path of the URL’s underlying resource changes.

If the original URL is a file path URL, this function returns a copy of the URL converted into a file reference URL. If the original URL is a file reference URL, this function returns the original. If the original URL is not a file URL, this function returns `nil`.

File reference URLs cannot be created to file system objects which do not exist or are not reachable. This function returns `nil` instead.

In some areas of the file system hierarchy, file reference URLs cannot be generated to the leaf node of the URL path.

> [!important] Important
> A file reference URL’s path should never be persistently stored, because it is not valid across system restarts or remounts of volumes. If you need to store a persistent reference to a file system object, use a bookmark instead. You can create a bookmark by calling [CFURLCreateBookmarkData](<cfurlcreatebookmarkdata(____________).md>).

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
- [CFURLCreateFromFileSystemRepresentation](<cfurlcreatefromfilesystemrepresentation(________).md>) — Creates a new `CFURL` object for a file system entity using the native representation.
- [CFURLCreateFromFileSystemRepresentationRelativeToBase](<cfurlcreatefromfilesystemrepresentationrelativetobase(__________).md>) — Creates a `CFURL` object from a native character string path relative to a base URL.
- [CFURLCreateFromFSRef](<cfurlcreatefromfsref(____).md>) — Creates a URL from a given directory or file. _(deprecated)_
- [CFURLCreateWithBytes](<cfurlcreatewithbytes(__________).md>) — Creates a `CFURL` object using a given character bytes.
- [CFURLCreateWithFileSystemPath](<cfurlcreatewithfilesystempath(________).md>) — Creates a `CFURL` object using a local file system path string.
- [CFURLCreateWithFileSystemPathRelativeToBase](<cfurlcreatewithfilesystempathrelativetobase(__________).md>) — Creates a `CFURL` object using a local file system path string relative to a base URL.
- [CFURLCreateWithString](<cfurlcreatewithstring(______).md>) — Creates a `CFURL` object using a given `CFString` object.
