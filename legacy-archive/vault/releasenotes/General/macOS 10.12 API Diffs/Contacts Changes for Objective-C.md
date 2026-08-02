---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/Contacts.html
archived_at: '2026-07-18T02:50:37.810414Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# Contacts Changes for Objective-C

### Contacts

#### CNContact.h

Added [CNContact.imageDataAvailable](https://developer.apple.com/documentation/contacts/cncontact/1614589-imagedataavailable)Added [CNContact.phoneticOrganizationName](https://developer.apple.com/documentation/contacts/cncontact/2142774-phoneticorganizationname)Added [CNContactImageDataAvailableKey](https://developer.apple.com/documentation/contacts/cncontactimagedataavailablekey)Added [CNContactPhoneticOrganizationNameKey](https://developer.apple.com/documentation/contacts/cncontactphoneticorganizationnamekey)

#### CNContactFetchRequest.h

Modified [CNContactFetchRequest](https://developer.apple.com/documentation/contacts/cncontactfetchrequest)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSSecureCoding |

#### CNContactVCardSerialization.h

Modified [+[CNContactVCardSerialization contactsWithData:error:]](https://developer.apple.com/documentation/contacts/cncontactvcardserialization/1403090-contacts)

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)contactsWithData:(NSData *)data error:(NSError * _Nullable *)error ``` |
| To | ``` + (NSArray<CNContact *> *)contactsWithData:(NSData *)data error:(NSError * _Nullable *)error ``` |

Modified [+[CNContactVCardSerialization dataWithContacts:error:]](https://developer.apple.com/documentation/contacts/cncontactvcardserialization/1403357-datawithcontacts)

|  | Declaration |
| --- | --- |
| From | ``` + (NSData *)dataWithContacts:(NSArray *)contacts error:(NSError * _Nullable *)error ``` |
| To | ``` + (NSData *)dataWithContacts:(NSArray<CNContact *> *)contacts error:(NSError * _Nullable *)error ``` |

#### CNMutableContact.h

Added [CNMutableContact.phoneticOrganizationName](https://developer.apple.com/documentation/contacts/cnmutablecontact/2138282-phoneticorganizationname)

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
