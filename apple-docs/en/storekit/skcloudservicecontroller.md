---
title: SKCloudServiceController
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.3+（18.0 起废弃）, iPadOS 9.3+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 9.3+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicecontroller
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecontroller.json'
content_hash: 'sha256:38c52fc4b148add0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKCloudServiceController

<sub>Class</sub>

An object that determines the current capabilities of a person’s Music library.

> [!warning] Deprecated
> Use [SwiftUI](../swiftui.md) and  [MusicKit](../musickit.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
class SKCloudServiceController
```

## Overview

Use an [SKCloudServiceController](skcloudservicecontroller.md) object to determine the current capabilities of a customer’s Music library, like whether the device allows playback of Apple Music catalog tracks and the addition of tracks to the library.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting authorization to access the Music library

- [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md) — Prompt the customer to authorize access to Apple Music library.
- [+ authorizationStatus](<skcloudservicecontroller/authorizationstatus().md>) — Returns the type of authorization the customer has for accessing the Music library on the device. _(deprecated)_
- [+ requestAuthorization:](<skcloudservicecontroller/requestauthorization(__).md>) — Asks the customer for permission to access the Music library on the device. _(deprecated)_
- [SKCloudServiceAuthorizationStatus](skcloudserviceauthorizationstatus.md) — Constants that indicate the type of authorization the customer has for accessing the Music library. _(deprecated)_

### Determining capabilities

- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md) — Determine which Apple Music capabilities are available on a customer’s device.
- [- requestUserTokenForDeveloperToken:completionHandler:](<skcloudservicecontroller/requestusertoken(fordevelopertoken_completionhandler_).md>) — Returns a user token that you use to access personalized Apple Music content. _(deprecated)_
- [- requestStorefrontCountryCodeWithCompletionHandler:](<skcloudservicecontroller/requeststorefrontcountrycode(completionhandler_).md>) — Gets the country code for the storefront associated with a customer’s iTunes account. _(deprecated)_
- [- requestCapabilitiesWithCompletionHandler:](<skcloudservicecontroller/requestcapabilities(completionhandler_).md>) — Gets the current capabilities associated with the Music library on the device. _(deprecated)_
- [SKCloudServiceCapability](skcloudservicecapability.md) — Constants that specify the current capabilities of the customer’s Music library on the device. _(deprecated)_
- [- requestStorefrontIdentifierWithCompletionHandler:](<skcloudservicecontroller/requeststorefrontidentifier(completionhandler_).md>) — Gets the device’s storefront identifier. _(deprecated)_
- [- requestPersonalizationTokenForClientToken:withCompletionHandler:](<skcloudservicecontroller/requestpersonalizationtoken(forclienttoken_withcompletionhandler_).md>) _(deprecated)_

### Notifications

- [SKStorefrontIdentifierDidChange](../foundation/nsnotification/name-swift.struct/skstorefrontidentifierdidchange.md) — A notification name for indicating a change in the storefront identifier associated with the device. _(deprecated)_
- [SKCloudServiceCapabilitiesDidChange](../foundation/nsnotification/name-swift.struct/skcloudservicecapabilitiesdidchange.md) — A notification name for indicating a change in the capabilities associated with the Music library on the device. _(deprecated)_
- [SKStorefrontCountryCodeDidChange](../foundation/nsnotification/name-swift.struct/skstorefrontcountrycodedidchange.md) — A notification name for indicating a change in the storefront country or region code associated with the device. _(deprecated)_

## See Also

### Deprecated

- [SKCloudServiceSetupViewController](skcloudservicesetupviewcontroller.md) — A view controller that helps people perform setup for a cloud service, like an Apple Music subscription. _(deprecated)_
