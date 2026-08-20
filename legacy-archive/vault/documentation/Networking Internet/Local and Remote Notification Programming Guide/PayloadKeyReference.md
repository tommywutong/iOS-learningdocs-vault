---
title: Local and Remote Notification Programming Guide
apple_id: TP40008194
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: AppKit
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/PayloadKeyReference.html
archived_at: '2026-07-15T08:19:08.727568Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Local and Remote Notification Programming Guide](index.md)



## Payload Key Reference

For each notification, you provide a payload with app-specific information and details about how to deliver the notification to the user. The payload is a JSON dictionary object (as defined by [RFC 4627](http://www.ietf.org/rfc/rfc4627.txt)) that you create on your server. The JSON dictionary object must contain an `aps` key, the value of which is a dictionary containing data used by the system to deliver the notification. The main contents of the `aps` dictionary determine whether the system does any of the following:

- Displays an alert message to the user
- Applies a badge to the app’s icon
- Plays a sound
- Delivers the notification silently

In addition to the `aps` dictionary, the JSON dictionary can include custom keys and values with your app-specific content. Custom values must use the JSON structure and use only primitive types such as dictionary (object), array, string, number, and Boolean. Do not include customer information or any sensitive data in your payload unless that data is encrypted or useless outside of the context of your app. For example, you could include a conversation identifier that your an instant messaging app could then use to locate the corresponding user conversation. The data in a notification should never be destructive—that is, your app should never use a notification to delete data on the user’s device.

When using the HTTP/2 based APNS provider API, the maximum size for your JSON dictionary is 4KB. For legacy APIs, the payload size is smaller.

For information and examples of how to create payloads, see [Creating the Remote Notification Payload](CreatingtheNotificationPayload.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjqfvjvomi).

### APS Dictionary Keys

The `aps` dictionary contains the keys used by Apple to deliver the notification to the user’s device. The keys specify the type of interactions that you want the system to use when alerting the user. Table 9-1 lists the keys to include in this dictionary along with the type of information to include in each. Any other keys in the aps dictionary are ignored by Apple.

__Table 9-1__Keys and values of the `aps` dictionary

| Key | Value type | Comment |
| --- | --- | --- |
| `alert` | Dictionary or String | Include this key when you want the system to display a standard alert or a banner. The notification settings for your app on the user’s device determine whether an alert or banner is displayed.  The preferred value for this key is a dictionary, the keys for which are listed in [Table 9-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjxfvjvoni). If you specify a string as the value of this key, that string is displayed as the message text of the alert or banner.  The JSON `\U` notation is not supported. Put the actual UTF-8 character in the alert text instead. |
| `badge` | Number | Include this key when you want the system to modify the badge of your app icon.  If this key is not included in the dictionary, the badge is not changed. To remove the badge, set the value of this key to `0`. |
| `sound` | String | Include this key when you want the system to play a sound. The value of this key is the name of a sound file in your app’s main bundle or in the `Library/Sounds` folder of your app’s data container. If the sound file cannot be found, or if you specify `default`for the value, the system plays the default alert sound.  For details about providing sound files for notifications; see [Preparing Custom Alert Sounds](SupportingNotificationsinYourApp.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnbnknltcma). |
| `content-available` | Number | Include this key with a value of `1` to configure a background update notification. When this key is present, the system wakes up your app in the background and delivers the notification to its app delegate. For information about configuring and handling background update notifications, see [Configuring a Background Update Notification](CreatingtheNotificationPayload.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjqfvjvooa). |
| `category` | String | Provide this key with a string value that represents the notification’s type. This value corresponds to the value in the [identifier](https://developer.apple.com/documentation/uikit/uimutableusernotificationcategory/1615376-identifier) property of one of your app’s registered categories. To learn more about using custom actions, see [Configuring Categories and Actionable Notifications](SupportingNotificationsinYourApp.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnbnknltenq). |
| `thread-id` | String | Provide this key with a string value that represents the app-specific identifier for grouping notifications. If you provide a Notification Content app extension, you can use this value to group your notifications together. For local notifications, this key corresponds to the [threadIdentifier](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/1649860-threadidentifier) property of the [UNNotificationContent](https://developer.apple.com/documentation/usernotifications/unnotificationcontent) object. |

### Alert Keys

Table 9-2 lists the keys and expected values for the `alert` dictionary.

__Table 9-2__Child properties of the `alert` property

| Key | Value type | Comment |
| --- | --- | --- |
| `title` | String | A short string describing the purpose of the notification. Apple Watch displays this string as part of the notification interface. This string is displayed only briefly and should be crafted so that it can be understood quickly. This key was added in iOS 8.2. |
| `body` | String | The text of the alert message. |
| `title-loc-key` | String or `null` | The key to a title string in the `Localizable.strings` file for the current localization. The key string can be formatted with `%@` and `%`_n_`$@` specifiers to take the variables specified in the `title-loc-args` array. See [Localizing the Content of Your Remote Notifications](CreatingtheNotificationPayload.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjqfvjvooi) for more information. This key was added in iOS 8.2. |
| `title-loc-args` | Array of strings or `null` | Variable string values to appear in place of the format specifiers in `title-loc-key`. See [Localizing the Content of Your Remote Notifications](CreatingtheNotificationPayload.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjqfvjvooi) for more information. This key was added in iOS 8.2. |
| `action-loc-key` | String or `null` | If a string is specified, the system displays an alert that includes the Close and View buttons. The string is used as a key to get a localized string in the current localization to use for the right button’s title instead of “View”. See [Localizing the Content of Your Remote Notifications](CreatingtheNotificationPayload.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjqfvjvooi) for more information. |
| `loc-key` | String | A key to an alert-message string in a `Localizable.strings` file for the current localization (which is set by the user’s language preference). The key string can be formatted with `%@` and `%`_n_`$@` specifiers to take the variables specified in the `loc-args` array. See [Localizing the Content of Your Remote Notifications](CreatingtheNotificationPayload.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjqfvjvooi) for more information. |
| `loc-args` | Array of strings | Variable string values to appear in place of the format specifiers in `loc-key`. See [Localizing the Content of Your Remote Notifications](CreatingtheNotificationPayload.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjqfvjvooi) for more information. |
| `launch-image` | String | The filename of an image file in the app bundle, with or without the filename extension. The image is used as the launch image when users tap the action button or move the action slider. If this property is not specified, the system either uses the previous snapshot, uses the image identified by the `UILaunchImageFile` key in the app’s `Info.plist` file, or falls back to `Default.png`. |

[Communicating with APNs](CommunicatingwithAPNs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjrfvjvomi)

[Binary Provider API](BinaryProviderAPI.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjtfvjvomi)
