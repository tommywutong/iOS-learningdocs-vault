---
title: 'appendingPathComponent(_:conformingTo:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurl/appendingpathcomponent(_:conformingto:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/appendingpathcomponent(_:conformingto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/appendingpathcomponent%28_%3Aconformingto%3A%29.json'
content_hash: 'sha256:660a54db9d169351'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# appendingPathComponent(_:conformingTo:)

<sub>Instance Method</sub>

Returns a URL by appending the specified path component with the file extension for a uniform type identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func appendingPathComponent(_ partialName: String, conformingTo contentType: UTType) -> URL
```

## Parameters

- `partialName` — The partial name to append.

- `contentType` — A uniform type identifier the resulting conforms to.

## Return Value

A new URL with the partial name and the type’s preferred extension appended.

## Discussion

Use this method when you want to mix partial input from a user or other source, and need to produce a complete filename suitable for that input. For example, if you download a file from the internet and know its MIME type, you can use this method to ensure the URL has the correct filename extension where you save the file.

If `partialName` already has a path extension, and that path extension is valid for file system objects of type `contentType`, the function doesn’t add an extension before appending it to the URL. For example, if the inputs are `puppy.jpg` and [image](../../uniformtypeidentifiers/uttype-swift.struct/image.md), respectively, the function returns a URL with an appended path component of `puppy.jpg`. However, if the inputs are `puppy.jpg` and [plainText](../../uniformtypeidentifiers/uttype-swift.struct/plaintext.md), respectively, the function returns a URL with an appended path component of `puppy.jpg.txt`. If you want to replace any existing path extension, use the [deletePathExtension()](<../url/deletepathextension().md>) method first.

If the function can’t append the path component, it returns an unchanged URL.

> [!note] Note
> The modified URL has a directory path if `contentType` conforms to [directory](../../uniformtypeidentifiers/uttype-swift.struct/directory.md).

For more information about types, see [Uniform Type Identifiers](../../uniformtypeidentifiers.md).

## See Also

### Modifying and Converting a File URL

- [filePathURL](filepathurl.md) — A file path URL that points to the same resource as the URL object. (read-only)
- [- fileReferenceURL](<filereferenceurl().md>) — Returns a new file reference URL that points to the same resource as the receiver.
- [- URLByAppendingPathComponent:](<appendingpathcomponent(__).md>) — Returns a new URL by appending a path component to the original URL.
- [- URLByAppendingPathComponent:isDirectory:](<appendingpathcomponent(__isdirectory_).md>) — Returns a new URL by appending a path component to the original URL, along with a trailing slash if the component is a directory.
- [- URLByAppendingPathExtension:](<appendingpathextension(__).md>) — Returns a new URL by appending a path extension to the original URL.
- [- URLByAppendingPathExtensionForType:](<appendingpathextension(for_).md>) — Returns a URL by appending the path extension for a uniform type identifier.
- [URLByDeletingLastPathComponent](deletinglastpathcomponent.md) — A URL you create by removing the last path component from the receiver. (read-only)
- [URLByDeletingPathExtension](deletingpathextension.md) — A URL you create by removing the path extension from the receiver, if any. (read-only)
- [URLByResolvingSymlinksInPath](resolvingsymlinksinpath.md) — A URL that points to the same resource as the receiver and includes no symbolic links. (read-only)
- [URLByStandardizingPath](standardizingpath.md) — A URL that points to the same resource as the original URL using an absolute path. (read-only)
- [hasDirectoryPath](hasdirectorypath.md) — A Boolean value that indicates whether the URL string’s path represents a directory.
