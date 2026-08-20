---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/Social.html
archived_at: '2026-07-18T02:53:44.155427Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Social Changes for Swift

### Social

Added [SLRequest.addMultipartData(_: NSData!, withName: String!, type: String!)](https://developer.apple.com/documentation/social/slrequest/1488544-addmultipartdata)Modified [SLComposeServiceViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class SLComposeServiceViewController : NSViewController, NSTextViewDelegate, NSTextDelegate, NSObjectProtocol {     func presentationAnimationDidFinish()     var textView: NSTextView! { get }     var contentText: String! { get }     var placeholder: String!     func didSelectPost()     func didSelectCancel()     func cancel()     func isContentValid() -> Bool     func validateContent()     var charactersRemaining: NSNumber! } ``` |
| To | ``` class SLComposeServiceViewController : NSViewController, NSTextViewDelegate, NSTextDelegate {     func presentationAnimationDidFinish()     var textView: NSTextView! { get }     var contentText: String! { get }     var placeholder: String!     func didSelectPost()     func didSelectCancel()     func cancel()     func isContentValid() -> Bool     func validateContent()     var charactersRemaining: NSNumber! } ``` |

Modified [SLRequest](https://developer.apple.com/documentation/social/slrequest)

|  | Declaration |
| --- | --- |
| From | ``` class SLRequest : NSObject {     init!(forServiceType serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) -> SLRequest     class func requestForServiceType(_ serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) -> SLRequest!     var account: ACAccount!     var requestMethod: SLRequestMethod { get }     var URL: NSURL! { get }     var parameters: [NSObject : AnyObject]! { get }     func addMultipartData(_ data: NSData!, withName name: String!, type type: String!, filename filename: String!)     func addMultipartData(_ data: NSData!, withName name: String!, type type: String!)     func preparedURLRequest() -> NSURLRequest!     func performRequestWithHandler(_ handler: SLRequestHandler!) } ``` |
| To | ``` class SLRequest : NSObject {      init!(forServiceType serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!)     class func requestForServiceType(_ serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) -> SLRequest!     var account: ACAccount!     var requestMethod: SLRequestMethod { get }     var URL: NSURL! { get }     var parameters: [NSObject : AnyObject]! { get }     func addMultipartData(_ data: NSData!, withName name: String!, type type: String!, filename filename: String!)     func addMultipartData(_ data: NSData!, withName name: String!, type type: String!)     func preparedURLRequest() -> NSURLRequest!     func performRequestWithHandler(_ handler: SLRequestHandler!) } ``` |

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
