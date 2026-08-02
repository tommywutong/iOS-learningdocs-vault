---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/Social.html
archived_at: '2026-07-15T07:34:47.373654Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Social Changes

## Social

SLComposeServiceViewController.h (Added)Added [SLComposeServiceViewController](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller)Added [-[SLComposeServiceViewController cancel]](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488548-cancel)Added [SLComposeServiceViewController.charactersRemaining](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488552-charactersremaining)Added [SLComposeServiceViewController.contentText](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488546-contenttext)Added [-[SLComposeServiceViewController didSelectCancel]](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488556-didselectcancel)Added [-[SLComposeServiceViewController didSelectPost]](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488578-didselectpost)Added [-[SLComposeServiceViewController isContentValid]](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488591-iscontentvalid)Added [SLComposeServiceViewController.placeholder](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488574-placeholder)Added [-[SLComposeServiceViewController presentationAnimationDidFinish]](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488598-presentationanimationdidfinish)Added [SLComposeServiceViewController.textView](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488586-textview)Added [-[SLComposeServiceViewController validateContent]](https://developer.apple.com/documentation/social/slcomposeserviceviewcontroller/1488550-validatecontent)SLRequest.hModified [SLRequest.URL](https://developer.apple.com/documentation/social/slrequest/1488602-url)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSURL *URL ``` |
| To | ``` @property(readonly, nonatomic) NSURL *URL ``` |

Modified [SLRequest.account](https://developer.apple.com/documentation/social/slrequest/1488582-account)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain, atomic) ACAccount *account ``` |
| To | ``` @property(retain, nonatomic) ACAccount *account ``` |

Modified [SLRequest.parameters](https://developer.apple.com/documentation/social/slrequest/1488603-parameters)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSDictionary *parameters ``` |
| To | ``` @property(readonly, nonatomic) NSDictionary *parameters ``` |

Modified [SLRequest.requestMethod](https://developer.apple.com/documentation/social/slrequest/1488589-requestmethod)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) SLRequestMethod requestMethod ``` |
| To | ``` @property(readonly, nonatomic) SLRequestMethod requestMethod ``` |

SocialDefines.hAdded #def SOCIAL_CLASS_AVAILABLE_IOSAdded #def SOCIAL_CLASS_AVAILABLE_MAC

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
