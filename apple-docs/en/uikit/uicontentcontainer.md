---
title: UIContentContainer
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentcontainer
source_url: 'https://developer.apple.com/documentation/uikit/uicontentcontainer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentcontainer.json'
content_hash: 'sha256:0f6a2afc5241e534'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentContainer

<sub>Protocol</sub>

A set of methods for adapting the contents of your view controllers to size and trait changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIContentContainer : NSObjectProtocol
```

## Overview

The methods of this protocol handle size-related transitions that are related to changes in the current trait environment or view controller hierarchy. When the parent view controller changes, or when trait changes occur that affect the size of a view controller, UIKit calls these methods to give the affected objects a chance to respond appropriately.

All [UIViewController](uiviewcontroller.md) and [UIPresentationController](uipresentationcontroller.md) objects provide default implementations for the methods of this protocol. When creating your own custom view controller or presentation controller, you can override the default implementations to make adjustments to your content. For example, you might use these methods to adjust the size or position of any child view controllers.

When overriding the methods of this protocol, call `super` to let UIKit perform any default behaviors. View controllers and presentation controllers perform their own adjustments when these methods are called. Calling `super` ensures that UIKit is able to continue adjusting other parts of your user interface.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UIActivityViewController](uiactivityviewcontroller.md), [UIAlertController](uialertcontroller.md), [UICloudSharingController](uicloudsharingcontroller.md), [UICollectionViewController](uicollectionviewcontroller.md), [UIColorPickerViewController](uicolorpickerviewcontroller.md), [UIDocumentBrowserViewController](uidocumentbrowserviewcontroller.md), [UIDocumentMenuViewController](uidocumentmenuviewcontroller.md), [UIDocumentPickerExtensionViewController](uidocumentpickerextensionviewcontroller.md), [UIDocumentPickerViewController](uidocumentpickerviewcontroller.md), [UIDocumentViewController](uidocumentviewcontroller.md), [UIFontPickerViewController](uifontpickerviewcontroller.md), [UIImagePickerController](uiimagepickercontroller.md), [UIInputViewController](uiinputviewcontroller.md), [UINavigationController](uinavigationcontroller.md), [UIPageViewController](uipageviewcontroller.md), [UIPopoverPresentationController](uipopoverpresentationcontroller.md), [UIPresentationController](uipresentationcontroller.md), [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md), [UISearchContainerViewController](uisearchcontainerviewcontroller.md), [UISearchController](uisearchcontroller.md), [UISheetPresentationController](uisheetpresentationcontroller.md), [UISplitViewController](uisplitviewcontroller.md), [UITabBarController](uitabbarcontroller.md), [UITableViewController](uitableviewcontroller.md), [UITextFormattingViewController](uitextformattingviewcontroller.md), [UIVideoEditorController](uivideoeditorcontroller.md), [UIViewController](uiviewcontroller.md)

## Topics

### Responding to environment changes

- [- viewWillTransitionToSize:withTransitionCoordinator:](<uicontentcontainer/viewwilltransition(to_with_).md>) — Notifies the container that the size of its view is about to change.
- [- willTransitionToTraitCollection:withTransitionCoordinator:](<uicontentcontainer/willtransition(to_with_).md>) — Notifies the container that its trait collection changed.

### Responding to changes in child view controllers

- [- sizeForChildContentContainer:withParentContainerSize:](<uicontentcontainer/size(forchildcontentcontainer_withparentcontainersize_).md>) — Returns the size of the specified child view controller’s content.
- [- preferredContentSizeDidChangeForChildContentContainer:](<uicontentcontainer/preferredcontentsizedidchange(forchildcontentcontainer_).md>) — Notifies an interested controller that the preferred content size of one of its children changed.
- [- systemLayoutFittingSizeDidChangeForChildContentContainer:](<uicontentcontainer/systemlayoutfittingsizedidchange(forchildcontentcontainer_).md>) — Notifies the container that a child view controller was resized using Auto Layout.
- [preferredContentSize](uicontentcontainer/preferredcontentsize.md) — The preferred size for the container’s content.

## See Also

### Content view controllers

- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md) — Build a view controller in storyboards, configure it with custom views, and fill those views with your app’s data.
- [Showing and hiding view controllers](showing-and-hiding-view-controllers.md) — Display view controllers using different techniques, and pass data between them during transitions.
- [UIViewController](uiviewcontroller.md) — An object that manages a view hierarchy for your UIKit app.
- [UITableViewController](uitableviewcontroller.md) — A view controller that specializes in managing a table view.
- [UICollectionViewController](uicollectionviewcontroller.md) — A view controller that specializes in managing a collection view.
