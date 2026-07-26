---
title: SKError.Code.invalidSignature
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 12.2+, iPadOS 12.2+, Mac Catalyst 13.1+, macOS 10.14.4+, tvOS 12.2+, visionOS 1.0+, watchOS 6.2+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skerror/code/invalidsignature
source_url: 'https://developer.apple.com/documentation/storekit/skerror/code/invalidsignature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skerror/code/invalidsignature.json'
content_hash: 'sha256:e3cd064bc648ab65'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKError](../../skerror.md) · [Code](../code.md)

# SKError.Code.invalidSignature

<sub>Case</sub>

Error code indicating that the signature in a payment discount isn’t valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case invalidSignature
```

## Discussion

The [signature](../../skpaymentdiscount/signature.md) is not valid.

## See Also

### Enumeration Cases

- [SKErrorUnknown](unknown.md) — Error code indicating that an unknown or unexpected error occurred.
- [SKErrorClientInvalid](clientinvalid.md) — Error code indicating that the client is not allowed to perform the attempted action.
- [SKErrorPaymentCancelled](paymentcancelled.md) — Error code indicating that the user canceled a payment request.
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
- [SKErrorMissingOfferParams](missingofferparams.md) — Error code indicating that parameters are missing in a payment discount.
- [SKErrorIneligibleForOffer](ineligibleforoffer.md) — An error code that indicates the user is ineligible for the subscription offer.
