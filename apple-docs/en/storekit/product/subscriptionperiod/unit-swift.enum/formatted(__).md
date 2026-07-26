---
title: 'formatted(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/subscriptionperiod/unit-swift.enum/formatted(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionperiod/unit-swift.enum/formatted(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionperiod/unit-swift.enum/formatted%28_%3A%29.json'
content_hash: 'sha256:a5def4b2c3793bbe'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionPeriod](../../subscriptionperiod.md) · [Unit](../unit-swift.enum.md)

# formatted(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formatted<S>(_ format: S) -> S.FormatOutput where S : FormatStyle, S.FormatInput == Product.SubscriptionPeriod.Unit
```

## See Also

### Getting the formatted description

- [FormatStyle](formatstyle.md)
