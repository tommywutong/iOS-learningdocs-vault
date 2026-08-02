---
title: In-App Purchase Programming Guide
apple_id: TP40008267
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: StoreKit
published: '2018-02-06'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/StoreKitGuide/Chapters/Subscriptions.html
archived_at: '2026-07-27T06:57:07.396007Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [In-App Purchase Programming Guide](About%20In-App%20Purchase.md)


[Next](Restoring%20Purchased%20Products.md)[Previous](Delivering%20Products.md)

# Working with Subscriptions

Apps that offer subscriptions have some additional behaviors and considerations. Because subscriptions involve an element of time, your app must be able to determine whether the subscription is currently active and determine the subscription states for past dates. Your app must also react to new, renewed, and lapsed subscriptions, and properly handle expired subscriptions. Figure 6-1 shows an example subscription timeline, including some of the complexities your app needs to handle.

__Figure 6-1__  Example subscription timeline

（原归档配图未能恢复：`subscription_timeline_2x.png`）

## Calculating a Subscription’s Active Period

Your app needs to determine which content the user has access to based on the period of time their subscription was active. For example, for a user with a subscription to a monthly magazine that publishes a new issue on the first day of each month, consider the timeline shown in Table 6-1.

__Table 6-1__  Timeline of a sample monthly subscription

| Date | Event | Subscription State |
| February 1 | February issue is published. It is not made available to the user because the user has not yet subscribed. | Not yet subscribed |
| February 20 | User subscribes to a monthly subscription plan. The February issue is the most recent, and is made available immediately. | Active |
| March 1 | March issue is published. It is made available immediately because the user has an active subscription. | Active |
| March 20 | The user’s subscription automatically renews for another month. | Active |
| April 1 | April issue is published. It is made available immediately because the user has an active subscription. | Active |
| April 20 | The user cancels their subscription, thus ending the subscription period. | Lapsed |
| May 1 | May issue is published. It is not made available to the user because the user’s subscription has lapsed. | Lapsed |
| June 1 | June issue is published. It is not made available to the user because the user’s subscription has lapsed. | Lapsed |
| June 17 | User resubscribes. June issue is made available immediately. | Active |
| July 1 | July issue is published. It is made available immediately because the user has an active subscription. | Active |

To provide access to all the content a customer is entitled to, keep a record of the date that each piece of content is published. Read the Original Purchase Date, Purchase Date, and Subscription Expiration Date field from each receipt entry to determine the start and end dates of each subscription period. (For information about the receipt, see _[Receipt Validation Programming Guide](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/About%20Receipt%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknzt)_.) The user has access to all content published between each subscription start and end date, and the content that was initially unlocked when the subscription was purchased. If the subscription lapsed, there will be multiple periods of time during which the subscription was active, and there will be pieces of content unlocked at the beginning of a subscription period.

To identify lapses in a subscription, compare the Subscription Expiration Date field from each receipt entry to the PurchaseDate field of the previous receipt entry for all entries in the receipt.

__Note:__ Don’t calculate the subscription period by adding a subscription duration to the purchase date. That approach fails to take into account the free trial period, the marketing opt-in period, and the content made available immediately after the user purchased the subscription.

For example, because content is always unlocked when a subscription is purchased, a user who purchases a monthly subscription mid-month to a magazine that publishes a new issue on the first day of every month gets access to two issues in their first month of subscribing: the most recently published issue, which is unlocked at the time that the subscription is purchased, and the issue you publish on the subsequent first day of the month, which is unlocked at the time you publish it.

Continuing with the example from Table 6-1, the receipt would show the following start and end dates:

- February 20 – March 20
- March 20 – April 20
- (The lapse from April 20 – June 17 is _not_ recorded explicitly in the receipt.)
- June 17 – July 17

The user has access to the February and June issues because they were initially unlocked when the subscription was purchased or restarted.

The user has access to the March, April, June, and July issues because the subscription is active at those times.

## Upgrades and Plan Changes

Users can manage their subscriptions in their account settings on the App Store, or within your app’s interface. For each subscription, the App Store shows all the renewal options that the subscription group offers. Users can easily change their service levels and choose to upgrade, downgrade, or cross-grade as often as they like. Downgrades of any duration or cross-grades with different durations go into effect at the next renewal date.

You can check the receipt’s Subscription Auto Renew Preference field to learn about any plan changes the user selected that will go into effect at the next renewal date. (For information about the receipt, see _[Receipt Validation Programming Guide](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/About%20Receipt%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknzt)_.)

## Expiration and Renewal

The subscription renewal process begins in the ten days before the expiration date. During those ten days, the App Store checks for any billing issues that might delay or prevent the subscription from being automatically renewed, for example:

- the customer’s payment method is no longer active,
- the product increased in price since the user bought the subscription,
- the product is no longer available.

The App Store may notify users of any issue so that they can resolve it before the subscription expires and avoid an interruption in their subscription service.

