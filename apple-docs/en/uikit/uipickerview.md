---
title: UIPickerView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipickerview
source_url: 'https://developer.apple.com/documentation/uikit/uipickerview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipickerview.json'
content_hash: 'sha256:871ec92546700a1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPickerView

<sub>Class</sub>

A view that uses a spinning-wheel or slot-machine metaphor to show one or more sets of values.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPickerView
```

## Overview

A picker view displays one or more wheels that the user manipulates to select items. Each wheel — known as a _component_ — has a series of indexed rows representing the selectable items. Each row displays a string or view so that the user can identify the item on that row. Users select items by rotating the wheels to the desired values, which align with a selection indicator.

> [!note] Note
> The [UIDatePicker](uidatepicker.md) class uses a custom subclass of [UIPickerView](uipickerview.md) to display dates and times. To see an example, tap the add (”+”) button in the Alarm pane of the Clock app.

You provide the data to display in your picker view using a picker data source (an object that adopts the [UIPickerViewDataSource](uipickerviewdatasource.md) protocol). Use your picker view delegate (an object that adopts the [UIPickerViewDelegate](uipickerviewdelegate.md) protocol) to provide views for displaying your data and responding to user selections.

> [!important] Important
> [UIPickerView](uipickerview.md) and its descendants aren’t available when the user interface idiom is [UIUserInterfaceIdiomMac](uiuserinterfaceidiom/mac.md).

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Providing the picker data

- [dataSource](uipickerview/datasource.md) — The data source for the picker view.
- [UIPickerViewDataSource](uipickerviewdatasource.md) — The interface for a picker view’s data source.

### Customizing the picker behavior

- [delegate](uipickerview/delegate.md) — The delegate for the picker view.
- [UIPickerViewDelegate](uipickerviewdelegate.md) — The interface for a picker view’s delegate.

### Getting the dimensions of the picker view

- [numberOfComponents](uipickerview/numberofcomponents.md) — The number of components for the picker view.
- [- numberOfRowsInComponent:](<uipickerview/numberofrows(incomponent_).md>) — Returns the number of rows for a component.
- [- rowSizeForComponent:](<uipickerview/rowsize(forcomponent_).md>) — Returns the size of a row for a component.

### Reloading the picker view

- [- reloadAllComponents](<uipickerview/reloadallcomponents().md>) — Reloads all components of the picker view.
- [- reloadComponent:](<uipickerview/reloadcomponent(__).md>) — Reloads a particular component of the picker view.

### Selecting rows in the view picker

- [- selectRow:inComponent:animated:](<uipickerview/selectrow(__incomponent_animated_).md>) — Selects a row in a specified component of the picker view.
- [- selectedRowInComponent:](<uipickerview/selectedrow(incomponent_).md>) — Returns the index of the selected row in a given component.

### Returning the view for a row and component

- [- viewForRow:forComponent:](<uipickerview/view(forrow_forcomponent_).md>) — Returns the view used by the picker view for a given row and component.

### Managing the appearance of the picker view

- [showsSelectionIndicator](uipickerview/showsselectionindicator.md) — A Boolean value that determines whether the selection indicator is displayed. _(deprecated)_

## See Also

### Content views

- [UIActivityIndicatorView](uiactivityindicatorview.md) — A view that shows that a task is in progress.
- [UICalendarView](uicalendarview.md) — A view that displays a calendar with date-specific decorations, and provides for user selection of a single date or multiple dates.
- [UIContentUnavailableView](uicontentunavailableview.md) — A view that indicates there’s no content to display.
- [UIImageView](uiimageview.md) — A view that displays a single image or a sequence of animated images in your interface.
- [UIProgressView](uiprogressview.md) — A view that depicts the progress of a task over time.
