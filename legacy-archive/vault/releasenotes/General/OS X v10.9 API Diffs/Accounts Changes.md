---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/Accounts.html
archived_at: '2026-07-18T02:54:08.215413Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# Accounts Changes

## Accounts

ACAccount.hModified [ACAccount.accountDescription](https://developer.apple.com/documentation/accounts/acaccount/1543836-accountdescription)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*accountDescription |
| To | @property(copy, atomic) NSString \*accountDescription |

Modified [ACAccount.accountType](https://developer.apple.com/documentation/accounts/acaccount/1543805-accounttype)

|  | Declaration |
| --- | --- |
| From | @property(strong) ACAccountType \*accountType |
| To | @property(strong, atomic) ACAccountType \*accountType |

Modified [ACAccount.credential](https://developer.apple.com/documentation/accounts/acaccount/1543779-credential)

|  | Declaration |
| --- | --- |
| From | @property(strong) ACAccountCredential \*credential |
| To | @property(strong, atomic) ACAccountCredential \*credential |

Modified [ACAccount.identifier](https://developer.apple.com/documentation/accounts/acaccount/1543840-identifier)

|  | Declaration |
| --- | --- |
| From | @property(readonly, weak) NSString \*identifier |
| To | @property(readonly, weak, atomic) NSString \*identifier |

Modified [ACAccount.username](https://developer.apple.com/documentation/accounts/acaccount/1543839-username)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*username |
| To | @property(copy, atomic) NSString \*username |

ACAccountCredential.hModified [ACAccountCredential.oauthToken](https://developer.apple.com/documentation/accounts/acaccountcredential/1507894-oauthtoken)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*oauthToken |
| To | @property(copy, atomic) NSString \*oauthToken |

ACAccountStore.hModified [ACAccountStore.accounts](https://developer.apple.com/documentation/accounts/acaccountstore/1493961-accounts)

|  | Declaration |
| --- | --- |
| From | @property(readonly, weak) NSArray \*accounts |
| To | @property(readonly, weak, atomic) NSArray \*accounts |

Modified [ACFacebookAppIdKey](https://developer.apple.com/documentation/accounts/acfacebookappidkey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceEveryone](https://developer.apple.com/documentation/accounts/acfacebookaudienceeveryone)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceFriends](https://developer.apple.com/documentation/accounts/acfacebookaudiencefriends)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceKey](https://developer.apple.com/documentation/accounts/acfacebookaudiencekey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceOnlyMe](https://developer.apple.com/documentation/accounts/acfacebookaudienceonlyme)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookPermissionsKey](https://developer.apple.com/documentation/accounts/acfacebookpermissionskey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

ACAccountType.hAdded [ACAccountTypeIdentifierLinkedIn](https://developer.apple.com/documentation/accounts/acaccounttypeidentifierlinkedin)Added [ACAccountTypeIdentifierTencentWeibo](https://developer.apple.com/documentation/accounts/acaccounttypeidentifiertencentweibo)Added [ACLinkedInAppIdKey](https://developer.apple.com/documentation/accounts/aclinkedinappidkey)Added [ACLinkedInPermissionsKey](https://developer.apple.com/documentation/accounts/aclinkedinpermissionskey)Added [ACTencentWeiboAppIdKey](https://developer.apple.com/documentation/accounts/actencentweiboappidkey)Modified [ACAccountType.accessGranted](https://developer.apple.com/documentation/accounts/acaccounttype/1543838-accessgranted)

|  | Declaration |
| --- | --- |
| From | @property(readonly) BOOL accessGranted |
| To | @property(readonly, atomic) BOOL accessGranted |

Modified [ACAccountType.accountTypeDescription](https://developer.apple.com/documentation/accounts/acaccounttype/1543834-accounttypedescription)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSString \*accountTypeDescription |
| To | @property(readonly, atomic) NSString \*accountTypeDescription |

Modified [ACAccountType.identifier](https://developer.apple.com/documentation/accounts/acaccounttype/1543833-identifier)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSString \*identifier |
| To | @property(readonly, atomic) NSString \*identifier |

Modified [ACFacebookAppIdKey](https://developer.apple.com/documentation/accounts/acfacebookappidkey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceEveryone](https://developer.apple.com/documentation/accounts/acfacebookaudienceeveryone)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceFriends](https://developer.apple.com/documentation/accounts/acfacebookaudiencefriends)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceKey](https://developer.apple.com/documentation/accounts/acfacebookaudiencekey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookAudienceOnlyMe](https://developer.apple.com/documentation/accounts/acfacebookaudienceonlyme)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

Modified [ACFacebookPermissionsKey](https://developer.apple.com/documentation/accounts/acfacebookpermissionskey)

|  | Header |
| --- | --- |
| From | Accounts/ACAccountStore.h |
| To | Accounts/ACAccountType.h |

ACError.hAdded [ACErrorAccessDeniedByProtectionPolicy](https://developer.apple.com/documentation/accounts/acerroraccessdeniedbyprotectionpolicy)Added [ACErrorClientPermissionDenied](https://developer.apple.com/documentation/accounts/acerrorclientpermissiondenied)Added [ACErrorCredentialNotFound](https://developer.apple.com/documentation/accounts/acerrorcredentialnotfound)Added [ACErrorFetchCredentialFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorfetchcredentialfailed)Added [ACErrorInvalidClientBundleID](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorinvalidclientbundleid)Added [ACErrorRemoveCredentialFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorremovecredentialfailed)Added [ACErrorStoreCredentialFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorstorecredentialfailed)Added [ACErrorUpdatingNonexistentAccount](https://developer.apple.com/documentation/accounts/acerrorupdatingnonexistentaccount)

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
