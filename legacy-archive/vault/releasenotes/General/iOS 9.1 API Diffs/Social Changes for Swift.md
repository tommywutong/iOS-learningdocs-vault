---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/Social.html
archived_at: '2026-07-18T02:57:10.917849Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# Social Changes for Swift

### Social

Modified [SLComposeServiceViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class SLComposeServiceViewController : UIViewController, UITextViewDelegate, UIScrollViewDelegate {     func presentationAnimationDidFinish()     var textView: UITextView! { get }     var contentText: String! { get }     var placeholder: String!     func didSelectPost()     func didSelectCancel()     func cancel()     func isContentValid() -> Bool     func validateContent()     var charactersRemaining: NSNumber!     func configurationItems() -> [AnyObject]!     func reloadConfigurationItems()     func pushConfigurationViewController(_ viewController: UIViewController!)     func popConfigurationViewController()     func loadPreviewView() -> UIView!     var autoCompletionViewController: UIViewController! } ``` | AnyObject, NSObjectProtocol, UIScrollViewDelegate, UITextViewDelegate |
| To | ``` class SLComposeServiceViewController : UIViewController, UITextViewDelegate {     func presentationAnimationDidFinish()     var textView: UITextView! { get }     var contentText: String! { get }     var placeholder: String!     func didSelectPost()     func didSelectCancel()     func cancel()     func isContentValid() -> Bool     func validateContent()     var charactersRemaining: NSNumber!     func configurationItems() -> [AnyObject]!     func reloadConfigurationItems()     func pushConfigurationViewController(_ viewController: UIViewController!)     func popConfigurationViewController()     func loadPreviewView() -> UIView!     var autoCompletionViewController: UIViewController! } ``` | UITextViewDelegate |

Modified [SLComposeSheetConfigurationItem](https://developer.apple.com/documentation/social/slcomposesheetconfigurationitem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SLComposeViewController](https://developer.apple.com/documentation/social/slcomposeviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SLComposeViewControllerResult [enum]](https://developer.apple.com/documentation/social/slcomposeviewcontrollerresult)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [SLRequest](https://developer.apple.com/documentation/social/slrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [SLRequestMethod [enum]](https://developer.apple.com/documentation/social/slrequestmethod)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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
