---
title: CLLocationPushServiceError
framework: Core Location
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationpushserviceerror-swift.struct
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationpushserviceerror-swift.struct.json'
content_hash: 'sha256:20d610de28b7d191'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationPushServiceError

<sub>Structure</sub>

Error codes the location manager returns if starting to monitor for location push notifications fails.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct CLLocationPushServiceError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the error code

- [unknown](cllocationpushserviceerror-swift.struct/unknown.md) — An error code that indicates the app was unable to start the location push service for an unknown reason.
- [missingPushExtension](cllocationpushserviceerror-swift.struct/missingpushextension.md) — An error code that indicates the app is missing a Location Push Service Extension.
- [missingPushServerEnvironment](cllocationpushserviceerror-swift.struct/missingpushserverenvironment.md) — An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [missingEntitlement](cllocationpushserviceerror-swift.struct/missingentitlement.md) — An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [unsupportedPlatform](cllocationpushserviceerror-swift.struct/unsupportedplatform.md) — An error code that indicates the location push service isn’t available on this platform.
- [Code](cllocationpushserviceerror-swift.struct/code.md) — Error codes the location manager returns if starting to monitor for location push notifications fails.

### Type Properties

- [errorDomain](cllocationpushserviceerror-swift.struct/errordomain.md)

## See Also

### Location push service extension

- [Location Push Service Extension](../bundleresources/entitlements/com.apple.developer.location.push.md) — An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
- [CLLocationPushServiceExtension](cllocationpushserviceextension.md) — The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.
- [CLLocationPushServiceErrorDomain](cllocationpushserviceerrordomain.md) — The domain for Location Push Service Extension errors.
- [Code](cllocationpushserviceerror-swift.struct/code.md) — Error codes the location manager returns if starting to monitor for location push notifications fails.
