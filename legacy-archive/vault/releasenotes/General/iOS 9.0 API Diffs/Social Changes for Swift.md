---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/Social.html
archived_at: '2026-07-18T02:56:58.594396Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Social Changes for Swift

### Social

Modified [SLComposeServiceViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class SLComposeServiceViewController : UIViewController, UITextViewDelegate, NSObjectProtocol, UIScrollViewDelegate {     func presentationAnimationDidFinish()     var textView: UITextView! { get }     var contentText: String! { get }     var placeholder: String!     func didSelectPost()     func didSelectCancel()     func cancel()     func isContentValid() -> Bool     func validateContent()     var charactersRemaining: NSNumber!     func configurationItems() -> [AnyObject]!     func reloadConfigurationItems()     func pushConfigurationViewController(_ viewController: UIViewController!)     func popConfigurationViewController()     func loadPreviewView() -> UIView!     var autoCompletionViewController: UIViewController! } ``` |
| To | ``` class SLComposeServiceViewController : UIViewController, UITextViewDelegate, UIScrollViewDelegate {     func presentationAnimationDidFinish()     var textView: UITextView! { get }     var contentText: String! { get }     var placeholder: String!     func didSelectPost()     func didSelectCancel()     func cancel()     func isContentValid() -> Bool     func validateContent()     var charactersRemaining: NSNumber!     func configurationItems() -> [AnyObject]!     func reloadConfigurationItems()     func pushConfigurationViewController(_ viewController: UIViewController!)     func popConfigurationViewController()     func loadPreviewView() -> UIView!     var autoCompletionViewController: UIViewController! } ``` |

Modified [SLComposeViewController](https://developer.apple.com/documentation/social/slcomposeviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class SLComposeViewController : UIViewController {     class func isAvailableForServiceType(_ serviceType: String!) -> Bool     init!(forServiceType serviceType: String!) -> SLComposeViewController     class func composeViewControllerForServiceType(_ serviceType: String!) -> SLComposeViewController!     var serviceType: String! { get }     func setInitialText(_ text: String!) -> Bool     func addImage(_ image: UIImage!) -> Bool     func removeAllImages() -> Bool     func addURL(_ url: NSURL!) -> Bool     func removeAllURLs() -> Bool     var completionHandler: SLComposeViewControllerCompletionHandler! } ``` |
| To | ``` class SLComposeViewController : UIViewController {     class func isAvailableForServiceType(_ serviceType: String!) -> Bool      init!(forServiceType serviceType: String!)     class func composeViewControllerForServiceType(_ serviceType: String!) -> SLComposeViewController!     var serviceType: String! { get }     func setInitialText(_ text: String!) -> Bool     func addImage(_ image: UIImage!) -> Bool     func removeAllImages() -> Bool     func addURL(_ url: NSURL!) -> Bool     func removeAllURLs() -> Bool     var completionHandler: SLComposeViewControllerCompletionHandler! } ``` |

Modified [SLComposeViewController.init(forServiceType: String!)](https://developer.apple.com/documentation/social/slcomposeviewcontroller/1624837-composeviewcontrollerforservicet)

|  | Declaration |
| --- | --- |
| From | ``` init!(forServiceType serviceType: String!) -> SLComposeViewController ``` |
| To | ``` init!(forServiceType serviceType: String!) ``` |

Modified [SLComposeViewControllerResult [enum]](https://developer.apple.com/documentation/social/slcomposeviewcontrollerresult)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [SLRequest](https://developer.apple.com/documentation/social/slrequest)

|  | Declaration |
| --- | --- |
| From | ``` class SLRequest : NSObject {     init!(forServiceType serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) -> SLRequest     class func requestForServiceType(_ serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) -> SLRequest!     var account: ACAccount!     var requestMethod: SLRequestMethod { get }     var URL: NSURL! { get }     var parameters: [NSObject : AnyObject]! { get }     func addMultipartData(_ data: NSData!, withName name: String!, type type: String!, filename filename: String!)     func preparedURLRequest() -> NSURLRequest!     func performRequestWithHandler(_ handler: SLRequestHandler!) } ``` |
| To | ``` class SLRequest : NSObject {      init!(forServiceType serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!)     class func requestForServiceType(_ serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) -> SLRequest!     var account: ACAccount!     var requestMethod: SLRequestMethod { get }     var URL: NSURL! { get }     var parameters: [NSObject : AnyObject]! { get }     func addMultipartData(_ data: NSData!, withName name: String!, type type: String!, filename filename: String!)     func preparedURLRequest() -> NSURLRequest!     func performRequestWithHandler(_ handler: SLRequestHandler!) } ``` |

Modified [SLRequest.init(forServiceType: String!, requestMethod: SLRequestMethod, URL: NSURL!, parameters: [NSObject : AnyObject]!)](https://developer.apple.com/documentation/social/slrequest/1488580-requestforservicetype)

|  | Declaration |
| --- | --- |
| From | ``` init!(forServiceType serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) -> SLRequest ``` |
| To | ``` init!(forServiceType serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) ``` |

Modified [SLRequestMethod [enum]](https://developer.apple.com/documentation/social/slrequestmethod)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

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
