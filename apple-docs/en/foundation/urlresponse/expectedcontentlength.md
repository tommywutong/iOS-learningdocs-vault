---
title: expectedContentLength
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlresponse/expectedcontentlength
source_url: 'https://developer.apple.com/documentation/foundation/urlresponse/expectedcontentlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresponse/expectedcontentlength.json'
content_hash: 'sha256:1a53b5ba0816b1a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResponse](../urlresponse.md)

# expectedContentLength

<sub>Instance Property</sub>

The expected length of the response’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var expectedContentLength: Int64 { get }
```

## Discussion

This property’s value is [NSURLResponseUnknownLength](../nsurlresponseunknownlength.md) if the length can’t be determined.

Some protocol implementations report the content length as part of the response, but not all protocols guarantee to deliver that amount of data. Your app should be prepared to deal with more or less data.

## See Also

### Getting the response properties

- [suggestedFilename](suggestedfilename.md) — A suggested filename for the response data.
- [MIMEType](mimetype.md) — The MIME type of the response.
- [textEncodingName](textencodingname.md) — The name of the text encoding provided by the response’s originating source.
- [URL](url.md) — The URL for the response.
