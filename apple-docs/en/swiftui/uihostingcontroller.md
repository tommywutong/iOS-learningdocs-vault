---
title: UIHostingController
framework: SwiftUI
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, tvOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/uihostingcontroller
source_url: 'https://developer.apple.com/documentation/swiftui/uihostingcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/uihostingcontroller.json'
content_hash: 'sha256:da66d02a8d864923'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# UIHostingController

<sub>Class</sub>

A UIKit view controller that manages a SwiftUI view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency class UIHostingController<Content> where Content : View
```

## Overview

Create a `UIHostingController` object when you want to integrate SwiftUI views into a UIKit view hierarchy. At creation time, specify the SwiftUI view you want to use as the root view for this view controller; you can change that view later using the [rootView](uihostingcontroller/rootview.md) property. Use the hosting controller like you would any other view controller, by presenting it or embedding it as a child view controller in your interface.

## Relationships

- **Inherits From**: [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Creating a hosting controller object

- [init(rootView:)](<uihostingcontroller/init(rootview_).md>) — Creates a hosting controller object that wraps the specified SwiftUI view.
- [init(coder:rootView:)](<uihostingcontroller/init(coder_rootview_).md>) — Creates a hosting controller object from an archive and the specified SwiftUI view.
- [init(coder:)](<uihostingcontroller/init(coder_).md>) — Creates a hosting controller object from the contents of the specified archive.

### Responding to view-related events

- [loadView()](<uihostingcontroller/loadview().md>)
- [viewWillAppear(_:)](<uihostingcontroller/viewwillappear(__).md>) — Notifies the view controller that its view is about to be added to a view hierarchy.
- [viewDidAppear(_:)](<uihostingcontroller/viewdidappear(__).md>) — Notifies the view controller that its view has been added to a view hierarchy.
- [viewWillDisappear(_:)](<uihostingcontroller/viewwilldisappear(__).md>) — Notifies the view controller that its view will be removed from a view hierarchy.
- [viewDidDisappear(_:)](<uihostingcontroller/viewdiddisappear(__).md>)
- [willMove(toParent:)](<uihostingcontroller/willmove(toparent_).md>)
- [didMove(toParent:)](<uihostingcontroller/didmove(toparent_).md>)
- [viewWillTransition(to:with:)](<uihostingcontroller/viewwilltransition(to_with_).md>)
- [viewWillLayoutSubviews()](<uihostingcontroller/viewwilllayoutsubviews().md>)
- [target(forAction:withSender:)](<uihostingcontroller/target(foraction_withsender_).md>)
- [rootView](uihostingcontroller/rootview.md) — The root view of the SwiftUI view hierarchy managed by this view controller.

### Checking for modality

- [isModalInPresentation](uihostingcontroller/ismodalinpresentation.md)

### Managing the size

- [sizingOptions](uihostingcontroller/sizingoptions.md) — The options for how the hosting controller tracks changes to the size of its SwiftUI content.
- [preferredContentSizeDidChange(forChildContentContainer:)](<uihostingcontroller/preferredcontentsizedidchange(forchildcontentcontainer_).md>)
- [sizeThatFits(in:)](<uihostingcontroller/sizethatfits(in_).md>) — Calculates and returns the most appropriate size for the current view.
- [safeAreaRegions](uihostingcontroller/safearearegions.md) — The safe area regions that this view controller adds to its view.

### Configuring the status bar

- [preferredStatusBarStyle](uihostingcontroller/preferredstatusbarstyle.md) — The preferred status bar style for the view controller.
- [preferredStatusBarUpdateAnimation](uihostingcontroller/preferredstatusbarupdateanimation.md) — The animation style to use when hiding or showing the status bar for this view controller.
- [prefersStatusBarHidden](uihostingcontroller/prefersstatusbarhidden.md) — A Boolean value that indicates whether the view controller prefers the status bar to be hidden or shown.
- [childForStatusBarStyle](uihostingcontroller/childforstatusbarstyle.md)
- [childForStatusBarHidden](uihostingcontroller/childforstatusbarhidden.md)

### Configuring the home indicator

- [prefersHomeIndicatorAutoHidden](uihostingcontroller/prefershomeindicatorautohidden.md) — A Boolean value that indicates whether the view controller prefers the home indicator to be hidden or shown.
- [childForHomeIndicatorAutoHidden](uihostingcontroller/childforhomeindicatorautohidden.md)

### Configuring the interface appearance

- [preferredUserInterfaceStyle](uihostingcontroller/preferreduserinterfacestyle.md) — The preferred interface style for this view controller.
- [preferredScreenEdgesDeferringSystemGestures](uihostingcontroller/preferredscreenedgesdeferringsystemgestures.md) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [childForScreenEdgesDeferringSystemGestures](uihostingcontroller/childforscreenedgesdeferringsystemgestures.md)

### Accessing the available key commands

- [keyCommands](uihostingcontroller/keycommands.md)

### Managing undo

- [undoManager](uihostingcontroller/undomanager.md)

### Instance Properties

- [childViewControllerForPreferredContainerBackgroundStyle](uihostingcontroller/childviewcontrollerforpreferredcontainerbackgroundstyle.md)
- [preferredContainerBackgroundStyle](uihostingcontroller/preferredcontainerbackgroundstyle.md)

### Instance Methods

- [addChild(_:)](<uihostingcontroller/addchild(__).md>)
- [canPerformAction(_:withSender:)](<uihostingcontroller/canperformaction(__withsender_).md>)

## See Also

### Displaying SwiftUI views in UIKit

- [Using SwiftUI with UIKit](../uikit/using-swiftui-with-uikit.md) — Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](unifying-your-app-s-animations.md) — Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [UIHostingControllerSizingOptions](uihostingcontrollersizingoptions.md) — Options for how a hosting controller tracks its content’s size.
- [UIHostingConfiguration](uihostingconfiguration.md) — A content configuration suitable for hosting a hierarchy of SwiftUI views.
- [UIHostingSceneDelegate](uihostingscenedelegate.md) — Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.
