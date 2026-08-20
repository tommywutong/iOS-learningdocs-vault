---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/Accounts.html
archived_at: '2026-07-18T02:56:07.236814Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# Accounts Changes

## Accounts

Modified ACAccount

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ACAccount.init(accountType: ACAccountType!)

|  | Declaration |
| --- | --- |
| From | ``` init(accountType type: ACAccountType!) ``` |
| To | ``` init!(accountType type: ACAccountType!) ``` |

Modified ACAccount.userFullName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified ACAccountCredential

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ACAccountCredential.init(OAuth2Token: String!, refreshToken: String!, expiryDate: NSDate!)

|  | Declaration |
| --- | --- |
| From | ``` init(OAuth2Token token: String!, refreshToken refreshToken: String!, expiryDate expiryDate: NSDate!) ``` |
| To | ``` init!(OAuth2Token token: String!, refreshToken refreshToken: String!, expiryDate expiryDate: NSDate!) ``` |

Modified ACAccountCredential.init(OAuthToken: String!, tokenSecret: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(OAuthToken token: String!, tokenSecret secret: String!) ``` |
| To | ``` init!(OAuthToken token: String!, tokenSecret secret: String!) ``` |

Modified ACAccountStore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ACAccountType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ACAccountStoreDidChangeNotification

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ACAccountTypeIdentifierFacebook

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ACAccountTypeIdentifierSinaWeibo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ACAccountTypeIdentifierTencentWeibo

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified ACAccountTypeIdentifierTwitter

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ACErrorDomain

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified ACFacebookAppIdKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ACFacebookAudienceEveryone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ACFacebookAudienceFriends

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ACFacebookAudienceKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ACFacebookAudienceOnlyMe

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ACFacebookPermissionsKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified ACTencentWeiboAppIdKey

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

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
