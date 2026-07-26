---
title: mimeType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresponse/mimetype
source_url: 'https://developer.apple.com/documentation/foundation/urlresponse/mimetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresponse/mimetype.json'
content_hash: 'sha256:12181d058311b5b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResponse](../urlresponse.md)

# mimeType

<sub>Instance Property</sub>

The MIME type of the response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mimeType: String? { get }
```

## Discussion

The MIME type is often provided by the response’s originating source. However, that value may be changed or corrected by a protocol implementation if it can be determined that the response’s source reported the information incorrectly.

If the response’s originating source does not provide a MIME type, an attempt to guess the MIME type may be made.

## See Also

### Getting the response properties

- [expectedContentLength](expectedcontentlength.md) — The expected length of the response’s content.
- [suggestedFilename](suggestedfilename.md) — A suggested filename for the response data.
- [textEncodingName](textencodingname.md) — The name of the text encoding provided by the response’s originating source.
- [URL](url.md) — The URL for the response.
