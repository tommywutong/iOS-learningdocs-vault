---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/NotificationCenter.html
archived_at: '2026-07-15T07:34:56.149501Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# NotificationCenter Changes

## NotificationCenter (Added)

Added NCUpdateResult [enum]Added NCUpdateResult.FailedAdded NCUpdateResult.NewDataAdded NCUpdateResult.NoDataAdded NCWidgetControllerAdded NCWidgetController.setHasContent(Bool, forWidgetWithBundleIdentifier: String!)Added NCWidgetController.widgetController() -> Self! [class]Added NCWidgetListViewControllerAdded NCWidgetListViewController.contentsAdded NCWidgetListViewController.delegateAdded NCWidgetListViewController.editingAdded NCWidgetListViewController.hasDividerLinesAdded NCWidgetListViewController.minimumVisibleRowCountAdded NCWidgetListViewController.rowForViewController(NSViewController!) -> IntAdded NCWidgetListViewController.showsAddButtonWhenEditingAdded NCWidgetListViewController.viewControllerAtRow(Int, makeIfNecessary: Bool) -> NSViewController!Added NCWidgetListViewDelegateAdded NCWidgetListViewDelegate.widgetList(NCWidgetListViewController!, didRemoveRow: Int)Added NCWidgetListViewDelegate.widgetList(NCWidgetListViewController!, didReorderRow: Int, toRow: Int)Added NCWidgetListViewDelegate.widgetList(NCWidgetListViewController!, shouldRemoveRow: Int) -> BoolAdded NCWidgetListViewDelegate.widgetList(NCWidgetListViewController!, shouldReorderRow: Int) -> BoolAdded NCWidgetListViewDelegate.widgetList(NCWidgetListViewController!, viewControllerForRow: Int) -> NSViewController!Added NCWidgetListViewDelegate.widgetListPerformAddAction(NCWidgetListViewController!)Added NCWidgetProvidingAdded NCWidgetProviding.widgetAllowsEditingAdded NCWidgetProviding.widgetDidBeginEditing()Added NCWidgetProviding.widgetDidEndEditing()Added NCWidgetProviding.widgetMarginInsetsForProposedMarginInsets(NSEdgeInsets) -> NSEdgeInsetsAdded NCWidgetProviding.widgetPerformUpdateWithCompletionHandler(((NCUpdateResult) -> Void)!)Added NCWidgetSearchViewControllerAdded NCWidgetSearchViewController.delegateAdded NCWidgetSearchViewController.searchDescriptionAdded NCWidgetSearchViewController.searchResultKeyPathAdded NCWidgetSearchViewController.searchResultsAdded NCWidgetSearchViewController.searchResultsPlaceholderStringAdded NCWidgetSearchViewDelegateAdded NCWidgetSearchViewDelegate.widgetSearch(NCWidgetSearchViewController!, resultSelected: AnyObject!)Added NCWidgetSearchViewDelegate.widgetSearch(NCWidgetSearchViewController!, searchForTerm: String!, maxResults: Int)Added NCWidgetSearchViewDelegate.widgetSearchTermCleared(NCWidgetSearchViewController!)Added NSViewController.presentViewControllerInWidget(NSViewController!)

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
