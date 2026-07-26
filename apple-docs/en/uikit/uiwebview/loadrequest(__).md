---
title: 'loadRequest(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiwebview/loadrequest(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/loadrequest(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/loadrequest%28_%3A%29.json'
content_hash: 'sha256:5706ef7a4d8d1d4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# loadRequest(_:)

<sub>Instance Method</sub>

Connects to a given URL by initiating an asynchronous client request.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func loadRequest(_ request: URLRequest)
```

## Parameters

- `request` — A URL request identifying the location of the content to load.

## Discussion

Don’t use this method to load local HTML files; instead, use [- loadHTMLString:baseURL:](<loadhtmlstring(__baseurl_).md>). To stop this load, use the [- stopLoading](<stoploading().md>) method. To see whether the receiver is done loading the content, use the [loading](isloading.md) property.

## See Also

### Loading content

- [- loadData:MIMEType:textEncodingName:baseURL:](<load(__mimetype_textencodingname_baseurl_).md>) — Sets the main page contents, MIME type, content encoding, and base URL. _(deprecated)_
- [- loadHTMLString:baseURL:](<loadhtmlstring(__baseurl_).md>) — Sets the main page content and base URL. _(deprecated)_
- [request](request.md) — The URL request identifying the location of the content to load. _(deprecated)_
- [loading](isloading.md) — A Boolean value indicating whether the receiver is done loading content. _(deprecated)_
- [- stopLoading](<stoploading().md>) — Stops the loading of any web content managed by the receiver. _(deprecated)_
- [- reload](<reload().md>) — Reloads the current page. _(deprecated)_
