---
title: preorderDate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/preorderdate
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/preorderdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/preorderdate.json'
content_hash: 'sha256:89d366ffb2f64031'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# preorderDate

<sub>Instance Property</sub>

The date the customer placed an order for the app before it’s available in the App Store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let preorderDate: Date?
```

## Discussion

This date is present if your app is available for preorder and the customer places an order before your app is available in the App Store. When your app becomes available, the App Store fulfills the customer’s order. The [preorderDate](preorderdate.md) remains the same.

Use this date to recognize customers who place preorders.

For more infomation about preorders, see [Offering Your Apps for Pre-Order](https://developer.apple.com/app-store/pre-orders/).

## See Also

### Getting purchase dates

- [originalPurchaseDate](originalpurchasedate.md) — The date the customer originally purchased the app from the App Store.
