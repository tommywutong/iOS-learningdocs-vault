---
title: 'init(receiptProperties:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+（18.0 起废弃）, iPadOS 7.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.9+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/storekit/skreceiptrefreshrequest/init(receiptproperties:)'
source_url: 'https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/init(receiptproperties:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skreceiptrefreshrequest/init%28receiptproperties%3A%29.json'
content_hash: 'sha256:750a63eba0d76f01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKReceiptRefreshRequest](../skreceiptrefreshrequest.md)

# init(receiptProperties:)

<sub>Initializer</sub>

Creates a receipt refresh request with optional properties.

> [!warning] Deprecated
> Use Transaction.all and AppTransaction.shared.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(receiptProperties properties: [String : Any]?)
```

## Parameters

- `properties` — In the test environment, the properties that the new receipt is to have. For keys, see Receipt Properties and Keys. In the production environment, set this parameter to `nil`.

## Return Value

The initialized request.

## Discussion

In the sandbox environment, you can initialize a receipt with any combination of properties to test the state transitions related to Volume Purchase Plan receipts. Set the `properties` when you call this initializer.
