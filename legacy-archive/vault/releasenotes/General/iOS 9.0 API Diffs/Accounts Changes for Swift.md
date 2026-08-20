---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/Accounts.html
archived_at: '2026-07-18T02:56:40.069746Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Accounts Changes for Swift

### Accounts

Removed ACErrorCode.valueAdded ACErrorCode.init(rawValue: UInt32)Added ACErrorCode.rawValueAdded [ACErrorCredentialItemNotExpired](https://developer.apple.com/documentation/accounts/acerrorcredentialitemnotexpired)Added [ACErrorCredentialItemNotFound](https://developer.apple.com/documentation/accounts/acerrorcredentialitemnotfound)Modified [ACAccount](https://developer.apple.com/documentation/accounts/acaccount)

|  | Declaration |
| --- | --- |
| From | ``` class ACAccount : NSObject {     init!(accountType type: ACAccountType!)     var identifier: String! { get }     var accountType: ACAccountType!     var accountDescription: String!     var username: String!     var userFullName: String! { get }     var credential: ACAccountCredential! } ``` |
| To | ``` class ACAccount : NSObject {     init!(accountType type: ACAccountType!)     var identifier: String? { get }     var accountType: ACAccountType!     var accountDescription: String!     var username: String!     var userFullName: String! { get }     var credential: ACAccountCredential! } ``` |

Modified [ACAccount.identifier](https://developer.apple.com/documentation/accounts/acaccount/1543840-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String? { get } ``` |

Modified [ACAccountCredentialRenewResult [enum]](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [ACAccountStore](https://developer.apple.com/documentation/accounts/acaccountstore)

|  | Declaration |
| --- | --- |
| From | ``` class ACAccountStore : NSObject {     var accounts: [AnyObject]! { get }     func accountWithIdentifier(_ identifier: String!) -> ACAccount!     func accountTypeWithAccountTypeIdentifier(_ typeIdentifier: String!) -> ACAccountType!     func accountsWithAccountType(_ accountType: ACAccountType!) -> [AnyObject]!     func saveAccount(_ account: ACAccount!, withCompletionHandler completionHandler: ACAccountStoreSaveCompletionHandler!)     func requestAccessToAccountsWithType(_ accountType: ACAccountType!, withCompletionHandler handler: ACAccountStoreRequestAccessCompletionHandler!)     func requestAccessToAccountsWithType(_ accountType: ACAccountType!, options options: [NSObject : AnyObject]!, completion completion: ACAccountStoreRequestAccessCompletionHandler!)     func renewCredentialsForAccount(_ account: ACAccount!, completion completionHandler: ACAccountStoreCredentialRenewalHandler!)     func removeAccount(_ account: ACAccount!, withCompletionHandler completionHandler: ACAccountStoreRemoveCompletionHandler!) } ``` |
| To | ``` class ACAccountStore : NSObject {     var accounts: [AnyObject]? { get }     func accountWithIdentifier(_ identifier: String!) -> ACAccount!     func accountTypeWithAccountTypeIdentifier(_ typeIdentifier: String!) -> ACAccountType!     func accountsWithAccountType(_ accountType: ACAccountType!) -> [AnyObject]!     func saveAccount(_ account: ACAccount!, withCompletionHandler completionHandler: ACAccountStoreSaveCompletionHandler!)     func requestAccessToAccountsWithType(_ accountType: ACAccountType!, withCompletionHandler handler: ACAccountStoreRequestAccessCompletionHandler!)     func requestAccessToAccountsWithType(_ accountType: ACAccountType!, options options: [NSObject : AnyObject]!, completion completion: ACAccountStoreRequestAccessCompletionHandler!)     func renewCredentialsForAccount(_ account: ACAccount!, completion completionHandler: ACAccountStoreCredentialRenewalHandler!)     func removeAccount(_ account: ACAccount!, withCompletionHandler completionHandler: ACAccountStoreRemoveCompletionHandler!) } ``` |

Modified [ACAccountStore.accounts](https://developer.apple.com/documentation/accounts/acaccountstore/1493961-accounts)

|  | Declaration |
| --- | --- |
| From | ``` var accounts: [AnyObject]! { get } ``` |
| To | ``` var accounts: [AnyObject]? { get } ``` |

Modified [ACErrorCode [struct]](https://developer.apple.com/documentation/accounts/acerrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ACErrorCode {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct ACErrorCode : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

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
