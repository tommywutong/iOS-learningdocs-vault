---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/TVMLKit.html
archived_at: '2026-07-18T02:58:07.004422Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# TVMLKit Changes for Swift

### TVMLKit

Added [TVInterfaceCreating.imageForResource(_: String) -> UIImage?](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating/1627677-resourceimage)Modified [TVInterfaceCreating](https://developer.apple.com/documentation/tvmlkit/tvinterfacecreating)

|  | Declaration |
| --- | --- |
| From | ``` protocol TVInterfaceCreating : NSObjectProtocol {     optional func viewForElement(_ element: TVViewElement, existingView existingView: UIView?) -> UIView?     optional func viewControllerForElement(_ element: TVViewElement, existingViewController existingViewController: UIViewController?) -> UIViewController?     optional func URLForResource(_ resourceName: String) -> NSURL? } ``` |
| To | ``` protocol TVInterfaceCreating : NSObjectProtocol {     optional func viewForElement(_ element: TVViewElement, existingView existingView: UIView?) -> UIView?     optional func viewControllerForElement(_ element: TVViewElement, existingViewController existingViewController: UIViewController?) -> UIViewController?     optional func URLForResource(_ resourceName: String) -> NSURL?     optional func imageForResource(_ resourceName: String) -> UIImage? } ``` |

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
