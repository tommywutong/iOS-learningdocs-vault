---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/Accounts.html
archived_at: '2026-07-15T07:34:43.651139Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Accounts Changes

## Accounts

ACAccount.hModified [-[ACAccount initWithAccountType:]](https://developer.apple.com/documentation/accounts/acaccount/1543781-initwithaccounttype)

|  | Declaration | Designated Initializer |
| --- | --- | --- |
| From | ``` - (id)initWithAccountType:(ACAccountType *)type ``` | -- |
| To | ``` - (instancetype)initWithAccountType:(ACAccountType *)type ``` | yes |

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

Modified [ACAccountCredential.oauthToken](https://developer.apple.com/documentation/accounts/acaccountcredential/1507894-oauthtoken)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *oauthToken ``` |
| To | ``` @property(copy, nonatomic) NSString *oauthToken ``` |

ACAccountType.hModified [ACAccountType.accessGranted](https://developer.apple.com/documentation/accounts/acaccounttype/1543838-accessgranted)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) BOOL accessGranted ``` |
| To | ``` @property(readonly, nonatomic) BOOL accessGranted ``` |

Modified [ACAccountType.accountTypeDescription](https://developer.apple.com/documentation/accounts/acaccounttype/1543834-accounttypedescription)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *accountTypeDescription ``` |
| To | ``` @property(readonly, nonatomic) NSString *accountTypeDescription ``` |

Modified [ACAccountType.identifier](https://developer.apple.com/documentation/accounts/acaccounttype/1543833-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *identifier ``` |
| To | ``` @property(readonly, nonatomic) NSString *identifier ``` |

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