During the 24-hour period before the subscription expires, the App Store starts trying to automatically renew it. The App Store makes several attempts to automatically renew the subscription over a period of time but eventually stops if there are too many failed attempts.

__Note:__ For billing-related issues, the App Store may attempt to renew a subscription for up to 60 days. You can check for a Subscription Retry Flag in the receipt to determine if the App Store is still attempting to renew the subscription.

The App Store renews the subscription slightly before it expires, to prevent any lapse in the subscription. However, lapses are still possible. For example, if the user’s payment information is no longer valid, the first renewal attempt fails. If the user updates their payment information after the subscription expires, there would be a short lapse in the subscription between the expiration date and the date that the subsequent automatic renewal attempt succeeds. The user can also disable automatic renewal and intentionally let a subscription expire, then renew it at a later date, creating a longer lapse in the subscription. Make sure your app’s subscription logic can handle lapses of various durations correctly. You can check the subscription auto renew status field to determine a subscription’s renewal status.

After a subscription is successfully renewed, StoreKit adds a transaction for the renewal to the transaction queue. Your app checks the transaction queue on launch and handles the renewal the same way as any other transaction. Note that if your app is already running when the subscription renews, the transaction observer is _not_ called; your app finds out about the renewal the next time the app is launched.

As an example, the timeline below shows a user’s account for a subscription to an app that provides service on a monthly basis. In the example, the subscription briefly lapses due to a billing issue. The user corrects the issue, and the subscription renews with a new monthly renewal date.

__Table 6-2__  Example of a timeline for a monthly subscription

| Date | Event | Subscription State |
| February 20 | User subscribes to a monthly subscription. Service is made available immediately. | Active |
| March 20 | The user’s subscription automatically renews for another month. Service remains available. | Active |
| April 19 | User’s payment method expires. | Active |
| April 20 | The user’s subscription fails to renew because the transaction failed. The subscription lapses. | Lapsed |
| May 5 | The user updates their payment method. The App Store is able to successfully renew the subscription. Service is made available immediately. | Active |
| June 5 | The user’s subscription automatically renews for another month. Service remains available. | Active |

## Cancellation

A subscription is paid for in full when it is purchased. Users can receive a refund only by contacting Apple customer service. For example, if the user accidentally buys the wrong product, customer support can cancel the subscription and issue a full or partial refund. Customers may cancel a subscription in the middle of a subscription period, but the subscription remains paid through the end of the same period.

To check whether a purchase has been canceled by Apple Customer Support, look for the Cancellation Date field in the receipt. If the field contains a date, regardless of the subscription’s expiration date, the purchase has been canceled. With respect to providing content or service, treat a canceled transaction the same as if no purchase had ever been made.

Depending on the type of product your app provides, you may need to check the currently active subscription period, or you may need to check all past subscription periods. For example, a magazine app needs to check all past subscription periods to determine which issues the user should have access to. An app with a streaming service only needs to check the currently active subscription to determine if the user should have access to its service.

## Status Update Notifications

A `statusUpdateNotification` is a server-to-server notification service for auto-renewable subscriptions. A notification specifies the status of a subscription at the time the notification is sent.

To obtain up-to-date information as you process events, your app should verify the latest receipt with the App Store. It is recommended that you use the status update notification service along with receipt validation to validate a user’s current subscription status and provide them with service. See _[Receipt Validation Programming Guide](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/About%20Receipt%20Validation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknzt)_ for information about receipt validation.

To receive status update notifications, configure a subscription status URL for your app in App Store Connect. The App Store will deliver JSON objects via an HTTP POST to your server for the key subscription events listed in [Table 6-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnznknltcni). Your server is responsible for parsing, interpreting, and responding to all `statusUpdateNotification` posts.

__Note:__ Using the server-to-server notification service is optional. You can opt in at any time.

The `statusUpdateNotification` is an HTTP POST. The body of the POST contains the data elements listed in the Table 6-3 .

__Table 6-3__  Status Update Notification Keys

