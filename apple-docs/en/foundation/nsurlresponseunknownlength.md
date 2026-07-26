---
title: NSURLResponseUnknownLength
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlresponseunknownlength
source_url: 'https://developer.apple.com/documentation/foundation/nsurlresponseunknownlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlresponseunknownlength.json'
content_hash: 'sha256:aa97288925c12948'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSURLResponseUnknownLength

<sub>Macro</sub>

The response length cannot be determined in advance of receiving the data from the server.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define NSURLResponseUnknownLength
```

## Discussion

For example, [NSURLResponseUnknownLength](nsurlresponseunknownlength.md) is returned when the server HTTP response does not include a `Content-Length` header.

## See Also

### Getting the response properties

- [expectedContentLength](urlresponse/expectedcontentlength.md) — The expected length of the response’s content.
- [suggestedFilename](urlresponse/suggestedfilename.md) — A suggested filename for the response data.
- [MIMEType](urlresponse/mimetype.md) — The MIME type of the response.
- [textEncodingName](urlresponse/textencodingname.md) — The name of the text encoding provided by the response’s originating source.
- [URL](urlresponse/url.md) — The URL for the response.
