---
title: 'contentURL(forProductID:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skdownload/contenturl(forproductid:)'
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/contenturl(forproductid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/contenturl%28forproductid%3A%29.json'
content_hash: 'sha256:151e2692c8540807'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# contentURL(forProductID:)

<sub>Type Method</sub>

Returns the local location for the previously downloaded flie.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>Mac Catalyst, macOS</sub>

```swift
class func contentURL(forProductID productID: String) -> URL?
```

## Parameters

- `productID` — The product identifier.

## Return Value

The local location for the previously downloaded flie.

## Discussion

Use this method to locate the content on subsequent launches of your app.

## See Also

### Managing Downloaded Content

- [+ deleteContentForProductID:](<deletecontent(forproductid_).md>) — Deletes the previously downloaded file. _(deprecated)_
