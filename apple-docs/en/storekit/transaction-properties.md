---
title: Transaction properties
framework: StoreKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction-properties
source_url: 'https://developer.apple.com/documentation/storekit/transaction-properties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction-properties.json'
content_hash: 'sha256:8d49c5437b9fee92'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md) · [In-App Purchase](in-app-purchase.md) · [Transaction](transaction.md)

# Transaction properties

<sub>API Collection</sub>

The properties of a transaction, including identifiers, purchase and revocation dates and details, status, and offer details.

## Topics

### Getting the environment and storefront

- [environment](transaction/environment.md) — The server environment that generates and signs the transaction.
- [storefront](transaction/storefront.md) — The App Store storefront associated with the transaction.

### Getting the original transaction identifier

- [originalID](transaction/originalid.md) — The original transaction identifier of a purchase.
- [originalPurchaseDate](transaction/originalpurchasedate.md) — The date of purchase for the original transaction.

### Identifying a transaction

- [id](transaction/id.md) — The unique identifier for the transaction.
- [webOrderLineItemID](transaction/weborderlineitemid.md) — A unique ID that identifies subscription purchase events across devices, including subscription renewals.

### Identifying the app and product

- [appBundleID](transaction/appbundleid.md) — The bundle identifier for the app.
- [productID](transaction/productid.md) — The product identifier of the in-app purchase.
- [productType](transaction/producttype.md) — The type of the in-app purchase.
- [subscriptionGroupID](transaction/subscriptiongroupid.md) — The identifier of the subscription group that the subscription belongs to.

### Getting purchase and expiration dates

- [purchaseDate](transaction/purchasedate.md) — The date that the App Store charged the user’s account for a purchased or restored product, or for a subscription purchase or renewal after a lapse.
- [expirationDate](transaction/expirationdate.md) — The date the subscription expires or renews.

### Getting the product price and currency

- [price](transaction/price.md) — The price of the in-app purchase that the system records in the transaction.
- [currency](transaction/currency.md) — The currency of the price of the product.

### Getting purchase details

- [isUpgraded](transaction/isupgraded.md) — A Boolean that indicates whether the user upgraded to another subscription.
- [ownershipType](transaction/ownershiptype-swift.property.md) — A value that indicates whether the transaction was purchased by the user, or is made available to them through Family Sharing.
- [OwnershipType](transaction/ownershiptype-swift.struct.md) — The types the system uses to describe whether the user purchased the product or it’s available to them through Family Sharing.
- [purchasedQuantity](transaction/purchasedquantity.md) — The number of consumable products purchased.

### Getting subscription status

- [subscriptionStatus](transaction/subscriptionstatus.md) — An array that contains status information for a subscription group, including renewal and transaction information.

### Getting transaction reason

- [reason](transaction/reason-swift.property.md) — The cause of the purchase transaction, whether it’s a customer’s purchase or an auto-renewable subscription renewal that the system initiates.
- [Reason](transaction/reason-swift.struct.md) — A cause of a purchase transaction, indicating whether it’s a customer’s purchase or an auto-renewable subscription renewal that the system initiates.

### Identifying offers

- [offer](transaction/offer-swift.property.md) — The offer that applies to the transaction, including its offer type, payment mode, and ID.
- [Offer](transaction/offer-swift.struct.md) — Discounts or promotions that apply to a transaction.

### Getting revocation status

- [revocationDate](transaction/revocationdate.md) — The date that the App Store refunded the transaction or revoked it from Family Sharing.
- [revocationReason](transaction/revocationreason-swift.property.md) — The reason that the App Store refunded the transaction or revoked it from Family Sharing.
- [RevocationReason](transaction/revocationreason-swift.struct.md) — Reasons that describe why the App Store may refund a transaction or revoke it from Family Sharing.

### Correlating transactions with accounts

- [appAccountToken](transaction/appaccounttoken.md) — A UUID that associates the transaction with a user on your own service.

### Getting the transaction information in JSON format

- [jsonRepresentation](transaction/jsonrepresentation.md) — The JSON representation of the transaction information.

### Deprecated

- [currencyCode](transaction/currencycode.md) — The three-letter ISO 4217 currency code for the price of the product. _(deprecated)_
- [environmentStringRepresentation](transaction/environmentstringrepresentation.md) — A string representation of the server environment. _(deprecated)_
- [offerID](transaction/offerid.md) — A string that identifies an offer applied to the current subscription. _(deprecated)_
- [offerPaymentModeStringRepresentation](transaction/offerpaymentmodestringrepresentation.md) — The string representation of the payment mode for a subscription offer. _(deprecated)_
- [offerType](transaction/offertype-swift.property.md) — The subscription offer type for the current subscription period. _(deprecated)_
- [reasonStringRepresentation](transaction/reasonstringrepresentation.md) — The string representation of the transaction reason. _(deprecated)_
- [storefrontCountryCode](transaction/storefrontcountrycode.md) — The three-letter code that represents the country or region associated with the App Store storefront of the purchase. _(deprecated)_

## See Also

### Transaction properties

- [appTransactionID](transaction/apptransactionid.md) — The unique identifier of the app download transaction.
