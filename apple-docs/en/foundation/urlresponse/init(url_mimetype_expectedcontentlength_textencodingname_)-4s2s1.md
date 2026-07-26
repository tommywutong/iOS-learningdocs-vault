---
title: 'init(url:mimeType:expectedContentLength:textEncodingName:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlresponse/init(url:mimetype:expectedcontentlength:textencodingname:)-4s2s1'
source_url: 'https://developer.apple.com/documentation/foundation/urlresponse/init(url:mimetype:expectedcontentlength:textencodingname:)-4s2s1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresponse/init%28url%3Amimetype%3Aexpectedcontentlength%3Atextencodingname%3A%29-4s2s1.json'
content_hash: 'sha256:d5723544cc7d35ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResponse](../urlresponse.md)

# init(url:mimeType:expectedContentLength:textEncodingName:)

<sub>Initializer</sub>

Creates an initialized [URLResponse](../urlresponse.md) object with the URL, MIME type, length, and text encoding set to given values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(url URL: URL, mimeType MIMEType: String?, expectedContentLength length: Int, textEncodingName name: String?)
```

## Parameters

- `URL` — The URL for the new object.

- `MIMEType` — The MIME type.

- `length` — The expected content length.This value should be `–1` if the expected length is undetermined

- `name` — The text encoding name. This value may be `nil`.

## Return Value

The initialized URL response.

## Discussion

This is the designated initializer for [URLResponse](../urlresponse.md).

## See Also

### Related Documentation

- [- initWithURL:statusCode:HTTPVersion:headerFields:](<../httpurlresponse/init(url_statuscode_httpversion_headerfields_)-21j4x.md>) — Initializes an HTTP URL response object with a status code, protocol version, and response headers.
