---
title: SKReceiptPropertyIsVolumePurchase
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+（18.0 起废弃）, iPadOS 7.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.9+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skreceiptpropertyisvolumepurchase
source_url: 'https://developer.apple.com/documentation/storekit/skreceiptpropertyisvolumepurchase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skreceiptpropertyisvolumepurchase.json'
content_hash: 'sha256:6428009f75676324'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKReceiptPropertyIsVolumePurchase

<sub>Global Variable</sub>

A key with a value that indicates whether the receipt is a Volume Purchase Plan receipt.

> [!warning] Deprecated
> No longer supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let SKReceiptPropertyIsVolumePurchase: String
```

## Discussion

This key’s value is an instance of [NSNumber](../foundation/nsnumber.md) that the system interprets as a Boolean value that indicates whether the receipt is a Volume Purchase Plan receipt.

## See Also

### Receipt Properties and Keys

- [receiptProperties](skreceiptrefreshrequest/receiptproperties.md) — The properties of the receipt. _(deprecated)_
- [SKReceiptPropertyIsExpired](skreceiptpropertyisexpired.md) — A key with a value that indicates whether the receipt is in an expired state. _(deprecated)_
- [SKReceiptPropertyIsRevoked](skreceiptpropertyisrevoked.md) — A key with a value that indicates whether the receipt is in a revoked state. _(deprecated)_
