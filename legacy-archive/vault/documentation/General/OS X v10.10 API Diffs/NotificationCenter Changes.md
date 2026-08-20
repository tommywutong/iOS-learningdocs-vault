---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/NotificationCenter.html
archived_at: '2026-07-15T07:34:46.944712Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# NotificationCenter Changes

## NotificationCenter (Added)

NCWidgetController.h (Added)Added [NCWidgetController](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller)Added [+[NCWidgetController defaultWidgetController]](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller/1456691-defaultwidgetcontroller)Added [-[NCWidgetController setHasContent:forWidgetWithBundleIdentifier:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller/1456693-sethascontent)Added [+[NCWidgetController widgetController]](https://developer.apple.com/documentation/notificationcenter/ncwidgetcontroller/1456687-widgetcontroller)NCWidgetListViewController.h (Added)Added [NCWidgetListViewController](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller)Added [NCWidgetListViewController.contents](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/1476057-contents)Added [NCWidgetListViewController.delegate](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/1476044-delegate)Added [NCWidgetListViewController.editing](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/1476039-editing)Added [NCWidgetListViewController.hasDividerLines](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/1476043-hasdividerlines)Added [NCWidgetListViewController.minimumVisibleRowCount](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/1476034-minimumvisiblerowcount)Added [-[NCWidgetListViewController rowForViewController:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/1476053-row)Added [NCWidgetListViewController.showsAddButtonWhenEditing](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/1476041-showsaddbuttonwhenediting)Added [-[NCWidgetListViewController viewControllerAtRow:makeIfNecessary:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/1476061-viewcontroller)Added [NCWidgetListViewDelegate](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate)Added [-[NCWidgetListViewDelegate widgetList:didRemoveRow:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/1476049-widgetlist)Added [-[NCWidgetListViewDelegate widgetList:didReorderRow:toRow:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/1476063-widgetlist)Added [-[NCWidgetListViewDelegate widgetList:shouldRemoveRow:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/1476035-widgetlist)Added [-[NCWidgetListViewDelegate widgetList:shouldReorderRow:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/1476059-widgetlist)Added [-[NCWidgetListViewDelegate widgetList:viewControllerForRow:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/1476055-widgetlist)Added [-[NCWidgetListViewDelegate widgetListPerformAddAction:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/1476037-widgetlistperformaddaction)NCWidgetProviding.h (Added)Added [NCWidgetProviding](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding)Added [NCWidgetProviding.widgetAllowsEditing](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490251-widgetallowsediting)Added [-[NCWidgetProviding widgetDidBeginEditing]](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490249-widgetdidbeginediting)Added [-[NCWidgetProviding widgetDidEndEditing]](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490258-widgetdidendediting)Added [-[NCWidgetProviding widgetMarginInsetsForProposedMarginInsets:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490248-widgetmargininsets)Added [-[NCWidgetProviding widgetPerformUpdateWithCompletionHandler:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetproviding/1490262-widgetperformupdatewithcompletio)Added [-[NSViewController presentViewControllerInWidget:]](https://developer.apple.com/documentation/appkit/nsviewcontroller/1490260-present)Added [NCUpdateResult](https://developer.apple.com/documentation/notificationcenter/ncupdateresult)Added [NCUpdateResultFailed](https://developer.apple.com/documentation/notificationcenter/ncupdateresult/ncupdateresultfailed)Added [NCUpdateResultNewData](https://developer.apple.com/documentation/notificationcenter/ncupdateresult/ncupdateresultnewdata)Added [NCUpdateResultNoData](https://developer.apple.com/documentation/notificationcenter/ncupdateresult/nodata)Added NSViewController(NCWidgetProvidingPresentationStyles)NCWidgetSearchViewController.h (Added)Added [NCWidgetSearchViewController](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller)Added [NCWidgetSearchViewController.delegate](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/1449562-delegate)Added [NCWidgetSearchViewController.searchDescription](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/1449554-searchdescription)Added [NCWidgetSearchViewController.searchResultKeyPath](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/1449556-searchresultkeypath)Added [NCWidgetSearchViewController.searchResults](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/1449551-searchresults)Added [NCWidgetSearchViewController.searchResultsPlaceholderString](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/1449552-searchresultsplaceholderstring)Added [NCWidgetSearchViewDelegate](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate)Added [-[NCWidgetSearchViewDelegate widgetSearch:resultSelected:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate/1449548-widgetsearch)Added [-[NCWidgetSearchViewDelegate widgetSearch:searchForTerm:maxResults:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate/1449558-widgetsearch)Added [-[NCWidgetSearchViewDelegate widgetSearchTermCleared:]](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewdelegate/1449550-widgetsearchtermcleared)NotificationCenter.h (Added)

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
