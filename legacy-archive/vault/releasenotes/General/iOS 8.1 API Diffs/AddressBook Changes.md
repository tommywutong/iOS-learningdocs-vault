---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/AddressBook.html
archived_at: '2026-07-18T02:56:07.328958Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# AddressBook Changes

## AddressBook

Modified ABAddressBookCopyArrayOfAllGroupsInSource(ABAddressBook!, ABRecord!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABAddressBookCopyArrayOfAllPeopleInSource(ABAddressBook!, ABRecord!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABAddressBookCopyArrayOfAllPeopleInSourceWithSortOrdering(ABAddressBook!, ABRecord!, ABPersonSortOrdering) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABAddressBookCopyArrayOfAllSources(ABAddressBook!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABAddressBookCopyDefaultSource(ABAddressBook!) -> Unmanaged<ABRecord>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABAddressBookCreateWithOptions(CFDictionary!, UnsafeMutablePointer<Unmanaged<CFError>?>) -> Unmanaged<ABAddressBook>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ABAddressBookGetAuthorizationStatus() -> ABAuthorizationStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ABAddressBookGetSourceWithRecordID(ABAddressBook!, ABRecordID) -> Unmanaged<ABRecord>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABAddressBookRequestAccessWithCompletion(ABAddressBook!, ABAddressBookRequestAccessCompletionHandler!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ABGroupCopySource(ABRecord!) -> Unmanaged<ABRecord>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABGroupCreateInSource(ABRecord!) -> Unmanaged<ABRecord>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABPersonCopyArrayOfAllLinkedPeople(ABRecord!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABPersonCopyCompositeNameDelimiterForRecord(ABRecord!) -> Unmanaged<CFString>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified ABPersonCopyImageDataWithFormat(ABRecord!, ABPersonImageFormat) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified ABPersonCopySource(ABRecord!) -> Unmanaged<ABRecord>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABPersonCreateInSource(ABRecord!) -> Unmanaged<ABRecord>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified ABPersonCreatePeopleInSourceWithVCardRepresentation(ABRecord!, CFData!) -> Unmanaged<CFArray>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ABPersonCreateVCardRepresentationWithPeople(CFArray!) -> Unmanaged<CFData>!

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ABPersonGetCompositeNameFormatForRecord(ABRecord!) -> ABPersonCompositeNameFormat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kABPersonInstantMessageServiceFacebook

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonInstantMessageServiceGaduGadu

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonInstantMessageServiceGoogleTalk

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonInstantMessageServiceQQ

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonInstantMessageServiceSkype

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonPhoneIPhoneLabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 3.0 |

Modified kABPersonPhoneOtherFAXLabel

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileProperty

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileServiceFacebook

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileServiceFlickr

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileServiceGameCenter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileServiceKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileServiceLinkedIn

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileServiceMyspace

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileServiceSinaWeibo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified kABPersonSocialProfileServiceTwitter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileURLKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileUserIdentifierKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABPersonSocialProfileUsernameKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified kABSourceNameProperty

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

Modified kABSourceTypeProperty

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.0 |

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
