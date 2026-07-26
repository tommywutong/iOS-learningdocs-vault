---
title: UIApplicationDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplicationdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate.json'
content_hash: 'sha256:761fe8bf06bf870d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIApplicationDelegate

<sub>Protocol</sub>

A set of methods to manage shared behaviors for your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIApplicationDelegate : NSObjectProtocol
```

## Overview

Your app delegate object manages your app’s shared behaviors. The app delegate is effectively the root object of your app, and it works in conjunction with [UIApplication](uiapplication.md) to manage some interactions with the system. Like the [UIApplication](uiapplication.md) object, UIKit creates your app delegate object early in your app’s launch cycle so it’s always present.

Use your app delegate object to handle the following tasks:

- Initializing your app’s central data structures
- Configuring your app’s scenes
- Responding to notifications originating from outside the app, such as low-memory warnings, download completion notifications, and more
- Responding to events that target the app itself, and aren’t specific to your app’s scenes, views, or view controllers
- Registering for any required services at launch time, such as Apple Push Notification service

For more information about how you use the app delegate object to initialize your app at launch time, see [Responding to the launch of your app](responding-to-the-launch-of-your-app.md).

### Life-cycle management in iOS 12 and earlier

In iOS 12 and earlier, you use your app delegate to manage major life cycle events in your app. Specifically, you use methods of the app delegate to update the state of your app when it enters the foreground or moves to the background.

- For information on what to do when your app enters the foreground, see [Preparing your UI to run in the foreground](preparing-your-ui-to-run-in-the-foreground.md).
- For information on what to do when your app enters the background, see [Preparing your UI to run in the background](preparing-your-ui-to-run-in-the-background.md).
- For general information about the life cycle of your app, see [Managing your app’s life cycle](managing-your-app-s-life-cycle.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing the app

- [- application:willFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__willfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process has begun.
- [- application:didFinishLaunchingWithOptions:](<uiapplicationdelegate/application(__didfinishlaunchingwithoptions_).md>) — Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [LaunchOptionsKey](uiapplication/launchoptionskey.md) — The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.
- [UIApplicationDidFinishLaunchingNotification](uiapplication/didfinishlaunchingnotification.md) — A notification that posts immediately after the app finishes launching.

### Configuring and discarding scenes

- [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>) — Retrieves the configuration data for UIKit to use when creating a new scene.
- [- application:didDiscardSceneSessions:](<uiapplicationdelegate/application(__diddiscardscenesessions_).md>) — Tells the delegate that the user closed one or more of the app’s scenes from the app switcher.

### Responding to app life-cycle events

- [- applicationDidBecomeActive:](<uiapplicationdelegate/applicationdidbecomeactive(__).md>) — Tells the delegate that the app has become active. _(deprecated)_
- [- applicationWillResignActive:](<uiapplicationdelegate/applicationwillresignactive(__).md>) — Tells the delegate that the app is about to become inactive. _(deprecated)_
- [- applicationDidEnterBackground:](<uiapplicationdelegate/applicationdidenterbackground(__).md>) — Tells the delegate that the app is now in the background.
- [- applicationWillEnterForeground:](<uiapplicationdelegate/applicationwillenterforeground(__).md>) — Tells the delegate that the app is about to enter the foreground. _(deprecated)_
- [- applicationWillTerminate:](<uiapplicationdelegate/applicationwillterminate(__).md>) — Tells the delegate when the app is about to terminate.
- [UIApplicationDidBecomeActiveNotification](uiapplication/didbecomeactivenotification.md) — A notification that posts when the app becomes active.
- [UIApplicationDidEnterBackgroundNotification](uiapplication/didenterbackgroundnotification.md) — A notification that posts when the app enters the background.
- [UIApplicationWillEnterForegroundNotification](uiapplication/willenterforegroundnotification.md) — A notification that posts shortly before an app leaves the background state on its way to becoming the active app.
- [UIApplicationWillResignActiveNotification](uiapplication/willresignactivenotification.md) — A notification that posts when the app is no longer active and loses focus.
- [UIApplicationWillTerminateNotification](uiapplication/willterminatenotification.md) — A notification that posts when the app is about to terminate.

### Responding to environment changes

- [- applicationProtectedDataDidBecomeAvailable:](<uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(__).md>) — Tells the delegate that protected files are available now.
- [- applicationProtectedDataWillBecomeUnavailable:](<uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(__).md>) — Tells the delegate that the protected files are about to become unavailable.
- [- applicationDidReceiveMemoryWarning:](<uiapplicationdelegate/applicationdidreceivememorywarning(__).md>) — Tells the delegate when the app receives a memory warning from the system.
- [- applicationSignificantTimeChange:](<uiapplicationdelegate/applicationsignificanttimechange(__).md>) — Tells the delegate when there is a significant change in the time.
- [UIApplicationProtectedDataDidBecomeAvailable](uiapplication/protecteddatadidbecomeavailablenotification.md) — A notification that posts when the protected files become available for your code to access.
- [UIApplicationProtectedDataWillBecomeUnavailable](uiapplication/protecteddatawillbecomeunavailablenotification.md) — A notification that posts shortly before protected files are locked down and become inaccessible.
- [UIApplicationDidReceiveMemoryWarningNotification](uiapplication/didreceivememorywarningnotification.md) — A notification that posts when the app receives a warning from the operating system about low memory availability.
- [UIApplicationSignificantTimeChangeNotification](uiapplication/significanttimechangenotification.md) — A notification that posts when there’s a significant change in time.

### Managing app state restoration

- [- application:shouldSaveSecureApplicationState:](<uiapplicationdelegate/application(__shouldsavesecureapplicationstate_).md>) — Asks the delegate whether to securely preserve the app’s state.
- [- application:shouldRestoreSecureApplicationState:](<uiapplicationdelegate/application(__shouldrestoresecureapplicationstate_).md>) — Asks the delegate whether to restore the app’s saved state.
- [- application:viewControllerWithRestorationIdentifierPath:coder:](<uiapplicationdelegate/application(__viewcontrollerwithrestorationidentifierpath_coder_).md>) — Asks the delegate to provide the specified view controller.
- [- application:willEncodeRestorableStateWithCoder:](<uiapplicationdelegate/application(__willencoderestorablestatewith_).md>) — Tells your delegate to save any high-level state information at the beginning of the state preservation process.
- [- application:didDecodeRestorableStateWithCoder:](<uiapplicationdelegate/application(__diddecoderestorablestatewith_).md>) — Tells your delegate to restore any high-level state information as part of the state restoration process.
- [UIApplicationStateRestorationBundleVersionKey](uiapplication/staterestorationbundleversionkey.md) — The version of your app responsible for creating the restoration archive.
- [UIApplicationStateRestorationSystemVersionKey](uiapplication/staterestorationsystemversionkey.md) — The version of the system on which your app created the restoration archive.
- [UIApplicationStateRestorationTimestampKey](uiapplication/staterestorationtimestampkey.md) — The time your app created the restoration archive.
- [UIApplicationStateRestorationUserInterfaceIdiomKey](uiapplication/staterestorationuserinterfaceidiomkey.md) — The user interface idiom that was in effect when your app created the restoration archive.
- [UIStateRestorationViewControllerStoryboardKey](uiapplication/staterestorationviewcontrollerstoryboardkey.md) — A reference to the storyboard that contains the view controller.

### Downloading data in the background

- [- application:handleEventsForBackgroundURLSession:completionHandler:](<uiapplicationdelegate/application(__handleeventsforbackgroundurlsession_completionhandler_).md>) — Tells the delegate that events related to a URL session are waiting to be processed.
- [UIBackgroundFetchResult](uibackgroundfetchresult.md) — Constants that indicate the result of a background fetch operation.

### Handling remote notification registration

- [- application:didRegisterForRemoteNotificationsWithDeviceToken:](<uiapplicationdelegate/application(__didregisterforremotenotificationswithdevicetoken_).md>) — Tells the delegate that the app successfully registered with Apple Push Notification service (APNs).
- [- application:didFailToRegisterForRemoteNotificationsWithError:](<uiapplicationdelegate/application(__didfailtoregisterforremotenotificationswitherror_).md>) — Tells the delegate when Apple Push Notification service cannot successfully complete the registration process.
- [- application:didReceiveRemoteNotification:fetchCompletionHandler:](<uiapplicationdelegate/application(__didreceiveremotenotification_fetchcompletionhandler_).md>) — Tells the app that a remote notification arrived that indicates there is data to be fetched.

### Continuing user activity and handling quick actions

- [- application:willContinueUserActivityWithType:](<uiapplicationdelegate/application(__willcontinueuseractivitywithtype_).md>) — Tells the delegate if your app takes responsibility for notifying users when a continuation activity takes longer than expected. _(deprecated)_
- [- application:continueUserActivity:restorationHandler:](<uiapplicationdelegate/application(__continue_restorationhandler_).md>) — Tells the delegate that the data for continuing an activity is available. _(deprecated)_
- [- application:didUpdateUserActivity:](<uiapplicationdelegate/application(__didupdate_).md>) — Tells the delegate that the activity was updated. _(deprecated)_
- [- application:didFailToContinueUserActivityWithType:error:](<uiapplicationdelegate/application(__didfailtocontinueuseractivitywithtype_error_).md>) — Tells the delegate that the activity couldn’t be continued. _(deprecated)_
- [- application:performActionForShortcutItem:completionHandler:](<uiapplicationdelegate/application(__performactionfor_completionhandler_).md>) — Tells the delegate that the user selected a Home screen quick action for your app, except when you’ve intercepted the interaction in a launch method. _(deprecated)_

### Interacting with WatchKit

- [- application:handleWatchKitExtensionRequest:reply:](<uiapplicationdelegate/application(__handlewatchkitextensionrequest_reply_).md>) — Asks the delegate to respond to a request from a paired watchOS app.

### Interacting with HealthKit

- [- applicationShouldRequestHealthAuthorization:](<uiapplicationdelegate/applicationshouldrequesthealthauthorization(__).md>) — Tells the delegate when your app should ask the user for access to his or her HealthKit data.

### Opening a URL-specified resource

- [- application:openURL:options:](<uiapplicationdelegate/application(__open_options_).md>) — Asks the delegate to open a resource specified by a URL, and provides a dictionary of launch options. _(deprecated)_
- [OpenURLOptionsKey](uiapplication/openurloptionskey.md) — Keys you use to access values in the options dictionary when opening a URL. _(deprecated)_

### Disallowing specified app extension types

- [- application:shouldAllowExtensionPointIdentifier:](<uiapplicationdelegate/application(__shouldallowextensionpointidentifier_).md>) — Asks the delegate to grant permission to use app extensions that are based on a specified extension point identifier.
- [ExtensionPointIdentifier](uiapplication/extensionpointidentifier.md) — A structure that identifies types of extensions.
- [UIApplicationKeyboardExtensionPointIdentifier](uiapplication/extensionpointidentifier/keyboard.md) — The identifier for custom keyboards.

### Handling SiriKit intents

- [- application:handlerForIntent:](<uiapplicationdelegate/application(__handlerfor_).md>) — Asks the delegate for an intent handler capable of handling the specified intent.

### Handling CloudKit invitations

- [- application:userDidAcceptCloudKitShareWithMetadata:](<uiapplicationdelegate/application(__userdidacceptcloudkitsharewith_).md>) — Tells the delegate that the app now has access to shared information in CloudKit. _(deprecated)_

### Localizing keyboard shortcuts

- [- applicationShouldAutomaticallyLocalizeKeyCommands:](<uiapplicationdelegate/applicationshouldautomaticallylocalizekeycommands(__).md>) — Returns a Boolean value that tells the system whether to remap menu shortcuts to support localized keyboards.

### Managing interface geometry

- [- application:supportedInterfaceOrientationsForWindow:](<uiapplicationdelegate/application(__supportedinterfaceorientationsfor_).md>) — Asks the delegate for the interface orientations to use for the view controllers in the specified window. _(deprecated)_
- [UIInterfaceOrientation](uiinterfaceorientation.md) — Constants that specify the orientation of the app’s user interface.
- [UIInterfaceOrientationMask](uiinterfaceorientationmask.md) — Constants that specify a view controller’s supported interface orientations.
- [UIApplicationInvalidInterfaceOrientationException](uiapplication/invalidinterfaceorientationexception.md) — An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.

### Providing a window for storyboarding

- [window](uiapplicationdelegate/window.md) — The window to use when presenting a storyboard.

### Providing the main entry point

- [main()](<uiapplicationdelegate/main().md>) — Provides the top-level entry point for the app.

### Deprecated

- [- applicationDidFinishLaunching:](<uiapplicationdelegate/applicationdidfinishlaunching(__).md>) — Tells the delegate when the app has finished launching. _(deprecated)_
- [Deprecated symbols](uiapplicationdelegate-deprecated-symbols.md) — Symbols that are no longer supported.

## See Also

### Life cycle

- [Managing your app’s life cycle](managing-your-app-s-life-cycle.md) — Respond to system notifications when your app is in the foreground or background, and handle other significant system-related events.
- [Responding to the launch of your app](responding-to-the-launch-of-your-app.md) — Initialize your app’s data structures, prepare your app to run, and respond to any launch-time requests from the system.
- [UIApplication](uiapplication.md) — The centralized point of control and coordination for apps running in iOS.
- [Scenes](scenes.md) — Manage multiple instances of your app’s UI simultaneously, and direct resources to the appropriate instance of your UI.
- [Transitioning to the UIKit scene-based life cycle](transitioning-to-the-uikit-scene-based-life-cycle.md) — Adopt the scene-based life cycle to replace the app delegate life cycle in UIKit.
