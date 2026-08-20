---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/Accounts.html
archived_at: '2026-07-18T02:52:48.812651Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Accounts Changes for Objective-C

### Accounts

#### ACAccount.h

Modified [ACAccount.identifier](https://developer.apple.com/documentation/accounts/acaccount/1543840-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, weak, atomic) NSString *identifier ``` |
| To | ``` @property(readonly, weak, atomic, nullable) NSString *identifier ``` |

#### ACAccountStore.h

Modified [ACAccountStore.accounts](https://developer.apple.com/documentation/accounts/acaccountstore/1493961-accounts)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, weak, atomic) NSArray *accounts ``` |
| To | ``` @property(readonly, weak, atomic, nullable) NSArray *accounts ``` |

#### ACError.h

Added [ACErrorCoreDataSaveFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorcoredatasavefailed)Added [ACErrorCredentialItemNotExpired](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorcredentialitemnotexpired)Added [ACErrorCredentialItemNotFound](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorcredentialitemnotfound)Added [ACErrorDeniedByPlugin](https://developer.apple.com/documentation/accounts/acerrorcode/acerrordeniedbyplugin)Added [ACErrorFailedSerializingAccountInfo](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorfailedserializingaccountinfo)Added [ACErrorInvalidCommand](https://developer.apple.com/documentation/accounts/acerrorinvalidcommand)Added [ACErrorMissingTransportMessageID](https://developer.apple.com/documentation/accounts/acerrormissingtransportmessageid)

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
