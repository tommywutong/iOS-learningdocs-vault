---
title: Local and Remote Notification Programming Guide
apple_id: TP40008194
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: AppKit
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/RevisionHistory.html
archived_at: '2026-07-15T08:19:09.286166Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Local and Remote Notification Programming Guide](index.md)



## Document Revision History

This table describes the changes to _Local and Remote Notification Programming Guide_.

| Date | Notes |
| --- | --- |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2017-11-13 | Noted that you can create a background update notification that also alerts the user; mentioned larger token size. |
| 2017-03-27 | Updated figures in APNs Overview chapter to clarify device token use.   Updated figures [Figure 6-7](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW15) and [Figure 6-5](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW2).   In [APNs Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1), clarified the differences between token-based and certificate-based provider-to-APNs trust.   Implemented clarifications throughout [APNs Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) and [Configuring Remote Notification Support](HandlingRemoteNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnrnknltc). |
| 2016-10-27 | Restructured the book to provide a more clear separation between app-specific and server-side functionality.   Updated the book to reflect the use of the User Notifications framework. |
| 2016-09-20 | Added guidance, primarily in the [APNs Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) chapter, on using a provider authentication token for APNs.   Corrected [Figure 6-5](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW2).   Updated [Figure 6-3](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW3) to illustrate using a provider authentication token.   Added a note in the [APNs Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) chapter that in iOS 10 and later you should implement local notifications with the User Notifications framework and the User Notifications UI framework.   Added a note about the requirement for a GeoTrust Global CA root certificate for providers, in [Provider-to-APNs Connection Trust](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW4).   Updated and expanded [HTTP/2 Response from APNs](CommunicatingwithAPNs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjrfvjvomq).   Clarified [Quality of Service, Store-and-Forward, and Coalesced Notifications](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW5). |
| 2016-03-21 | Minor clarifications and corrections throughout document.   Removed information about the `content-length` property from the [Communicating with APNs](CommunicatingwithAPNs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjrfvjvomi) chapter. This property is not relevant to the APNs provider API because of two factors. 1. An APNs payload always fits inside a single `DATA` frame. 2. The length of a `DATA` frame is declared in the frame header, according to the HTTP/2 specification. Eliminating the content-length property reduces bandwidth, complexity, and processing time for APNs requests. |
| 2015-12-17 | Updated to describe the HTTP/2-based APNs provider API, available starting December 2015. |
| 2015-10-21 | Updated information about the provisioning and development workflow. |
| 2015-09-16 | Clarified where custom notification sounds can be stored and made minor corrections. |
| 2015-03-09 | Added information about users changing their notification settings in the Settings app. |
| 2014-10-31 | Made minor corrections. |
| 2014-10-16 | Added information about custom notification actions and location-based notifications. Removed note stating that not all notification types are available in OS X—all types are delivered.   Changed title from _Local and Push Notification Programming Guide_. |
| 2014-09-17 | Added note about content-available key. Added information about notification custom actions and location-based notifications.   Changed title from _Local and Push Notification Programming Guide_. |
| 2014-02-11 | Added note about content-available key. |
| 2013-09-18 | Added information about setting priority for a push notification. |
| 2013-04-23 | Updated chapter "Provider Communication with Apple Push Notification Service". Minor changes throughout other chapters.   Added section [Provider Authentication Tokens](CommunicatingwithAPNs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjrfvjvomy). Added error code 10 to [Note](CommunicatingwithAPNs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjrfvjvona). Expanded discussion in [APNs Provider Certificates](CommunicatingwithAPNs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjrfvjvoni). Moved discussion of a legacy protocol to an appendix. |
| 2011-08-09 | Added information about implementing push notifications on an OS X desktop client. Unified the guide for iOS and OS X. |
| 2010-08-03 | Describes how to determine if an application is launched because the user tapped the notification alert's action button. |
| 2010-07-08 | Changed occurrences of "iPhone OS" to "iOS." |
| 2010-05-27 | Updated and reorganized to describe local notifications, a feature introduced in iOS 4.0. Also describes a new format for push notifications sent to APNs. |
| 2010-01-28 | Made many small corrections. |
| 2009-08-14 | Made minor corrections and linked to short inline articles on Cocoa concepts. |
| 2009-05-22 | Added notes about Wi-Fi and frequency of registration, and gateway address for the development environment. Updated with various clarifications and enhancements. |
| 2009-03-15 | First version of a document that explains how providers can send push notifications to client applications using Apple Push Notification Service. |

