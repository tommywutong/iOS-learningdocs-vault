---
title: iOS 9.3 API Diffs
apple_id: TP40016662
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-03-01'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS93APIDiffs/Swift/AddressBook.html
archived_at: '2026-07-18T02:57:14.881934Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.3 API Diffs](iOS%209.2%20to%20iOS%209.3%20API%20Differences.md)


# AddressBook Changes for Swift

### AddressBook

Modified [ABAddressBook](https://developer.apple.com/documentation/addressbook/abaddressbook-kkq)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABAddressBookRef = ABAddressBook ``` |
| To | ``` typealias ABAddressBook = CFTypeRef ``` |

Modified [ABMultiValue](https://developer.apple.com/documentation/addressbook/abmultivalue-kj7)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABMultiValueRef = ABMultiValue ``` |
| To | ``` typealias ABMultiValue = CFTypeRef ``` |

Modified [ABRecordRef](https://developer.apple.com/documentation/addressbook/abrecordref)

|  | Declaration |
| --- | --- |
| From | ``` typealias ABRecordRef = ABRecord ``` |
| To | ``` typealias ABRecord = CFTypeRef ``` |

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
