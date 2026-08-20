---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/RequestPayment.html
archived_at: '2026-07-27T06:57:07.335918Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [In-App Purchase Programming Guide](About%20In-App%20Purchase.md)


[Next](Promoting%20In-App%20Purchases.md)[Previous](Retrieving%20Product%20Information.md)

# Requesting Payment

In the second part of the purchase process, after the user has chosen to purchase a particular product, your app submits a payment request to the App Store, as shown in Figure 3-1.

__Figure 3-1__  Stages of the purchase process—requesting payment

（原归档配图未能恢复：`requesting_payment_2x.png`）

## Creating a Payment Request

When the user selects a product to buy, create a payment request using a product object, and set the quantity if needed, as shown in Listing 3-1. The product object comes from the array of products returned by your app’s products request, as discussed in [Retrieving Product Information](Retrieving%20Product%20Information.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqmznknlts).

__Listing 3-1__  Creating a payment request

```
SKProduct *product = <# Product returned by a products request #>;
SKMutablePayment *payment = [SKMutablePayment paymentWithProduct:product];
payment.quantity = 2;
```

## Detecting Irregular Activity

The App Store uses an irregular activity detection engine to help combat fraud. Some apps can provide additional information to improve the engine’s ability to detect unusual transactions. If your users have an account with you, in addition to their App Store accounts, provide this additional piece of information when requesting payment.

By way of illustration, consider the following two examples. In the normal case, many different users on your server each buy coins to use in your game, and each user pays for the purchase from a different App Store account. In contrast, it would be very unusual for a single user on your server to buy coins multiple times, paying for each purchase from a different App Store account. The App Store can’t detect this kind of irregular activity on its own—it needs information from your app about which account on your server is associated with the transaction.

To provide this information, populate the [applicationUsername](https://developer.apple.com/documentation/storekit/skpayment/1506116-applicationusername) property of the payment object with a one-way hash of the user’s account name on your server, such as in the example shown in Listing 3-2.

__Listing 3-2__  Providing an application username

```objc
#import <CommonCrypto/CommonCrypto.h>

// Custom method to calculate the SHA-256 hash using Common Crypto
- (NSString *)hashedValueForAccountName:(NSString*)userAccountName
{
    const int HASH_SIZE = 32;
    unsigned char hashedChars[HASH_SIZE];
    const char *accountName = [userAccountName UTF8String];
    size_t accountNameLen = strlen(accountName);

    // Confirm that the length of the user name is small enough
    // to be recast when calling the hash function.
    if (accountNameLen > UINT32_MAX) {
        NSLog(@"Account name too long to hash: %@", userAccountName);
        return nil;
    }
    CC_SHA256(accountName, (CC_LONG)accountNameLen, hashedChars);

    // Convert the array of bytes into a string showing its hex representation.
    NSMutableString *userAccountHash = [[NSMutableString alloc] init];
    for (int i = 0; i < HASH_SIZE; i++) {
        // Add a dash every four bytes, for readability.
        if (i != 0 && i%4 == 0) {
            [userAccountHash appendString:@"-"];
        }
        [userAccountHash appendFormat:@"%02x", hashedChars[i]];
    }

    return userAccountHash;
}
```

If you use another approach to populate this property, ensure that the value you provide is an opaque identifier uniquely associated with the user’s account on your server. Don’t use the Apple ID for your developer account, the user’s Apple ID, or the user’s unhashed account name on your server.

## Submitting a Payment Request

Adding a payment request to the transaction queue submits it to the App Store. If you add a payment object to the queue multiple times, it’s submitted multiple times—the user is charged multiple times and your app is expected to deliver the product multiple times.

```
[[SKPaymentQueue defaultQueue] addPayment:payment];
```

For every payment request your app submits, it gets back a corresponding transaction that it must process. Transactions and the transaction queue are discussed in [Waiting for the App Store to Process Transactions](Delivering%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnjnknlti).

[Next](Promoting%20In-App%20Purchases.md)[Previous](Retrieving%20Product%20Information.md)
