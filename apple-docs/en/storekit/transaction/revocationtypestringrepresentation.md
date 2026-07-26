---
title: revocationTypeStringRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+（26.4 起废弃）, iPadOS 15.0+（26.4 起废弃）, macOS 12.0+（26.4 起废弃）, tvOS 15.0+（26.4 起废弃）, visionOS 1.0+（26.4 起废弃）, watchOS 8.0+（26.4 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/transaction/revocationtypestringrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/transaction/revocationtypestringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/revocationtypestringrepresentation.json'
content_hash: 'sha256:029a1d337ac560be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# revocationTypeStringRepresentation

<sub>Instance Property</sub>

The string representation of the [revocationType](revocationtype-swift.property.md), or `nil` if the transaction was not revoked.

> [!warning] Deprecated
> Use the [revocationType](revocationtype-swift.property.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 26.4, macOS 26.4, tvOS 26.4, watchOS 26.4, visionOS 26.4)
var revocationTypeStringRepresentation: String? { get }
```
