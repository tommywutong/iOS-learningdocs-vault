---
title: SKError.Code
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.7+, visionOS 1.0+, watchOS 6.2+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skerror/code
source_url: 'https://developer.apple.com/documentation/storekit/skerror/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skerror/code.json'
content_hash: 'sha256:39b39a03e1875a67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKError](../skerror.md)

# SKError.Code

<sub>Enumeration</sub>

Error codes for StoreKit errors.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [SKErrorUnknown](code/unknown.md) — Error code indicating that an unknown or unexpected error occurred.
- [SKErrorClientInvalid](code/clientinvalid.md) — Error code indicating that the client is not allowed to perform the attempted action.
- [SKErrorPaymentCancelled](code/paymentcancelled.md) — Error code indicating that the user canceled a payment request.
- [SKErrorPaymentInvalid](code/paymentinvalid.md) — Error code indicating that one of the payment parameters wasn’t recognized by the App Store.
- [SKErrorPaymentNotAllowed](code/paymentnotallowed.md) — Error code indicating that the user is not allowed to authorize payments.
- [SKErrorStoreProductNotAvailable](code/storeproductnotavailable.md) — Error code indicating that the requested product is not available in the store.
- [SKErrorCloudServicePermissionDenied](code/cloudservicepermissiondenied.md) — Error code indicating that the user has not allowed access to Cloud service information.
- [SKErrorCloudServiceNetworkConnectionFailed](code/cloudservicenetworkconnectionfailed.md) — Error code indicating that the device could not connect to the network.
- [SKErrorCloudServiceRevoked](code/cloudservicerevoked.md) — Error code indicating that the user has revoked permission to use this cloud service.
- [SKErrorPrivacyAcknowledgementRequired](code/privacyacknowledgementrequired.md) — Error code indicating that the user has not yet acknowledged Apple’s privacy policy for Apple Music.
- [SKErrorUnauthorizedRequestData](code/unauthorizedrequestdata.md) — Error code indicating that the app is attempting to use a property for which it does not have the required entitlement.
- [SKErrorInvalidOfferIdentifier](code/invalidofferidentifier.md) — Error code indicating that the offer identifier is invalid.
- [SKErrorInvalidOfferPrice](code/invalidofferprice.md) — Error code indicating that the price you specified in App Store Connect is no longer valid.
- [SKErrorInvalidSignature](code/invalidsignature.md) — Error code indicating that the signature in a payment discount isn’t valid.
- [SKErrorMissingOfferParams](code/missingofferparams.md) — Error code indicating that parameters are missing in a payment discount.
- [SKErrorIneligibleForOffer](code/ineligibleforoffer.md) — An error code that indicates the user is ineligible for the subscription offer.
- [SKErrorOverlayCancelled](code/overlaycancelled.md) — An error code that indicates the cancellation of an overlay.
- [SKErrorOverlayInvalidConfiguration](code/overlayinvalidconfiguration.md) — An error code that indicates the overlay’s configuration is invalid.
- [SKErrorOverlayPresentedInBackgroundScene](code/overlaypresentedinbackgroundscene.md)
- [SKErrorOverlayTimeout](code/overlaytimeout.md)
- [SKErrorUnsupportedPlatform](code/unsupportedplatform.md) — An error code that indicates the current platform doesn’t support overlays.
- [SKErrorPaymentMethodBindingConfigurationRequired](code/paymentmethodbindingconfigurationrequired.md)

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Errors

- [Handling errors](../handling-errors.md) — Determine the underlying cause of errors that result from StoreKit requests.
- [SKError](../skerror.md) — StoreKit error descriptions, codes, and domains.
- [SKErrorDomain](../skerrordomain.md) — The error domain name for StoreKit errors.
