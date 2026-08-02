---
title: Receipt Validation Programming Guide
apple_id: TP40010573
resource_type: Guide
platform: tvOS|iOS|macOS
topic: General
technology: null
published: '2017-12-11'
source_url: https://developer.apple.com/library/archive/releasenotes/General/ValidateAppStoreReceipt/Introduction.html
archived_at: '2026-07-27T06:57:08.245691Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md)



# About Receipt Validation

The receipt for an application or in-app purchase is a record of the sale of the application and of any in-app purchases made from within the application. You can add receipt validation code to your application to prevent unauthorized copies of your application from running. Refer to the license agreement and the review guidelines for specific information about what your application may and may not do to implement copy protection.

Receipt validation requires an understanding of cryptography and a variety of secure coding techniques. It's important that you employ a solution that is unique to your application.

## At a Glance

There are two ways to validate receipts: locally and with the App Store. Compare both approaches and determine which is a better fit for your app and your infrastructure. You can also choose to implement both approaches.

### Validating Receipts Locally

Validating locally requires code to read and validate a PKCS #7 signature, and code to parse and validate the signed payload.

__Relevant Chapters:__ [Validating Receipts Locally](Validating%20Receipts%20Locally.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjnknlte), [Receipt Fields](Receipt%20Fields.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgywvgvzr)

### Validating Receipts With the App Store

Validating with the App Store requires a secure connection between your app and your server, and code on your server to to validate the receipt with the App Store.

__Relevant Chapters:__ [Validating Receipts With the App Store](Validating%20Receipts%20With%20the%20App%20Store.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgqwvgvzr), [Receipt Fields](Receipt%20Fields.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgywvgvzr)
