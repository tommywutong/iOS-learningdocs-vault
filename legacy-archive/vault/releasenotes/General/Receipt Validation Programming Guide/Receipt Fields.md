---
title: Receipt Validation Programming Guide
apple_id: TP40010573
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: null
published: '2017-12-11'
source_url: https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ReceiptFields.html
archived_at: '2026-07-27T06:57:08.301620Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [Receipt Validation Programming Guide](About%20Receipt%20Validation.md)



# Receipt Fields

Receipts are made up of a number of fields. Some fields are only available locally, in the ASN.1 form of the receipt, or only when validating with the App Store, in the JSON form of the receipt. Keys not documented below are reserved for use by Apple and must be ignored by your app.

## App Receipt Fields

### Bundle Identifier

The app’s bundle identifier.

__ASN.1 Field Type__ 2

__ASN.1 Field Value__ UTF8STRING

__JSON Field Name__ bundle_id

__JSON Field Value__ string

This corresponds to the value of `CFBundleIdentifier` in the `Info.plist` file. Use this value to validate if the receipt was indeed generated for your app.

### App Version

The app’s version number.

__ASN.1 Field Type__ 3

__ASN.1 Field Value__ UTF8STRING

__JSON Field Name__ application_version

__JSON Field Value__ string

This corresponds to the value of `CFBundleVersion` (in iOS) or `CFBundleShortVersionString` (in macOS) in the `Info.plist`.

### Opaque Value

An opaque value used, with other data, to compute the SHA-1 hash during validation.

__ASN.1 Field Type__ 4

__ASN.1 Field Value__ A series of bytes

__JSON Field Name__ (none)

__JSON Field Value__ (none)

### SHA-1 Hash

A SHA-1 hash, used to validate the receipt.

__ASN.1 Field Type__ 5

__ASN.1 Field Value__ 20-byte SHA-1 digest

__JSON Field Name__ (none)

__JSON Field Value__ (none)

### In-App Purchase Receipt

The receipt for an in-app purchase.

__ASN.1 Field Type__ 17

__ASN.1 Field Value__ SET of in-app purchase receipt attributes

__JSON Field Name__ in_app

__JSON Field Value__ array of in-app purchase receipts

In the JSON file, the value of this key is an array containing all in-app purchase receipts based on the in-app purchase transactions present in the input base-64 receipt-data. For receipts containing auto-renewable subscriptions, check the value of the latest_receipt_info key to get the status of the most recent renewal.

In the ASN.1 file, there are multiple fields that all have type 17, each of which contains a single in-app purchase receipt.

__Note:__ An empty array is a valid receipt.

The in-app purchase receipt for a consumable product is added to the receipt when the purchase is made. It is kept in the receipt until your app finishes that transaction. After that point, it is removed from the receipt the next time the receipt is updated - for example, when the user makes another purchase or if your app explicitly refreshes the receipt.

The in-app purchase receipt for a non-consumable product, auto-renewable subscription, non-renewing subscription, or free subscription remains in the receipt indefinitely.

### Original Application Version

The version of the app that was originally purchased.

__ASN.1 Field Type__ 19

__ASN.1 Field Value__ UTF8STRING

__JSON Field Name__ original_application_version

__JSON Field Value__ string

This corresponds to the value of `CFBundleVersion` (in iOS) or `CFBundleShortVersionString` (in macOS) in the `Info.plist` file when the purchase was originally made.

In the sandbox environment, the value of this field is always “1.0”.

### Receipt Creation Date

The date when the app receipt was created.

__ASN.1 Field Type__ 12

__ASN.1 Field Value__ IA5STRING, interpreted as an RFC 3339 date

__JSON Field Name__ receipt_creation_date

__JSON Field Value__ IA5STRING, interpreted as an RFC 3339 date

When validating a receipt, use this date to validate the receipt’s signature.

__Note:__ Many cryptographic libraries default to using the device’s current time and date when validating a PKCS7 package, but this may not produce the correct results when validating a receipt’s signature. For example, if the receipt was signed with a valid certificate, but the certificate has since expired, using the device’s current date incorrectly returns an invalid result.

Therefore, make sure your app always uses the date from the Receipt Creation Date field to validate the receipt’s signature.

### Receipt Expiration Date

The date that the app receipt expires.

__ASN.1 Field Type__ 21

__ASN.1 Field Value__ IA5STRING, interpreted as an RFC 3339 date

__JSON Field Name__ expiration_date

__JSON Field Value__ IA5STRING, interpreted as an RFC 3339 date

This key is present only for apps purchased through the Volume Purchase Program. If this key is not present, the receipt does not expire.

When validating a receipt, compare this date to the current date to determine whether the receipt is expired. Do not try to use this date to calculate any other information, such as the time remaining before expiration.

## In-App Purchase Receipt Fields

### Quantity

The number of items purchased.

__ASN.1 Field Type__ 1701

__ASN.1 Field Value__ INTEGER

__JSON Field Name__ quantity

__JSON Field Value__ string, interpreted as an integer

This value corresponds to the [quantity](https://developer.apple.com/documentation/storekit/skpayment/1506077-quantity) property of the [SKPayment](https://developer.apple.com/documentation/storekit/skpayment) object stored in the transaction’s [payment](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411286-payment) property.

### Product Identifier

The product identifier of the item that was purchased.

__ASN.1 Field Type__ 1702

__ASN.1 Field Value__ UTF8STRING

__JSON Field Name__ product_id

__JSON Field Value__ string

This value corresponds to the [productIdentifier](https://developer.apple.com/documentation/storekit/skpayment/1506155-productidentifier) property of the [SKPayment](https://developer.apple.com/documentation/storekit/skpayment) object stored in the transaction’s [payment](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411286-payment) property.

### Transaction Identifier

The transaction identifier of the item that was purchased.

__ASN.1 Field Type__ 1703

__ASN.1 Field Value__ UTF8STRING

__JSON Field Name__ transaction_id

__JSON Field Value__ string

This value corresponds to the transaction’s [transactionIdentifier](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411288-transactionidentifier) property.

For a transaction that restores a previous transaction, this value is different from the transaction identifier of the original purchase transaction. In an auto-renewable subscription receipt, a new value for the transaction identifier is generated every time the subscription automatically renews or is restored on a new device.

### Original Transaction Identifier

For a transaction that restores a previous transaction, the transaction identifier of the original transaction. Otherwise, identical to the transaction identifier.

__ASN.1 Field Type__ 1705

__ASN.1 Field Value__ UTF8STRING

__JSON Field Name__ original_transaction_id

__JSON Field Value__ string

This value corresponds to the original transaction’s [transactionIdentifier](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411288-transactionidentifier) property.

This value is the same for all receipts that have been generated for a specific subscription. This value is useful for relating together multiple iOS 6 style transaction receipts for the same individual customer’s subscription.

### Purchase Date

The date and time that the item was purchased.

__ASN.1 Field Type__ 1704

__ASN.1 Field Value__ IA5STRING, interpreted as an RFC 3339 date

__JSON Field Name__ purchase_date

__JSON Field Value__ string, interpreted as an RFC 3339 date

This value corresponds to the transaction’s [transactionDate](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411273-transactiondate) property.

For a transaction that restores a previous transaction, the purchase date is the same as the original purchase date. Use [Original Purchase Date](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgywvgvzu) to get the date of the original transaction.

In an auto-renewable subscription receipt, the purchase date is the date when the subscription was either purchased or renewed (with or without a lapse). For an automatic renewal that occurs on the expiration date of the current period, the purchase date is the start date of the next period, which is identical to the end date of the current period.

### Original Purchase Date

For a transaction that restores a previous transaction, the date of the original transaction.

__ASN.1 Field Type__ 1706

__ASN.1 Field Value__ IA5STRING, interpreted as an RFC 3339 date

__JSON Field Name__ original_purchase_date

__JSON Field Value__ string, interpreted as an RFC 3339 date

This value corresponds to the original transaction’s [transactionDate](https://developer.apple.com/documentation/storekit/skpaymenttransaction/1411273-transactiondate) property.

In an auto-renewable subscription receipt, this indicates the beginning of the subscription period, even if the subscription has been renewed.

### Subscription Expiration Date

The expiration date for the subscription, expressed as the number of milliseconds since January 1, 1970, 00:00:00 GMT.

__ASN.1 Field Type__ 1708

__ASN.1 Field Value__ IA5STRING, interpreted as an RFC 3339 date

__JSON Field Name__ expires_date

__JSON Field Value__ string, interpreted as an RFC 3339 date

This key is only present for auto-renewable subscription receipts. Use this value to identify the date when the subscription will renew or expire, to determine if a customer should have access to content or service. After validating the latest receipt, if the subscription expiration date for the latest renewal transaction is a past date, it is safe to assume that the subscription has expired.

### Subscription Expiration Intent

For an expired subscription, the reason for the subscription expiration.

__ASN.1 Field Type__ (none)

__ASN.1 Field Value__ (none)

__JSON Field Name__ expiration_intent

__JSON Field Value__ string, interpreted as an integer

“1” - Customer canceled their subscription.

“2” - Billing error; for example customer’s payment information was no longer valid.

“3” - Customer did not agree to a recent price increase.

“4” - Product was not available for purchase at the time of renewal.

“5” - Unknown error.

This key is only present for a receipt containing an expired auto-renewable subscription. You can use this value to decide whether to display appropriate messaging in your app for customers to resubscribe.

### Subscription Retry Flag

For an expired subscription, whether or not Apple is still attempting to automatically renew the subscription.

__ASN.1 Field Type__ (none)

__ASN.1 Field Value__ (none)

__JSON Field Name__ is_in_billing_retry_period

__JSON Field Value__ string, interpreted as an integer

“1” - App Store is still attempting to renew the subscription.

“0” - App Store has stopped attempting to renew the subscription.

This key is only present for auto-renewable subscription receipts. If the customer’s subscription failed to renew because the App Store was unable to complete the transaction, this value will reflect whether or not the App Store is still trying to renew the subscription.

### Subscription Trial Period

For a subscription, whether or not it is in the free trial period.

__ASN.1 Field Type__ (none)

__ASN.1 Field Value__ (none)

__JSON Field Name__ is_trial_period

__JSON Field Value__ string

This key is only present for auto-renewable subscription receipts. The value for this key is `"true"` if the customer’s subscription is currently in the free trial period, or `"false"` if not.

Note: If a previous subscription period in the receipt has the value “true” for either the `is_trial_period` or the `is_in_intro_offer_period` key, the user is not eligible for a free trial or introductory price within that subscription group.

### Subscription Introductory Price Period

For an auto-renewable subscription, whether or not it is in the introductory price period.

__ASN.1 Field Type__ 1719

__ASN.1 Field Value__ INTEGER

__JSON Field Name__ is_in_intro_offer_period

__JSON Field Value__ string

This key is only present for auto-renewable subscription receipts. The value for this key is `"true"` if the customer’s subscription is currently in an introductory price period, or `"false"` if not.

Note: If a previous subscription period in the receipt has the value “true” for either the `is_trial_period` or the `is_in_intro_offer_period` key, the user is not eligible for a free trial or introductory price within that subscription group.

### Cancellation Date

For a transaction that was canceled by Apple customer support, the time and date of the cancellation. For an auto-renewable subscription plan that was upgraded, the time and date of the upgrade transaction.

__ASN.1 Field Type__ 1712

__ASN.1 Field Value__ IA5STRING, interpreted as an RFC 3339 date

__JSON Field Name__ cancellation_date

__JSON Field Value__ string, interpreted as an RFC 3339 date

Treat a canceled receipt the same as if no purchase had ever been made.

__Note:__ A canceled in-app purchase remains in the receipt indefinitely. Only applicable if the refund was for a non-consumable product, an auto-renewable subscription, a non-renewing subscription, or for a free subscription.

### Cancellation Reason

For a transaction that was canceled, the reason for cancellation.

__ASN.1 Field Type__ (none)

__ASN.1 Field Value__ (none)

__JSON FieldName__ cancellation_reason

__JSON Field Value__ string, interpreted as an integer

“1” - Customer canceled their transaction due to an actual or perceived issue within your app.

“0” - Transaction was canceled for another reason, for example, if the customer made the purchase accidentally.

Use this value along with the cancellation date to identify possible issues in your app that may lead customers to contact Apple customer support.

### App Item ID

A string that the App Store uses to uniquely identify the application that created the transaction.

__ASN.1 Field Type__ (none)

__ASN.1 Field Value__ (none)

__JSON Field Name__ app_item_id

__JSON Field Value__ string

If your server supports multiple applications, you can use this value to differentiate between them.

Apps are assigned an identifier only in the production environment, so this key is not present for receipts created in the test environment.

This field is not present for Mac apps.

See also [Bundle Identifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgywvgvzt).

### External Version Identifier

An arbitrary number that uniquely identifies a revision of your application.

__ASN.1 Field Type__ (none)

__ASN.1 Field Value__ (none)

__JSON Field Name__ version_external_identifier

__JSON Field Value__ string

This key is not present for receipts created in the test environment. Use this value to identify the version of the app that the customer bought.

### Web Order Line Item ID

The primary key for identifying subscription purchases.

__ASN.1 Field Type__ 1711

__ASN.1 Field Value__ INTEGER

__JSON Field Name__ web_order_line_item_id

__JSON Field Value__ string

This value is a unique ID that identifies purchase events across devices, including subscription renewal purchase events.

### Subscription Auto Renew Status

The current renewal status for the auto-renewable subscription.

__ASN.1 Field Type__ (none)

__ASN.1 Field Value__ (none)

__JSON Field Name__ auto_renew_status

__JSON Field Value__ string, interpreted as an integer

“1” - Subscription will renew at the end of the current subscription period.

“0” - Customer has turned off automatic renewal for their subscription.

This key is only present for auto-renewable subscription receipts, for active or expired subscriptions. The value for this key should not be interpreted as the customer’s subscription status. You can use this value to display an alternative subscription product in your app, for example, a lower level subscription plan that the customer can downgrade to from their current plan.

### Subscription Auto Renew Preference

The current renewal preference for the auto-renewable subscription.

__ASN.1 Field Type__ (none)

__ASN.1 Field Value__ (none)

__JSON Field Name__ auto_renew_product_id

__JSON Field Value__ string

This key is only present for auto-renewable subscription receipts. The value for this key corresponds to the [productIdentifier](https://developer.apple.com/documentation/storekit/skproduct/1506080-productidentifier) property of the product that the customer’s subscription renews. You can use this value to present an alternative service level to the customer before the current subscription period ends.

### Subscription Price Consent Status

The current price consent status for a subscription price increase.

__ASN.1 Field Type__ (none)

__ASN.1 Field Value__ (none)

__JSON Field Name__ price_consent_status

__JSON Field Value__ string, interpreted as an integer

“1” - Customer has agreed to the price increase. Subscription will renew at the higher price.

“0” - Customer has not taken action regarding the increased price. Subscription expires if the customer takes no action before the renewal date.

This key is only present for auto-renewable subscription receipts if the subscription price was increased without keeping the existing price for active subscribers. You can use this value to track customer adoption of the new price and take appropriate action.
