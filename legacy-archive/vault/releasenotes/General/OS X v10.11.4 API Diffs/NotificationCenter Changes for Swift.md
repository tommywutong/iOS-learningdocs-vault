---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/NotificationCenter.html
archived_at: '2026-07-18T02:53:52.711872Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# NotificationCenter Changes for Swift

### NotificationCenter

Modified [NCWidgetListViewController](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class NCWidgetListViewController : NSViewController {     @IBOutlet weak var delegate: NCWidgetListViewDelegate?     var contents: [AnyObject]!     var minimumVisibleRowCount: Int     var hasDividerLines: Bool     var editing: Bool     var showsAddButtonWhenEditing: Bool     func viewControllerAtRow(_ row: Int, makeIfNecessary makeIfNecesary: Bool) -> NSViewController!     func rowForViewController(_ viewController: NSViewController!) -> Int } ``` |
| To | ``` class NCWidgetListViewController : NSViewController {     @IBOutlet weak var delegate: NCWidgetListViewDelegate!     var contents: [AnyObject]!     var minimumVisibleRowCount: Int     var hasDividerLines: Bool     var editing: Bool     var showsAddButtonWhenEditing: Bool     func viewControllerAtRow(_ row: Int, makeIfNecessary makeIfNecesary: Bool) -> NSViewController!     func rowForViewController(_ viewController: NSViewController!) -> Int } ``` |

Modified [NCWidgetListViewController.delegate](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewcontroller/1476044-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @IBOutlet weak var delegate: NCWidgetListViewDelegate? ``` |
| To | ``` @IBOutlet weak var delegate: NCWidgetListViewDelegate! ``` |

Modified [NCWidgetSearchViewController](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class NCWidgetSearchViewController : NSViewController {     @IBOutlet weak var delegate: NCWidgetSearchViewDelegate?     var searchResults: [AnyObject]!     var searchDescription: String!     var searchResultsPlaceholderString: String!     var searchResultKeyPath: String! } ``` |
| To | ``` class NCWidgetSearchViewController : NSViewController {     @IBOutlet weak var delegate: NCWidgetSearchViewDelegate!     var searchResults: [AnyObject]!     var searchDescription: String!     var searchResultsPlaceholderString: String!     var searchResultKeyPath: String! } ``` |

Modified [NCWidgetSearchViewController.delegate](https://developer.apple.com/documentation/notificationcenter/ncwidgetsearchviewcontroller/1449562-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @IBOutlet weak var delegate: NCWidgetSearchViewDelegate? ``` |
| To | ``` @IBOutlet weak var delegate: NCWidgetSearchViewDelegate! ``` |

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