| Key | Description |
| `environment` | Specifies whether the notification is for a sandbox or a production environment:  `Sandbox`  `PROD` |
| `notification_type` | Describes the kind of event that triggered the notification. See values in [Table 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnznknltcnq). |
| `password` | This value is the same as the shared secret you POST when validating receipts. See [Validating Receipts With the App Store](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/Validating%20Receipts%20With%20the%20App%20Store.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgq). |
| `original_transaction_id` | This value is the same as the Original Transaction Identifier in the receipt. You can use this value to relate multiple iOS 6-style transaction receipts for an individual customer’s subscription. |
| `cancellation_date` | The time and date that a transaction was cancelled by Apple customer support. Posted only if the `notification_type` is `CANCEL`. See values in [Table 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnznknltcnq). |
| `web_order_line_item_id` | The primary key for identifying a subscription purchase. Posted only if the `notification_type` is `CANCEL`. See values in [Table 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnznknltcnq). |
| `latest_receipt` | The base-64 encoded transaction receipt for the most recent renewal transaction. Posted only if the `notification_type` is `RENEWAL` or `INTERACTIVE_RENEWAL`, and only if the renewal is successful. |
| `latest_receipt_info` | The JSON representation of the receipt for the most recent renewal. Posted only if renewal is successful. Not posted for `notification_type` `CANCEL`. See values in [Table 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnznknltcnq). |
| `latest_expired_receipt` | The base-64 encoded transaction receipt for the most recent renewal transaction. Posted only if the subscription expired. |
| `latest_expired_receipt_info` | The JSON representation of the receipt for the most recent renewal transaction. Posted only if the `notification_type` is `RENEWAL` or `CANCEL` or if renewal failed and subscription expired. |
| `auto_renew_status` | A Boolean value indicated by strings “true” or “false”. This is the same as the auto renew status in the receipt. See also [Receipt Fields](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/Receipt%20Fields.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgy). |
| `auto_renew_adam_id` | The current renewal preference for the auto-renewable subscription. This is the Apple ID of the product. |
| `auto_renew_product_id` | This is the same as the Subscription Auto Renew Preference in the receipt. See also[Receipt Fields](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/Receipt%20Fields.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgy). |
| `expiration_intent` | This is the same as the Subscription Expiration Intent in the receipt. Posted only if `notification_type` is `RENEWAL` or `INTERACTIVE_RENEWAL`. See also [Receipt Fields](../../../releasenotes/General/Receipt%20Validation%20Programming%20Guide/Receipt%20Fields.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydknztfvbuqmjqgy). |

The App Store may post a notification under any of the conditions listed in [Table 6-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4denrxfvbuqnznknltcnq), which represents a complete list of notification types and corresponding subscription events.

__Table 6-4__  Status Update Notification Types

| notification_type | Description |
| `INITIAL_BUY` | Initial purchase of the subscription. Store the `latest_receipt` on your server as a token to verify the user’s subscription status at any time, by validating it with the App Store. |
| `CANCEL` | Subscription was canceled by Apple customer support. Check `Cancellation Date` to know the date and time when the subscription was canceled. |
| `RENEWAL` | Automatic renewal was successful for an __expired__ subscription. Check `Subscription Expiration Date` to determine the next renewal date and time. |
| `INTERACTIVE_RENEWAL` | Customer renewed a subscription interactively after it lapsed, either by using your app’s interface or on the App Store in account settings. Service is made available immediately. |
| `DID_CHANGE_RENEWAL_PREF` | Customer changed the plan that takes affect at the next subscription renewal. Current active plan is not affected. |

To indicate success from a `statusUpdateNotification` post, your server should send an HTTP status code of 200; your server is not required to return a data value. If your server sends a 50x or 40x HTTP code, the App Store will retry the notification. The App Store makes several attempts to retry the notification over a period of time but eventually stops if there are too many failed attempts.

### Security Requirements

Before sending a notification, the App Store tries to establish a secure network connection with your server by using App Transport Security (ATS) protocols. To learn more about ATS requirements, see “[Requirements for Connecting Using ATS](../../General/Information%20Property%20List%20Key%20Reference/Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvonjx)”. If a secure connection cannot be established, notifications will not be sent to your server. For more about security, see https://developer.apple.com/security/.

### Status Update Notifications in the Test Environment

It is recommended that you test `statusUpdateNotifications` for transactions in the test environment before implementing this logic in production.

To determine if a status update notifications for a subscription event is in the test environment, check if the value of the `environment` key in the `statusUpdateNotification` JSON object equals `SANDBOX`.

## Cross-Platform Considerations

Product identifiers are associated with a single app. Apps that have an iOS version and a macOS version have separate products, with unique product identifiers on each platform. You could let users who have a subscription in an iOS app access the content from a macOS app (or vice versa), but implementing that functionality is your responsibility. You would need a system to identify users and keep track of the content they are subscribed to, similar to what you would implement for an app that uses non-renewable subscriptions.

## Enabling Users to Manage Subscriptions

Rather than implementing your own subscription management UI, your app can open the following URL:

```
https://buy.itunes.apple.com/WebObjects/MZFinance.woa/wa/manageSubscriptions
```

Opening this URL launches iTunes or iTunes Store and displays the Manage Subscription page.

## The Test Environment

The behavior of auto-renewable subscriptions differs between the testing environment and the production environment.

In the testing environment, subscription renewals happen at an accelerated rate, and auto-renewable subscriptions renew a maximum of six times per day. This enables you to test how your app handles a subscription renewal, a subscription lapse, and a subscription history that includes gaps.

Because of the accelerated expiration and renewal rates, a subscription can expire before the system tries to renew the subscription, leaving a small lapse in the subscription period. Such lapses are also possible in production for a variety of reasons—make sure your app handles them correctly.

[Next](Restoring%20Purchased%20Products.md)[Previous](Delivering%20Products.md)
