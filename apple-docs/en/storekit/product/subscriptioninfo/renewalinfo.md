---
title: Product.SubscriptionInfo.RenewalInfo
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo.json'
content_hash: 'sha256:29edce1ba959d8d1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionInfo](../subscriptioninfo.md)

# Product.SubscriptionInfo.RenewalInfo

<sub>Structure</sub>

The renewal information for an auto-renewable subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RenewalInfo
```

## Overview

`Product.SubscriptionInfo.RenewalInfo` provides information about the next subscription renewal period. Check the [state](status-swift.struct/state.md) to determine whether the subscription will be active (subscribed), expired, or in another state at the next renewal period.

## Relationships

- **Conforms To**: [Copyable](../../../swift/copyable.md), [CustomDebugStringConvertible](../../../swift/customdebugstringconvertible.md), [Equatable](../../../swift/equatable.md), [Escapable](../../../swift/escapable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Getting the environment

- [environment](renewalinfo/environment.md) — The server environment that signs the renewal information for an auto-renewable subscription.

### Getting the transaction ID

- [originalTransactionID](renewalinfo/originaltransactionid.md) — The transaction identifier of the original purchase.

### Identifying the account

- [appAccountToken](renewalinfo/appaccounttoken.md) — The app account token you provided during the subscription purchase, if one exists.
- [appTransactionID](renewalinfo/apptransactionid.md) — The unique identifier of the app download transaction.

### Getting the product ID

- [currentProductID](renewalinfo/currentproductid.md) — The subscription product ID that the customer is subscribed to.

### Getting subscription dates

- [recentSubscriptionStartDate](renewalinfo/recentsubscriptionstartdate.md) — The earliest start date of a subscription in a series of auto-renewable subscription purchases that ignores all lapses of paid service shorter than 60 days.
- [renewalDate](renewalinfo/renewaldate.md) — The UNIX time, in milliseconds, that the most recent auto-renewable subscription purchase expires.

### Getting the renewal or expiration state

- [state](status-swift.struct/state.md) — The renewal state of the auto-renewable subscription.
- [autoRenewPreference](renewalinfo/autorenewpreference.md) — The product ID of the auto-renewable subscription that will automatically renew.
- [willAutoRenew](renewalinfo/willautorenew.md) — A Boolean value that indicates whether the subscription automatically renews in the next period.
- [expirationReason](renewalinfo/expirationreason-swift.property.md) — The reason the auto-renewable subscription expired.
- [ExpirationReason](renewalinfo/expirationreason-swift.struct.md) — The reasons for auto-renewable subscription expirations.

### Getting offers

- [offer](renewalinfo/offer.md) — A subscription offer that applies to the transaction at the next renewal period.
- [Offer](../../transaction/offer-swift.struct.md) — Discounts or promotions that apply to a transaction.
- [eligibleWinBackOfferIDs](renewalinfo/eligiblewinbackofferids.md) — An array of strings that represent identifiers of win-back offers that the customer is eligible to redeem, sorted with the best offers first.

### Getting the renewal price and currency

- [renewalPrice](renewalinfo/renewalprice.md) — The renewal price of the auto-renewable subscription that renews at the next billing period.
- [currency](renewalinfo/currency.md) — The currency of the subscription’s renewal price.

### Getting billing status

- [isInBillingRetry](renewalinfo/isinbillingretry.md) — A Boolean value that indicates whether an auto-renewable subscription is in the billing retry period.
- [gracePeriodExpirationDate](renewalinfo/graceperiodexpirationdate.md) — The date the billing grace period expires for the auto-renewable subscription.

### Getting the price increase status

- [Managing Price Increases for Auto-Renewable Subscriptions](../../managing-price-increases-for-auto-renewable-subscriptions.md) — Identify the price increase status for auto-renewable subscriptions in your app and on your server.
- [priceIncreaseStatus](renewalinfo/priceincreasestatus-swift.property.md) — The status that indicates whether the auto-renewable subscription is subject to a price increase.
- [PriceIncreaseStatus](renewalinfo/priceincreasestatus-swift.enum.md) — Status values that indicate whether an auto-renewable subscription is subject to a price increase.

### Verifying subscription renewal information

- [deviceVerification](renewalinfo/deviceverification.md) — The device verification value to use to verify whether the renewal information belongs to the device.
- [deviceVerificationNonce](renewalinfo/deviceverificationnonce.md) — The UUID to use to compute the device verification value.
- [signedDate](renewalinfo/signeddate.md) — The date that the App Store signed the JWS renewal information.

### Getting subscription renewal info in JSON format

- [jsonRepresentation](renewalinfo/jsonrepresentation.md) — The JSON representation of the subscription renewal information.

### Getting renewal information for Advanced Commerce API

- [advancedCommerceInfo](renewalinfo/advancedcommerceinfo-swift.property.md) — Renewal information for a subscription that uses the Advanced Commerce API.
- [AdvancedCommerceInfo](renewalinfo/advancedcommerceinfo-swift.struct.md) — Renewal information for subscriptions that use the Advanced Commerce API.

### Deprecated

- [environmentStringRepresentation](renewalinfo/environmentstringrepresentation.md) — The string representation of the server environment that signs the renewal information for an auto-renewable subscription. _(deprecated)_
- [offerID](renewalinfo/offerid.md) — A string that identifies an offer that applies to the next subscription period. _(deprecated)_
- [offerType](renewalinfo/offertype.md) — The subscription offer type for the next subscription period. _(deprecated)_
- [currencyCode](renewalinfo/currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [offerPaymentModeStringRepresentation](renewalinfo/offerpaymentmodestringrepresentation.md) _(deprecated)_
- [offerPeriodStringRepresentation](renewalinfo/offerperiodstringrepresentation.md) — The string representation of the subscription offer period applied to the next billing period. _(deprecated)_

### Structures

- [CommitmentInfo](renewalinfo/commitmentinfo-swift.struct.md)

### Instance Properties

- [bundleOriginalTransactionID](renewalinfo/bundleoriginaltransactionid.md)
- [bundleProductID](renewalinfo/bundleproductid.md) — Identifies the bundle product the next renewal is for. If the next renewal is created as part of a subscription bundle, this field will be populated with the product ID of the bundle.
- [bundleSubscriptionGroupID](renewalinfo/bundlesubscriptiongroupid.md) — Identifies the subscription bundle group the next renewal is for.
- [commitmentInfo](renewalinfo/commitmentinfo-swift.property.md)
- [renewalBillingPlanType](renewalinfo/renewalbillingplantype.md)
- [willUnbundle](renewalinfo/willunbundle.md) — Whether the subscription will leave the bundle at the next renewal and renew as a standalone product.

## See Also

### Subscription status and renewal information

- [Status](status-swift.struct.md) — The renewal status information for an auto-renewable subscription.
- [SubscriptionRenewalInfo](../../subscriptionrenewalinfo.md) — Represents the renewal information for an auto-renewable subscription.
- [RenewalState](renewalstate.md) — The renewal states of auto-renewable subscriptions.
- [SubscriptionRenewalState](../../subscriptionrenewalstate.md) — The renewal states of auto-renewable subscriptions.
- [SubscriptionPeriod](../../subscriptionperiod.md) — Represents the duration of time between subscription renewals.
