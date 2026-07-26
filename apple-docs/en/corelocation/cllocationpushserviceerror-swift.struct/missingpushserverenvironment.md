---
title: missingPushServerEnvironment
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationpushserviceerror-swift.struct/missingpushserverenvironment
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/missingpushserverenvironment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationpushserviceerror-swift.struct/missingpushserverenvironment.json'
content_hash: 'sha256:c18de78ceb5973b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationPushServiceError](../cllocationpushserviceerror-swift.struct.md)

# missingPushServerEnvironment

<sub>Type Property</sub>

An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var missingPushServerEnvironment: CLLocationPushServiceError.Code { get }
```

## Discussion

A Location Push Service Extension requires that your app has the APNs environment entitlement. For more information, see [APS Environment Entitlement](../../bundleresources/entitlements/aps-environment.md).

## See Also

### Getting the error code

- [unknown](unknown.md) — An error code that indicates the app was unable to start the location push service for an unknown reason.
- [missingPushExtension](missingpushextension.md) — An error code that indicates the app is missing a Location Push Service Extension.
- [missingEntitlement](missingentitlement.md) — An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [unsupportedPlatform](unsupportedplatform.md) — An error code that indicates the location push service isn’t available on this platform.
- [Code](code.md) — Error codes the location manager returns if starting to monitor for location push notifications fails.
