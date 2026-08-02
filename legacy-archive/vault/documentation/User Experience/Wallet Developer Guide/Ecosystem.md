---
title: Wallet Developer Guide
apple_id: TP40012195
resource_type: Guide
platform: watchOS|iOS
topic: User Experience
technology: PassKit
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/PassKit_PG/Ecosystem.html
archived_at: '2026-07-18T02:12:14.850093Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Wallet Developer Guide](index.md)



## Wallet Ecosystem Design

There are three major parts to the pass life cycle: creation, management, and redemption. Wallet handles the middle; it lets users view and manage their passes and provides lock screen integration. You are responsible for the two ends, creating passes and redeeming passes.

### You Create and Distribute Passes

You are responsible for distributing passes to your users. Mail and Safari understand how to work with passes—in iOS they install passes directly, and in macOS they install passes through iCloud—so you can use them to add passes. Your app can also install passes using the PassKit framework.

### Passes Are Presented and Managed by the Wallet App

Passes contain text, images, and a barcode. You set the pass’s style, provide images, and set colors and text formatting. The Wallet app then lays out and presents the pass for you. It also provides controls, letting the user manage and delete passes.

For more information, see Wallet in _iOS Human Interface Guidelines_.

### Your App Can Interact with Passes Using PassKit

The PassKit framework provides APIs that let apps interact with passes in the PassKit library. Companion apps should not duplicate the functionality of the Wallet app, rather they should enrich the user experience by doing things that Wallet can’t do, such as letting the user ask for a different seat on a flight and then updating the pass. Passes need to be useful even if the user doesn’t have your app installed.

Your app can interact only with passes whose pass type identifier matches the app’s entitlements—either passes you created or some subset of those passes.

For more information, see _[Pass Kit Framework Reference](https://developer.apple.com/documentation/passkit)_

### Your Server Can Update Passes

Updating passes is a cooperative effort between your server and Wallet. When information on a pass changes, your server sends a push notification to the user’s device. The device communicates with your server to find out what has changed and to get the latest version of your passes.

Passes are updated by providing the latest version of the pass, not by providing a list of what changed. Anything in the pass can be updated except for the pass type ID and serial number. However, only certain kinds of changes actually make sense to the user. Updating a train ticket to reflect a delayed departure or a store card to show the current balance keeps the pass current and won’t cause confusion. Replacing a coupon for a free order of breadsticks with a coupon for a free drink is likely to confuse the user—from the user’s perspective, one coupon disappeared and another coupon was unexpectedly added. In that case, you should create a new pass for the drink coupon.

For more information on implementing your update service’s API, see _[PassKit Web Service Reference](https://developer.apple.com/library/archive/documentation/PassKit/Reference/PassKit_WebService/WebService.html#//apple_ref/doc/uid/TP40011988)_. For more information on sending push notifications, see _[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_.

### You Are Responsible for Pass Redemption

Determining when passes are valid and controlling how many times they can be redeemed are your responsibility. You must also manage the effects of redeeming a pass, such as updating a balance in your records. The following sections describe several use cases for passes and explain how you might implement them. These use cases illustrate interesting ideas and approaches, but they’re not meant to be fully worked solutions.

### Pass for a One-Time-Use Coupon

Suppose you want to give out a coupon for 10 percent off that can only be used once. You include a unique number on each coupon from 1 to 500, and you write the numbers 1 through 500 on a piece of paper next to the cash register. When the cashiers ring up a coupon, they consult the paper and cross off that coupon’s number.

This works on a very small scale, and illustrates the principle of a central trusted authority. You don’t control what your customers do with their passes or devices (or even with their paper coupons), so you can’t use that as a starting point for trusting information. Instead, you trust your database, and use the pass as a quick way to look up a particular record. The data in the pass itself is just a snapshot of some particular database state.

Using a pass to create a one-time-use coupon follows a similar pattern. Include a unique ID in the pass’s barcode. Your server keeps track of all the valid IDs. When a user redeems the pass, you scan the barcode and consult your server to determine whether the pass is still valid.

Don’t try to make a single-use pass by giving the pass only to a single device. Users with multiple iOS devices want your pass on all of their devices, and iCloud syncs their passes across devices for them. If you email your pass to your users, they can forward the email and its pass. Your scanning and redemption system is responsible for implementing policies such as “This pass is only valid once.”

Don’t try to expire or void a pass by pushing an update. Updates are not guaranteed to be delivered, because the user may not have a network connection or may have disabled updates for the pass. Instead, update your database to indicate that the pass is invalid, and consult your database when the pass is redeemed. Additionally, your app should not remove expired passes without the user’s consent.

### Pass for a Store Card with a Balance

Suppose you own a coffee shop and your customers typically pay with a card that carries a balance, such as a gift card or store card. Just as you did in the one-time-use pass, access information about the pass from a trustworthy source. In this case, you need to look up the pass’s current balance.

The implementation is similar to the one-time-use coupon. Give each pass a unique ID in the barcode, and then scan the barcode at the point of sale. Before completing the sale, consult your server to read the pass’s current balance, record the transaction, and update the pass’s balance. Once this is done, the cashier completes the sale.

If you need to verify that the person presenting the pass is actually the account owner, you have several options. Generic style passes include a thumbnail image. You can use this image to display the account holder’s picture directly on the pass. For greater security, store the account holder’s picture in your database and display it on the cashier’s screen when the pass is scanned. Other approaches are also possible, such as asking for an photo ID.

After the sale is completed, push an update to the pass with the account’s new balance. Your users can easily check their balance because it’s displayed on the pass. You must push this update from a server that implements the web service API; however, it does not need to be the same server that was used to process the transactions.

> [!NOTE]
> 

### Pass for a Season Membership

Suppose you work for a museum that supports Wallet for its annual memberships. You want to let your members use the same pass for the entire year, with occasional updates to display current information about traveling exhibits.

You could implement this pass similarly to the one-time-use coupon or store card—giving each pass a unique ID and then verifying the account against your server. However, in this case, it is also possible to store trusted information directly on the pass. This would allow you to use scanners that don’t have a network connection.

In this case, you want to store a more complex message in the barcode. This message includes all the vital information needed by the scanner (for example, the account’s unique ID, as well as the membership start and end dates). The message also needs to include a cryptographic signature for this information. Your scanners can then use the cryptographic signature to validate the information stored in the barcode, ensuring that it came from your servers.

This approach works because the information stored in the barcode does not change. When you scan the pass, you simply read the information. You do not update it. Both the one-time-use coupon and the store card need to update their trusted information each time the pass is used. For the coupon, the pass is invalidated after use. For the store card, the pass’s balance is updated.

> [!NOTE]
> 

[Introducing Wallet](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojvfvbuqmjnknltc)

[Building Your First Pass](YourFirst.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojvfvbuqmrnknltc)
