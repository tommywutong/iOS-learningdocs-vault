---
title: Transaction.Transactions
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/transactions
source_url: 'https://developer.apple.com/documentation/storekit/transaction/transactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/transactions.json'
content_hash: 'sha256:f9c57760cef4eef9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# Transaction.Transactions

<sub>Structure</sub>

An asynchronous sequence of transactions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Transactions
```

## Overview

You don’t create a [Transactions](transactions.md) sequence directly. Use methods such as [all](all.md), [updates](updates.md), or [currentEntitlements](currententitlements.md) to get transactions.

## Relationships

- **Conforms To**: [AsyncSequence](../../swift/asyncsequence.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## See Also

### Monitoring transaction-related changes

- [updates](updates.md) — The asynchronous sequence that emits a transaction when the system creates or updates transactions that occur outside the app or on other devices.
