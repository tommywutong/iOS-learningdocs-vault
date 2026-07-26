---
title: Transaction.RefundRequestError.duplicateRequest
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/refundrequesterror/duplicaterequest
source_url: 'https://developer.apple.com/documentation/storekit/transaction/refundrequesterror/duplicaterequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/refundrequesterror/duplicaterequest.json'
content_hash: 'sha256:dca4dfb4a189c751'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [RefundRequestError](../refundrequesterror.md)

# Transaction.RefundRequestError.duplicateRequest

<sub>Case</sub>

The App Store has already received a refund request for this in-app purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case duplicateRequest
```

## Discussion

StoreKit returns this error if the App Store has previously received a refund request for this transaction and the refund decision is still pending, has been previously denied, or has been previously approved.

Consider checking the transaction’s [revocationDate](../revocationdate.md) or [revocationReason](../revocationreason-swift.property.md) before calling [beginRefundRequest(for:in:)](<../beginrefundrequest(for_in_)-65tph.md>) to identify whether the App Store has already refunded the transaction.

## See Also

### Error Enumeration

- [Transaction.RefundRequestError.failed](failed.md) — The refund request submission failed.
