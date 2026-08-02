---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/Social.html
archived_at: '2026-07-18T02:54:21.757179Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# Social Changes

## Social

SLRequest.hAdded [SLRequestMethodPUT](https://developer.apple.com/documentation/social/slrequestmethod/put)Modified [SLRequest.URL](https://developer.apple.com/documentation/social/slrequest/1488602-url)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSURL \*URL |
| To | @property(readonly, atomic) NSURL \*URL |

Modified [SLRequest.account](https://developer.apple.com/documentation/social/slrequest/1488582-account)

|  | Declaration |
| --- | --- |
| From | @property(retain) ACAccount \*account |
| To | @property(retain, atomic) ACAccount \*account |

Modified [SLRequest.parameters](https://developer.apple.com/documentation/social/slrequest/1488603-parameters)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSDictionary \*parameters |
| To | @property(readonly, atomic) NSDictionary \*parameters |

Modified [SLRequest.requestMethod](https://developer.apple.com/documentation/social/slrequest/1488589-requestmethod)

|  | Declaration |
| --- | --- |
| From | @property(readonly) SLRequestMethod requestMethod |
| To | @property(readonly, atomic) SLRequestMethod requestMethod |

SLServiceTypes.hAdded [SLServiceTypeLinkedIn](https://developer.apple.com/documentation/social/slservicetypelinkedin)Added [SLServiceTypeTencentWeibo](https://developer.apple.com/documentation/social/slservicetypetencentweibo)

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
