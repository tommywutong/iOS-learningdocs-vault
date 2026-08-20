---
title: Multiple User Environment Programming Topics
apple_id: 10000180i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPMultipleUsers/BPMultipleUsers.html
archived_at: '2026-07-15T08:16:24.399743Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Root%20and%20Login%20Sessions.md)

# Introduction to Multiple User Environments

This programming topic provides background information about the multiple user environment of OS X. It also provides guidelines on how to write software to support this type of environment, including ways you may need to change your existing Mac apps.

OS X has always supported the use of a single machine by multiple users. Initially, this usage was exclusive; only one user at a time could log in to the console and use the machine. In version 10.3, OS X introduced a feature called _fast user switching_ that lets multiple login sessions run concurrently on the same machine. With this feature, one user at a time is active on the machine while the other user’s sessions continue to run in the background.

Prior to the introduction of fast user switching, developers could rely on the fact that only one user at a time was active on the system console. This meant that applications could make some assumptions about the availability of resources. Unfortunately, some of these assumptions may cause applications to fail in a fast user switching environment. If you are developing applications to run in OS X, you should examine your designs and make sure they take multiple simultaneous users into account.

This programming topic contains the following articles:

- [Root and Login Sessions](Root%20and%20Login%20Sessions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgiydqlkcineugrsdjjea) provides advanced material for daemon developers that describes the organization of the OS X process space and how that organization impacts applications.
- [Supporting Fast User Switching](Supporting%20Fast%20User%20Switching.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgiydslkciffeiskiijfa) provides general guidelines for application developers on how to make your application work in a fast user switching environment.
- [User Switch Notifications](User%20Switch%20Notifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgiytalkdjjbeurcbi5da) shows you how to handle the notifications that occur when the console user changes.

If you want to know more about the login/logout process, are writing a daemon or startup item, or want to know more about the daemons that run in the root session, see _[Daemons and Services Programming Guide](../Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_.

[Next](Root%20and%20Login%20Sessions.md)

