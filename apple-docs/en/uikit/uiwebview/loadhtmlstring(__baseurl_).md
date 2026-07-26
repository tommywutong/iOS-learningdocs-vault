---
title: 'loadHTMLString(_:baseURL:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiwebview/loadhtmlstring(_:baseurl:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/loadhtmlstring(_:baseurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/loadhtmlstring%28_%3Abaseurl%3A%29.json'
content_hash: 'sha256:0dea28062ca7e056'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# loadHTMLString(_:baseURL:)

<sub>Instance Method</sub>

Sets the main page content and base URL.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func loadHTMLString(_ string: String, baseURL: URL?)
```

## Parameters

- `string` — The content for the main page.

- `baseURL` — The base URL for the content.

## Discussion

To help you avoid being vulnerable to security attacks, be sure to use this method to load local HTML files; don’t use [- loadRequest:](<loadrequest(__).md>).

## See Also

### Loading content

- [- loadData:MIMEType:textEncodingName:baseURL:](<load(__mimetype_textencodingname_baseurl_).md>) — Sets the main page contents, MIME type, content encoding, and base URL. _(deprecated)_
- [- loadRequest:](<loadrequest(__).md>) — Connects to a given URL by initiating an asynchronous client request. _(deprecated)_
- [request](request.md) — The URL request identifying the location of the content to load. _(deprecated)_
- [loading](isloading.md) — A Boolean value indicating whether the receiver is done loading content. _(deprecated)_
- [- stopLoading](<stoploading().md>) — Stops the loading of any web content managed by the receiver. _(deprecated)_
- [- reload](<reload().md>) — Reloads the current page. _(deprecated)_
