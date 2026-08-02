---
title: In-App Purchase Receipt Validation for iOS 5.1 and Earlier
apple_id: TP40012484
resource_type: Release Note
platform: iOS
topic: null
technology: StoreKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/releasenotes/StoreKit/IAP_ReceiptValidation/index.html
archived_at: '2026-07-18T02:59:02.411641Z'
---
> 导航：[总目录](../README.md) · [releasenotes](../_indexes/releasenotes.md)



# In-App Purchase Receipt Validation for iOS 5.1 and Earlier

> [!IMPORTANT]
> 

A vulnerability has been discovered in iOS 5.1 and earlier related to validating in-app purchase receipts by connecting to the App Store server directly from an iOS device. An attacker can alter the DNS table to redirect these requests to a server controlled by the attacker. Using a certificate authority controlled by the attacker and installed on the device by the user, the attacker can issue a SSL certificate that fraudulently identifies the attacker’s server as an App Store server. When this fraudulent server is asked to validate an invalid receipt, it responds as if the receipt were valid.

This vulnerability is addressed in iOS 6.0 and later. If your app follows the best practices described below then it is not affected by this attack.

#### Contents:

- [My app performs validation by connecting to my own server. How am I affected?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdiobufvbuqmbnknlti)
- [My app performs validation by connecting to the App Store server directly. How am I affected?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdiobufvbuqmbnknltk)
- [How can I validate transactions that have already completed?](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdiobufvbuqmbnknltq)
- [Code Listings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdiobufvbuqmbnknlto)

### My app performs validation by connecting to my own server. How am I affected?

If your app follows best practices and performs receipt validation by sending the receipt to your server and having your server perform the validation with the App Store server, your app is not affected by this attack because it does not connect to the App Store server. However, it may be vulnerable to similar attacks when connecting to your server.

Use the appropriate cryptographic techniques to ensure that your app is actually connected to your server, and that your server is actually connected to the App Store server. You can use the mitigation strategy outlined in this document as a starting point. For more information, see _[Security Overview](../documentation/Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_.

### My app performs validation by connecting to the App Store server directly. How am I affected?

The best practice for validating receipts is to send the receipt to your server, and have your server perform the validation with the App Store server.

If your app connects to the App Store server directly from the device, your app may be affected by this vulnerability. You can address this vulnerability as follows:

- Check that the SSL certificate used to connect to the App Store server is an EV certificate.
- Check that the information returned from validation matches the information in the `SKPayment` object.
- Check that the receipt has a valid signature.
- Check that new transactions have a unique transaction ID.

### How can I validate transactions that have already completed?

__Consumables__ If you have saved the receipts, either on the device or on your server, revalidate the receipts after implementing your mitigation strategy. If you have not saved the receipts, you cannot validate these past transactions; you should not take any action.

__Nonconsumables__ Set aside the current receipts, perform a restore operation, and validate the new receipts. Avoid redownloading content that is already on the device during this process.

### Code Listings

The code listings in this document’s companion files illustrate an implementation approach for the mitigation strategy described in this document.

> [!NOTE]
> 

To add this code to your project:

1. Download and unzip this document’s companion files. (The link is in the top right corner of this page.)
2. Add the `VerificationController.h` and `VerificationController.m` files to your project in Xcode, and add them to the appropriate targets.
3. Link your project against the Security framework.
4. Provide a base64 encoder, a base64 decoder, and the action to perform when validation succeeds.
