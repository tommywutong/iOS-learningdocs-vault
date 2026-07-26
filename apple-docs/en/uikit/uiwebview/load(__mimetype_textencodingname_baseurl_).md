---
title: 'load(_:mimeType:textEncodingName:baseURL:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiwebview/load(_:mimetype:textencodingname:baseurl:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/load(_:mimetype:textencodingname:baseurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/load%28_%3Amimetype%3Atextencodingname%3Abaseurl%3A%29.json'
content_hash: 'sha256:c479729f0582e486'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# load(_:mimeType:textEncodingName:baseURL:)

<sub>Instance Method</sub>

Sets the main page contents, MIME type, content encoding, and base URL.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func load(_ data: Data, mimeType MIMEType: String, textEncodingName: String, baseURL: URL)
```

## Parameters

- `data` — The content for the main page.

- `MIMEType` — The MIME type of the content.

- `textEncodingName` — The IANA encoding name as in `utf-8` or `utf-16`.

- `baseURL` — The base URL for the content.

## See Also

### Loading content

- [- loadHTMLString:baseURL:](<loadhtmlstring(__baseurl_).md>) — Sets the main page content and base URL. _(deprecated)_
- [- loadRequest:](<loadrequest(__).md>) — Connects to a given URL by initiating an asynchronous client request. _(deprecated)_
- [request](request.md) — The URL request identifying the location of the content to load. _(deprecated)_
- [loading](isloading.md) — A Boolean value indicating whether the receiver is done loading content. _(deprecated)_
- [- stopLoading](<stoploading().md>) — Stops the loading of any web content managed by the receiver. _(deprecated)_
- [- reload](<reload().md>) — Reloads the current page. _(deprecated)_
