---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/MessageUI.html
archived_at: '2026-07-18T02:56:35.006423Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# MessageUI Changes for Objective-C

### MessageUI

#### MFMailComposeViewController.h

Modified [-[MFMailComposeViewController setBccRecipients:]](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616887-setbccrecipients)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setBccRecipients:(NSArray *)bccRecipients ``` |
| To | ``` - (void)setBccRecipients:(NSArray<NSString *> * _Nullable)bccRecipients ``` |

Modified [-[MFMailComposeViewController setCcRecipients:]](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616889-setccrecipients)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setCcRecipients:(NSArray *)ccRecipients ``` |
| To | ``` - (void)setCcRecipients:(NSArray<NSString *> * _Nullable)ccRecipients ``` |

Modified [-[MFMailComposeViewController setToRecipients:]](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/1616872-settorecipients)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setToRecipients:(NSArray *)toRecipients ``` |
| To | ``` - (void)setToRecipients:(NSArray<NSString *> * _Nullable)toRecipients ``` |

#### MFMessageComposeViewController.h

Modified [MFMessageComposeViewController.attachments](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614066-attachments)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy, readonly) NSArray *attachments ``` |
| To | ``` @property(nonatomic, copy, readonly, nullable) NSArray<NSDictionary *> *attachments ``` |

Modified [MFMessageComposeViewController.recipients](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/1614071-recipients)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSArray *recipients ``` |
| To | ``` @property(nonatomic, copy, nullable) NSArray<NSString *> *recipients ``` |

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
