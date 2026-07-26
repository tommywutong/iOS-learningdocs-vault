---
title: UIActivityViewController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactivityviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityviewcontroller.json'
content_hash: 'sha256:be34455e3cd6b490'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActivityViewController

<sub>Class</sub>

A view controller that you use to offer standard services from your app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIActivityViewController
```

## Overview

The system provides several standard services, such as copying items to the pasteboard, posting content to social media sites, sending items via email or SMS, and more. Apps can also define custom services.

Your app is responsible for configuring, presenting, and dismissing this view controller. Configuration for the view controller involves specifying the data objects on which the view controller should act. (You can also specify the list of custom services your app supports.) When presenting the view controller, you must do so using the appropriate means for the current device. On iPad, you must present the view controller in a popover. On iPhone and iPod touch, you must present it modally.

## Relationships

- **Inherits From**: [UIViewController](uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIStateRestoring](uistaterestoring.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Initializing the activity view controller

- [- initWithActivityItems:applicationActivities:](<uiactivityviewcontroller/init(activityitems_applicationactivities_).md>) — Initializes a new activity view controller object that acts on the specified data.
- [- initWithActivityItemsConfiguration:](<uiactivityviewcontroller/init(activityitemsconfiguration_).md>) — Initializes a new activity view controller object that acts on the specified configuration.
- [UIActivityItemsConfiguration](uiactivityitemsconfiguration.md) — A configuration that allows a responder to export data through a variety of interactions.
- [UIActivityItemsConfigurationReading](uiactivityitemsconfigurationreading.md) — A set of methods adopted by an object so that the object can act as an activity items configuration.

### Accessing the completion handler

- [completionWithItemsHandler](uiactivityviewcontroller/completionwithitemshandler-swift.property.md) — The completion handler to execute after the activity view controller is dismissed.
- [CompletionWithItemsHandler](uiactivityviewcontroller/completionwithitemshandler-swift.typealias.md) — A completion handler to execute after the activity view controller is dismissed.

### Excluding specific activity types

- [excludedActivityTypes](uiactivityviewcontroller/excludedactivitytypes.md) — The list of services that should not be displayed.

### Excluding specific sections

- [excludedActivitySectionTypes](uiactivityviewcontroller/excludedactivitysectiontypes.md) — Hides some sections of the activity view controller. Default is none
- [UIActivitySectionTypes](uiactivitysectiontypes.md)

### Elevating a prominent activity

- [allowsProminentActivity](uiactivityviewcontroller/allowsprominentactivity.md) — A Boolean value the system uses to elevate a system activity to make it more prominent.

### Deprecated

- [completionHandler](uiactivityviewcontroller/completionhandler-swift.property.md) — The completion handler to execute after the activity view controller is dismissed. _(deprecated)_
- [CompletionHandler](uiactivityviewcontroller/completionhandler-swift.typealias.md) — A completion handler to execute after the activity view controller is dismissed. _(deprecated)_

## See Also

### Services

- [UIActivity](uiactivity.md) — An abstract class that you subclass to implement app-specific services.
- [UIActivityItemSource](uiactivityitemsource.md) — A set of methods that an activity view controller uses to retrieve the data items to act on.
- [UIActivityItemProvider](uiactivityitemprovider.md) — A proxy for data that passes to an activity view controller.
