---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/Collaboration.html
archived_at: '2026-07-18T02:52:57.161269Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# Collaboration Changes for Objective-C

### Collaboration

#### CBIdentity.h

Removed [-[CBIdentity isHidden]](https://developer.apple.com/documentation/collaboration/cbidentity/1805296-ishidden)Removed [-[CBUserIdentity isEnabled]](https://developer.apple.com/documentation/collaboration/cbuseridentity/1805246-isenabled)Added [CBGroupIdentity.memberIdentities](https://developer.apple.com/documentation/collaboration/cbgroupidentity/1423890-memberidentities)Added [CBIdentity.hidden](https://developer.apple.com/documentation/collaboration/cbidentity/1423883-ishidden)Added [+[CBIdentity identityWithUniqueIdentifier:authority:]](https://developer.apple.com/documentation/collaboration/cbidentity/1423900-identitywithuniqueidentifier)Added [CBIdentity.uniqueIdentifier](https://developer.apple.com/documentation/collaboration/cbidentity/1423929-uniqueidentifier)Added [CBUserIdentity.enabled](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423888-enabled)Modified [+[CBGroupIdentity groupIdentityWithPosixGID:authority:]](https://developer.apple.com/documentation/collaboration/cbgroupidentity/1423869-groupidentitywithposixgid)

|  | Declaration |
| --- | --- |
| From | ``` + (CBGroupIdentity *)groupIdentityWithPosixGID:(gid_t)gid authority:(CBIdentityAuthority *)authority ``` |
| To | ``` + (CBGroupIdentity * _Nullable)groupIdentityWithPosixGID:(gid_t)gid authority:(CBIdentityAuthority * _Nonnull)authority ``` |

Modified [CBGroupIdentity.members](https://developer.apple.com/documentation/collaboration/cbgroupidentity/1570848-members)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (NSArray *)members ``` | -- |
| To | ``` @property(readonly, nonatomic, nullable) NSArray *members ``` | OS X 10.11 |

Modified [CBGroupIdentity.posixGID](https://developer.apple.com/documentation/collaboration/cbgroupidentity/1423857-posixgid)

|  | Declaration |
| --- | --- |
| From | ``` - (gid_t)posixGID ``` |
| To | ``` @property(readonly, nonatomic) gid_t posixGID ``` |

Modified [CBIdentity.aliases](https://developer.apple.com/documentation/collaboration/cbidentity/1423871-aliases)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)aliases ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSArray<NSString *> *aliases ``` |

Modified [CBIdentity.authority](https://developer.apple.com/documentation/collaboration/cbidentity/1423859-authority)

|  | Declaration |
| --- | --- |
| From | ``` - (CBIdentityAuthority *)authority ``` |
| To | ``` @property(readonly, nonatomic, nonnull) CBIdentityAuthority *authority ``` |

Modified [CBIdentity.CSIdentity](https://developer.apple.com/documentation/collaboration/cbidentity/1570846-csidentity)

|  | Declaration |
| --- | --- |
| From | ``` - (CSIdentityRef)CSIdentity ``` |
| To | ``` @property(readonly, nonnull) CSIdentityRef CSIdentity ``` |

Modified [CBIdentity.emailAddress](https://developer.apple.com/documentation/collaboration/cbidentity/1423923-emailaddress)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)emailAddress ``` |
| To | ``` @property(readonly, nonatomic, nullable) NSString *emailAddress ``` |

Modified [CBIdentity.fullName](https://developer.apple.com/documentation/collaboration/cbidentity/1423863-fullname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)fullName ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSString *fullName ``` |

Modified [+[CBIdentity identityWithCSIdentity:]](https://developer.apple.com/documentation/collaboration/cbidentity/1570847-identitywithcsidentity)

|  | Declaration |
| --- | --- |
| From | ``` + (CBIdentity *)identityWithCSIdentity:(CSIdentityRef)csIdentity ``` |
| To | ``` + (CBIdentity * _Nonnull)identityWithCSIdentity:(CSIdentityRef _Nonnull)csIdentity ``` |

Modified [+[CBIdentity identityWithName:authority:]](https://developer.apple.com/documentation/collaboration/cbidentity/1423881-init)

|  | Declaration |
| --- | --- |
| From | ``` + (CBIdentity *)identityWithName:(NSString *)name authority:(CBIdentityAuthority *)authority ``` |
| To | ``` + (CBIdentity * _Nullable)identityWithName:(NSString * _Nonnull)name authority:(CBIdentityAuthority * _Nonnull)authority ``` |

Modified [+[CBIdentity identityWithPersistentReference:]](https://developer.apple.com/documentation/collaboration/cbidentity/1423945-init)

|  | Declaration |
| --- | --- |
| From | ``` + (CBIdentity *)identityWithPersistentReference:(NSData *)data ``` |
| To | ``` + (CBIdentity * _Nullable)identityWithPersistentReference:(NSData * _Nonnull)data ``` |

Modified [+[CBIdentity identityWithUUIDString:authority:]](https://developer.apple.com/documentation/collaboration/cbidentity/1423855-identitywithuuidstring)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` + (CBIdentity *)identityWithUUIDString:(NSString *)uuid authority:(CBIdentityAuthority *)authority ``` | -- |
| To | ``` + (CBIdentity * _Nullable)identityWithUUIDString:(NSString * _Nonnull)uuid authority:(CBIdentityAuthority * _Nonnull)authority ``` | OS X 10.11 |

Modified [CBIdentity.image](https://developer.apple.com/documentation/collaboration/cbidentity/1423873-image)

|  | Declaration |
| --- | --- |
| From | ``` - (NSImage *)image ``` |
| To | ``` @property(readonly, nonatomic, nullable) NSImage *image ``` |

Modified [-[CBIdentity isMemberOfGroup:]](https://developer.apple.com/documentation/collaboration/cbidentity/1423867-ismember)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)isMemberOfGroup:(CBGroupIdentity *)group ``` |
| To | ``` - (BOOL)isMemberOfGroup:(CBGroupIdentity * _Nonnull)group ``` |

Modified [CBIdentity.persistentReference](https://developer.apple.com/documentation/collaboration/cbidentity/1423911-persistentreference)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)persistentReference ``` |
| To | ``` @property(readonly, nonatomic, nullable) NSData *persistentReference ``` |

Modified [CBIdentity.posixName](https://developer.apple.com/documentation/collaboration/cbidentity/1423913-posixname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)posixName ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSString *posixName ``` |

Modified [CBIdentity.UUIDString](https://developer.apple.com/documentation/collaboration/cbidentity/1423879-uuidstring)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (NSString *)UUIDString ``` | -- |
| To | ``` @property(readonly, nonatomic, nonnull) NSString *UUIDString ``` | OS X 10.11 |

Modified [-[CBUserIdentity authenticateWithPassword:]](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423892-authenticatewithpassword)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)authenticateWithPassword:(NSString *)password ``` |
| To | ``` - (BOOL)authenticateWithPassword:(NSString * _Nonnull)password ``` |

Modified [CBUserIdentity.certificate](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423917-certificate)

|  | Declaration |
| --- | --- |
| From | ``` - (SecCertificateRef)certificate ``` |
| To | ``` @property(readonly, nonatomic, nullable) SecCertificateRef certificate ``` |

Modified [CBUserIdentity.posixUID](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423927-posixuid)

|  | Declaration |
| --- | --- |
| From | ``` - (uid_t)posixUID ``` |
| To | ``` @property(readonly, nonatomic) uid_t posixUID ``` |

Modified [+[CBUserIdentity userIdentityWithPosixUID:authority:]](https://developer.apple.com/documentation/collaboration/cbuseridentity/1423925-useridentitywithposixuid)

|  | Declaration |
| --- | --- |
| From | ``` + (CBUserIdentity *)userIdentityWithPosixUID:(uid_t)uid authority:(CBIdentityAuthority *)authority ``` |
| To | ``` + (CBUserIdentity * _Nullable)userIdentityWithPosixUID:(uid_t)uid authority:(CBIdentityAuthority * _Nonnull)authority ``` |

#### CBIdentityAuthority.h

Modified [CBIdentityAuthority.CSIdentityAuthority](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1514476-csidentityauthority)

|  | Declaration |
| --- | --- |
| From | ``` - (CSIdentityAuthorityRef)CSIdentityAuthority ``` |
| To | ``` @property(readonly, nonnull) CSIdentityAuthorityRef CSIdentityAuthority ``` |

Modified [+[CBIdentityAuthority defaultIdentityAuthority]](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1423853-defaultidentityauthority)

|  | Declaration |
| --- | --- |
| From | ``` + (CBIdentityAuthority *)defaultIdentityAuthority ``` |
| To | ``` + (CBIdentityAuthority * _Nonnull)defaultIdentityAuthority ``` |

Modified [+[CBIdentityAuthority identityAuthorityWithCSIdentityAuthority:]](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1514478-identityauthoritywithcsidentitya)

|  | Declaration |
| --- | --- |
| From | ``` + (CBIdentityAuthority *)identityAuthorityWithCSIdentityAuthority:(CSIdentityAuthorityRef)CSIdentityAuthority ``` |
| To | ``` + (CBIdentityAuthority * _Nonnull)identityAuthorityWithCSIdentityAuthority:(CSIdentityAuthorityRef _Nonnull)CSIdentityAuthority ``` |

Modified [+[CBIdentityAuthority localIdentityAuthority]](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1423861-localidentityauthority)

|  | Declaration |
| --- | --- |
| From | ``` + (CBIdentityAuthority *)localIdentityAuthority ``` |
| To | ``` + (CBIdentityAuthority * _Nonnull)localIdentityAuthority ``` |

Modified [CBIdentityAuthority.localizedName](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1423875-localizedname)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)localizedName ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSString *localizedName ``` |

Modified [+[CBIdentityAuthority managedIdentityAuthority]](https://developer.apple.com/documentation/collaboration/cbidentityauthority/1423865-managed)

|  | Declaration |
| --- | --- |
| From | ``` + (CBIdentityAuthority *)managedIdentityAuthority ``` |
| To | ``` + (CBIdentityAuthority * _Nonnull)managedIdentityAuthority ``` |

#### CBIdentityPicker.h

Removed [-[CBIdentityPicker setAllowsMultipleSelection:]](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423921-allowsmultipleselection)Removed [-[CBIdentityPicker setTitle:]](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423919-title)Added [-[CBIdentityPicker runModalForWindow:completionHandler:]](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423915-runmodalforwindow)Modified [CBIdentityPicker.allowsMultipleSelection](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423921-allowsmultipleselection)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)allowsMultipleSelection ``` |
| To | ``` @property(readwrite, nonatomic) BOOL allowsMultipleSelection ``` |

Modified [CBIdentityPicker.identities](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423877-identities)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)identities ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSArray<CBIdentity *> *identities ``` |

Modified [-[CBIdentityPicker runModalForWindow:modalDelegate:didEndSelector:contextInfo:]](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423893-runmodal)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (void)runModalForWindow:(NSWindow *)window modalDelegate:(id)delegate didEndSelector:(SEL)didEndSelector contextInfo:(void *)contextInfo ``` | -- |
| To | ``` - (void)runModalForWindow:(NSWindow * _Nonnull)window modalDelegate:(id _Nullable)delegate didEndSelector:(SEL _Nullable)didEndSelector contextInfo:(void * _Nullable)contextInfo ``` | OS X 10.11 |

Modified [CBIdentityPicker.title](https://developer.apple.com/documentation/collaboration/cbidentitypicker/1423919-title)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)title ``` |
| To | ``` @property(readwrite, nonatomic, copy, nullable) NSString *title ``` |

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
