---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.030.html
archived_at: '2026-07-15T07:58:40.108179Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](NewInWO4.029.md)

## New Notifications

WOApplication now declares two notifications:

- WOApplicationWillFinishLaunchingNotification
- WOApplicationDidFinishLaunchingNotification

Objects can observe one or both of these notifications to add WORequestHandlers to WOApplication's list of request handlers. Alternatively, you can register handlers in your application subclass's __init__ method or constructor. However, if you define a request handler inside of a framework, your framework's class should observe this notification and register itself when the notification is received.
WOSession now declares the following notifications:

- WOSessionDidTimeOutNotification
- WOSessionDidRestoreNotification
- WOSessionDidCreateNotification

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.031.md)
