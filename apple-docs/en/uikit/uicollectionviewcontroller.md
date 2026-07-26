---
title: UICollectionViewController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcontroller.json'
content_hash: 'sha256:4e8d6cb5df24e618'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UICollectionViewController

<sub>Class</sub>

A view controller that specializes in managing a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UICollectionViewController
```

## Overview

A view controller implements the following behavior:

- If the collection view controller has an assigned nib file or was loaded from a storyboard, it loads its view from the corresponding nib file or storyboard. If you create the collection view controller programmatically, it automatically creates a new unconfigured collection view object, which you can access using the [collectionView](uicollectionviewcontroller/collectionview.md) property.
- When loading a collection view from a storyboard or nib file, the data source and delegate objects for the collection view are obtained from the nib file. If a data source or delegate is not specified, the collection view controller assigns itself to the unspecified role.
- When the collection view is about to appear for the first time, the collection view controller reloads the collection view data. It also clears the current selection every time the view is displayed. You can change this behavior by setting the value of the [clearsSelectionOnViewWillAppear](uicollectionviewcontroller/clearsselectiononviewwillappear.md) property to [false](../swift/false.md).

You create a custom subclass of `UICollectionViewController` for each collection view that you want to manage. When you initialize the controller, using the [- initWithCollectionViewLayout:](<uicollectionviewcontroller/init(collectionviewlayout_).md>) method, you specify the layout the collection view should have. Because the initially created collection view is without dimensions or content, the collection view’s data source and delegate—typically the collection view controller itself—must provide this information.

You may override the [- loadView](<uiviewcontroller/loadview().md>) method or any other superclass method, but if you do, be sure to call `super` in the implementation of your method. If you do not, the collection view controller may not be able to perform all of the tasks needed to maintain the integrity of the collection view.

## Relationships

- **Inherits From**: [UIViewController](uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICollectionViewDataSource](uicollectionviewdatasource.md), [UICollectionViewDelegate](uicollectionviewdelegate.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIScrollViewDelegate](uiscrollviewdelegate.md), [UIStateRestoring](uistaterestoring.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a collection view controller

- [- initWithCollectionViewLayout:](<uicollectionviewcontroller/init(collectionviewlayout_).md>) — Initializes a collection view controller and configures the collection view with the provided layout.
- [- initWithNibName:bundle:](<uicollectionviewcontroller/init(nibname_bundle_).md>) — Returns a newly initialized view controller with the nib file in the specified bundle.
- [- initWithCoder:](<uicollectionviewcontroller/init(coder_).md>) — Creates a collection view controller with the nib file in the specified bundle.

### Getting the collection view

- [collectionView](uicollectionviewcontroller/collectionview.md) — The collection view object managed by this view controller.
- [collectionViewLayout](uicollectionviewcontroller/collectionviewlayout.md) — The layout object used to initialize the collection view controller.

### Configuring the collection view behavior

- [clearsSelectionOnViewWillAppear](uicollectionviewcontroller/clearsselectiononviewwillappear.md) — A Boolean value indicating if the controller clears the selection when the collection view appears.
- [installsStandardGestureForInteractiveMovement](uicollectionviewcontroller/installsstandardgestureforinteractivemovement.md) — A Boolean value indicating whether the collection view controller installs a standard gesture recognizer to drive the reordering process.

### Integrating with a navigation controller

- [useLayoutToLayoutNavigationTransitions](uicollectionviewcontroller/uselayouttolayoutnavigationtransitions.md) — A Boolean that indicates whether the collection view controller coordinates with a navigation controller for transitions.

## See Also

### Content view controllers

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md) — Build a view controller in storyboards, configure it with custom views, and fill those views with your app’s data.
- [Showing and hiding view controllers](showing-and-hiding-view-controllers.md) — Display view controllers using different techniques, and pass data between them during transitions.
- [UIViewController](uiviewcontroller.md) — An object that manages a view hierarchy for your UIKit app.
- [UITableViewController](uitableviewcontroller.md) — A view controller that specializes in managing a table view.
- [UIContentContainer](uicontentcontainer.md) — A set of methods for adapting the contents of your view controllers to size and trait changes.
