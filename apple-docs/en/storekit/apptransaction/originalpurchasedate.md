---
title: originalPurchaseDate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/originalpurchasedate
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/originalpurchasedate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/originalpurchasedate.json'
content_hash: 'sha256:042f0158e8428113'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# originalPurchaseDate

<sub>Instance Property</sub>

The date the customer originally purchased the app from the App Store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let originalPurchaseDate: Date
```

## Discussion

The original purchase date remains the same, even if the customer deletes and reinstalls the app.

In the sandbox testing environment, the original purchase date is always 2013-08-01 12 AM PDT, which is 1375340400000 milliseconds in UNIX epoch time.

## See Also

### Getting purchase dates

- [preorderDate](preorderdate.md) — The date the customer placed an order for the app before it’s available in the App Store.
