---
title: UISearchDisplayDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uisearchdisplaydelegate
source_url: 'https://developer.apple.com/documentation/uikit/uisearchdisplaydelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchdisplaydelegate.json'
content_hash: 'sha256:dbf988e1413bb78c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchDisplayDelegate

<sub>Protocol</sub>

The interface for the delegate of a search display controller.

> [!warning] Deprecated
> Use [UISearchControllerDelegate](uisearchcontrollerdelegate.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol UISearchDisplayDelegate : NSObjectProtocol
```

## Overview

This protocol defines delegate methods for [UISearchDisplayController](uisearchdisplaycontroller.md) objects.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to search state change

- [- searchDisplayControllerWillBeginSearch:](<uisearchdisplaydelegate/searchdisplaycontrollerwillbeginsearch(__).md>) — Tells the delegate that the controller is about to begin searching. _(deprecated)_
- [- searchDisplayControllerDidBeginSearch:](<uisearchdisplaydelegate/searchdisplaycontrollerdidbeginsearch(__).md>) — Tells the delegate that the controller has started searching. _(deprecated)_
- [- searchDisplayControllerWillEndSearch:](<uisearchdisplaydelegate/searchdisplaycontrollerwillendsearch(__).md>) — Tells the delegate that the controller is about to end searching. _(deprecated)_
- [- searchDisplayControllerDidEndSearch:](<uisearchdisplaydelegate/searchdisplaycontrollerdidendsearch(__).md>) — Tells the delegate that the controller has finished searching. _(deprecated)_

### Loading and unloading the table view

- [- searchDisplayController:didLoadSearchResultsTableView:](<uisearchdisplaydelegate/searchdisplaycontroller(__didloadsearchresultstableview_).md>) — Tells the delegate that the controller has loaded its table view. _(deprecated)_
- [- searchDisplayController:willUnloadSearchResultsTableView:](<uisearchdisplaydelegate/searchdisplaycontroller(__willunloadsearchresultstableview_).md>) — Tells the delegate that the controller is about to unload its table view. _(deprecated)_

### Showing and hiding the table view

- [- searchDisplayController:willShowSearchResultsTableView:](<uisearchdisplaydelegate/searchdisplaycontroller(__willshowsearchresultstableview_).md>) — Tells the delegate that the controller is about to display its table view. _(deprecated)_
- [- searchDisplayController:didShowSearchResultsTableView:](<uisearchdisplaydelegate/searchdisplaycontroller(__didshowsearchresultstableview_).md>) — Tells the delegate that the controller just displayed its table view. _(deprecated)_
- [- searchDisplayController:willHideSearchResultsTableView:](<uisearchdisplaydelegate/searchdisplaycontroller(__willhidesearchresultstableview_).md>) — Tells the delegate that the controller is about to hide its table view. _(deprecated)_
- [- searchDisplayController:didHideSearchResultsTableView:](<uisearchdisplaydelegate/searchdisplaycontroller(__didhidesearchresultstableview_).md>) — Tells the delegate that the controller just hid its table view. _(deprecated)_

### Responding to changes in search criteria

- [- searchDisplayController:shouldReloadTableForSearchString:](<uisearchdisplaydelegate/searchdisplaycontroller(__shouldreloadtableforsearch_).md>) — Asks the delegate if the table view should be reloaded for a given search string. _(deprecated)_
- [- searchDisplayController:shouldReloadTableForSearchScope:](<uisearchdisplaydelegate/searchdisplaycontroller(__shouldreloadtableforsearchscope_).md>) — Asks the delegate if the table view should be reloaded for a given scope. _(deprecated)_

## See Also

### Deprecated protocols

- [UIActionSheetDelegate](uiactionsheetdelegate.md) — The interface for the delegate of an action sheet object. _(deprecated)_
- [UIAlertViewDelegate](uialertviewdelegate.md) — The interface for the delegate of an alert view object. _(deprecated)_
- [UIPopoverControllerDelegate](uipopovercontrollerdelegate.md) — The interface for the delegate of a popover controller object. _(deprecated)_
- [UIViewControllerPreviewing](uiviewcontrollerpreviewing.md) — A set of methods that define the interface for configuring a previewing view controller on devices that support 3D Touch. _(deprecated)_
- [UIViewControllerPreviewingDelegate](uiviewcontrollerpreviewingdelegate.md) — A set of methods used by the delegate to respond, with a preview view controller and a commit view controller, to the user pressing a view object on the screen of a device that supports 3D Touch. _(deprecated)_
