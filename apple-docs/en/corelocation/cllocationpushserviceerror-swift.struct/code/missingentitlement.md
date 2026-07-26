---
title: CLLocationPushServiceError.Code.missingEntitlement
framework: Core Location
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationpushserviceerror-swift.struct/code/missingentitlement
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code/missingentitlement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationpushserviceerror-swift.struct/code/missingentitlement.json'
content_hash: 'sha256:d89e331d95b1cb6c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLLocationPushServiceError](../../cllocationpushserviceerror-swift.struct.md) · [Code](../code.md)

# CLLocationPushServiceError.Code.missingEntitlement

<sub>Case</sub>

An error code that indicates the app is missing the entitlement it needs to use the location push service.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case missingEntitlement
```

## Discussion

For more information, see [Creating a location push service extension](../../creating-a-location-push-service-extension.md).

## See Also

### Getting the error code

- [CLLocationPushServiceErrorUnknown](unknown.md) — An error code that indicates the app was unable to start the location push service for an unknown reason.
- [CLLocationPushServiceErrorMissingPushExtension](missingpushextension.md) — An error code that indicates the app is missing a Location Push Service Extension.
- [CLLocationPushServiceErrorMissingPushServerEnvironment](missingpushserverenvironment.md) — An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [CLLocationPushServiceErrorUnsupportedPlatform](unsupportedplatform.md) — An error code that indicates the location push service isn’t available on this platform.
