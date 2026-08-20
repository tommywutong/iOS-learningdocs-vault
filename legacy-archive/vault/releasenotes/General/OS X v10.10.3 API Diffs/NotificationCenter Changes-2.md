---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/NotificationCenter.html
archived_at: '2026-07-18T02:52:34.174608Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# NotificationCenter Changes

## NotificationCenter

Added NSViewController.presentViewControllerInWidget(NSViewController!)Modified NCWidgetListViewController.delegate

|  | Declaration |
| --- | --- |
| From | ``` @IBOutlet var delegate: NCWidgetListViewDelegate! ``` |
| To | ``` @IBOutlet weak var delegate: NCWidgetListViewDelegate! ``` |

Modified NCWidgetListViewDelegate.widgetList(NCWidgetListViewController!, didRemoveRow: Int)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetListViewDelegate.widgetList(NCWidgetListViewController!, didReorderRow: Int, toRow: Int)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetListViewDelegate.widgetList(NCWidgetListViewController!, shouldRemoveRow: Int) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetListViewDelegate.widgetList(NCWidgetListViewController!, shouldReorderRow: Int) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetListViewDelegate.widgetListPerformAddAction(NCWidgetListViewController!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetProviding.widgetAllowsEditing

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetProviding.widgetDidBeginEditing()

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetProviding.widgetDidEndEditing()

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetProviding.widgetMarginInsetsForProposedMarginInsets(NSEdgeInsets) -> NSEdgeInsets

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetProviding.widgetPerformUpdateWithCompletionHandler(((NCUpdateResult) -> Void)!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified NCWidgetSearchViewController.delegate

|  | Declaration |
| --- | --- |
| From | ``` @IBOutlet var delegate: NCWidgetSearchViewDelegate! ``` |
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
