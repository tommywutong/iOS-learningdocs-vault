---
title: Local and Remote Notification Programming Guide
apple_id: TP40008194
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: AppKit
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SchedulingandHandlingLocalNotifications.html
archived_at: '2026-07-15T08:19:09.574063Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Local and Remote Notification Programming Guide](index.md)



## Scheduling and Handling Local Notifications

Local notifications give you a way to alert the user at times when your app might not be running. You schedule local notifications at a time when your app is running either in the foreground or background. After scheduling a notification, the system takes on the responsibility of delivering the notification to the user at the appropriate time. Your app does not need to be running for the system to deliver the notification.

If your app is not running, or if it is in the background, the system displays local notifications directly to the user. The system can alert the user with an alert panel or banner, with a sound, or by badging your app’s icon. If your app provides a notification content app extension, the system can even use your custom interface to alert the user. If your app is in the foreground when a notification arrives, the system gives your app the opportunity to handle the notification internally.

> [!NOTE]
> 

### Configuring a Local Notification

The steps for configuring a local notification are as follows:

1. Create and configure a [UNMutableNotificationContent](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent) object with the notification details.
2. Create a [UNCalendarNotificationTrigger](https://developer.apple.com/documentation/usernotifications/uncalendarnotificationtrigger), [UNTimeIntervalNotificationTrigger](https://developer.apple.com/documentation/usernotifications/untimeintervalnotificationtrigger), or [UNLocationNotificationTrigger](https://developer.apple.com/documentation/usernotifications/unlocationnotificationtrigger) object to describe the conditions under which the notification is delivered.
3. Create a [UNNotificationRequest](https://developer.apple.com/documentation/usernotifications/unnotificationrequest) object with the content and trigger information.
4. Call the [addNotificationRequest:withCompletionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649508-addnotificationrequest) method to schedule the notification; see [Scheduling Local Notifications for Delivery](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnjnknltk)

When creating the content for a notification, fill in the properties of the `UNMutableNotificationContent` object that reflect the type of interaction you want with the user. For example, fill in the [title](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/1649858-title) and [body](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/1649874-body) properties when you want to display an alert. The system uses the information you provide to determine how to interact with the user. You can also use the data in this object when handling a local notification that has been delivered to your app.

After creating the notification content, create a trigger object that defines when to deliver the notification. The User Notifications framework provides both time-based and location-based triggers. Configure the trigger with the required conditions and use that object plus your content to create the `UNNotificationRequest` object.

Listing 3-1 shows how to create and configure a local notification related to an alarm. The use of a `UNCalendarNotificationTrigger` causes the notification to be delivered at a specific date or time, which in this example is the next time the clock reaches 7:00 in the morning.

__Listing 3-1__Creating and configuring a local notification

Objective-C

1. `UNMutableNotificationContent* content = [[UNMutableNotificationContent alloc] init];`
2. `content.title = [NSString localizedUserNotificationStringForKey:@"Wake up!" arguments:nil];`
3. `content.body = [NSString localizedUserNotificationStringForKey:@"Rise and shine! It's morning time!"`
4. `arguments:nil];`
6. `// Configure the trigger for a 7am wakeup.`
7. `NSDateComponents* date = [[NSDateComponents alloc] init];`
8. `date.hour = 7;`
9. `date.minute = 0;`
10. `UNCalendarNotificationTrigger* trigger = [UNCalendarNotificationTrigger`
11. `triggerWithDateMatchingComponents:date repeats:NO];`
13. `// Create the request object.`
14. `UNNotificationRequest* request = [UNNotificationRequest`
15. `requestWithIdentifier:@"MorningAlarm" content:content trigger:trigger];`

Swift

1. `let content = UNMutableNotificationContent()`
2. `content.title = NSString.localizedUserNotificationString(forKey: "Wake up!", arguments: nil)`
3. `content.body = NSString.localizedUserNotificationString(forKey: "Rise and shine! It's morning time!",`
4. `arguments: nil)`
6. `// Configure the trigger for a 7am wakeup.`
7. `var dateInfo = DateComponents()`
8. `dateInfo.hour = 7`
9. `dateInfo.minute = 0`
10. `let trigger = UNCalendarNotificationTrigger(dateMatching: dateInfo, repeats: false)`
12. `// Create the request object.`
13. `let request = UNNotificationRequest(identifier: "MorningAlarm", content: content, trigger: trigger)`

Providing an identifier for the `UNNotificationRequest` object gives you a way to identify local notifications after they have been scheduled. You can use identifiers to look up pending requests later and to cancel them before they are delivered. For more information on scheduling and canceling requests, see [Scheduling Local Notifications for Delivery](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnjnknltk).

### Assigning Custom Actions to a Local Notification

To display custom actions in the interface for a local notification, assign one of your registered category identifiers to the [categoryIdentifier](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/1649866-categoryidentifier) property of your [UNMutableNotificationContent](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent) object during configuration. The system uses the category information to determine which action buttons, if any, to include in the notification interface. You must assign a value to this property before scheduling the notification request.

Listing 3-2 shows how to specify the category identifier for a local notification. In this example, the “TIMER_EXPIRED” string represents a category that was defined at launch time and that includes two custom actions. The code for registering this category is shown in [Listing 2-3](SupportingNotificationsinYourApp.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnbnknlti).

__Listing 3-2__Defining a category of actions for a local notification

Objective-C

1. `UNNotificationContent *content = [[UNNotificationContent alloc] init];`
2. `// Configure the content. . .`
4. `// Assign the category (and the associated actions).`
5. `content.categoryIdentifier = @"TIMER_EXPIRED";`
7. `// Create the request and schedule the notification.`

Swift

1. `let content = UNMutableNotificationContent()`
2. `// Configure the content. . .`
4. `// Assign the category (and the associated actions).`
5. `content.categoryIdentifier = "TIMER_EXPIRED"`
7. `// Create the request and schedule the notification.`

For information on how to register custom actions with a category, see [Configuring Categories and Actionable Notifications](SupportingNotificationsinYourApp.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnbnknltenq)

### Adding a Sound to the Notification Content

If you want a local notification to play a sound when it is delivered, assign a value to the [sound](https://developer.apple.com/documentation/usernotifications/unmutablenotificationcontent/1649868-sound) property of your `UNMutableNotificationContent` object. You specify sounds using a [UNNotificationSound](https://developer.apple.com/documentation/usernotifications/unnotificationsound) object, which lets you play either a custom sound or the default notification sound. Custom sounds must reside locally on the user’s device before they can be played. Store the sound files for your notifications in your app’s main bundle or download them and store them in the `Library/Sounds` subdirectory of your app’s container directory.

To play the default sound, create the sound file and assign it to your notification content. For example:

Objective-C

1. `content.sound = [UNNotificationSound defaultSound];`

Swift

1. `content.sound = UNNotificationSound.default()`

When specifying custom sounds, specify only the filename of the sound file that you want played. If the system finds a suitable sound file with the name you provided, it plays that sound when delivering the notification. If the system does not find a suitable sound file, it plays the default sound.

Objective-C

1. `content.sound = [UNNotificationSound soundNamed:@"MySound.aiff"];`

Swift

1. `content.sound = UNNotificationSound(named: "MySound.aiff")`

For information about the supported sound file formats, see _[UNNotificationSound Class Reference](https://developer.apple.com/documentation/usernotifications/unnotificationsound)_.

### Scheduling Local Notifications for Delivery

To schedule a local notification for delivery, create your [UNNotificationRequest](https://developer.apple.com/documentation/usernotifications/unnotificationrequest) object and call the [addNotificationRequest:withCompletionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649508-addnotificationrequest) method of `UNUserNotificationCenter`. The system schedules local notifications asynchronously, calling your completion handler block when scheduling is complete or when an error occurs. Listing 3-3 shows how to schedule a local notification for delivery. The code in this example completes the scheduling of the notification created in [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnjnknltm).

__Listing 3-3__Scheduling a local notification for delivery

Objective-C

1. `// Create the request object.`
2. `UNNotificationRequest* request = [UNNotificationRequest`
3. `requestWithIdentifier:@"MorningAlarm" content:content trigger:trigger];`
5. `UNUserNotificationCenter* center = [UNUserNotificationCenter currentNotificationCenter];`
6. `[center addNotificationRequest:request withCompletionHandler:^(NSError * _Nullable error) {`
7. `if (error != nil) {`
8. `NSLog(@"%@", error.localizedDescription);`
9. `}`
10. `}];`

Swift

1. `// Create the request object.`
2. `let request = UNNotificationRequest(identifier: "MorningAlarm", content: content, trigger: trigger)`
4. `// Schedule the request.`
5. `let center = UNUserNotificationCenter.current()`
6. `center.add(request) { (error : Error?) in`
7. `if let theError = error {`
8. `print(theError.localizedDescription)`
9. `}`
10. `}`

Scheduled local notifications remain active until they are unscheduled by the system or until you cancel them explicitly. The system unschedules notifications automatically after they are delivered, unless the notification’s trigger is configured to repeat. To cancel an individual notification before it is delivered, or to cancel a repeating notification, call the [removePendingNotificationRequestsWithIdentifiers:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649517-removependingnotificationrequest) method of `UNUserNotificationCenter`. The notification being canceled must have an [identifier](https://developer.apple.com/documentation/usernotifications/unnotificationrequest/1649634-identifier) assigned to its [UNNotificationRequest](https://developer.apple.com/documentation/usernotifications/unnotificationrequest) object. To cancel all pending local notifications, regardless of whether they have a request identifier, call the [removeAllPendingNotificationRequests](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649509-removeallpendingnotificationrequ) method instead.

### Responding to the Delivery of Notifications

When your app is not running or is in the background, the system automatically delivers local and remote notifications using the interactions you specified. If the user selects an action, or chooses one of the standard interactions, the system notifies your app of the user’s selection. Your code can then use that selection to perform additional tasks. If your app is running in the foreground, notifications are delivered directly to your app. You can then decide whether to handle the notification quietly or alert the user.

To respond to the delivery of notifications, you must implement a delegate for the shared `UNUserNotificationCenter` object. Your delegate object must conform to the [UNUserNotificationCenterDelegate](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) protocol, which the notification center uses to deliver notification information to your app. A delegate is required if your notifications contain custom actions.

> [!IMPORTANT]
> 

For additional information on how to implement your delegate object, see _[UNUserNotificationCenterDelegate Protocol Reference](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate)_.

### Handling Notifications When Your App Is in the Foreground

If a notification arrives while your app is in the foreground, you can silence that notification or tell the system to continue to display the notification interface. The system silences notifications for foreground apps by default, delivering the notification’s data directly to your app. You can use the notification data to update your app’s interface directly. For example, if a new sports score arrived, you would just update that information in your interface.

If you want the system to continue to display the notification interface, provide a delegate object for the `UNUserNotificationCenter` and implement the [userNotificationCenter:willPresentNotification:withCompletionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/1649518-usernotificationcenter) method. Your implementation of this method should still process the notification data. When finished, execute the provided completion handler block with the delivery option (if any) that you want the system to use. If you do not specify any options, the system silences the notification. Listing 3-4 shows a sample implementation of this method that tells the system to play a sound. The notification’s payload identifies which sound to play.

__Listing 3-4__Playing a sound while your app is in the foreground

Objective-C

1. `- (void)userNotificationCenter:(UNUserNotificationCenter *)center`
2. `willPresentNotification:(UNNotification *)notification`
3. `withCompletionHandler:(void (^)(UNNotificationPresentationOptions options))completionHandler {`
4. `// Update the app interface directly.`
6. `// Play a sound.`
7. `completionHandler(UNNotificationPresentationOptionSound);`
8. `}`

Swift

1. `func userNotificationCenter(_ center: UNUserNotificationCenter,`
2. `willPresent notification: UNNotification,`
3. `withCompletionHandler completionHandler: @escaping (UNNotificationPresentationOptions) -> Void) {`
4. `// Update the app interface directly.`
6. `// Play a sound.`
7. `completionHandler(UNNotificationPresentationOptions.sound)`
8. `}`

The system does not call the `userNotificationCenter:willPresentNotification:withCompletionHandler:` method when your app is in the background or is not running. In those cases, the system alerts the user according to the information in the notification itself. You can still determine whether a notification was delivered using the [getDeliveredNotificationsWithCompletionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter/1649520-getdeliverednotifications) method of the `UNUserNotificationCenter` object.

### Responding to the Selection of a Custom Action

When the user selects a custom action from the notification interface, the system notifies your app of the user’s choice. Responses to custom actions are packaged in a [UNNotificationResponse](https://developer.apple.com/documentation/usernotifications/unnotificationresponse) object and delivered to the delegate of your app’s shared [UNUserNotificationCenter](https://developer.apple.com/documentation/usernotifications/unusernotificationcenter) object. To receive responses, your delegate object must implement the [userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/1649501-usernotificationcenter) method. Your implementation of that method must be able to process all of the custom actions supported by your app or app extension.

If your app or app extension is not running when a response is received, the system launches your app or app extension in the background to process the response. Use the provided background time to update your data structures and your app’s interface to reflect the user’s choice. Do not use the time to perform tasks unrelated to the processing of the custom action.

Listing 3-5 shows an implementation of the response handler method for a timer app with multiple categories and custom actions. The implementation uses both the action and the [categoryIdentifier](https://developer.apple.com/documentation/usernotifications/unnotificationcontent/1649866-categoryidentifier) property to determine an appropriate course of action.

__Listing 3-5__Handling a custom notification action

Objective-C

1. `- (void)userNotificationCenter:(UNUserNotificationCenter *)center`
2. `didReceiveNotificationResponse:(UNNotificationResponse *)response`
3. `withCompletionHandler:(void (^)(void))completionHandler {`
4. `if ([response.notification.request.content.categoryIdentifier isEqualToString:@"TIMER_EXPIRED"]) {`
5. `// Handle the actions for the expired timer.`
6. `if ([response.actionIdentifier isEqualToString:@"SNOOZE_ACTION"])`
7. `{`
8. `// Invalidate the old timer and create a new one. . .`
9. `}`
10. `else if ([response.actionIdentifier isEqualToString:@"STOP_ACTION"])`
11. `{`
12. `// Invalidate the timer. . .`
13. `}`
15. `}`
17. `// Else handle actions for other notification types. . .`
18. `}`

Swift

1. `func userNotificationCenter(_ center: UNUserNotificationCenter,`
2. `didReceive response: UNNotificationResponse,`
3. `withCompletionHandler completionHandler: @escaping () -> Void) {`
4. `if response.notification.request.content.categoryIdentifier == "TIMER_EXPIRED" {`
5. `// Handle the actions for the expired timer.`
6. `if response.actionIdentifier == "SNOOZE_ACTION" {`
7. `// Invalidate the old timer and create a new one. . .`
8. `}`
9. `else if response.actionIdentifier == "STOP_ACTION" {`
10. `// Invalidate the timer. . .`
11. `}`
12. `}`
14. `// Else handle actions for other notification types. . .`
15. `}`

### Handling the Standard System Actions

In the system’s notification interface, users can explicitly dismiss the notification interface or launch your app instead of selecting one of your custom actions. Dismissing the interface involves tapping an applicable button or closing the interface directly; ignoring a notification or flicking a notification banner away does not represent an explicit dismissal. When system actions are triggered, the user notification center reports them to the [userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/1649501-usernotificationcenter) method its delegate. The response object passed to that method contains one of the following action identifiers:

- [UNNotificationDismissActionIdentifier](https://developer.apple.com/documentation/usernotifications/unnotificationdismissactionidentifier) lets you know that the user explicitly dismissed the notification interface without selecting a custom action.
- [UNNotificationDefaultActionIdentifier](https://developer.apple.com/documentation/usernotifications/unnotificationdefaultactionidentifier) lets you know that the user launched your app without selecting a custom action.

You handle the standard system actions in the same way that you handle other actions. Listing 3-6 shows a template for the [userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate/1649501-usernotificationcenter) method that checks for these special actions.

__Listing 3-6__Handling the standard system actions

Objective-C

1. `- (void)userNotificationCenter:(UNUserNotificationCenter *)center`
2. `didReceiveNotificationResponse:(UNNotificationResponse *)response`
3. `withCompletionHandler:(void (^)(void))completionHandler {`
4. `if ([response.actionIdentifier isEqualToString:UNNotificationDismissActionIdentifier]) {`
5. `// The user dismissed the notification without taking action.`
6. `}`
7. `else if ([response.actionIdentifier isEqualToString:UNNotificationDefaultActionIdentifier]) {`
8. `// The user launched the app.`
9. `}`
11. `// Else handle any custom actions. . .`
12. `}`

Swift

1. `func userNotificationCenter(_ center: UNUserNotificationCenter,`
2. `didReceive response: UNNotificationResponse,`
3. `withCompletionHandler completionHandler: @escaping () -> Void) {`
4. `if response.actionIdentifier == UNNotificationDismissActionIdentifier {`
5. `// The user dismissed the notification without taking action`
6. `}`
7. `else if response.actionIdentifier == UNNotificationDefaultActionIdentifier {`
8. `// The user launched the app`
9. `}`
11. `// Else handle any custom actions. . .`
12. `}`

[Managing Your App’s Notification Support](SupportingNotificationsinYourApp.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnbnknltc)

[Configuring Remote Notification Support](HandlingRemoteNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnrnknltc)
