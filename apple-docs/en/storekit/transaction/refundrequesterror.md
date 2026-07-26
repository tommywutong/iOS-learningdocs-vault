---
title: Transaction.RefundRequestError
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/refundrequesterror
source_url: 'https://developer.apple.com/documentation/storekit/transaction/refundrequesterror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/refundrequesterror.json'
content_hash: 'sha256:c244c71a4e2650ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# Transaction.RefundRequestError

<sub>Enumeration</sub>

The error codes for refund requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum RefundRequestError
```

## Overview

The following methods throw refund request errors: [beginRefundRequest(in:)](<beginrefundrequest(in_)-9k0pj.md>), [beginRefundRequest(for:in:)](<beginrefundrequest(for_in_)-65tph.md>), [beginRefundRequest(in:)](<beginrefundrequest(in_)-63bvd.md>), and [beginRefundRequest(for:in:)](<beginrefundrequest(for_in_)-9mscy.md>).

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [LocalizedError](../../foundation/localizederror.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error Enumeration

- [Transaction.RefundRequestError.duplicateRequest](refundrequesterror/duplicaterequest.md) — The App Store has already received a refund request for this in-app purchase.
- [Transaction.RefundRequestError.failed](refundrequesterror/failed.md) — The refund request submission failed.

### Enumeration Cases

- [Transaction.RefundRequestError.ineligible](refundrequesterror/ineligible.md) _(beta)_

## See Also

### Requesting refunds

- [Testing refund requests](../testing-refund-requests.md) — Test your app’s implementation of refund requests, and your app’s and server’s handling of approved and declined refunds.
- [beginRefundRequest(in:)](<beginrefundrequest(in_)-9k0pj.md>) — Presents the refund request sheet for the transaction in a window scene.
- [beginRefundRequest(in:)](<beginrefundrequest(in_)-63bvd.md>) — Presents the refund request sheet for the transaction in a view controller.
- [beginRefundRequest(for:in:)](<beginrefundrequest(for_in_)-65tph.md>) — Presents the refund request sheet for the specified transaction in a window scene.
- [beginRefundRequest(for:in:)](<beginrefundrequest(for_in_)-9mscy.md>) — Presents the refund request sheet for the specified transaction in a view controller.
- [RefundRequestStatus](refundrequeststatus.md) — The status codes for refund requests.
