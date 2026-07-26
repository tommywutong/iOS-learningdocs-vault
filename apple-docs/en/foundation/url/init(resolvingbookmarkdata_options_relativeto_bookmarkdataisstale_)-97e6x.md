---
title: 'init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-97e6x'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(resolvingbookmarkdata:options:relativeto:bookmarkdataisstale:)-97e6x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28resolvingbookmarkdata%3Aoptions%3Arelativeto%3Abookmarkdataisstale%3A%29-97e6x.json'
content_hash: 'sha256:17419865e877dda0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)

<sub>Initializer</sub>

Initializes a URL that refers to a location specified by resolving bookmark data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(resolvingBookmarkData data: Data, options: URL.BookmarkResolutionOptions = [], relativeTo url: URL? = nil, bookmarkDataIsStale: inout Bool) throws
```

## See Also

### Creating a URL from a string

- [init(string:)](<init(string_).md>) — Creates a URL instance from the provided string.
- [init(string:encodingInvalidCharacters:)](<init(string_encodinginvalidcharacters_).md>) — Creates a URL instance from the provided string, optionally IDNA- and percent-encoding any invalid characters.
- [init(string:relativeTo:)](<init(string_relativeto_).md>) — Creates a URL instance from the provided string, relative to another URL.
- [init(resolvingBookmarkData:options:relativeTo:bookmarkDataIsStale:)](<init(resolvingbookmarkdata_options_relativeto_bookmarkdataisstale_)-3ic6f.md>) — Creates a URL that refers to a location specified by resolving bookmark data.
