---
title: Local and Remote Notification Programming Guide
apple_id: TP40008194
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: AppKit
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/HandlingRemoteNotifications.html
archived_at: '2026-07-15T08:19:05.583622Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Local and Remote Notification Programming Guide](index.md)



## Configuring Remote Notification Support

By supporting remote notifications you can provide up-to-date information to users of your app, even when the app is not running. To be able to receive and handle remote notifications, your app must:

1. Enable remote notifications.
2. Register with Apple Push Notification service (APNs) and receive an app-specific device token.
3. Send the device token to your notification provider server.
4. Implement support for handling incoming remote notifications.

This chapter explains these steps, all of which you implement in your app. For more about providers, which are servers that you deploy and manage for building and sending notification requests to APNs—read [APNs Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

> [!NOTE]
> 

### Enabling the Push Notifications Capability

For an app to handle remote notifications, it must have the proper entitlements to talk to APNs. You add this entitlement to your app using the Capabilities pane of your Xcode project, as described in “[Enable push notifications](http://help.apple.com/xcode/mac/current/#/dev11b059073?sub=dev73a37248c)” in Xcode Help.

Apps without required entitlements are rejected during the App Store review process. During testing, trying to register with APNs without the proper entitlement returns an error.

### Registering to Receive Remote Notifications

Each time your app launches, it must register with APNs. The methods to use differ according to the platform, but in all cases it works as follows:

1. Your app asks to be registered with APNs.
2. On successful registration, APNs sends an app-specific device token to the device.
3. The system delivers the device to your app by calling a method in your app delegate.
4. Your app sends the device token to the app’s associated provider.

For code snippets showing these steps, see [Obtaining a Device Token in iOS and tvOS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnrnknlti) and [Obtaining a Device Token in macOS](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnrnknltm).

An app-specific device token is globally unique and identifies one app-device combination. Upon receiving a device token from APNs in your app, it is your responsibility to open a network connection to your provider. It is also your responsibility, in your app, to then forward the device token along with any other relevant data you want to send to the provider. When the provider later sends remote notification requests to APNs, it must include the device token, along with the notification payload. For more on this, see [APNs Overview](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

Never cache device tokens in your app; instead, get them from the system when you need them. APNs issues a new device token to your app when certain events happen. The device token is guaranteed to be different, for example, when a user restores a device from a backup, when the user installs your app on a new device, and when the user reinstalls the operating system. Fetching the token, rather than relying on a cache, ensures that you have the current device token needed for your provider to communicate with APNs. When you attempt to fetch a device token but it has not changed, the fetch method returns quickly.

> [!IMPORTANT]
> 

Apps running on watchOS do not register for remote notifications explicitly. Instead, they rely on their paired iPhone to forward remote notifications for display on the watch. The forwarding of remote notifications happens when the iPhone is locked (or the screen is asleep) and the Apple Watch is on the user’s wrist and unlocked.

For information about the data format for remote notifications and about how to send that data to APNs, see [Communicating with APNs](CommunicatingwithAPNs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjrfvjvomi).

### Obtaining a Device Token in iOS and tvOS

In iOS and tvOS, you initiate APNs registration for your app by calling the [registerForRemoteNotifications](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications) method of the `UIApplication` object. Call this method at launch time as part of your normal startup sequence. The first time your app calls this method, the app object contacts APNs and requests the app-specific device token on your behalf. The system then asynchronously calls one of two following app delegate methods, depending on success or failure:

- On successful issuance of an app-specific device token, the system calls the [application:didRegisterForRemoteNotificationsWithDeviceToken:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622958-application) method. Implement this method to receive the token and forward it to your provider.
- On error, the system calls the [application:didFailToRegisterForRemoteNotificationsWithError:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622962-application) method. Implement this method to respond to APNs registration errors.

> [!IMPORTANT]
> 

After successful APNs registration, the app object contacts APNs only when the device token has changed; otherwise, calling the `registerForRemoteNotifications` method results in a call to the `application:didRegisterForRemoteNotificationsWithDeviceToken:` method which returns the existing token quickly.

> [!NOTE]
> 

Listing 4-1 shows how to fetch the device token for your iOS or tvOS app. The app delegate calls the `registerForRemoteNotifications` method as part of its regular launch-time setup. Upon receiving the device token, the `application:didRegisterForRemoteNotificationsWithDeviceToken:` method forwards it to the app’s associated provider using a custom method. If an error occurs during registration, the app temporarily disables any features related to remote notifications. Those features are reenabled when a valid device token is received.

__Listing 4-1__Registering for remote notifications in iOS

Objective-C

1. `- (void)applicationDidFinishLaunching:(UIApplication *)app {`
2. `// Configure the user interactions first.`
3. `[self configureUserInteractions];`
5. `// Register for remote notifications.`
6. `[[UIApplication sharedApplication] registerForRemoteNotifications];`
7. `}`
9. `// Handle remote notification registration.`
10. `- (void)application:(UIApplication *)app`
11. `didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)devToken {`
12. `// Forward the token to your provider, using a custom method.`
13. `[self enableRemoteNotificationFeatures];`
14. `[self forwardTokenToServer:devTokenBytes];`
15. `}`
17. `- (void)application:(UIApplication *)app`
18. `didFailToRegisterForRemoteNotificationsWithError:(NSError *)err {`
19. `// The token is not currently available.`
20. `NSLog(@"Remote notification support is unavailable due to error: %@", err);`
21. `[self disableRemoteNotificationFeatures];`
22. `}`

Swift

1. `func application(_ application: UIApplication,`
2. `didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {`
3. `// Configure the user interactions first.`
4. `self.configureUserInteractions()`
6. `// Register with APNs`
7. `UIApplication.shared.registerForRemoteNotifications()`
8. `}`
10. `// Handle remote notification registration.`
11. `func application(_ application: UIApplication,`
12. `didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data){`
13. `// Forward the token to your provider, using a custom method.`
14. `self.enableRemoteNotificationFeatures()`
15. `self.forwardTokenToServer(token: deviceToken)`
16. `}`
18. `func application(_ application: UIApplication,`
19. `didFailToRegisterForRemoteNotificationsWithError error: Error) {`
20. `// The token is not currently available.`
21. `print("Remote notification support is unavailable due to error: \(error.localizedDescription)")`
22. `self.disableRemoteNotificationFeatures()`
23. `}`

If a cellular or Wi-Fi connection is not available, neither the [application:didRegisterForRemoteNotificationsWithDeviceToken:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622958-application) method nor the [application:didFailToRegisterForRemoteNotificationsWithError:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1622962-application) method is called. For Wi-Fi connections, this sometimes occurs when the device cannot connect with APNs over the configured port. If this happens, the user can move to another Wi-Fi network that isn’t blocking the required port. On devices with a cellular radio, the user can also wait until the cellular data service becomes available.

In your `application:didFailToRegisterForRemoteNotificationsWithError:` implementation, use the error object to disable any features related to remote notifications. Because notifications are not going to be arriving anyway, it is better to degrade gracefully and avoid any local work needed to facilitate remote notifications. If remote notifications become available later, the app object notifies you by calling your delegate’s `application:didRegisterForRemoteNotificationsWithDeviceToken:` method.

### Obtaining a Device Token in macOS

In macOS, you obtain a device token for your app by calling the [registerForRemoteNotificationTypes:](https://developer.apple.com/documentation/appkit/nsapplication/1428476-registerforremotenotifications) method of the `NSApplication` object. It is recommended that you call this method at launch time as part of your normal startup sequence. The first time your app calls this method, the app object requests the token from APNs. After the initial call, the app object contacts APNs only when the device token changes; otherwise, it returns the existing token quickly.

The app object notifies its delegate asynchronously upon the successful or unsuccessful retrieval of the device token. You use these delegate callbacks to process the device token or to handle any errors that arose. You must implement the following delegate methods to track whether registration was successful:

- Use the [application:didRegisterForRemoteNotificationsWithDeviceToken:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428766-application) to receive the device token and forward it to your provider.
- Use the [application:didFailToRegisterForRemoteNotificationsWithError:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428554-application) to respond to errors.

> [!NOTE]
> 

Listing 4-2 shows how to fetch the device token for your macOS app. The app delegate calls the `registerForRemoteNotificationTypes:` method as part of its regular launch-time setup, passing along the types of interactions that you intend to use. Upon receiving the device token, the `application:didRegisterForRemoteNotificationsWithDeviceToken:` method forwards it to the app’s associated provider using a custom method. If an error occurs during registration, the app temporarily disables any features related to remote notifications. Those features are reenabled when a valid device token is received.

__Listing 4-2__Registering for remote notifications in macOS

Objective-C

1. `- (void)applicationDidFinishLaunching:(NSNotification *)notification {`
2. `// Configure the user interactions first.`
3. `[self configureUserInteractions];`
5. `[NSApp registerForRemoteNotificationTypes:(NSRemoteNotificationTypeAlert | NSRemoteNotificationTypeSound)];`
6. `}`
8. `- (void)application:(NSApplication *)application`
9. `didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {`
10. `// Forward the token to your provider, using a custom method.`
11. `[self forwardTokenToServer:deviceToken];`
12. `}`
14. `- (void)application:(NSApplication *)application`
15. `didFailToRegisterForRemoteNotificationsWithError:(NSError *)error {`
16. `NSLog(@"Remote notification support is unavailable due to error: %@", error);`
17. `[self disableRemoteNotificationFeatures];`
18. `}`

Swift

1. `func applicationDidFinishLaunching(_ aNotification: Notification) {`
2. `// Configure the user interactions first.`
3. `self.configureUserInteractions()`
5. `NSApplication.shared().registerForRemoteNotifications(matching: [.alert, .sound])`
6. `}`
8. `// Handle remote notification registration.`
9. `func application(_ application: NSApplication,`
10. `didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {`
11. `// Forward the token to your provider, using a custom method.`
12. `self.forwardTokenToServer(token: deviceToken)`
13. `}`
15. `func application(_ application: NSApplication,`
16. `didFailToRegisterForRemoteNotificationsWithError error: Error) {`
17. `// The token is not currently available.`
18. `print("Remote notification support is unavailable due to error: \(error.localizedDescription)")`
19. `}`

### Handling Remote Notifications

The User Notifications framework offers a unified API for use in iOS, watchOS, and tvOS apps, and supports most tasks associated with local and remote notifications. Here are some examples of tasks you can perform with this framework:

- If your app is in the foreground, you can receive the notification directly and silence it.
- If your app is in the background or not running:

  - You can respond when the user selects a custom action associated with a notification.
  - You can respond when the user dismisses the notification or launches your app.

Your app receives the payload of a remote notification through its app delegate. When a remote notification arrives, the system handles user interactions normally when the app is in the background. In iOS and tvOS, the system delivers the notification payload to the [application:didReceiveRemoteNotification:fetchCompletionHandler:](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application) method of the app delegate. In macOS, the system delivers the payload to the [application:didReceiveRemoteNotification:](https://developer.apple.com/documentation/appkit/nsapplicationdelegate/1428430-application) method of the app delegate. You can use these methods to examine the payload and perform any related tasks. For example, upon receiving a background update remote notification, you might start downloading new content for your app.

For information about how to handle notifications using the methods of the User Notifications framework, see [Responding to the Delivery of Notifications](SchedulingandHandlingLocalNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnjnknltcna). For information about how to handle notifications in your app delegate, see the _[UIApplicationDelegate Protocol Reference](https://developer.apple.com/documentation/uikit/uiapplicationdelegate)_ or _[NSApplicationDelegate Protocol Reference](https://developer.apple.com/documentation/appkit/nsapplicationdelegate)_ reference.

[Scheduling and Handling Local Notifications](SchedulingandHandlingLocalNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqnjnknltc)

[Modifying and Presenting Notifications](ModifyingNotifications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcojufvbuqmjwfvjvomi)
