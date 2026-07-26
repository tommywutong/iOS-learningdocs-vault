---
title: originalPlatformStringRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+（18.4 起废弃）, iPadOS 16.0+（18.4 起废弃）, macOS 13.0+（15.4 起废弃）, tvOS 16.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 9.0+（11.4 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/apptransaction/originalplatformstringrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/originalplatformstringrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/originalplatformstringrepresentation.json'
content_hash: 'sha256:5430f1b9fe5f72e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# originalPlatformStringRepresentation

<sub>Instance Property</sub>

The string representation of the platform on which the customer originally purchased the app.

> [!warning] Deprecated
> Use the originalPlatform property instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var originalPlatformStringRepresentation: String { get }
```
