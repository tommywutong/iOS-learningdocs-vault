---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Objective-C/StoreKit.html
archived_at: '2026-07-18T02:57:14.224328Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# StoreKit Changes for Objective-C

### StoreKit

#### SKCloudServiceController.h (Added)

Added [SKCloudServiceController](https://developer.apple.com/documentation/storekit/skcloudservicecontroller)Added [+[SKCloudServiceController authorizationStatus]](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620631-authorizationstatus)Added [+[SKCloudServiceController requestAuthorization:]](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620609-requestauthorization)Added [-[SKCloudServiceController requestCapabilitiesWithCompletionHandler:]](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620610-requestcapabilitieswithcompletio)Added [-[SKCloudServiceController requestStorefrontIdentifierWithCompletionHandler:]](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620618-requeststorefrontidentifierwithc)Added [SKCloudServiceAuthorizationStatus](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus)Added [SKCloudServiceAuthorizationStatusAuthorized](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/skcloudserviceauthorizationstatusauthorized)Added [SKCloudServiceAuthorizationStatusDenied](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/skcloudserviceauthorizationstatusdenied)Added [SKCloudServiceAuthorizationStatusNotDetermined](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/notdetermined)Added [SKCloudServiceAuthorizationStatusRestricted](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/restricted)Added [SKCloudServiceCapabilitiesDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620626-skcloudservicecapabilitiesdidcha)Added [SKCloudServiceCapability](https://developer.apple.com/documentation/storekit/skcloudservicecapability)Added [SKCloudServiceCapabilityAddToCloudMusicLibrary](https://developer.apple.com/documentation/storekit/skcloudservicecapability/1620629-addtocloudmusiclibrary)Added [SKCloudServiceCapabilityMusicCatalogPlayback](https://developer.apple.com/documentation/storekit/skcloudservicecapability/skcloudservicecapabilitymusiccatalogplayback)Added [SKCloudServiceCapabilityNone](https://developer.apple.com/documentation/storekit/skcloudservicecapability/skcloudservicecapabilitynone)Added [SKStorefrontIdentifierDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620636-skstorefrontidentifierdidchange)

#### SKError.h

Added [SKErrorCloudServiceNetworkConnectionFailed](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorcloudservicenetworkconnectionfailed)Added [SKErrorCloudServicePermissionDenied](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorcloudservicepermissiondenied)Added [SKErrorCode](https://developer.apple.com/documentation/storekit/skerror/code)

#### SKStoreProductViewController.h

Added [SKStoreProductParameterAdvertisingPartnerToken](https://developer.apple.com/documentation/storekit/skstoreproductparameteradvertisingpartnertoken)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
