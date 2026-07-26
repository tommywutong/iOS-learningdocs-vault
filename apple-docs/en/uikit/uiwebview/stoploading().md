---
title: stopLoading()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（12.0 起废弃）, iPadOS 2.0+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwebview/stoploading()
source_url: 'https://developer.apple.com/documentation/uikit/uiwebview/stoploading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwebview/stoploading%28%29.json'
content_hash: 'sha256:eabfbd15c8da07d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWebView](../uiwebview.md)

# stopLoading()

<sub>Instance Method</sub>

Stops the loading of any web content managed by the receiver.

> [!warning] Deprecated
> For more information, see [UIWebView](../uiwebview.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func stopLoading()
```

## Discussion

Stops any content in the process of being loaded by the main frame or any of its children frames. Does nothing if no content is being loaded.

## See Also

### Loading content

- [- loadData:MIMEType:textEncodingName:baseURL:](<load(__mimetype_textencodingname_baseurl_).md>) — Sets the main page contents, MIME type, content encoding, and base URL. _(deprecated)_
- [- loadHTMLString:baseURL:](<loadhtmlstring(__baseurl_).md>) — Sets the main page content and base URL. _(deprecated)_
- [- loadRequest:](<loadrequest(__).md>) — Connects to a given URL by initiating an asynchronous client request. _(deprecated)_
- [request](request.md) — The URL request identifying the location of the content to load. _(deprecated)_
- [loading](isloading.md) — A Boolean value indicating whether the receiver is done loading content. _(deprecated)_
- [- reload](<reload().md>) — Reloads the current page. _(deprecated)_
