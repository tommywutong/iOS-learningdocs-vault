---
title: UIScene
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene
source_url: 'https://developer.apple.com/documentation/uikit/uiscene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene.json'
content_hash: 'sha256:792c9d3fc84f7f01'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIScene

<sub>Class</sub>

An object that represents one instance of your app’s user interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIScene
```

## Overview

UIKit creates a scene object for each instance of your app’s UI that the user or your app requests. Typically, UIKit creates a [UIWindowScene](uiwindowscene.md) object instead of a [UIScene](uiscene.md) object, but you use the methods and properties of this class to access information about a scene.

Every scene object has an associated delegate object, an object that adopts the [UISceneDelegate](uiscenedelegate.md) protocol. When the state of the scene changes, the scene object notifies its delegate object and posts appropriate notifications to registered observer objects. Use the delegate object and notifications to respond to changes in the state of the scene. For example, use it to determine when your scene moves to the background.

You don’t create scene objects directly. You can programmatically ask UIKit to create a scene object for your app by calling the [- requestSceneSessionActivation:userActivity:options:errorHandler:](<uiapplication/requestscenesessionactivation(__useractivity_options_errorhandler_).md>) method of [UIApplication](uiapplication.md). UIKit also creates scenes in response to user interactions. When configuring your app’s scene support, specify [UIWindowScene](uiwindowscene.md) objects instead of [UIScene](uiscene.md) objects.

## Relationships

- **Inherits From**: [UIResponder](uiresponder.md)

- **Inherited By**: [UIWindowScene](uiwindowscene.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a scene object

- [- initWithSession:connectionOptions:](<uiscene/init(session_connectionoptions_).md>) — Creates a scene object using the specified session and connection information.

### Managing the life cycle of a scene

- [delegate](uiscene/delegate.md) — The object you use to receive life-cycle events associated with the scene.
- [UISceneDelegate](uiscenedelegate.md) — The core methods you use to respond to life-cycle events occurring within a scene.

### Getting the scene attributes

- [activationState](uiscene/activationstate-swift.property.md) — The current execution state of the scene.
- [ActivationState](uiscene/activationstate-swift.enum.md) — Constants that indicate the foreground or background execution state of your app.
- [title](uiscene/title.md) — A user-visible string you supply to help users differentiate among your app’s scenes.
- [subtitle](uiscene/subtitle.md) — A string that the app displays in the title bar of a window when running in macOS.

### Specifying the scene’s activation conditions

- [activationConditions](uiscene/activationconditions.md) — The conditions that define when UIKit activates the scene object.
- [UISceneActivationConditions](uisceneactivationconditions.md) — The set of conditions that define when UIKit activates the current scene.

### Specifying the scene’s destruction conditions

- [destructionConditions](uiscene/destructionconditions-9rfrj.md)

### Responding to life cycle notifications

- [UISceneWillConnectNotification](uiscene/willconnectnotification.md) — A notification that indicates that UIKit added a scene to your app.
- [UISceneDidDisconnectNotification](uiscene/diddisconnectnotification.md) — A notification that indicates that UIKit removed a scene from your app.
- [UISceneWillEnterForegroundNotification](uiscene/willenterforegroundnotification.md) — A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.
- [UISceneDidActivateNotification](uiscene/didactivatenotification.md) — A notification that indicates that the scene is now onscreen and responding to user events.
- [UISceneWillDeactivateNotification](uiscene/willdeactivatenotification.md) — A notification that indicates that the scene is about to resign the active state and stop responding to user events.
- [UISceneDidEnterBackgroundNotification](uiscene/didenterbackgroundnotification.md) — A notification that indicates that the scene is running in the background and is no longer onscreen.

### Working with system protection manager

- [systemProtectionManager](uiscene/systemprotectionmanager-swift.property.md) — The system protection manager associated with this scene.
- [SystemProtectionManager](uiscene/systemprotectionmanager-swift.class.md) — A class that represents the status of system protection for the scene.
- [UISceneSystemProtectionDidChangeNotification](uiscene/systemprotectiondidchangenotification.md) — A notification posted when the system-protection attributes of a scene change.

### Getting the scene’s session

- [session](uiscene/session.md) — The session associated with the scene.
- [UISceneSession](uiscenesession.md) — An object that contains information about one of your app’s scenes.

### Opening URLs

- [- openURL:options:completionHandler:](<uiscene/open(__options_completionhandler_).md>) — Attempts to open the resource at the specified URL asynchronously.
- [OpenExternalURLOptions](uiscene/openexternalurloptions.md) — Options you specify when asking a scene to open a URL.

### Supporting state restoration

- [- completeStateRestoration](<uiscene/completestaterestoration().md>)
- [- extendStateRestoration](<uiscene/extendstaterestoration().md>)

### Getting the pointer lock state

- [pointerLockState](uiscene/pointerlockstate.md) — The pointer lock state for the scene.
- [UIPointerLockState](uipointerlockstate.md) — An object that contains information about a scene’s pointer lock state.

### Constants

- [ActivationRequestOptions](uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
- [UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.
- [OpenURLOptions](uiscene/openurloptions.md) — Options that UIKit provides when asking your app to open a URL.

### Structures

- [DestructionCondition](uiscene/destructioncondition.md)
- [DidActivateMessage](uiscene/didactivatemessage.md)
- [DidEnterBackgroundMessage](uiscene/didenterbackgroundmessage.md)
- [SystemProtectionDidChangeMessage](uiscene/systemprotectiondidchangemessage.md)
- [WillConnectMessage](uiscene/willconnectmessage.md)
- [WillDeactivateMessage](uiscene/willdeactivatemessage.md)
- [WillEnterForegroundMessage](uiscene/willenterforegroundmessage.md)

### Instance Methods

- [- getDefaultAudioSessionWithCompletionHandler:](<uiscene/getdefaultaudiosession(completionhandler_).md>) — Retrieves the audio session that contains all sounds that implicitly belong to this scene.

## See Also

### Window scenes

- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md) — Support side-by-side instances of your app’s interface and create new windows.
- [UIWindowSceneDelegate](uiwindowscenedelegate.md) — Additional methods that you use to manage app-specific tasks occurring in a scene.
- [UIWindowScene](uiwindowscene.md) — A scene that manages one or more windows for your app.
- [UISceneDelegate](uiscenedelegate.md) — The core methods you use to respond to life-cycle events occurring within a scene.
