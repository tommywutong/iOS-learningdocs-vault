---
title: 'cookies(withResponseHeaderFields:for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/httpcookie/cookies(withresponseheaderfields:for:)'
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/cookies(withresponseheaderfields:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/cookies%28withresponseheaderfields%3Afor%3A%29.json'
content_hash: 'sha256:f3e7131ad50d3a86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# cookies(withResponseHeaderFields:for:)

<sub>Type Method</sub>

Creates an array of HTTP cookies that corresponds to the provided response header fields for the provided URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func cookies(withResponseHeaderFields headerFields: [String : String], for URL: URL) -> [HTTPCookie]
```

## Parameters

- `headerFields` — The header fields used to create the [HTTPCookie](../httpcookie.md) objects.

- `URL` — The URL associated with the created cookies.

## Return Value

The array of created cookies.

## Discussion

This method ignores irrelevant header fields in `headerFields`, allowing dictionaries to contain additional data.

If `headerFields` doesn’t specify a domain for a given cookie, the cookie is created with a default domain value of `URL`.

If `headerFields` doesn’t specify a path for a given cookie, the cookie is created with a default path value of `"/"`.

## See Also

### Creating cookies

- [- initWithProperties:](<init(properties_).md>) — Initializes an HTTP cookie object with the given cookie properties.
