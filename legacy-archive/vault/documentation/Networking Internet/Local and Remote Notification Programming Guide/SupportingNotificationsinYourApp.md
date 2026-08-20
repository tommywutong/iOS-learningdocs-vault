---
title: Local and Remote Notification Programming Guide
apple_id: TP40008194
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: AppKit
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html
archived_at: '2026-07-15T08:19:10.181705Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Local and Remote Notification Programming Guide](index.md)



## Managing Your App’s Notification Support

Apps must be configured at launch time to support local and remote notifications. Specifically, you must configure your app in advance if it does any of the following:

- Displays alerts, play sounds, or badges its icon in response to an arriving notification.
- Displays custom action buttons with a notification.

Typically, you perform all of your configuration before your application finishes launching. In iOS and tvOS, this means configuring your notification support no later than the [application:didFinishLaunchingWithOptions:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622921-application) method of your `UIApplication` delegate. In watchOS, configure that support no later than the [applicationDidFinishLaunching](https://developer.apple.com/documentation/watchkit/wkextensiondelegate/1628241-applicationdidfinishlaunching) method of your `WKExtension` delegate. You may perform this configuration at a later time, but you must avoid scheduling any local or remote notifications targeting your app until this configuration is complete.

Apps that support remote notifications require additional configuration, which is described in [Configuring Remote Notification Support](HandlingRemoteNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnrnknltc).

### Requesting Authorization to Interact with the User

In iOS, tvOS, and watchOS, apps must have authorization to display alerts, play sounds, or badge the app’s icon in response to incoming notifications. Requesting authorization puts control of those interactions in the hands of the user, who can grant or deny your request. The user can also change the authorization settings for your app later in the system settings.

To request authorization, call the [requestAuthorizationWithOptions:completionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649527-requestauthorization) method of the shared `UNUserNotificationCenter` object. If your app is authorized for all of the requested interaction types, the system calls your completion handler block with the `granted` parameter set to `YES``true`. If one or more interaction type is disallowed, the parameter is `NO``false`. Listing 2-1 shows how to request authorization to play sounds and display alerts. Use the completion handler block to update your app’s behaviors based on whether the interaction types were granted or denied.

__Listing 2-1__Requesting authorization for user interactions

Objective-C

1. `UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];`
2. `[center requestAuthorizationWithOptions:(UNAuthorizationOptionAlert + UNAuthorizationOptionSound)`
3. `completionHandler:^(BOOL granted, NSError * _Nullable error) {`
4. `// Enable or disable features based on authorization.`
5. `}];`

Swift

1. `let center = UNUserNotificationCenter.current()`
2. `center.requestAuthorization(options: [.alert, .sound]) { (granted, error) in`
3. `// Enable or disable features based on authorization.`
4. `}`

The first time that your app launches and calls the [requestAuthorizationWithOptions:completionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649527-requestauthorization) method, the system prompts the user to grant or deny the requested interactions. Because the system saves the user’s response, calls to this method during subsequent launches do not prompt the user again.

> [!NOTE]
> 

### Configuring Categories and Actionable Notifications

Actionable notifications give the user a quick and easy way to perform relevant tasks in response to a notification. Instead of the user being forced to launch your app, the interface for an actionable notification displays custom action buttons that the user can tap. When tapped, each button dismisses the notification interface and forwards the selected action to your app for immediate handling. Forwarding the action to your app avoids the need for the user to navigate further in your app to perform the action, thereby saving time.

Apps must explicitly add support for actionable notifications. At launch time, apps must register one or more categories, which define the types of notifications that your app sends. Associated with each category are the actions that the user can perform when a notification of that type is delivered. Each category can have up to four actions associated with it, although the number of actions actually displayed depends on how and where the notification is displayed. For example, banners display no more than two actions.

> [!NOTE]
> 

### Registering the Notification Categories for Your App

Categories define the types of notifications that your app supports and communicate to the system how you want a notification to be presented. You use categories to associate custom actions with a notification and to specify options for how to handle notifications of that type. For example, you use the category options to specify whether the notification can be displayed in a CarPlay environment.

At launch time, you register all of your app’s categories at once using the [setNotificationCategories:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649512-setnotificationcategories) method of the shared [UNUserNotificationCenter](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter) object. Before calling that method, you create one or more instances of the [UNNotificationCategory](https://developer.apple.com/documentation/usernotifications/unnotificationcategory) class and specify the category name and options to use when displaying notifications of that type. Category names are internal to your app and are never seen by the user. When scheduling notifications, you include the category name in the notification’s payload, which the system then uses to retrieve the options and display the notification.

Listing 2-2 shows how to create a simple [UNNotificationCategory](https://developer.apple.com/documentation/usernotifications/unnotificationcategory) object and register it with the system. This category has the name “GENERAL” and is configured with a custom dismiss action option, which causes the system to notify the app when the user dismisses the notification interface without taking any other actions.

__Listing 2-2__Creating and registering a notification category

Objective-C

1. `UNNotificationCategory* generalCategory = [UNNotificationCategory`
2. `categoryWithIdentifier:@"GENERAL"`
3. `actions:@[]`
4. `intentIdentifiers:@[]`
5. `options:UNNotificationCategoryOptionCustomDismissAction];`
7. `// Register the notification categories.`
8. `UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];`
9. `[center setNotificationCategories:[NSSet setWithObjects:generalCategory, nil]];`

Swift

1. `let generalCategory = UNNotificationCategory(identifier: "GENERAL",`
2. `actions: [],`
3. `intentIdentifiers: [],`
4. `options: .customDismissAction)`
6. `// Register the category.`
7. `let center = UNUserNotificationCenter.current()`
8. `center.setNotificationCategories([generalCategory])`

You are not required to assign a category to all of the notifications that you schedule from your app. However, if you do not include a category, your notification is displayed without any custom actions or configuration options.

### Adding Custom Actions to Your Categories

Each of the categories you register may contain up to four custom actions. When a category contains custom actions, the system adds buttons to the notification interface, each with the title of one of your custom actions. If the user taps one of your custom actions, the system sends the corresponding action identifier to your app, launching your app as needed.

To define a custom action, create a [UNNotificationAction](https://developer.apple.com/documentation/usernotifications/unnotificationaction) object and add it to one of your category objects. Each action contains the title string for the corresponding button and options for how to display the button and process the associated task. When the user selects an action, the system provides your app with the action’s identifier string, which you then use to identify the task to perform. Listing 2-3 extends the example in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnbnknltg) by adding a new category with two custom actions.

__Listing 2-3__Defining custom actions for a category

Objective-C

1. `UNNotificationCategory* generalCategory = [UNNotificationCategory`
2. `categoryWithIdentifier:@"GENERAL"`
3. `actions:@[]`
4. `intentIdentifiers:@[]`
5. `options:UNNotificationCategoryOptionCustomDismissAction];`
7. `// Create the custom actions for expired timer notifications.`
8. `UNNotificationAction* snoozeAction = [UNNotificationAction`
9. `actionWithIdentifier:@"SNOOZE_ACTION"`
10. `title:@"Snooze"`
11. `options:UNNotificationActionOptionNone];`
13. `UNNotificationAction* stopAction = [UNNotificationAction`
14. `actionWithIdentifier:@"STOP_ACTION"`
15. `title:@"Stop"`
16. `options:UNNotificationActionOptionForeground];`
18. `// Create the category with the custom actions.`
19. `UNNotificationCategory* expiredCategory = [UNNotificationCategory`
20. `categoryWithIdentifier:@"TIMER_EXPIRED"`
21. `actions:@[snoozeAction, stopAction]`
22. `intentIdentifiers:@[]`
23. `options:UNNotificationCategoryOptionNone];`
25. `// Register the notification categories.`
26. `UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];`
27. `[center setNotificationCategories:[NSSet setWithObjects:generalCategory, expiredCategory,`
28. `nil]];`

Swift

1. `let generalCategory = UNNotificationCategory(identifier: "GENERAL",`
2. `actions: [],`
3. `intentIdentifiers: [],`
4. `options: .customDismissAction)`
6. `// Create the custom actions for the TIMER_EXPIRED category.`
7. `let snoozeAction = UNNotificationAction(identifier: "SNOOZE_ACTION",`
8. `title: "Snooze",`
9. `options: UNNotificationActionOptions(rawValue: 0))`
10. `let stopAction = UNNotificationAction(identifier: "STOP_ACTION",`
11. `title: "Stop",`
12. `options: .foreground)`
14. `let expiredCategory = UNNotificationCategory(identifier: "TIMER_EXPIRED",`
15. `actions: [snoozeAction, stopAction],`
16. `intentIdentifiers: [],`
17. `options: UNNotificationCategoryOptions(rawValue: 0))`
19. `// Register the notification categories.`
20. `let center = UNUserNotificationCenter.current()`
21. `center.setNotificationCategories([generalCategory, expiredCategory])`

Although you may specify up to four custom actions for each category, the system may display only the first two actions in some circumstances. For example, the system displays only two actions when displaying the notification in a banner. When initializing your [UNNotificationCategory](https://developer.apple.com/documentation/usernotifications/unnotificationcategory) objects, always configure the array of actions so that the most relevant actions are first in the array.

If you configure an action using the [UNTextInputNotificationAction](https://developer.apple.com/documentation/usernotifications/untextinputnotificationaction) class, the system provides a way for the user to enter text as part of the notification response. Text input actions are useful for gathering free form text from the user. For example, a message app could allow the user to provide a custom response to a message. When a text input action is delivered to your app to handle, the system packages the user’s response in a [UNTextInputNotificationResponse](https://developer.apple.com/documentation/usernotifications/untextinputnotificationresponse) object.

For information about how to handle the selection of a custom action, see [Responding to the Selection of a Custom Action](SchedulingandHandlingLocalNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnjnknlte).

### Preparing Custom Alert Sounds

Local and remote notifications can specify custom alert sounds to be played when the notification is delivered. You can package the audio data in an `aiff`, `wav`, or `caf` file. Because they are played by the system-sound facility, custom sounds must be in one of the following audio data formats:

- Linear PCM
- MA4 (IMA/ADPCM)
- µLaw
- aLaw

Place custom sound files in your app bundle or in the `Library/Sounds` folder of your app’s container directory. Custom sounds must be under 30 seconds when played. If a custom sound is over that limit, the default system sound is played instead.

You can use the `afconvert` tool to convert sounds. For example, to convert the 16-bit linear PCM system sound `Submarine.aiff` to IMA4 audio in a CAF file, use the following command in the Terminal app:

1. `afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v`

For information on how to associate a sound file with a notification, see [Adding a Sound to the Notification Content](SchedulingandHandlingLocalNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnjnknltg).

### Managing Your App’s Notification Settings

Because users can change the notification settings for your app at any time, you can use the [getNotificationSettingsWithCompletionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649524-getnotificationsettingswithcompl) method of the shared `UNUserNotificationCenter` object to get your app’s authorization status at any time. That method returns a `UNNotificationSettings` object whose contents reflect your app’s current authorization status and the current notification environment.

Use the information in the [UNNotificationSettings](https://developer.apple.com/documentation/usernotifications/unnotificationsettings) object to adjust your app’s notification-related code. You can communicate your app’s alert, badge, and sound authorization settings to your provider so that it can adjust the options it includes in any remote notification payloads. (A _provider_ is a server, that you deploy and manage, that you configure to work with APNs. For more on providers, see [APNs Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).) You can use other settings to adjust how you schedule and configure notifications. For more information about the available settings, see _[UNNotificationSettings Class Reference](https://developer.apple.com/documentation/usernotifications/unnotificationsettings)_.

### Managing Delivered Notifications

When local and remote notifications are not handled directly by your app or the user, they are displayed in Notification Center so that they can be viewed later. Use the [getDeliveredNotificationsWithCompletionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649520-getdeliverednotifications) method of the shared `UNUserNotificationCenter` object to get a list of notifications still being displayed in Notification Center. If you find any notifications that are now outdated and should not be displayed to the user, you can remove them using the [removeDeliveredNotificationsWithIdentifiers:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649500-removedeliverednotificationswith) method.

[Local and Remote Notifications Overview](index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmznknltc)

[Scheduling and Handling Local Notifications](SchedulingandHandlingLocalNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnjnknltc)
