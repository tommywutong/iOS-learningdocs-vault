---
title: CLLocationPushServiceError.Code.missingPushServerEnvironment
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationpushserviceerror-swift.struct/code/missingpushserverenvironment
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code/missingpushserverenvironment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationpushserviceerror-swift.struct/code/missingpushserverenvironment.json'
content_hash: 'sha256:c15b890b800036a6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLLocationPushServiceError](../../cllocationpushserviceerror-swift.struct.md) · [Code](../code.md)

# CLLocationPushServiceError.Code.missingPushServerEnvironment

<sub>Case</sub>

An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case missingPushServerEnvironment
```

## Discussion

A Location Push Service Extension requires that your app has the APNs environment entitlement. For more information, see [APS Environment Entitlement](../../../bundleresources/entitlements/aps-environment.md).

## See Also

### Getting the error code

- [CLLocationPushServiceErrorUnknown](unknown.md) — An error code that indicates the app was unable to start the location push service for an unknown reason.
- [CLLocationPushServiceErrorMissingPushExtension](missingpushextension.md) — An error code that indicates the app is missing a Location Push Service Extension.
- [CLLocationPushServiceErrorMissingEntitlement](missingentitlement.md) — An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [CLLocationPushServiceErrorUnsupportedPlatform](unsupportedplatform.md) — An error code that indicates the location push service isn’t available on this platform.
