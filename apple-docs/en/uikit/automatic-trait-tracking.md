---
title: Automatic trait tracking
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/automatic-trait-tracking
source_url: 'https://developer.apple.com/documentation/uikit/automatic-trait-tracking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/automatic-trait-tracking.json'
content_hash: 'sha256:a64da2b13aa7f5db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md) · [Multitasking on iPad, Mac, and Apple Vision Pro](multitasking-on-ipad-mac-and-apple-vision-pro.md)

# Automatic trait tracking

<sub>API Collection</sub>

Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.

## Overview

Automatic trait tracking is a UIKit feature that eliminates the need to manually register for trait changes when you use traits in a supported method or closure. This feature reduces the amount of code you need to write and maintain, improves performance, and encourages the best practice of using traits within the scope of the supported APIs. For more information, see [Adapting your app when traits change](adapting-your-app-when-traits-change.md).

Some properties aren’t appropriate to change during [- layoutSubviews](<uiview/layoutsubviews().md>), for example, properties where setting the value has a side-effect of invalidating the view’s layout. Update these properties in a view’s [- updateProperties](<uiview/updateproperties().md>) method, or a view controller’s [- updateProperties](<uiviewcontroller/updateproperties().md>) method. These methods support automatic trait tracking, and automatic observation tracking on objects that use the [Observable()](<../observation/observable().md>) macro. Notify an object of other updates to its properties by calling [- setNeedsUpdateProperties](<uiview/setneedsupdateproperties().md>) on your view, or [- setNeedsUpdateProperties](<uiviewcontroller/setneedsupdateproperties().md>) on your view controller. Force an object to immediately update its properties by calling [- updatePropertiesIfNeeded](<uiview/updatepropertiesifneeded().md>) on your view, or [- updatePropertiesIfNeeded](<uiviewcontroller/updatepropertiesifneeded().md>) on your view controller. For more information on automatically observing property updates, see [Updating views automatically with observation tracking in UIKit](updating-views-automatically-with-observation-tracking-in-uikit.md).

> [!important] Important
> Avoid causing excessive updates by avoiding changes in [- layoutSubviews](<uiview/layoutsubviews().md>) that update properties the object tracks in [- updateProperties](<uiview/updateproperties().md>), or that invalidate the view’s layout.

A complete list of APIs that support automatic trait tracking appears below.

## Topics

### Views

- [- updateProperties](<uiview/updateproperties().md>) — Configures the view’s content and styling properties before layout.
- [- setNeedsUpdateProperties](<uiview/setneedsupdateproperties().md>) — Call to manually request a properties update for the view. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [- updatePropertiesIfNeeded](<uiview/updatepropertiesifneeded().md>) — Forces an immediate properties update for this view (and its view controller, if applicable) and any subviews, including any view controllers or views in its subtree.
- [- layoutSubviews](<uiview/layoutsubviews().md>) — Lays out subviews.
- [- updateConstraints](<uiview/updateconstraints().md>) — Updates constraints for the view.
- [- drawRect:](<uiview/draw(__).md>) — Draws the view’s image within the passed-in rectangle.
- [Properties](uiview/invalidations/properties.md)

### View controllers

- [- updateProperties](<uiviewcontroller/updateproperties().md>) — Configures the view controller’s content and styling properties.
- [- setNeedsUpdateProperties](<uiviewcontroller/setneedsupdateproperties().md>) — Call to manually request a properties update for the view controller. Multiple requests may be coalesced into a single update alongside the next layout pass.
- [- updatePropertiesIfNeeded](<uiviewcontroller/updatepropertiesifneeded().md>) — Forces an immediate properties update for this view controller and its view, including any view controllers and views in this subtree.
- [- viewWillLayoutSubviews](<uiviewcontroller/viewwilllayoutsubviews().md>) — Notifies the view controller that its view is about to lay out its subviews.
- [- viewDidLayoutSubviews](<uiviewcontroller/viewdidlayoutsubviews().md>) — Notifies the view controller when its view finishes laying out its subviews.
- [- updateViewConstraints](<uiviewcontroller/updateviewconstraints().md>) — Notifies the view controller when its view needs to update its constraints.
- [updateContentUnavailableConfiguration(using:)](<uiviewcontroller/updatecontentunavailableconfiguration(using_).md>) — Updates the content-unavailable configuration for the provided state.

### Presentation controllers

- [- containerViewWillLayoutSubviews](<uipresentationcontroller/containerviewwilllayoutsubviews().md>) — Notifies the presentation controller that layout is about to begin on the views of the container view.
- [- containerViewDidLayoutSubviews](<uipresentationcontroller/containerviewdidlayoutsubviews().md>) — Notifies the presentation controller when layout ends on the views of the container view.

### Buttons

- [- updateConfiguration](<uibutton/updateconfiguration().md>) — Updates the button configuration in response to a button state change.
- [configurationUpdateHandler](uibutton/configurationupdatehandler-swift.property.md) — A closure that executes when the button state changes.

### Collection view cells

- [updateConfiguration(using:)](<uicollectionviewcell/updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](uicollectionviewcell/configurationupdatehandler-7rqbu.md) — A block for handling updates to the cell’s configuration using the current state.

### Table view cells

- [updateConfiguration(using:)](<uitableviewcell/updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](uitableviewcell/configurationupdatehandler-974.md) — A block for handling updates to the cell’s configuration using the current state.

### Table view headers and footers

- [updateConfiguration(using:)](<uitableviewheaderfooterview/updateconfiguration(using_).md>) — Updates the view’s configuration using the current state.
- [configurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-49slo.md) — A block for handling updates to the view’s configuration using the current state.

### Collection view compositional layouts

- [UICollectionViewCompositionalLayoutSectionProvider](uicollectionviewcompositionallayoutsectionprovider.md) — A closure that creates and returns each of the layout’s sections.

## See Also

### Adaptivity

- [UITraitCollection](uitraitcollection.md) — A collection of data that represents the environment for an individual element in your app’s user interface.
- [UITraitEnvironment](uitraitenvironment.md) — A set of methods that makes the iOS interface environment available to your app.
- [UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md) — A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [UIContentContainer](uicontentcontainer.md) — A set of methods for adapting the contents of your view controllers to size and trait changes.
