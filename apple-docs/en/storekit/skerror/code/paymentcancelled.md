---
title: SKError.Code.paymentCancelled
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.7+, visionOS 1.0+, watchOS 6.2+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skerror/code/paymentcancelled
source_url: 'https://developer.apple.com/documentation/storekit/skerror/code/paymentcancelled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skerror/code/paymentcancelled.json'
content_hash: 'sha256:65822b729881bffc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKError](../../skerror.md) · [Code](../code.md)

# SKError.Code.paymentCancelled

<sub>Case</sub>

Error code indicating that the user canceled a payment request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case paymentCancelled
```

## See Also

### Enumeration Cases

- [SKErrorUnknown](unknown.md) — Error code indicating that an unknown or unexpected error occurred.
- [SKErrorClientInvalid](clientinvalid.md) — Error code indicating that the client is not allowed to perform the attempted action.
- [SKErrorPaymentInvalid](paymentinvalid.md) — Error code indicating that one of the payment parameters wasn’t recognized by the App Store.
- [SKErrorPaymentNotAllowed](paymentnotallowed.md) — Error code indicating that the user is not allowed to authorize payments.
- [SKErrorStoreProductNotAvailable](storeproductnotavailable.md) — Error code indicating that the requested product is not available in the store.
- [SKErrorCloudServicePermissionDenied](cloudservicepermissiondenied.md) — Error code indicating that the user has not allowed access to Cloud service information.
- [SKErrorCloudServiceNetworkConnectionFailed](cloudservicenetworkconnectionfailed.md) — Error code indicating that the device could not connect to the network.
- [SKErrorCloudServiceRevoked](cloudservicerevoked.md) — Error code indicating that the user has revoked permission to use this cloud service.
- [SKErrorPrivacyAcknowledgementRequired](privacyacknowledgementrequired.md) — Error code indicating that the user has not yet acknowledged Apple’s privacy policy for Apple Music.
- [SKErrorUnauthorizedRequestData](unauthorizedrequestdata.md) — Error code indicating that the app is attempting to use a property for which it does not have the required entitlement.
- [SKErrorInvalidOfferIdentifier](invalidofferidentifier.md) — Error code indicating that the offer identifier is invalid.
- [SKErrorInvalidOfferPrice](invalidofferprice.md) — Error code indicating that the price you specified in App Store Connect is no longer valid.
- [SKErrorInvalidSignature](invalidsignature.md) — Error code indicating that the signature in a payment discount isn’t valid.
- [SKErrorMissingOfferParams](missingofferparams.md) — Error code indicating that parameters are missing in a payment discount.
- [SKErrorIneligibleForOffer](ineligibleforoffer.md) — An error code that indicates the user is ineligible for the subscription offer.
