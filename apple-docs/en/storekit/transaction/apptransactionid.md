---
title: appTransactionID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/apptransactionid
source_url: 'https://developer.apple.com/documentation/storekit/transaction/apptransactionid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/apptransactionid.json'
content_hash: 'sha256:1a7ac1af5be41224'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# appTransactionID

<sub>Instance Property</sub>

The unique identifier of the app download transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var appTransactionID: String { get }
```

## Discussion

The App Store server APIs and StoreKit provide this value in several APIs. For more information, see [appTransactionID](../apptransaction/apptransactionid.md) in [AppTransaction](../apptransaction.md).

## See Also

### Transaction properties

- [Transaction properties](../transaction-properties.md) — The properties of a transaction, including identifiers, purchase and revocation dates and details, status, and offer details.
