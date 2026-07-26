---
title: AppStore
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/appstore
source_url: 'https://developer.apple.com/documentation/storekit/appstore'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/appstore.json'
content_hash: 'sha256:f09f29c5f4800783'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# AppStore

<sub>Enumeration</sub>

Interactions with the App Store, such as managing subscriptions, verifying devices, authorizing payments, synchronizing transactions, getting the environment, and more.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AppStore
```

## Overview

Use these static functions and variables to perform tasks like showing the manage subscriptions sheet, getting the device verification ID, determining whether users can make purchases, and more.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Checking the environment

- [Environment](appstore/environment.md) — Constants that represent the App Store server environment.

### Checking payment setup

- [canMakePayments](appstore/canmakepayments.md) — A Boolean value that indicates whether the person can make purchases.

### Checking current age rating

- [ageRatingCode](appstore/ageratingcode.md) — The current age rating code for your app.

### Verifying devices

- [deviceVerificationID](appstore/deviceverificationid.md) — The device verification identifier to use to verify whether signed information is valid for the current device.

### Getting the platform

- [Platform](appstore/platform.md) — Values that represent Apple platforms.

### Managing subscriptions

- [showManageSubscriptions(in:)](<appstore/showmanagesubscriptions(in_).md>) — Presents the App Store sheet for managing subscriptions.
- [showManageSubscriptions(in:subscriptionGroupID:)](<appstore/showmanagesubscriptions(in_subscriptiongroupid_).md>) — Presents the App Store sheet for managing subscriptions for a subscription group.

### Requesting reviews

- [RequestReviewAction](requestreviewaction.md) — An instance that tells StoreKit to request an App Store rating or review, if appropriate.
- [requestReview(in:)](<appstore/requestreview(in_)-1q8qs.md>) — Tells StoreKit to request an App Store rating or review from the user, if appropriate, using the specified scene.
- [requestReview(in:)](<appstore/requestreview(in_)-4r0y9.md>) — Tells StoreKit to request an App Store rating or review from the user, if appropriate, using the specified view controller.

### Presenting the offer code redemption sheet

- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md) — Enable customers to redeem offer codes through the App Store or within your app.
- [presentOfferCodeRedeemSheet(from:options:)](<appstore/presentoffercoderedeemsheet(from_options_)-89agc.md>) — Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect. _(beta)_
- [offerCodeRedemption(options:isPresented:onCompletion:)](<../swiftui/view/offercoderedemption(options_ispresented_oncompletion_).md>) — Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect. _(beta)_

### Restoring purchases

- [sync()](<appstore/sync().md>) — Synchronizes your app’s transaction information and subscription status with information from the App Store.

### Merchandising

- [AppStoreMerchandisingKind](appstoremerchandisingkind.md)

### Deprecated

- [presentOfferCodeRedeemSheet(in:)](<appstore/presentoffercoderedeemsheet(in_).md>) — Displays a sheet in the window scene that enables customers to redeem an offer code that you configure in App Store Connect. _(deprecated)_
- [offerCodeRedemption(isPresented:onCompletion:)](<../swiftui/view/offercoderedemption(ispresented_oncompletion_).md>) _(deprecated)_
- [presentOfferCodeRedeemSheet(from:)](<appstore/presentoffercoderedeemsheet(from_).md>) — Displays a sheet in the view that enables customers to redeem an offer code that you configure in App Store Connect. _(deprecated)_

### Type Methods

- [presentMerchandising(_:from:)](<appstore/presentmerchandising(__from_)-8bblo.md>) — Display a merchandising view.
- [presentMerchandising(_:from:)](<appstore/presentmerchandising(__from_)-hkrd.md>) — Display a merchandising view.
- [presentOfferCodeRedeemSheet(from:options:)](<appstore/presentoffercoderedeemsheet(from_options_)-gj8m.md>) — Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect. _(beta)_

## See Also

### App Store interactions

- [AppTransaction](apptransaction.md) — Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.
