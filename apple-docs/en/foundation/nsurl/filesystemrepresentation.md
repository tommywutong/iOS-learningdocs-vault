---
title: fileSystemRepresentation
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/filesystemrepresentation
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/filesystemrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/filesystemrepresentation.json'
content_hash: 'sha256:33e69b847df30060'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# fileSystemRepresentation

<sub>Instance Property</sub>

A C string containing the URL’s file system path. (read-only)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileSystemRepresentation: UnsafePointer<CChar> { get }
```

## Discussion

This returns a null-terminated C string in file system representation.

This string is automatically freed in the same way that a returned object would be released. The caller must either copy the string or use [- getFileSystemRepresentation:maxLength:](<getfilesystemrepresentation(__maxlength_).md>) if it needs to store the representation outside of the autorelease context in which the value was obtained.

The file system representation format is described in File Encodings and Fonts.

## See Also

### Accessing the Parts of the URL

- [absoluteString](absolutestring.md) — The URL string for the receiver as an absolute URL. (read-only)
- [absoluteURL](absoluteurl.md) — An absolute URL that refers to the same resource as the receiver. (read-only)
- [baseURL](baseurl.md) — The base URL. (read-only)
- [fragment](fragment.md) — The fragment identifier, conforming to RFC 1808. (read-only)
- [host](host.md) — The host, conforming to RFC 1808. (read-only)
- [lastPathComponent](lastpathcomponent.md) — The last path component. (read-only)
- [parameterString](parameterstring.md) — The parameter string conforming to RFC 1808. (read-only) _(deprecated)_
- [password](password.md) — The password conforming to RFC 1808. (read-only)
- [path](path.md) — The path, conforming to RFC 1808. (read-only)
- [pathComponents](pathcomponents.md) — An array containing the  path components. (read-only)
- [pathExtension](pathextension.md) — The path extension. (read-only)
- [port](port.md) — The port, conforming to RFC 1808.
- [query](query.md) — The query string, conforming to RFC 1808.
- [relativePath](relativepath.md) — The relative path, conforming to RFC 1808. (read-only)
- [relativeString](relativestring.md) — A string representation of the relative portion of the URL. (read-only)
