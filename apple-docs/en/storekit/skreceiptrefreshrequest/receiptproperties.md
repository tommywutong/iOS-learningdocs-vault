---
title: receiptProperties
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（18.0 起废弃）, iPadOS 7.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.9+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skreceiptrefreshrequest/receiptproperties
source_url: 'https://developer.apple.com/documentation/storekit/skreceiptrefreshrequest/receiptproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skreceiptrefreshrequest/receiptproperties.json'
content_hash: 'sha256:0b3caff33d6f79b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKReceiptRefreshRequest](../skreceiptrefreshrequest.md)

# receiptProperties

<sub>Instance Property</sub>

The properties of the receipt.

> [!warning] Deprecated
> Use Transaction.all and AppTransaction.shared.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var receiptProperties: [String : Any]? { get }
```

## Discussion

Receipt properties include [SKReceiptPropertyIsExpired](../skreceiptpropertyisexpired.md), [SKReceiptPropertyIsRevoked](../skreceiptpropertyisrevoked.md), and [SKReceiptPropertyIsVolumePurchase](../skreceiptpropertyisvolumepurchase.md).

## See Also

### Receipt Properties and Keys

- [SKReceiptPropertyIsExpired](../skreceiptpropertyisexpired.md) — A key with a value that indicates whether the receipt is in an expired state. _(deprecated)_
- [SKReceiptPropertyIsRevoked](../skreceiptpropertyisrevoked.md) — A key with a value that indicates whether the receipt is in a revoked state. _(deprecated)_
- [SKReceiptPropertyIsVolumePurchase](../skreceiptpropertyisvolumepurchase.md) — A key with a value that indicates whether the receipt is a Volume Purchase Plan receipt. _(deprecated)_
