---
title: Determining a person’s Apple Music capabilities
framework: StoreKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/determining-a-person-s-apple-music-capabilities
source_url: 'https://developer.apple.com/documentation/storekit/determining-a-person-s-apple-music-capabilities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/determining-a-person-s-apple-music-capabilities.json'
content_hash: 'sha256:57d2a6486e8510fb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [SKCloudServiceController](skcloudservicecontroller.md)

# Determining a person’s Apple Music capabilities

<sub>Article</sub>

Determine which Apple Music capabilities are available on a customer’s device.

## Overview

After you request the user’s permission to access their Apple Music library (see [Requesting Access to Apple Music Library](requesting-access-to-apple-music-library.md)), you confirm that authorization and then identify Apple Music capabilities on the user’s device.

### Confirm Whether the User Authorized Access to Apple Music Library

Use [SKCloudServiceController](skcloudservicecontroller.md)’s [+ authorizationStatus](<skcloudservicecontroller/authorizationstatus().md>) to check whether the user has authorized access to Apple Music Library. If the authorization status is [SKCloudServiceAuthorizationStatusNotDetermined](skcloudserviceauthorizationstatus/notdetermined.md), call [SKCloudServiceController](skcloudservicecontroller.md)’s [+ requestAuthorization:](<skcloudservicecontroller/requestauthorization(__).md>) to prompt the user for access.

**Swift**

```swift
guard SKCloudServiceController.authorizationStatus() == .notDetermined else { return }
```

**Objective-C**

```objc
 SKCloudServiceAuthorizationStatus status = ([SKCloudServiceController authorizationStatus] == SKCloudServiceAuthorizationStatusNotDetermined);
```

If the authorization status is [SKCloudServiceAuthorizationStatusAuthorized](skcloudserviceauthorizationstatus/authorized.md), your app can proceed to determine which Apple Music capabilities ([SKCloudServiceCapabilityMusicCatalogPlayback](skcloudservicecapability/musiccatalogplayback.md), [SKCloudServiceCapabilityMusicCatalogSubscriptionEligible](skcloudservicecapability/musiccatalogsubscriptioneligible.md), or [SKCloudServiceCapabilityAddToCloudMusicLibrary](skcloudservicecapability/addtocloudmusiclibrary.md)) are available on the user’s device.

**Swift**

```swift
guard SKCloudServiceController.authorizationStatus() == .authorized else { return }
fetchCurrentAppleMusicCapabilities()
```

**Objective-C**

```objc
if ([SKCloudServiceController authorizationStatus] == SKCloudServiceAuthorizationStatusAuthorized) {
   [self fetchCurrentAppleMusicCapabilities];
}
```

### Create a Cloud Service Controller and Its Handler to Fetch Capabilities

First, create an [SKCloudServiceController](skcloudservicecontroller.md) object:

**Swift**

```swift
let controller = SKCloudServiceController()
```

**Objective-C**

```objc
SKCloudServiceController *controller = [[SKCloudServiceController alloc] init];
```

Then call its [- requestCapabilitiesWithCompletionHandler:](<skcloudservicecontroller/requestcapabilities(completionhandler_).md>) method to fetch the current Apple Music capabilities, as described in the sections that follow.

### Check for the Capability to Play Apple Music Content

If you want your app to play Apple Music content, check whether `capabilities` includes [SKCloudServiceCapabilityMusicCatalogPlayback](skcloudservicecapability/musiccatalogplayback.md):

**Swift**

```swift
controller.requestCapabilities {(capabilities: SKCloudServiceCapability, error: Error?) in
   guard error == nil else { return }
   if capabilities.contains(.musicCatalogPlayback) {
      // Allows playback of songs in the Apple Music catalog.
   }
}
```

**Objective-C**

