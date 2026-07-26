---
title: path
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurl/path
source_url: 'https://developer.apple.com/documentation/foundation/nsurl/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurl/path.json'
content_hash: 'sha256:40b414e9c33cb25e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURL](../nsurl.md)

# path

<sub>Instance Property</sub>

The path, conforming to RFC 1808. (read-only)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var path: String? { get }
```

## Discussion

This property contains the path, unescaped using the [- stringByReplacingPercentEscapesUsingEncoding:](<../nsstring/replacingpercentescapes(using_).md>) method. If the receiver does not conform to RFC 1808, this property contains `nil`.

If the receiver contains a file or file reference URL (as determined with [fileURL](isfileurl.md)), this property’s value is suitable for input into methods of `NSFileManager` or `NSPathUtilities`. If the path has a trailing slash, it is stripped.

If the receiver contains a file reference URL, this property’s value provides the _current path_ for the referenced resource, which may be `nil` if the resource no longer exists.

If the [parameterString](parameterstring.md) property contains a non-`nil` value, the path may be incomplete. If the receiver contains an unencoded semicolon, the path property ends at the character before the semicolon. The remainder of the URL is provided in the [parameterString](parameterstring.md) property.

To obtain the complete path, if [parameterString](parameterstring.md) contains a non-`nil` value, append a semicolon, followed by the parameter string.

Per RFC 3986, the leading slash after the authority (host name and port) portion is treated as part of the path. For example, in the URL `http://www.example.com/index.html`, the path is `/index.html`.

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
- [pathComponents](pathcomponents.md) — An array containing the  path components. (read-only)
- [pathExtension](pathextension.md) — The path extension. (read-only)
- [port](port.md) — The port, conforming to RFC 1808.
- [query](query.md) — The query string, conforming to RFC 1808.
- [relativePath](relativepath.md) — The relative path, conforming to RFC 1808. (read-only)
- [relativeString](relativestring.md) — A string representation of the relative portion of the URL. (read-only)
