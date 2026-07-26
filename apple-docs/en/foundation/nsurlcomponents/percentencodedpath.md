---
title: percentEncodedPath
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents/percentencodedpath
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/percentencodedpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/percentencodedpath.json'
content_hash: 'sha256:2a9b7aaa7237cad3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# percentEncodedPath

<sub>Instance Property</sub>

The path URL component expressed as a URL-encoded string, or `nil` if not present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var percentEncodedPath: String? { get set }
```

## Discussion

For example, in the URL `http://www.example.com/index.html`, the path is `/index.html`.

If you set this value to something that is not a valid, percent-encoded string, this class throws an exception.

> [!note] Note
> Although an unencoded semicolon is a valid character in a percent-encoded path, for compatibility with the [NSURL](../nsurl.md) class, you should always percent-encode it. To properly encode a string for use in the path component of a URL, use the character set returned by the `URLPathAllowedCharacterSet` method in conjunction with the [- stringByAddingPercentEncodingWithAllowedCharacters:](<../nsstring/addingpercentencoding(withallowedcharacters_).md>) method.

## See Also

### Accessing components in URL-encoded format

- [percentEncodedFragment](percentencodedfragment.md) — The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedHost](percentencodedhost.md) — The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present. _(deprecated)_
- [percentEncodedPassword](percentencodedpassword.md) — The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedQuery](percentencodedquery.md) — The query URL component expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedUser](percentencodeduser.md) — The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
