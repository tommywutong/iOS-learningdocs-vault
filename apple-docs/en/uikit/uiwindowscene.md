---
title: UIWindowScene
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene.json'
content_hash: 'sha256:32cc67769c3a8846'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWindowScene

<sub>Class</sub>

A scene that manages one or more windows for your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIWindowScene
```

## Overview

A [UIWindowScene](uiwindowscene.md) object manages one instance of your app’s UI, including one or more windows that you display from that scene. The scene object manages the display of your windows on the user’s device, and the life cycle of that scene as the user interacts with it. When the state of the scene changes, the scene object notifies its delegate object, which adopts the [UIWindowSceneDelegate](uiwindowscenedelegate.md) protocol. The scene also posts appropriate notifications to registered observers. Use the delegate object or notification observers to respond to any changes.

Don’t create window scene objects directly. Instead, specify that you want a [UIWindowScene](uiwindowscene.md) object at configuration time by including the class name for the scene in the scene configuration details of your app’s `Info.plist` file. You can also specify the class name when creating a [UISceneConfiguration](uisceneconfiguration.md) object in your app delegate’s [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>) method. When the user interacts with your app, the system creates an appropriate scene object based on the configuration data you provided. To create a scene programmatically, call the [- requestSceneSessionActivation:userActivity:options:errorHandler:](<uiapplication/requestscenesessionactivation(__useractivity_options_errorhandler_).md>) method of [UIApplication](uiapplication.md).

## Relationships

- **Inherits From**: [UIScene](uiscene.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Getting the active windows

- [windows](uiwindowscene/windows.md) — The windows associated with the scene.
- [keyWindow](uiwindowscene/keywindow.md) — The key window associated with the scene.
- [screen](uiwindowscene/screen.md) — The screen that displays the contents of the scene.

### Getting the interface attributes

- [traitCollection](uiwindowscene/traitcollection.md) — The traits that describe the current environment of the scene.
- [sizeRestrictions](uiwindowscene/sizerestrictions.md) — The minimum and maximum size of the app’s windows.
- [UISceneSizeRestrictions](uiscenesizerestrictions.md) — An object that specifies the minimum and maximum sizes for resizable windows.

### Observing trait changes

- [UITraitChangeObservable](uitraitchangeobservable-67e94.md) — A type that calls your code in reaction to changes in the trait environment.

### Overriding trait values

- [traitOverrides](uiwindowscene/traitoverrides-1klo1.md)
- [UITraitOverrides](uitraitoverrides-swift.struct.md) — A mutable container of traits you use to set trait changes for an object and its descendants.

### Providing a PDF version of your scene

- [screenshotService](uiwindowscene/screenshotservice.md) — An object that generates a high-fidelity version of your app’s content.
- [UIScreenshotService](uiscreenshotservice.md) — An object that coordinates the creation of PDF screenshots of an app’s content.

### Sharing content

- [activityItemsConfigurationSource](uiwindowscene/activityitemsconfigurationsource.md) — An object that can provide shareable items for a scene.
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md) — An interface that provides a source for shareable content to fulfill user requests to share current content.

### Determining window behaviors

- [fullScreen](uiwindowscene/isfullscreen.md) — A Boolean value that indicates whether the window scene is full screen or windowed.
- [windowingBehaviors](uiwindowscene/windowingbehaviors.md) — An object that specifies the behaviors of the window.
- [UISceneWindowingBehaviors](uiscenewindowingbehaviors.md) — An object with properties that determine the behavior of a window.

### Working with window geometry

- [effectiveGeometry](uiwindowscene/effectivegeometry.md) — The current values for the window scene’s geometry in system space.
- [- requestGeometryUpdateWithPreferences:errorHandler:](<uiwindowscene/requestgeometryupdate(__errorhandler_).md>) — Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [Geometry](uiwindowscene/geometry.md) — An object that provides geometry information about the window scene.
- [GeometryPreferences](uiwindowscene/geometrypreferences.md) — An abstract superclass for representing window scene geometry preferences.
- [iOS](uiwindowscene/geometrypreferences/ios.md) — An object that represents the geometry preferences for a window scene in an iOS app.
- [Mac](uiwindowscene/geometrypreferences/mac.md) — An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [Vision](uiwindowscene/geometrypreferences/vision.md)
- [UIProposedSceneSizeNoPreference](uiproposedscenesizenopreference.md) — Used as the value for a dimension of a size related preference when wanting to leave it unchanged.

### Working with focus

- [focusSystem](uiwindowscene/focussystem.md) — The focus system that’s responsible for the window scene.

### Getting the status bar configuration

- [statusBarManager](uiwindowscene/statusbarmanager.md) — The current configuration of the status bar.
- [UIStatusBarManager](uistatusbarmanager.md) — An object that describes the configuration of the status bar.

### Configuring a window’s title bar

- [titlebar](uiwindowscene/titlebar.md) — The title bar displayed in a window of a Mac app.
- [UITitlebar](uititlebar.md) — An object that you use to configure the title bar of a window in a Mac app built with Mac Catalyst.

### Configuring the windowing control style

- [WindowingControlStyle](uiwindowscene/windowingcontrolstyle.md) — Describes the placement and style of the system windowing controls for a scene

### Supporting types

- [ActivationAction](uiwindowscene/activationaction.md) — A menu element that requests a window scene.
- [ActivationConfiguration](uiwindowscene/activationconfiguration.md) — An object that provides configuration options for a window scene request.
- [ActivationInteraction](uiwindowscene/activationinteraction.md) — An interaction that facilitates activating a window scene when a user pinches out on the interaction’s view.
- [ActivationRequestOptions](uiwindowscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating a new window scene.
- [UIWindowSceneDestructionRequestOptions](uiwindowscenedestructionrequestoptions.md) — An object that contains information to use when removing a window scene from your app.
- [DismissalAnimation](uiwindowscene/dismissalanimation.md) — Constants that indicate the types of animations available for dismissing a scene’s windows.
- [UIWindowSceneDragInteraction](uiwindowscenedraginteraction.md) — An interaction you add to a view that enables pan gestures to change the containing window scene’s position.
- [ResizingRestrictions](uiwindowscene/resizingrestrictions.md)
- [UIWindowSceneResizingRestrictions](uiwindowsceneresizingrestrictions.md)
- [PresentationStyle](uiwindowscene/presentationstyle.md) — The placement of a window scene relative to other scenes in the workspace. _(deprecated)_

### Deprecated symbols

- [coordinateSpace](uiwindowscene/coordinatespace.md) — The coordinate space occupied by the scene. _(deprecated)_
- [interfaceOrientation](uiwindowscene/interfaceorientation.md) — The orientation to use when displaying content in your windows. _(deprecated)_

### Instance Properties

- [closureConfirmation](uiwindowscene/closureconfirmation.md) — A configuration describing a confirmation dialog to be shown when a user action will result in destruction of the scene session and disconnection of the scene. _(beta)_

### Instance Methods

- [displayLink(action:)](<uiwindowscene/displaylink(action_).md>)
- [- displayLinkWithTarget:selector:](<uiwindowscene/displaylink(target_selector_).md>) — Creates a display link targeting the display associated with this scene. _(beta)_

## See Also

### Window scenes

- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md) — Support side-by-side instances of your app’s interface and create new windows.
- [UIWindowSceneDelegate](uiwindowscenedelegate.md) — Additional methods that you use to manage app-specific tasks occurring in a scene.
- [UIScene](uiscene.md) — An object that represents one instance of your app’s user interface.
- [UISceneDelegate](uiscenedelegate.md) — The core methods you use to respond to life-cycle events occurring within a scene.
