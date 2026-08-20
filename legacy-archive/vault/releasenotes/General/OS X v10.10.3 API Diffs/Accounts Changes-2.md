---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Accounts.html
archived_at: '2026-07-18T02:51:57.505595Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Accounts Changes

## Accounts

Modified ACAccount

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified ACAccount.init(accountType: ACAccountType!)

|  | Declaration |
| --- | --- |
| From | ``` init(accountType type: ACAccountType!) ``` |
| To | ``` init!(accountType type: ACAccountType!) ``` |

Modified ACAccountCredential

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

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
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified ACAccountType

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified ACAccountStoreDidChangeNotification

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACAccountStoreDidChangeNotification: NSString! ``` | OS X 10.10 |
| To | ``` let ACAccountStoreDidChangeNotification: String ``` | OS X 10.8 |

Modified ACAccountTypeIdentifierFacebook

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACAccountTypeIdentifierFacebook: NSString! ``` | OS X 10.10 |
| To | ``` let ACAccountTypeIdentifierFacebook: String ``` | OS X 10.8 |

Modified ACAccountTypeIdentifierLinkedIn

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACAccountTypeIdentifierLinkedIn: NSString! ``` | OS X 10.10 |
| To | ``` let ACAccountTypeIdentifierLinkedIn: String ``` | OS X 10.9 |

Modified ACAccountTypeIdentifierSinaWeibo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACAccountTypeIdentifierSinaWeibo: NSString! ``` | OS X 10.10 |
| To | ``` let ACAccountTypeIdentifierSinaWeibo: String ``` | OS X 10.8 |

Modified ACAccountTypeIdentifierTencentWeibo

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACAccountTypeIdentifierTencentWeibo: NSString! ``` | OS X 10.10 |
| To | ``` let ACAccountTypeIdentifierTencentWeibo: String ``` | OS X 10.9 |

Modified ACAccountTypeIdentifierTwitter

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACAccountTypeIdentifierTwitter: NSString! ``` | OS X 10.10 |
| To | ``` let ACAccountTypeIdentifierTwitter: String ``` | OS X 10.8 |

Modified ACErrorDomain

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACErrorDomain: NSString! ``` | OS X 10.10 |
| To | ``` let ACErrorDomain: String ``` | OS X 10.8 |

Modified ACFacebookAppIdKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACFacebookAppIdKey: NSString! ``` | OS X 10.10 |
| To | ``` let ACFacebookAppIdKey: String ``` | OS X 10.8 |

Modified ACFacebookAudienceEveryone

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACFacebookAudienceEveryone: NSString! ``` | OS X 10.10 |
| To | ``` let ACFacebookAudienceEveryone: String ``` | OS X 10.8 |

Modified ACFacebookAudienceFriends

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACFacebookAudienceFriends: NSString! ``` | OS X 10.10 |
| To | ``` let ACFacebookAudienceFriends: String ``` | OS X 10.8 |

Modified ACFacebookAudienceKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACFacebookAudienceKey: NSString! ``` | OS X 10.10 |
| To | ``` let ACFacebookAudienceKey: String ``` | OS X 10.8 |

Modified ACFacebookAudienceOnlyMe

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACFacebookAudienceOnlyMe: NSString! ``` | OS X 10.10 |
| To | ``` let ACFacebookAudienceOnlyMe: String ``` | OS X 10.8 |

Modified ACFacebookPermissionsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACFacebookPermissionsKey: NSString! ``` | OS X 10.10 |
| To | ``` let ACFacebookPermissionsKey: String ``` | OS X 10.8 |

Modified ACLinkedInAppIdKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACLinkedInAppIdKey: NSString! ``` | OS X 10.10 |
| To | ``` let ACLinkedInAppIdKey: String ``` | OS X 10.9 |

Modified ACLinkedInPermissionsKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACLinkedInPermissionsKey: NSString! ``` | OS X 10.10 |
| To | ``` let ACLinkedInPermissionsKey: String ``` | OS X 10.9 |

Modified ACTencentWeiboAppIdKey

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let ACTencentWeiboAppIdKey: NSString! ``` | OS X 10.10 |
| To | ``` let ACTencentWeiboAppIdKey: String ``` | OS X 10.9 |

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
