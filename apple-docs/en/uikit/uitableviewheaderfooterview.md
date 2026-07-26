---
title: UITableViewHeaderFooterView
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitableviewheaderfooterview
source_url: 'https://developer.apple.com/documentation/uikit/uitableviewheaderfooterview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitableviewheaderfooterview.json'
content_hash: 'sha256:e43840b6507270c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITableViewHeaderFooterView

<sub>Class</sub>

A reusable view that you place at the top or bottom of a table section to display additional information for that section.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UITableViewHeaderFooterView
```

## Overview

Use [UITableViewHeaderFooterView](uitableviewheaderfooterview.md) objects to manage the header and footer content of your table’s sections efficiently. A header-footer view is a reusable view that you can subclass or use as is. To configure the content and appearance of a header-footer view, you can set its [contentConfiguration](uitableviewheaderfooterview/contentconfiguration-6b4eg.md) and [backgroundConfiguration](uitableviewheaderfooterview/backgroundconfiguration-52wng.md).

To promote the reuse of your header-footer views, register them by calling the [- registerClass:forHeaderFooterViewReuseIdentifier:](<uitableview/register(__forheaderfooterviewreuseidentifier_)-20ybb.md>) or [- registerNib:forHeaderFooterViewReuseIdentifier:](<uitableview/register(__forheaderfooterviewreuseidentifier_)-1rgvc.md>) method of the table view. In the [- tableView:viewForHeaderInSection:](<uitableviewdelegate/tableview(__viewforheaderinsection_).md>) or [- tableView:viewForFooterInSection:](<uitableviewdelegate/tableview(__viewforfooterinsection_).md>) method of your delegate object, call the table view’s [- dequeueReusableHeaderFooterViewWithIdentifier:](<uitableview/dequeuereusableheaderfooterview(withidentifier_).md>) method to create your view. That method returns a recycled view (if one is available) or creates a new view using the information you registered.

A simple alternative to creating custom header-footer views is to implement the [- tableView:titleForHeaderInSection:](<uitableviewdatasource/tableview(__titleforheaderinsection_).md>) and [- tableView:titleForFooterInSection:](<uitableviewdatasource/tableview(__titleforfooterinsection_).md>) methods of your data source object. When you implement those methods, the table view creates a standard header or footer view and displays the text you supply.

## Relationships

- **Inherits From**: [UIView](uiview.md)

- **Conforms To**: [CALayerDelegate](../quartzcore/calayerdelegate.md), [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md), [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAccessibilityIdentification](uiaccessibilityidentification.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearance](uiappearance.md), [UIAppearanceContainer](uiappearancecontainer.md), [UICoordinateSpace](uicoordinatespace.md), [UIDynamicItem](uidynamicitem.md), [UIFocusEnvironment](uifocusenvironment.md), [UIFocusItem](uifocusitem.md), [UIFocusItemContainer](uifocusitemcontainer.md), [UILargeContentViewerItem](uilargecontentvieweritem.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating the view

- [- initWithReuseIdentifier:](<uitableviewheaderfooterview/init(reuseidentifier_).md>) — Initializes a header-footer view with the specified reuse identifier.
- [- initWithCoder:](<uitableviewheaderfooterview/init(coder_).md>) — Creates a header-footer view from data in an unarchiver.

### Managing view reuse

- [reuseIdentifier](uitableviewheaderfooterview/reuseidentifier.md) — A string used to identify a reusable header or footer.
- [- prepareForReuse](<uitableviewheaderfooterview/prepareforreuse().md>) — Prepares a reusable header or footer view for reuse by the table.

### Configuring the background

- [defaultBackgroundConfiguration()](<uitableviewheaderfooterview/defaultbackgroundconfiguration().md>) — Retrieves a background configuration with system default values.
- [backgroundConfiguration](uitableviewheaderfooterview/backgroundconfiguration-52wng.md) — The current background configuration of the view.
- [automaticallyUpdatesBackgroundConfiguration](uitableviewheaderfooterview/automaticallyupdatesbackgroundconfiguration.md) — A Boolean value that determines whether the view automatically updates its background configuration when its state changes.
- [backgroundView](uitableviewheaderfooterview/backgroundview.md) — The background view of the header or footer.

### Managing the content

- [defaultContentConfiguration()](<uitableviewheaderfooterview/defaultcontentconfiguration().md>) — Retrieves a default list content configuration for the view’s style.
- [contentConfiguration](uitableviewheaderfooterview/contentconfiguration-6b4eg.md) — The current content configuration of the view.
- [automaticallyUpdatesContentConfiguration](uitableviewheaderfooterview/automaticallyupdatescontentconfiguration.md) — A Boolean value that determines whether the view automatically updates its content configuration when its state changes.
- [contentView](uitableviewheaderfooterview/contentview.md) — The content view of the header or footer.

### Managing the state

- [configurationState](uitableviewheaderfooterview/configurationstate-7xj7r.md) — The current configuration state of the view.
- [- setNeedsUpdateConfiguration](<uitableviewheaderfooterview/setneedsupdateconfiguration().md>) — Informs the view to update its configuration for its current state.
- [updateConfiguration(using:)](<uitableviewheaderfooterview/updateconfiguration(using_).md>) — Updates the view’s configuration using the current state.
- [configurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-49slo.md) — A block for handling updates to the view’s configuration using the current state.
- [ConfigurationUpdateHandler](uitableviewheaderfooterview/configurationupdatehandler-swift.typealias.md) — The type of block for handling updates to the view’s configuration using the current state.

### Deprecated

- [textLabel](uitableviewheaderfooterview/textlabel.md) — A primary text label for the view. _(deprecated)_
- [detailTextLabel](uitableviewheaderfooterview/detailtextlabel.md) — A detail text label for the view. _(deprecated)_

## See Also

### Cells, headers, and footers

- [Configuring the cells for your table](configuring-the-cells-for-your-table.md) — Specify the appearance and content of your table’s rows by defining one or more prototype cells in your storyboard.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md) — Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [Adding headers and footers to table sections](adding-headers-and-footers-to-table-sections.md) — Differentiate groups of rows visually by adding header and footer views to your table view’s sections.
- [UITableViewCell](uitableviewcell.md) — The visual representation of a single row in a table view.
