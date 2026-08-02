---
title: Notification Hacks
apple_id: DTS10000194
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Notification_Hacks/Introduction/Intro.html
archived_at: '2026-07-18T03:17:05.470818Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](GestaltTalk-GestaltTalk.h.md)

# Notification Hacks

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

PoliteNotification extension prevents notification dialogs from begin displayed by storing the text in a private buffer, accessable through a buffer located via Gestalt. TrashCanNotifications displayes the most recent notification text in the trash can window. Really in any window named trash. Patched EndUpdate to do this. NotificationMon registers with the PoliteNotification extension when it runs. When a notification is received, it saves the text in a window. Save does not work, but who the heck would want to save the notification text anyway. GestaltTalk contains a protocol for accessing the buffer that contains the notifications. Right now it only saves one thing. I would like to extend it to queue up entries, but did not have the time. This may be useful for other Extensions that need to communicate to an application.

[Next](GestaltTalk-GestaltTalk.h.md)