```objc
[controller requestCapabilitiesWithCompletionHandler:^(SKCloudServiceCapability capabilities, NSError *error){
    if (error != nil) {
        // Handle error.
    } else if (capabilities & SKCloudServiceCapabilityMusicCatalogPlayback) {
         // Allows playback of songs in the Apple Music catalog.
    }
}];

```

### Check for the Subscription-Eligible Capability

A user is eligible for an Apple Music subscription offer when `capabilities` doesn’t include [SKCloudServiceCapabilityMusicCatalogPlayback](skcloudservicecapability/musiccatalogplayback.md) but contains [SKCloudServiceCapabilityMusicCatalogSubscriptionEligible](skcloudservicecapability/musiccatalogsubscriptioneligible.md). If you want your app to present the user with an offer to subscribe to Apple Music, check `capabilities` for these features:

**Swift**

```swift
controller.requestCapabilities {(capabilities: SKCloudServiceCapability, error: Error?) in
   guard error == nil else { return } 
   if capabilities.contains(.musicCatalogSubscriptionEligible) && !capabilities.contains(.musicCatalogPlayback) {
      // Allows subscription to the Apple Music catalog.
   }
}
```

**Objective-C**

```objc
[controller requestCapabilitiesWithCompletionHandler:^(SKCloudServiceCapability capabilities, NSError *error){
    if (error != nil) {
        // Handle error.
    } else if ((capabilities & SKCloudServiceCapabilityMusicCatalogSubscriptionEligible) && (!(capabilities & SKCloudServiceCapabilityMusicCatalogPlayback))) {
         // Allows subscription to the Apple Music catalog.
    }
}];
```

You can present the offer using [SKCloudServiceSetupViewController](skcloudservicesetupviewcontroller.md).

### Check for the Capability to Add Songs to the User’s iCloud Music Library

If you want your app to add tracks to the user’s iCloud music library, check whether `capabilities` includes [SKCloudServiceCapabilityAddToCloudMusicLibrary](skcloudservicecapability/addtocloudmusiclibrary.md):

**Swift**

```swift
controller.requestCapabilities {(capabilities: SKCloudServiceCapability, error: Error?) in
   guard error == nil else { return }
   if capabilities.contains(.addToCloudMusicLibrary) {
       // Allows songs to be added to the user’s iCloud music library.
    }
}
```

**Objective-C**

```objc
[controller requestCapabilitiesWithCompletionHandler:^(SKCloudServiceCapability capabilities, NSError *error){
    if (error != nil) {
        // Handle error.
    } else if (capabilities & SKCloudServiceCapabilityAddToCloudMusicLibrary) {
         // Allows songs to be added to the user’s iCloud music library.
    }
}];
```

## See Also

### Determining capabilities

- [- requestUserTokenForDeveloperToken:completionHandler:](<skcloudservicecontroller/requestusertoken(fordevelopertoken_completionhandler_).md>) — Returns a user token that you use to access personalized Apple Music content. _(deprecated)_
- [- requestStorefrontCountryCodeWithCompletionHandler:](<skcloudservicecontroller/requeststorefrontcountrycode(completionhandler_).md>) — Gets the country code for the storefront associated with a customer’s iTunes account. _(deprecated)_
- [- requestCapabilitiesWithCompletionHandler:](<skcloudservicecontroller/requestcapabilities(completionhandler_).md>) — Gets the current capabilities associated with the Music library on the device. _(deprecated)_
- [SKCloudServiceCapability](skcloudservicecapability.md) — Constants that specify the current capabilities of the customer’s Music library on the device. _(deprecated)_
- [- requestStorefrontIdentifierWithCompletionHandler:](<skcloudservicecontroller/requeststorefrontidentifier(completionhandler_).md>) — Gets the device’s storefront identifier. _(deprecated)_
- [- requestPersonalizationTokenForClientToken:withCompletionHandler:](<skcloudservicecontroller/requestpersonalizationtoken(forclienttoken_withcompletionhandler_).md>) _(deprecated)_
