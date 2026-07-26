---
title: Automatic observation tracking
framework: UIKit
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/automatic-observation-tracking
source_url: 'https://developer.apple.com/documentation/uikit/automatic-observation-tracking'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/automatic-observation-tracking.json'
content_hash: 'sha256:0c48b8ab1dc89057'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md)

# Automatic observation tracking

<sub>API Collection</sub>

Simplify updating views when data changes by making updates in methods that support automatic observation tracking.

## Overview

Use automatic observation tracking to update your views in response to model object changes without manually invalidating views. Mark your model classes with the [Observable](../observation/observable.md) macro, then read model properties in methods like [- updateProperties](<uiview/updateproperties().md>) or [- layoutSubviews](<uiview/layoutsubviews().md>). UIKit tracks which properties you access and automatically calls these methods again when those properties change. This approach eliminates the need to manually call methods like [- setNeedsLayout](<uiview/setneedslayout().md>) or [- setNeedsDisplay](<uiview/setneedsdisplay().md>) after updating model data, reducing opportunities for bugs and outdated displays.

These methods support automatic observation tracking in views, view controllers, presentation controllers, buttons, collection view cells, table view cells, and table view headers and footers. For more information, see [Updating views automatically with observation tracking in UIKit](updating-views-automatically-with-observation-tracking-in-uikit.md).

## Topics

### Observing data in views

- [- updateProperties](<uiview/updateproperties().md>) — Configures the view’s content and styling properties before layout.
- [- layoutSubviews](<uiview/layoutsubviews().md>) — Lays out subviews.
- [- updateConstraints](<uiview/updateconstraints().md>) — Updates constraints for the view.
- [- drawRect:](<uiview/draw(__).md>) — Draws the view’s image within the passed-in rectangle.

### Observing data in view controllers

- [- updateProperties](<uiviewcontroller/updateproperties().md>) — Configures the view controller’s content and styling properties.
- [- viewWillLayoutSubviews](<uiviewcontroller/viewwilllayoutsubviews().md>) — Notifies the view controller that its view is about to lay out its subviews.
- [- viewDidLayoutSubviews](<uiviewcontroller/viewdidlayoutsubviews().md>) — Notifies the view controller when its view finishes laying out its subviews.
- [- updateViewConstraints](<uiviewcontroller/updateviewconstraints().md>) — Notifies the view controller when its view needs to update its constraints.
- [updateContentUnavailableConfiguration(using:)](<uiviewcontroller/updatecontentunavailableconfiguration(using_).md>) — Updates the content-unavailable configuration for the provided state.

### Observing data in presentation controllers

- [- containerViewWillLayoutSubviews](<uipresentationcontroller/containerviewwilllayoutsubviews().md>) — Notifies the presentation controller that layout is about to begin on the views of the container view.
- [- containerViewDidLayoutSubviews](<uipresentationcontroller/containerviewdidlayoutsubviews().md>) — Notifies the presentation controller when layout ends on the views of the container view.

### Observing data in buttons

- [- updateConfiguration](<uibutton/updateconfiguration().md>) — Updates the button configuration in response to a button state change.
- [configurationUpdateHandler](uibutton/configurationupdatehandler-swift.property.md) — A closure that executes when the button state changes.

### Observing data in collection view cells

- [updateConfiguration(using:)](<uicollectionviewcell/updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](uicollectionviewcell/configurationupdatehandler-7rqbu.md) — A block for handling updates to the cell’s configuration using the current state.

### Observing data in table view cells

- [updateConfiguration(using:)](<uitableviewcell/updateconfiguration(using_).md>) — Updates the cell’s configuration using the current state.
- [configurationUpdateHandler](uitableviewcell/configurationupdatehandler-974.md) — A block for handling updates to the cell’s configuration using the current state.

### Observing data in table header and footer views

- [updateConfiguration(using:)](<uitableviewheaderfooterview/updateconfiguration(using_).md>) — Updates the view’s configuration using the current state.
- [configurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-49slo.md) — A block for handling updates to the view’s configuration using the current state.

### Observing data in collection view layouts

- [UICollectionViewCompositionalLayoutSectionProvider](uicollectionviewcompositionallayoutsectionprovider.md) — A closure that creates and returns each of the layout’s sections.
- [- initWithSectionProvider:](<uicollectionviewcompositionallayout/init(sectionprovider_).md>) — Creates a compositional layout object with a section provider to supply the layout’s sections.
- [- initWithSectionProvider:configuration:](<uicollectionviewcompositionallayout/init(sectionprovider_configuration_).md>) — Creates a compositional layout object with a section provider and an additional configuration.

## See Also

### Data observation

- [Updating views automatically with observation tracking in UIKit](updating-views-automatically-with-observation-tracking-in-uikit.md) — Use Swift Observation and automatic tracking to update your views in response to model data updates.
