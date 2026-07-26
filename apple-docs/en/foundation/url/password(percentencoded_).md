---
title: 'password(percentEncoded:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/password(percentencoded:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/password(percentencoded:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/password%28percentencoded%3A%29.json'
content_hash: 'sha256:0b931cdd5a08ff1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# password(percentEncoded:)

<sub>Instance Method</sub>

Returns the password component of the URL, optionally removing any percent-encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func password(percentEncoded: Bool = true) -> String?
```

## Parameters

- `percentEncoded` — A Boolean value that indicates whether the URL percent-encodes any unreserved characters. Defaults to `true`.

## Return Value

The password component of the URL, optionally percent-encoding any unreserved characters.

## Discussion

The system doesn’t allow certain characters in the URL password component, so [URL](../url.md) percent-encodes those characters to create a valid URL. Calling this function with `percentEncoded = false` removes any percent-encoding and returns the unencoded password.

If the URL doesn’t contain a password component according to [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt), this function returns `nil`.

## See Also

### Accessing the parts of a URL

- [fragment(percentEncoded:)](<fragment(percentencoded_).md>) — Returns the fragment component of the URL, optionally removing any percent-encoding.
- [fragment](fragment.md) — The fragment component of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [host(percentEncoded:)](<host(percentencoded_).md>) — Returns the host component of the URL, optionally removing any percent-encoding.
- [host](host.md) — The host component of a URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [lastPathComponent](lastpathcomponent.md) — The last path component of the URL, or an empty string if the path is an empty string.
- [path(percentEncoded:)](<path(percentencoded_).md>) — Returns the path component of the URL, optionally removing any percent-encoding.
- [path](path.md) — The path component of the URL if the URL conforms to RFC 3986; otherwise, an empty string. _(deprecated)_
- [password](password.md) — The password component of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [pathComponents](pathcomponents.md) — The path components of the URL, or an empty array if the path is an empty string.
- [pathExtension](pathextension.md) — The path extension of the URL, or an empty string if the path is an empty string.
- [port](port.md) — The port component of the URL if the URL conforms to RFC 3986; otherwise, nil.
- [query(percentEncoded:)](<query(percentencoded_).md>) — Returns the query component of the URL, optionally removing any percent-encoding.
- [query](query.md) — The query of the URL if the URL conforms to RFC 3986; otherwise, nil. _(deprecated)_
- [scheme](scheme.md) — The scheme of the URL.
- [user(percentEncoded:)](<user(percentencoded_).md>) — Returns the user component of the URL, optionally removing any percent-encoding.
