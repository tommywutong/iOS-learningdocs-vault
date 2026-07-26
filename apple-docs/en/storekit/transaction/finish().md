---
title: finish()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/finish()
source_url: 'https://developer.apple.com/documentation/storekit/transaction/finish()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/finish%28%29.json'
content_hash: 'sha256:e1e68d61f29a69ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# finish()

<sub>Instance Method</sub>

Indicates to the App Store that the app delivered the purchased content or enabled the service to finish the transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finish() async
```

## Discussion

Call [finish()](<finish().md>) to complete a transaction after you deliver the purchased content or enable the purchased service. For on-demand resources, don’t finish the transaction until the app completes downloading the resource or you’ve otherwise delivered the resource.

## See Also

### Finishing the transaction

- [unfinished](unfinished.md) — A sequence that emits unfinished transactions for the customer.
