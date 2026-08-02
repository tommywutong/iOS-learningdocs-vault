---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Social.html
archived_at: '2026-07-18T02:52:40.709545Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Social Changes

## Social

Added SLRequest.accountModified SLRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified SLRequest.init(forServiceType: String!, requestMethod: SLRequestMethod, URL: NSURL!, parameters:[NSObject: AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(forServiceType serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) -> SLRequest ``` |
| To | ``` init!(forServiceType serviceType: String!, requestMethod requestMethod: SLRequestMethod, URL url: NSURL!, parameters parameters: [NSObject : AnyObject]!) -> SLRequest ``` |

Modified SLServiceTypeFacebook

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SLServiceTypeFacebook: NSString! ``` | OS X 10.10 |
| To | ``` let SLServiceTypeFacebook: String ``` | OS X 10.8 |

Modified SLServiceTypeLinkedIn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SLServiceTypeLinkedIn: NSString! ``` | OS X 10.10 |
| To | ``` let SLServiceTypeLinkedIn: String ``` | OS X 10.9 |

Modified SLServiceTypeSinaWeibo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SLServiceTypeSinaWeibo: NSString! ``` | OS X 10.10 |
| To | ``` let SLServiceTypeSinaWeibo: String ``` | OS X 10.8 |

Modified SLServiceTypeTencentWeibo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SLServiceTypeTencentWeibo: NSString! ``` | OS X 10.10 |
| To | ``` let SLServiceTypeTencentWeibo: String ``` | OS X 10.9 |

Modified SLServiceTypeTwitter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let SLServiceTypeTwitter: NSString! ``` | OS X 10.10 |
| To | ``` let SLServiceTypeTwitter: String ``` | OS X 10.8 |

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
