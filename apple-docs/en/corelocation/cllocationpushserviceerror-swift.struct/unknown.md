---
title: unknown
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationpushserviceerror-swift.struct/unknown
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/unknown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationpushserviceerror-swift.struct/unknown.json'
content_hash: 'sha256:885f08b81c1e145e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationPushServiceError](../cllocationpushserviceerror-swift.struct.md)

# unknown

<sub>Type Property</sub>

An error code that indicates the app was unable to start the location push service for an unknown reason.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var unknown: CLLocationPushServiceError.Code { get }
```

## See Also

### Getting the error code

- [missingPushExtension](missingpushextension.md) — An error code that indicates the app is missing a Location Push Service Extension.
- [missingPushServerEnvironment](missingpushserverenvironment.md) — An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [missingEntitlement](missingentitlement.md) — An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [unsupportedPlatform](unsupportedplatform.md) — An error code that indicates the location push service isn’t available on this platform.
- [Code](code.md) — Error codes the location manager returns if starting to monitor for location push notifications fails.
