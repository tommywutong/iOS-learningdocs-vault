---
title: Notification Programming Guide for Websites
apple_id: TP40013225
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: WebKit
published: '2018-04-09'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/LocalNotifications/LocalNotifications.html
archived_at: '2026-07-15T08:18:52.313859Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Notification Programming Guide for Websites](About%20Notifications%20for%20Websites.md)


[Next](Document%20Revision%20History.md)[Previous](Configuring%20Safari%20Push%20Notifications.md)

# Configuring Local Notifications

As of OS X v10.8, webpages in Safari can post notifications to the systemwide notification system known as _Notification Center_. Local notifications are dispatched by the WebKit `Notification` object and follow the implementation outlined by the [W3C specification](http://dev.w3.org/2006/webapi/WebNotifications/publish/Notifications.html).

Because your website’s visitors could be running an older version of OS X, first determine whether notifications are supported by their browser. Do this by making sure that the `window.Notification` object is defined.

If the `window.Notification` object does indeed exist, you can continue to check for permissions by accessing the `permission` property. The `permission` property can return three possible states:

- `default`—The user has not yet specified whether he or she approves of notifications being sent from this domain.
- `granted`—The user has given permission for notifications to be sent from this domain.
- `denied`—The user has denied permission for notifications to be sent from this domain.

If the permission level is `default`, it’s likely that the user hasn’t yet been prompted to grant access to notifications from your domain. Prompt your users with a Safari dialog box, as shown in Figure 3-1, by calling the `requestPermission()` function on the `Notification` object. This function accepts one parameter, a callback function, which executes when the user grants or denies permission.

__Figure 3-1__  A dialog box prompting for permission

!

Creating a local notification is as simple as creating a new object.

```
var n = new Notification(title [, options]);
```

The only required parameter is the title, which is a string. Available keys that can be included in the `options` object are as follows:

- `body`—The notification’s subtitle.
- `tag`—The notification’s unique identifier. This tag prevents duplicate entries from appearing in Notification Center if the user has multiple instances of your website open.

The notification is placed in a queue and is shown when it isn’t preceded by another notification. The subtitle is always the domain or extension name from which the notification originated, and the icon is always the Safari icon, as shown in Figure 3-2.

__Figure 3-2__  A notification banner

!

A notification stays in Notification Center (see Figure 3-3) until the user explicitly clears all notifications from Safari, or until you close the notification programmatically. To close notifications programmatically, call the `close()` function on the notification object.

__Figure 3-3__  A notification in Notification Center

!

To remove a local notification from Notification Center immediately after it is clicked, call `close()` in the notification’s `onclick` event handler. The `onclick` event handler, and other JavaScript event handlers, are listed in Table 3-1.

__Table 3-1__  Available notification events

| Event handler | Description |
| `onshow` | An event that triggers when the notification is first presented onscreen. |
| `onclick` | An event that triggers if the user clicks on the notification as an alert, a banner, or in Notification Center. By default, clicking a notification brings the receiving window into focus, even if another app is in the foreground. |
| `onclose` | An event that triggers when the notification is dismissed, or closed in Notification Center. Calling `close()` on the notification object triggers the `onclose` event handler. |
| `onerror` | An event that triggers when the notification cannot be presented to the user. This event is fired if the permission level is set to `denied` or `default`. |

Listing 3-1 shows how to send a local notification while adhering to the permission level a user has set.

__Listing 3-1__  Implementing local notification support

```
var notify = function () {
    // Check for notification compatibility.
    if (!'Notification' in window) {
        // If the browser version is unsupported, remain silent.
        return;
    }
    // Log current permission level
    console.log(Notification.permission);
    // If the user has not been asked to grant or deny notifications
    // from this domain...
    if (Notification.permission === 'default') {
        Notification.requestPermission(function () {
            // ...callback this function once a permission level has been set.
            notify();
        });
    }
    // If the user has granted permission for this domain to send notifications...
    else if (Notification.permission === 'granted') {
        var n = new Notification(
                    'New message from Liz',
                    {
                      'body': 'Liz: "Hi there!"',
                      // ...prevent duplicate notifications
                      'tag' : 'unique string'
                    }
                );
        // Remove the notification from Notification Center when clicked.
        n.onclick = function () {
            this.close();
        };
        // Callback function when the notification is closed.
        n.onclose = function () {
            console.log('Notification closed');
        };
    }
    // If the user does not want notifications to come from this domain...
    else if (Notification.permission === 'denied') {
        // ...remain silent.
        return;
    }
};
```

[Next](Document%20Revision%20History.md)[Previous](Configuring%20Safari%20Push%20Notifications.md)

