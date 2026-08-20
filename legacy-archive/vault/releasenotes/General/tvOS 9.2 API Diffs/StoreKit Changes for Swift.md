---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/StoreKit.html
archived_at: '2026-07-18T02:58:06.601492Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# StoreKit Changes for Swift

### StoreKit

Removed [SKErrorClientInvalid](https://developer.apple.com/documentation/storekit/skerror/code/clientinvalid)Removed [SKErrorPaymentCancelled](https://developer.apple.com/documentation/storekit/skerror/code/paymentcancelled)Removed [SKErrorPaymentInvalid](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorpaymentinvalid)Removed [SKErrorPaymentNotAllowed](https://developer.apple.com/documentation/storekit/skerror/code/paymentnotallowed)Removed SKErrorStoreProductNotAvailableRemoved [SKErrorUnknown](https://developer.apple.com/documentation/storekit/skerror/code/unknown)Added [SKCloudServiceAuthorizationStatus [enum]](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus)Added [SKCloudServiceAuthorizationStatus.Authorized](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/authorized)Added [SKCloudServiceAuthorizationStatus.Denied](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/skcloudserviceauthorizationstatusdenied)Added [SKCloudServiceAuthorizationStatus.NotDetermined](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/notdetermined)Added [SKCloudServiceAuthorizationStatus.Restricted](https://developer.apple.com/documentation/storekit/skcloudserviceauthorizationstatus/restricted)Added [SKCloudServiceCapability [struct]](https://developer.apple.com/documentation/storekit/skcloudservicecapability)Added [SKCloudServiceCapability.AddToCloudMusicLibrary](https://developer.apple.com/documentation/storekit/skcloudservicecapability/1620629-addtocloudmusiclibrary)Added [SKCloudServiceCapability.init(rawValue: UInt)](https://developer.apple.com/documentation/storekit/skcloudservicecapability/1620621-init)Added [SKCloudServiceCapability.MusicCatalogPlayback](https://developer.apple.com/documentation/storekit/skcloudservicecapability/skcloudservicecapabilitymusiccatalogplayback)Added [SKCloudServiceCapability.None](https://developer.apple.com/documentation/storekit/skcloudservicecapability/skcloudservicecapabilitynone)Added [SKCloudServiceController](https://developer.apple.com/documentation/storekit/skcloudservicecontroller)Added [SKCloudServiceController.authorizationStatus() -> SKCloudServiceAuthorizationStatus [class]](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620631-authorizationstatus)Added [SKCloudServiceController.requestAuthorization(_: (SKCloudServiceAuthorizationStatus) -> Void) [class]](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620609-requestauthorization)Added [SKCloudServiceController.requestCapabilitiesWithCompletionHandler(_: (SKCloudServiceCapability, NSError?) -> Void)](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620610-requestcapabilities)Added [SKCloudServiceController.requestStorefrontIdentifierWithCompletionHandler(_: (String?, NSError?) -> Void)](https://developer.apple.com/documentation/storekit/skcloudservicecontroller/1620618-requeststorefrontidentifier)Added [SKErrorCode [enum]](https://developer.apple.com/documentation/storekit/skerrorcode)Added [SKErrorCode.ClientInvalid](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorclientinvalid)Added [SKErrorCode.CloudServiceNetworkConnectionFailed](https://developer.apple.com/documentation/storekit/skerror/code/cloudservicenetworkconnectionfailed)Added [SKErrorCode.CloudServicePermissionDenied](https://developer.apple.com/documentation/storekit/skerror/code/cloudservicepermissiondenied)Added [SKErrorCode.PaymentCancelled](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorpaymentcancelled)Added [SKErrorCode.PaymentInvalid](https://developer.apple.com/documentation/storekit/skerror/code/paymentinvalid)Added [SKErrorCode.PaymentNotAllowed](https://developer.apple.com/documentation/storekit/skerror/code/paymentnotallowed)Added [SKErrorCode.StoreProductNotAvailable](https://developer.apple.com/documentation/storekit/skerror/code/storeproductnotavailable)Added [SKErrorCode.Unknown](https://developer.apple.com/documentation/storekit/skerrorcode/skerrorunknown)Added [SKCloudServiceCapabilitiesDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1620626-skcloudservicecapabilitiesdidcha)Added [SKStorefrontIdentifierDidChangeNotification](https://developer.apple.com/documentation/storekit/skstorefrontidentifierdidchangenotification)Added [SKStoreProductParameterAdvertisingPartnerToken](https://developer.apple.com/documentation/storekit/skstoreproductparameteradvertisingpartnertoken)

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
