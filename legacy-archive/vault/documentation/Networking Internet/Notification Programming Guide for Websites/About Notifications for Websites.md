---
title: Notification Programming Guide for Websites
apple_id: TP40013225
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: WebKit
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/Introduction/Introduction.html
archived_at: '2026-07-15T08:18:51.200754Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Understanding%20the%20User%20Experience.md)

# About Notifications for Websites

Notifications are concise, unobtrusive messages that appear in the top-right corner of the screen, alerting Mac users about a new message or a completed task. As a web developer, you can configure your website to send notifications to Mac users, even if you don’t have a native Cocoa app.

__Figure I-1__  Notifications in Notification Center

!

There are two kinds of notifications for websites:

- _Safari Push Notifications_, which is an Apple-exclusive technology and triggered remotely using Apple Push Notification service (APNs).
- _Local Notifications_, which are specified by a [W3C standard](http://www.w3.org/TR/notifications/) and triggered locally using JavaScript.

This document explains the key concepts of notifications for websites and how to implement them in your ecosystem.

### Users Control Their Notifications

Review the preferences available to users to better understand how to implement your notification service.

### Safari Push Notifications Are Deployed from Your Server

In OS X v10.9 and later, you can send push notifications to your website users. Safari doesn’t need to be open for the notification to appear, and your visitors have control over their notification settings on a per-website basis.

### Local Notifications Are Invoked with JavaScript

In OS X v10.8 and later, you can tap into Notification Center through a JavaScript API. After visitors grant permission to receive local notifications, you can trigger notifications to appear as long as the webpage remains in an open tab.

- [WWDC 2013: Implementing OS X Push Notifications for Websites](https://developer.apple.com/wwdc/videos/?id=614) shows best practices for implementing push notifications for websites.
- _[Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194)_ describes how to send push notifications to iOS and OS X apps.
- _[WebKit DOM Programming Topics](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/index.html#//apple_ref/doc/uid/TP40001483)_ describes other JavaScript APIs available to WebKit browsers.
- _[Safari Web Content Guide](../../Apple%20Applications/Safari%20Web%20Content%20Guide/Developing%20Web%20Content%20for%20Safari.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjr)_ describes how to create websites for Safari.
- [Developer Account Help](https://help.apple.com/developer-account/) describes how to manage your developer account.
[Next](Understanding%20the%20User%20Experience.md)

