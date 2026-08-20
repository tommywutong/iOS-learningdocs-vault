---
title: Receipt Validation Programming Guide
apple_id: TP40010573
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: null
published: '2017-12-11'
source_url: https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Chapters/ValidateRemotely.html
archived_at: '2026-07-27T06:57:08.281526Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [Receipt Validation Programming Guide](About%20Receipt%20Validation.md)



# Validating Receipts With the App Store

Use a trusted server to communicate with the App Store. Using your own server lets you design your app to recognize and trust only your server, and lets you ensure that your server connects with the App Store server. It is not possible to build a trusted connection between a user’s device and the App Store directly because you don’t control either end of that connection, and therefore can be susceptible to a man-in-the-middle attack.

__Important:__ Do not call the App Store server `/verifyReceipt` endpoint from your app.

Communication with the App Store is structured as JSON dictionaries, as defined in RFC 4627. Binary data is base64 encoded, as defined in RFC 4648.

## Read the Receipt Data

To retrieve the receipt data, use the [appStoreReceiptURL](https://developer.apple.com/documentation/foundation/nsbundle/1407276-appstorereceipturl) method of [NSBundle](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSBundle/Description.html#//apple_ref/occ/cl/NSBundle) to locate the app’s receipt, and then read the entire file. Send this data to your server—as with all interactions with your server, the details are your responsibility.

```
// Load the receipt from the app bundle.
NSURL *receiptURL = [[NSBundle mainBundle] appStoreReceiptURL];
NSData *receipt = [NSData dataWithContentsOfURL:receiptURL];
if (!receipt) { /* No local receipt -- handle the error. */ }

/* ... Send the receipt data to your server ... */
```

## Send the Receipt Data to the App Store

On your server, create a JSON object with the following keys:

KeyValue

receipt-data

The base64 encoded receipt data.

password

_Only used for receipts that contain auto-renewable subscriptions._ Your app’s shared secret (a hexadecimal string).

exclude-old-transactions

_Only used for iOS7 style app receipts that contain auto-renewable or non-renewing subscriptions._ If value is true, response includes only the latest renewal transaction for any subscriptions.

Submit this JSON object as the payload of an HTTP POST request. In the test environment, use `https://sandbox.itunes.apple.com/verifyReceipt` as the URL. In production, use `https://buy.itunes.apple.com/verifyReceipt` as the URL.

## Parse the Response

The response’s payload is a JSON object that contains the following keys and values:

KeyValue

status

Either `0` if the receipt is valid, or one of the error codes listed in [Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgqwvgvzv).

For iOS 6 style transaction receipts, the status code reflects the status of the specific transaction’s receipt.

For iOS 7 style app receipts, the status code is reflects the status of the app receipt as a whole. For example, if you send a valid app receipt that contains an expired subscription, the response is `0` because the receipt as a whole is valid.

receipt

A JSON representation of the receipt that was sent for verification. For information about keys found in a receipt, see [Receipt Fields](Receipt%20Fields.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgywvgvzr).

latest_receipt

_Only returned for receipts containing auto-renewable subscriptions._ For iOS 6 style transaction receipts, this is the base-64 encoded receipt for the most recent renewal. For iOS 7 style app receipts, this is the latest base-64 encoded app receipt.

latest_receipt_info

_Only returned for receipts containing auto-renewable subscriptions._ For iOS 6 style transaction receipts, this is the JSON representation of the receipt for the most recent renewal. For iOS 7 style app receipts, the value of this key is an array containing all in-app purchase transactions. This excludes transactions for a consumable product that have been marked as finished by your app.

latest_expired_receipt_info

_Only returned for iOS 6 style transaction receipts, for an auto-renewable subscription._ The JSON representation of the receipt for the expired subscription.

pending_renewal_info

_Only returned for iOS 7 style app receipts containing auto-renewable subscriptions._ In the JSON file, the value of this key is an array where each element contains the pending renewal information for each auto-renewable subscription identified by the [Product Identifier](Receipt%20Fields.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgywvgvzrge). A pending renewal may refer to a renewal that is scheduled in the future or a renewal that failed in the past for some reason.

is-retryable

Retry validation for this receipt. _Only applicable to status codes 21100-21199 (listed in_ [Table 2-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgqwvgvzv))

__Table 2-1__  Status codes

| Status Code | Description |
| 21000 | The App Store could not read the JSON object you provided. |
| 21002 | The data in the `receipt-data` property was malformed or missing. |
| 21003 | The receipt could not be authenticated. |
| 21004 | The shared secret you provided does not match the shared secret on file for your account. |
| 21005 | The receipt server is not currently available. |
| 21006 | This receipt is valid but the subscription has expired. When this status code is returned to your server, the receipt data is also decoded and returned as part of the response.  _Only returned for iOS 6 style transaction receipts for auto-renewable subscriptions._ |
| 21007 | This receipt is from the test environment, but it was sent to the production environment for verification. Send it to the test environment instead. |
| 21008 | This receipt is from the production environment, but it was sent to the test environment for verification. Send it to the production environment instead. |
| 21010 | This receipt could not be authorized. Treat this the same as if a purchase was never made. |
| 21100-21199 | Internal data access error. |

The values of the `latest_receipt` and `latest_receipt_info` keys are useful when checking whether an auto-renewable subscription is currently active.

The values of `latest_expired_receipt_info` key are useful when checking whether an auto-renewable subscription has expired. Use this along with the value for [Subscription Expiration Intent](Receipt%20Fields.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgywvgvzsga) to get the reason for expiration.

The values of `pending_renewal_info` key are useful to get critical information about any pending renewal transactions for an auto-renewable subscription.

By providing an app receipt or any transaction receipt for the subscription and checking these values, you can get information about the currently-active subscription period. If the receipt being validated is for the latest renewal, the value for `latest_receipt` is the same as `receipt-data` (in the request) and the value for `latest_receipt_info` is the same as `receipt`.
