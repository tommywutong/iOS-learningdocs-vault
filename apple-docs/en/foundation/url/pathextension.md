---
title: pathExtension
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/pathextension
source_url: 'https://developer.apple.com/documentation/foundation/url/pathextension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/pathextension.json'
content_hash: 'sha256:1b75f52d89d250cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# pathExtension

<sub>Instance Property</sub>

The path extension of the URL, or an empty string if the path is an empty string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pathExtension: String { get }
```

## See Also

### Accessing the parts of a URL

- [fragment(percentEncoded:)](<fragment(percentencoded_).md>) — Returns the fragment component of the URL, optionally removing any percent-encoding.
- [fragment](fragment.md) — The fragment component of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [host(percentEncoded:)](<host(percentencoded_).md>) — Returns the host component of the URL, optionally removing any percent-encoding.
- [host](host.md) — The host component of a URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [lastPathComponent](lastpathcomponent.md) — The last path component of the URL, or an empty string if the path is an empty string.
- [path(percentEncoded:)](<path(percentencoded_).md>) — Returns the path component of the URL, optionally removing any percent-encoding.
- [path](path.md) — The path component of the URL if the URL conforms to RFC 3986; otherwise, an empty string. _(deprecated)_
- [password(percentEncoded:)](<password(percentencoded_).md>) — Returns the password component of the URL, optionally removing any percent-encoding.
- [password](password.md) — The password component of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [pathComponents](pathcomponents.md) — The path components of the URL, or an empty array if the path is an empty string.
- [port](port.md) — The port component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [query(percentEncoded:)](<query(percentencoded_).md>) — Returns the query component of the URL, optionally removing any percent-encoding.
- [query](query.md) — The query of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [scheme](scheme.md) — The scheme of the URL.
- [user(percentEncoded:)](<user(percentencoded_).md>) — Returns the user component of the URL, optionally removing any percent-encoding.
