---
title: Transaction.RefundRequestStatus
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/refundrequeststatus
source_url: 'https://developer.apple.com/documentation/storekit/transaction/refundrequeststatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/refundrequeststatus.json'
content_hash: 'sha256:025bb4086bc0b666'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# Transaction.RefundRequestStatus

<sub>Enumeration</sub>

The status codes for refund requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum RefundRequestStatus
```

## Overview

The following methods throw the refund request status: [beginRefundRequest(in:)](<beginrefundrequest(in_)-9k0pj.md>),  [beginRefundRequest(for:in:)](<beginrefundrequest(for_in_)-65tph.md>), [beginRefundRequest(in:)](<beginrefundrequest(in_)-63bvd.md>), and [beginRefundRequest(for:in:)](<beginrefundrequest(for_in_)-9mscy.md>).

The refund request status reflects the status of the request, not the status of the refund itself.

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting Refund Request Status

- [Transaction.RefundRequestStatus.userCancelled](refundrequeststatus/usercancelled.md) — The user canceled submission of their refund request.
- [Transaction.RefundRequestStatus.success](refundrequeststatus/success.md) — The App Store has received the refund request.

## See Also

### Requesting refunds

- [Testing refund requests](../testing-refund-requests.md) — Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [beginRefundRequest(in:)](<beginrefundrequest(in_)-9k0pj.md>) — Presents the refund request sheet for the transaction in a window scene.
- [beginRefundRequest(in:)](<beginrefundrequest(in_)-63bvd.md>) — Presents the refund request sheet for the transaction in a view controller.
- [beginRefundRequest(for:in:)](<beginrefundrequest(for_in_)-65tph.md>) — Presents the refund request sheet for the specified transaction in a window scene.
- [beginRefundRequest(for:in:)](<beginrefundrequest(for_in_)-9mscy.md>) — Presents the refund request sheet for the specified transaction in a view controller.
- [RefundRequestError](refundrequesterror.md) — The error codes for refund requests.
