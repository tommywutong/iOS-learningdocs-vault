---
title: Notification Programming Guide for Websites
apple_id: TP40013225
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: WebKit
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/UserExperience/UserExperience.html
archived_at: '2026-07-15T08:18:56.889509Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Notification Programming Guide for Websites](About%20Notifications%20for%20Websites.md)


[Next](Configuring%20Safari%20Push%20Notifications.md)[Previous](About%20Notifications%20for%20Websites.md)

# Understanding the User Experience

To best serve notifications to your users, you must first understand how OS X displays notifications. In this chapter, you learn the difference between local notifications and push notifications for websites, how users grant permission for websites to display notifications, and how users manage their notification preferences.

Starting in OS X v10.8, Safari users can allow websites to display banners and alerts in Notification Center. Through a JavaScript API, you can create notifications that appear and behave like notifications from native Cocoa apps, as shown in Figure 1-1 and Figure 1-2.

__Figure 1-1__  A banner showing a local notification

!

__Figure 1-2__  A local notification in Notification Center

!

Because local notifications are controlled entirely by JavaScript, the user must have your website open in a Safari window (or tab) for your notification to appear. Safari can be minimized or hidden, or your website could be loaded in an inactive tab, but it must be open to run the JavaScript that creates the notification.

Local notifications display the Safari icon, and appear under the Safari section in Notification Center. The Safari section in Notification Center is where local notifications from all websites appear. The notification title, domain, and body are shown. Because local notifications appear as coming from Safari, rather than from your website directly, the user’s notification preferences for Safari are applied.

Push notifications are similar to local notifications. They exhibit the same appearance, except that they have their own icon and section in Notification Center, as shown in Figure 1-3 and Figure 1-4.

__Figure 1-3__  A banner showing a push notification sent from a web server

!

__Figure 1-4__  A push notification in Notification Center

!

Unlike local notifications, push notifications don’t display the website domain, because the icon makes it clear which website it represents. More importantly, push notifications can be received even when Safari is closed.

Users must opt in to receive notifications. The opt-in process only occurs once per domain. The presentation of asking for permission is identical for all website notifications. In fact, the permission policy that a user chooses for push notifications applies to local notifications. Compare the appearance of requesting both kinds of notifications in Figure 1-5 and Figure 1-6.

__Figure 1-5__  Requesting to display local notifications

!

__Figure 1-6__  Requesting to display push notifications

!

As you can see, the permission sheets for local and push notifications look very similar. The request appears only once; after a user sets the permission level, the preference is saved.

Users can adjust their notification preferences in Safari preferences and System Preferences.

In Safari preferences, users can choose to allow or deny notifications from websites on a per-domain basis by selecting Notifications, as shown in Figure 1-7. In the Notifications pane, users can grant permission for some websites to send notifications while denying permission to others.

__Figure 1-7__  Controlling which websites have authorization to send notifications

!!

Users choose how they want notifications to appear in the Notifications pane of System Preferences, as shown in Figure 1-8. Local notifications respect the preferences set for Safari, and push notifications respect the preferences for each website that issues push notifications. Some users may prefer that notifications display as alerts, which stay on the screen until dismissed. Other users may choose not to display notifications at all.

__Figure 1-8__  Adjusting the appearance of notifications

!!

Because some users may have configured their system or browser to block your notifications, be sure you present only information that is informative. Never use a notification to provide crucial information.

Your website becomes notified if a user changes their preferences for a website employing push notifications. You can use this information to change the notification settings for your user’s account in your web interface. For more information, skip down to [Configuring Your Web Service Endpoints](Configuring%20Safari%20Push%20Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeztemrvfvbuqmznknltemq).

[Next](Configuring%20Safari%20Push%20Notifications.md)[Previous](About%20Notifications%20for%20Websites.md)

