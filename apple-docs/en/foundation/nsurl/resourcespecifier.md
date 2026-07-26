---
title: resourceSpecifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/resourcespecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/resourcespecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/resourcespecifier.json'
content_hash: 'sha256:4c077838eee9362f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# resourceSpecifier

<sub>Instance Property</sub>

The resource specifier. (read-only)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resourceSpecifier: String? { get }
```

## Discussion

This property contains the resource specifier. Any percent-encoded characters are not unescaped. For example, in the URL `http://www.example.com/index.html?key1=value1#jumplink`, the resource specifier is `//www.example.com/index.html?key1=value1#jumplink` (everything after the colon).

> [!important] Important
> If the receiver does not specify a net location portion of the URL, as returned by the toll-free bridged `CFURL` function [CFURLCopyNetLocation(_:)](<../../corefoundation/cfurlcopynetlocation(__).md>), then this method returns only the path of the receiver. For example, in the URL `file:///file.txt`, the resource specifier is `/file.txt`.

## See Also

### Accessing the Parts of the URL

- [absoluteString](absolutestring.md) — The URL string for the receiver as an absolute URL. (read-only)
- [absoluteURL](absoluteurl.md) — An absolute URL that refers to the same resource as the receiver. (read-only)
- [baseURL](baseurl.md) — The base URL. (read-only)
- [fileSystemRepresentation](filesystemrepresentation.md) — A C string containing the URL’s file system path. (read-only)
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
