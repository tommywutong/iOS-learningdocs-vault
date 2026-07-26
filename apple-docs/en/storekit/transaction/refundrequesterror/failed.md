---
title: Transaction.RefundRequestError.failed
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/refundrequesterror/failed
source_url: 'https://developer.apple.com/documentation/storekit/transaction/refundrequesterror/failed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/refundrequesterror/failed.json'
content_hash: 'sha256:411edfd641fdd674'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [RefundRequestError](../refundrequesterror.md)

# Transaction.RefundRequestError.failed

<sub>Case</sub>

The refund request submission failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failed
```

## Discussion

A refund request submission can fail for many reasons, such as having an invalid transaction identifier, or if the App Store can’t process the request for some other reason.

## See Also

### Error Enumeration

- [Transaction.RefundRequestError.duplicateRequest](duplicaterequest.md) — The App Store has already received a refund request for this in-app purchase.
