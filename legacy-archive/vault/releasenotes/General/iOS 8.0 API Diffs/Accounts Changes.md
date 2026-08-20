---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/Accounts.html
archived_at: '2026-07-18T02:55:55.438783Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# Accounts Changes

## Accounts

ACAccount.hModified [-[ACAccount initWithAccountType:]](https://developer.apple.com/documentation/accounts/acaccount/1543781-initwithaccounttype)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithAccountType:(ACAccountType *)type ``` |
| To | ``` - (instancetype)initWithAccountType:(ACAccountType *)type ``` |

ACAccountCredential.hModified [-[ACAccountCredential initWithOAuth2Token:refreshToken:expiryDate:]](https://developer.apple.com/documentation/accounts/acaccountcredential/1507892-initwithoauth2token)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithOAuth2Token:(NSString *)token refreshToken:(NSString *)refreshToken expiryDate:(NSDate *)expiryDate ``` |
| To | ``` - (instancetype)initWithOAuth2Token:(NSString *)token refreshToken:(NSString *)refreshToken expiryDate:(NSDate *)expiryDate ``` |

Modified [-[ACAccountCredential initWithOAuthToken:tokenSecret:]](https://developer.apple.com/documentation/accounts/acaccountcredential/1507896-initwithoauthtoken)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithOAuthToken:(NSString *)token tokenSecret:(NSString *)secret ``` |
| To | ``` - (instancetype)initWithOAuthToken:(NSString *)token tokenSecret:(NSString *)secret ``` |

ACError.hAdded [ACErrorCoreDataSaveFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorcoredatasavefailed)Added [ACErrorDeniedByPlugin](https://developer.apple.com/documentation/accounts/acerrorcode/acerrordeniedbyplugin)Added [ACErrorFailedSerializingAccountInfo](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorfailedserializingaccountinfo)Added [ACErrorInvalidCommand](https://developer.apple.com/documentation/accounts/acerrorinvalidcommand)Added ACErrorMissingMessageID

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
