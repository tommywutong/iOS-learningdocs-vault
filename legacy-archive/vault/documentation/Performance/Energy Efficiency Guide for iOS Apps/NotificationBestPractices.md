---
title: Energy Efficiency Guide for iOS Apps
apple_id: TP40015243
resource_type: Guide
platform: watchOS|iOS
topic: Performance
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/NotificationBestPractices.html
archived_at: '2026-07-18T01:48:25.242290Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Energy Efficiency Guide for iOS Apps](index.md)



## Notification Best Practices

Notifications enable an app to inform the user of something—such as the receipt of an incoming message—when the app is no longer running in the foreground. iOS supports local and remote notifications.

Local notifications are scheduled by an app, for local delivery on the same device. For example, a calendar alert or other time-based reminder might be a local notification.

Remote notifications, also known as push notifications, use a client/server architecture. Your server sends notifications to the Apple Push Notification service, which delivers them to the user’s device—the client. For example, a sports app might receive remote notifications on the user’s device whenever the user’s favorite football team wins a game.

To the user, local and remote notifications are the same. They both just indicate that information is available. However, local and remote notifications have different effects on energy.

> [!NOTE]
> 

### Use Local Notifications Whenever Possible

If your app requires time-based notifications that don’t rely on external data, it should use local notifications to give network hardware a rest. As a side benefit, local notifications occur even if your app isn’t running. Local notifications still wake an idle device, though, so you should always avoid sending notifications unnecessarily.

### Prioritize Remote Notification Delivery

Remote notifications provided by your server to the Apple Notification Service include a variety of elements, including payload data, an expiration date, a priority, and more. Remote notifications support two levels of push priority. One delivers the notification immediately. The other delays delivery of the notification until an energy-efficient time. Unless a notification truly requires an immediate delivery, use the deferred delivery method.

[Reduce the Frequency of Motion Updates](MotionBestPractices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmzyfvjvomi)

[Bluetooth Best Practices](BluetoothBestPractices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbtfvbuqmryfvjvomi)
