---
title: request
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/request
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/request'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/request.json'
content_hash: 'sha256:e6aa2553b983499d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# request

<sub>Instance Property</sub>

The URL request identifying the location of the content to load.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var request: URLRequest? { get }
```

## See Also

### Loading content

- [- loadData:MIMEType:textEncodingName:baseURL:](<load(__mimetype_textencodingname_baseurl_).md>) — Sets the main page contents, MIME type, content encoding, and base URL. _(deprecated)_
- [- loadHTMLString:baseURL:](<loadhtmlstring(__baseurl_).md>) — Sets the main page content and base URL. _(deprecated)_
- [- loadRequest:](<loadrequest(__).md>) — Connects to a given URL by initiating an asynchronous client request. _(deprecated)_
- [loading](isloading.md) — A Boolean value indicating whether the receiver is done loading content. _(deprecated)_
- [- stopLoading](<stoploading().md>) — Stops the loading of any web content managed by the receiver. _(deprecated)_
- [- reload](<reload().md>) — Reloads the current page. _(deprecated)_
