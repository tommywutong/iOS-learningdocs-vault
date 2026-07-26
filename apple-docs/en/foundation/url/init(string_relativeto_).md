---
title: 'init(string:relativeTo:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(string:relativeto:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(string:relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28string%3Arelativeto%3A%29.json'
content_hash: 'sha256:caf8f64cb693ebb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(string:relativeTo:)

<sub>Initializer</sub>

Creates a URL instance from the provided string, relative to another URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(string: String, relativeTo url: URL?)
```

## Parameters

- `string` — A relative URL location.

- `url` — A URL that provides a base location that the string extends.

## Discussion

> [!important] Important
> For apps linked on or after iOS 17 and aligned OS versions, [URL](../url.md) parsing has updated from the obsolete RFC 1738/1808 parsing to the same [RFC 3986](https://www.ietf.org/rfc/rfc3986.txt) parsing as [URLComponents](../urlcomponents.md). This unifies the parsing behaviors of the `URL` and `URLComponents` APIs. Now, `URL` automatically percent- and IDNA-encodes invalid characters to help create a valid URL.

This initializer returns `nil` if the string doesn’t represent a valid URL even after encoding invalid characters. To check if a URL string is strictly valid according to the RFC, use the new [init(string:encodingInvalidCharacters:)](<init(string_encodinginvalidcharacters_).md>) initializer and pass `encodingInvalidCharacters: false`. This leaves all characters as they are and returns `nil` if the URL string is explicitly invalid.

## See Also

### Creating a URL from a string

- [init(string:)](<init(string_).md>) — Creates a URL instance from the provided string.
- [init(string:encodingInvalidCharacters:)](<init(string_encodinginvalidcharacters_).md>) — Creates a URL instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)](<init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_)-3ic6f.md>) — Creates a URL that refers to a location specified by resolving bookmark data.
- [init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)](<init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_)-97e6x.md>) — Initializes a URL that refers to a location specified by resolving bookmark data.
