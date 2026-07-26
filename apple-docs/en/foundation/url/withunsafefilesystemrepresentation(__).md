---
title: 'withUnsafeFileSystemRepresentation(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/withunsafefilesystemrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/withunsafefilesystemrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/withunsafefilesystemrepresentation%28_%3A%29.json'
content_hash: 'sha256:06a0b7d0e79aba55'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# withUnsafeFileSystemRepresentation(_:)

<sub>Instance Method</sub>

Passes the URL’s path in the file system representation to a closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withUnsafeFileSystemRepresentation<ResultType>(_ block: (UnsafePointer<Int8>?) throws -> ResultType) rethrows -> ResultType
```

## Parameters

- `block` — A closure to execute, which receives a C string as its parameter, and returns a value of a type you choose. The parameter passed to the closure is `nil` if the URL cannot be represented by the file system. For example, if the URL contains an accented character and the file system only supports ASCII, no file system representation is possible.

## Return Value

The value returned by your closure, if any.

## Discussion

The file system representation is a null-terminated C string with canonical UTF-8 encoding.

> [!note] Note
> The pointer is not valid outside the context of the closure.

## See Also

### Working with file URLs

- [isFileURL](isfileurl.md) — A Boolean that is true if the scheme is `file:`.
- [hasDirectoryPath](hasdirectorypath.md) — A Boolean that is true if the URL path represents a directory.
- [resolveSymlinksInPath()](<resolvesymlinksinpath().md>) — Resolves any symlinks in the path of a file URL.
- [resolvingSymlinksInPath()](<resolvingsymlinksinpath().md>) — Resolves any symlinks in the path of a file URL.
- [standardize()](<standardize().md>) — Standardizes the path of a file URL.
