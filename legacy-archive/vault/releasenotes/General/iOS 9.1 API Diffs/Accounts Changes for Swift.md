---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/Accounts.html
archived_at: '2026-07-18T02:57:05.860864Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# Accounts Changes for Swift

### Accounts

Modified [ACAccount](https://developer.apple.com/documentation/accounts/acaccount)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [ACAccountCredential](https://developer.apple.com/documentation/accounts/acaccountcredential)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [ACAccountCredentialRenewResult [enum]](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [ACAccountStore](https://developer.apple.com/documentation/accounts/acaccountstore)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [ACAccountType](https://developer.apple.com/documentation/accounts/acaccounttype)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [ACErrorCode [struct]](https://developer.apple.com/documentation/accounts/acerrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ACErrorCode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |
| To | ``` struct ACErrorCode : RawRepresentable, Equatable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | Equatable, RawRepresentable |

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
