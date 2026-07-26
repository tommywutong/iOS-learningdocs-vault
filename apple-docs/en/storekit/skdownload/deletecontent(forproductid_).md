---
title: 'deleteContent(forProductID:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [Mac Catalyst 13.0+（16.0 起废弃）, macOS 10.8+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skdownload/deletecontent(forproductid:)'
source_url: 'https://developer.apple.com/documentation/storekit/skdownload/deletecontent(forproductid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skdownload/deletecontent%28forproductid%3A%29.json'
content_hash: 'sha256:69ecd7f621fb031a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKDownload](../skdownload.md)

# deleteContent(forProductID:)

<sub>Type Method</sub>

Deletes the previously downloaded file.

> [!warning] Deprecated
> Hosted content is no longer supported.

<sub>Mac Catalyst, macOS</sub>

```swift
class func deleteContent(forProductID productID: String)
```

## Parameters

- `productID` — The product identifier.

## See Also

### Managing Downloaded Content

- [+ contentURLForProductID:](<contenturl(forproductid_).md>) — Returns the local location for the previously downloaded flie. _(deprecated)_
