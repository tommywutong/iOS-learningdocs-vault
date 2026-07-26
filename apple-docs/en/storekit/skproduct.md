---
title: SKProduct
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.0+（18.0 起废弃）, iPadOS 3.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.7+（15.0 起废弃）, tvOS（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 6.2+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skproduct
source_url: 'https://developer.apple.com/documentation/storekit/skproduct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skproduct.json'
content_hash: 'sha256:70975d3b11f42633'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKProduct

<sub>Class</sub>

Information about a registered product in App Store Connect.

> [!warning] Deprecated
> Use Product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class SKProduct
```

## Overview

[SKProduct](skproduct.md) objects are returned as part of an [SKProductsResponse](skproductsresponse.md) object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Product Identifier

- [productIdentifier](skproduct/productidentifier.md) — The string that identifies the product to the Apple App Store. _(deprecated)_

### Getting Product Attributes

- [localizedDescription](skproduct/localizeddescription.md) — A description of the product. _(deprecated)_
- [localizedTitle](skproduct/localizedtitle.md) — The name of the product. _(deprecated)_
- [contentVersion](skproduct/contentversion.md) — A string that identifies the version of the content. _(deprecated)_
- [isFamilyShareable](skproduct/isfamilyshareable.md) — A Boolean value that indicates whether the product is available for Family Sharing in App Store Connect. _(deprecated)_
- [contentLengths](skproduct/contentlengths.md) — The total size of the content, in bytes. _(deprecated)_

### Getting Pricing Information

- [price](skproduct/price.md) — The cost of the product in the local currency. _(deprecated)_
- [priceLocale](skproduct/pricelocale.md) — The locale used to format the price of the product. _(deprecated)_
- [introductoryPrice](skproduct/introductoryprice.md) — The object containing introductory price information for the product. _(deprecated)_
- [discounts](skproduct/discounts.md) — An array of subscription offers available for the auto-renewable subscription. _(deprecated)_
- [SKProductDiscount](skproductdiscount.md) — The details of an introductory offer or a promotional offer for an auto-renewable subscription. _(deprecated)_

### Getting Subscription Information

- [subscriptionGroupIdentifier](skproduct/subscriptiongroupidentifier.md) — The identifier of the subscription group to which the subscription belongs. _(deprecated)_
- [subscriptionPeriod](skproduct/subscriptionperiod.md) — The period details for products that are subscriptions. _(deprecated)_
- [SKProductSubscriptionPeriod](skproductsubscriptionperiod.md) — An object containing the subscription period duration information. _(deprecated)_
- [PeriodUnit](skproduct/periodunit.md) — Values representing the duration of an interval, from a day up to a year. _(deprecated)_

### Getting Downloadable Content Information

- [isDownloadable](skproduct/isdownloadable.md) — A Boolean value that indicates whether the App Store has downloadable content for this product. _(deprecated)_
- [downloadContentLengths](skproduct/downloadcontentlengths.md) — The lengths of the downloadable files available for this product. _(deprecated)_
- [downloadContentVersion](skproduct/downloadcontentversion.md) — A string that identifies which version of the content is available for download. _(deprecated)_
- [downloadable](skproduct/downloadable.md) — A Boolean value that indicates whether the App Store has downloadable content for this product. _(deprecated)_

## See Also

### Product information

- [Loading in-app product identifiers](loading-in-app-product-identifiers.md) — Load the unique identifiers for your in-app products to retrieve product information from the App Store.
- [Fetching product information from the App Store](fetching-product-information-from-the-app-store.md) — Retrieve up-to-date information about the products for sale in your app to display to your customers.
- [SKProductsRequest](skproductsrequest.md) — An object that can retrieve localized information from the App Store about a specified list of products. _(deprecated)_
- [SKProductsResponse](skproductsresponse.md) — An App Store response to a request for information about a list of products. _(deprecated)_
