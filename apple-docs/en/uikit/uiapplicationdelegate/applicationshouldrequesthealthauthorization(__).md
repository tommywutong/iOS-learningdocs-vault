---
title: 'applicationShouldRequestHealthAuthorization(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationdelegate/applicationshouldrequesthealthauthorization(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/applicationshouldrequesthealthauthorization(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/applicationshouldrequesthealthauthorization%28_%3A%29.json'
content_hash: 'sha256:307e50a76f74f6de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# applicationShouldRequestHealthAuthorization(_:)

<sub>Instance Method</sub>

Tells the delegate when your app should ask the user for access to his or her HealthKit data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func applicationShouldRequestHealthAuthorization(_ application: UIApplication)
```

## Parameters

- `application` — Your singleton app object.

## Discussion

In your implementation of this method, call the [handleAuthorizationForExtension(completion:)](<../../healthkit/hkhealthstore/handleauthorizationforextension(completion_).md>) method of the [HKHealthStore](../../healthkit/hkhealthstore.md) object.
