---
title: CLLocationPushServiceError.Code
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationpushserviceerror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationpushserviceerror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationpushserviceerror-swift.struct/code.json'
content_hash: 'sha256:f353ae191e631865'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationPushServiceError](../cllocationpushserviceerror-swift.struct.md)

# CLLocationPushServiceError.Code

<sub>Enumeration</sub>

Error codes the location manager returns if starting to monitor for location push notifications fails.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum Code
```

## Overview

These error codes are returned from [- startMonitoringLocationPushesWithCompletion:](<../cllocationmanager/startmonitoringlocationpushes(completion_).md>)

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the error code

- [CLLocationPushServiceErrorUnknown](code/unknown.md) — An error code that indicates the app was unable to start the location push service for an unknown reason.
- [CLLocationPushServiceErrorMissingPushExtension](code/missingpushextension.md) — An error code that indicates the app is missing a Location Push Service Extension.
- [CLLocationPushServiceErrorMissingPushServerEnvironment](code/missingpushserverenvironment.md) — An error code that indicates the app is missing an Apple Push Notification service (APNs) environment entitlement.
- [CLLocationPushServiceErrorMissingEntitlement](code/missingentitlement.md) — An error code that indicates the app is missing the entitlement it needs to use the location push service.
- [CLLocationPushServiceErrorUnsupportedPlatform](code/unsupportedplatform.md) — An error code that indicates the location push service isn’t available on this platform.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Location push service extension

- [Location Push Service Extension](../../bundleresources/entitlements/com.apple.developer.location.push.md) — An entitlement to enable a location-sharing app to query someone’s location in response to a push notification.
- [CLLocationPushServiceExtension](../cllocationpushserviceextension.md) — The interface you adopt in the type that acts as the main entry point for a Location Push Service Extension.
- [CLLocationPushServiceError](../cllocationpushserviceerror-swift.struct.md) — Error codes the location manager returns if starting to monitor for location push notifications fails.
- [CLLocationPushServiceErrorDomain](../cllocationpushserviceerrordomain.md) — The domain for Location Push Service Extension errors.
