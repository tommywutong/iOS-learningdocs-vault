---
title: Debugging issues with CloudKit subscriptions
apple_id: DTS40017578
resource_type: QA
platform: tvOS|iOS|macOS
topic: Data Management
technology: CloudKit
published: '2016-11-16'
source_url: https://developer.apple.com/library/archive/qa/qa1917/_index.html
archived_at: '2026-07-18T02:36:50.250410Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1917

# Debugging issues with CloudKit subscriptions

## Q:  My CloudKit subscriptions don’t trigger notifications after relevant changes are made. How to debug that?

A: Most CloudKit subscription issues are either due to incorrect assumptions about when and where notifications should fire or improperly configured CloudKit containers or subscriptions. This document will introduce you some cases that aren't expected to trigger CloudKit notifications, following with how to verify the state of your iCloud container and how to avoid some common issues related to CloudKit subscriptions.

When working with CloudKit subscriptions, be aware that:

- Notifications won't be delivered to your device if the notification settings for your app are off. CloudKit relies on the Apple Push Notification service (APNs) to deliver notifications. If your app is not allowed for push notifications on the device, you won't see them. To turn the settings on, go to `Settings > Notifications`, then navigate to your app's setting screen.
- CloudKit notifications won’t be delivered to the device on which the relevant changes are made.
- The Simulators don't support push notifications. To test push notifications you must be running directly on the target platform.
- CloudKit notifications won’t be delivered to your app if the notifications' [shouldSendContentAvailable](https://developer.apple.com/reference/cloudkit/cknotificationinfo/1515110-shouldsendcontentavailable) property is `true` and meanwhile your app is force quit. On iOS, users can force quit an app by double-tapping the home button and swiping it away from the multitasking UI.
- CloudKit generates a notification for every relevant change. However, notifications can be coalesced by the APNs if too many occur in a short period time. In that case, you will still get the last notification, thus can retrieve the unhandled ones with `CKFetchNotificationChangesOperation` and process them from there.

With these cases in mind, if your issue is still there, the next step is to verify the state of your iCloud container.

You can verify the state of your iCloud container with the following steps:

1. Prepare two iOS devices running the latest iOS, log in iCloud with the same Apple ID, and make sure iCloud Drive is On. You can use an iOS Simulator to change the CloudKit database, but only a device can register and receive push notifications. CloudKit works on macOS and tvOS as well, so you can set up Macs or Apple TVs similarly if you are using a macOS or tvOS app for this verification.
2. Download Apple's [CloudKit Catalog sample](https://developer.apple.com/library/content/samplecode/CloudAtlas/Introduction/Intro.html#//apple_ref/doc/uid/TP40014599), change the bundle ID to the one being used in your app, pick the right iCloud container in Xcode’s `Capabilities` pane if you use a custom one, then build and run the sample on your devices. Make sure notification settings are allowed, as discussed above.
3. Create a query subscription to track record creations. On one device, run the CloudKit Catalog sample, go to `Subscriptions` > `saveSubscription` screen, set the `subscriptionType` to `Query`, input something in the `name BEGINSWITH` field that will be used in the subscription predicate, then tap the `Run` `Code` button.
4. One the other device, go to `Records` > `saveRecord` screen and add a new record, make sure the record name begins with the string you just input so that it matches the subscription predicate, then tap the `Run` `Code` button.

Your first device should soon get a notification, proving that your iCloud container is functioning. If this does not work, it is likely that your iCloud container is in an invalid state. In that case, you can report it by [filing a bug report](https://developer.apple.com/bug-reporting/), and continue your development using a new iCloud container and / or logging in iCloud with a new Apple ID.

To use a new iCloud container, go to the Xcode's `Capabilities` panel, switch the `iCloud` > `Containers` options to `Specify custom containers`, then pick or add a new container. To create a new Apple ID, follow the steps on the [Create Your Apple ID](https://appleid.apple.com/account#!&page=create) page.

With the same iCloud container and Apple ID, if CloudKit Catalog works well but your app doesn’t, the next step is to check if your app has any coding issue related to CloudKit subscriptions.

The following issues are frequently seen when working with CloudKit subscriptions:

- Apps haven't registered for push notifications.

  When you pick the CloudKit service on the `Capabilities` pane, Xcode automatically adds the Push Notifications service for your app so you don't need to do extra configuration on your app ID in the membership portal. However, like other apps, CloudKit apps need to register for push notifications as well by calling `UIApplication`'s `registerForRemoteNotifications()` method. See the [Registering for Push Notifications](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG21) section of TN2265 for the details.

  Note that CloudKit does handle device tokens for you, so you don't need to implement the `application(_:didRegisterForRemoteNotificationsWithDeviceToken:)` method, unless you need that for another purpose.
- Apps fail to create subscriptions.

  Creating subscriptions can fail for a number of reasons, so error handling when saving subscriptions is very important. Due to the asynchronous nature of CloudKit work, error handling is an essential part of writing a CloudKit application. See the WWDC session, [CloudKit Best Practices](https://developer.apple.com/videos/play/wwdc2016/231/), for how to better handle CloudKit errors.

  One common error is saving subscriptions that refer to un-indexed fields in the production environment, which will generate an Invalid Arguments (`CKError.code.``invalidArguments`) error. You can fix it by going to the production environment in [CloudKit Dashboard](https://icloud.developer.apple.com/dashboard/), selecting the field, and checking the `Query` box under the `Index` column.
- Apps don't create subscriptions for every user.

  CloudKit subscriptions are per-user, which means your app needs to create subscriptions for each and every user that should receive push notifications. Logging in CloudKit Dashboard with your account and seeing subscriptions there doesn’t mean all users have them.

  For debugging purpose, you can use `CKFetchSubscriptionsOperation` to fetch and look into all subscriptions for the current user. However, you don’t need to check the existence before creating subscriptions. Instead, you can create subscriptions with specified subscription IDs and save them directly – if a subscription with the same ID has already existed on the server, no duplicate will be created.
- The changes don’t really match the subscription predicate.

  When creating a subscription whose predicate contains a `CKReference` field, be sure to use a `CKRecordID` object as the value for the field when creating the predicate. Using a `CKRecord` object in this case doesn't currently work.

  To rule out issues related to predicate formats and values in debugging time, simply replace your predicate with `truePredicate` and check if the issue is still there.
- Notifications get lost in the delivery process.

  CloudKit notifications can get lost if something is wrong on the network connection used by the APNs. If your issue doesn't fall into the above cases, check if notifications are lost in the delivery process by installing the [Persistent Connection Logging profile](https://developer.apple.com/library/content/technotes/tn2265/tn2265_PersistentConnectionLogging.zip) (未归档：ZIP 按安全策略跳过) on your device, then analyzing the push service logs. See the [Observing Push Status Messages](https://developer.apple.com/library/content/technotes/tn2265/_index.html#//apple_ref/doc/uid/DTS40010376-CH1-TNTAG21) section of TN2265 for how to do that.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-11-16 | New document that explains how to debug the issue that CloudKit subscriptions don't trigger notifications when the relevant changes are made. |

