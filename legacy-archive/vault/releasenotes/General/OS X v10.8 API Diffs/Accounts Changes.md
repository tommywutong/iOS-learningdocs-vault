---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/Accounts.html
archived_at: '2026-07-18T02:53:55.710357Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# Accounts Changes

## Accounts

ACAccount.hAdded [ACAccount](https://developer.apple.com/documentation/accounts/acaccount)Added [ACAccount.accountDescription](https://developer.apple.com/documentation/accounts/acaccount/1543836-accountdescription)Added [ACAccount.accountType](https://developer.apple.com/documentation/accounts/acaccount/1543805-accounttype)Added [ACAccount.credential](https://developer.apple.com/documentation/accounts/acaccount/1543779-credential)Added [ACAccount.identifier](https://developer.apple.com/documentation/accounts/acaccount/1543840-identifier)Added [-[ACAccount initWithAccountType:]](https://developer.apple.com/documentation/accounts/acaccount/1543781-initwithaccounttype)Added [ACAccount.username](https://developer.apple.com/documentation/accounts/acaccount/1543839-username)ACAccountCredential.hAdded [ACAccountCredential](https://developer.apple.com/documentation/accounts/acaccountcredential)Added [-[ACAccountCredential initWithOAuth2Token:refreshToken:expiryDate:]](https://developer.apple.com/documentation/accounts/acaccountcredential/1507892-initwithoauth2token)Added [-[ACAccountCredential initWithOAuthToken:tokenSecret:]](https://developer.apple.com/documentation/accounts/acaccountcredential/1507896-initwithoauthtoken)Added [ACAccountCredential.oauthToken](https://developer.apple.com/documentation/accounts/acaccountcredential/1507894-oauthtoken)ACAccountStore.hAdded [ACAccountStore](https://developer.apple.com/documentation/accounts/acaccountstore)Added [-[ACAccountStore accountTypeWithAccountTypeIdentifier:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493967-accounttype)Added [-[ACAccountStore accountWithIdentifier:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493947-account)Added [ACAccountStore.accounts](https://developer.apple.com/documentation/accounts/acaccountstore/1493961-accounts)Added [-[ACAccountStore accountsWithAccountType:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493942-accountswithaccounttype)Added [-[ACAccountStore renewCredentialsForAccount:completion:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493959-renewcredentialsforaccount)Added [-[ACAccountStore requestAccessToAccountsWithType:options:completion:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493964-requestaccesstoaccounts)Added [-[ACAccountStore saveAccount:withCompletionHandler:]](https://developer.apple.com/documentation/accounts/acaccountstore/1493957-saveaccount)Added [ACAccountCredentialRenewResult](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult)Added [ACAccountCredentialRenewResultFailed](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult/acaccountcredentialrenewresultfailed)Added [ACAccountCredentialRenewResultRejected](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult/rejected)Added [ACAccountCredentialRenewResultRenewed](https://developer.apple.com/documentation/accounts/acaccountcredentialrenewresult/acaccountcredentialrenewresultrenewed)Added [ACAccountStoreCredentialRenewalHandler](https://developer.apple.com/documentation/accounts/acaccountstorecredentialrenewalhandler)Added [ACAccountStoreDidChangeNotification](https://developer.apple.com/documentation/foundation/nsnotification/name/1493946-acaccountstoredidchange)Added [ACAccountStoreRequestAccessCompletionHandler](https://developer.apple.com/documentation/accounts/acaccountstorerequestaccesscompletionhandler)Added [ACAccountStoreSaveCompletionHandler](https://developer.apple.com/documentation/accounts/acaccountstoresavecompletionhandler)Added [ACFacebookAppIdKey](https://developer.apple.com/documentation/accounts/acfacebookappidkey)Added ACFacebookAppVersionKeyAdded ACFacebookPermissionGroupKeyAdded ACFacebookPermissionGroupReadAdded ACFacebookPermissionGroupReadWriteAdded ACFacebookPermissionGroupWriteAdded [ACFacebookPermissionsKey](https://developer.apple.com/documentation/accounts/acfacebookpermissionskey)Added NS_ENUM() (no architecture available)ACAccountType.hAdded [ACAccountType](https://developer.apple.com/documentation/accounts/acaccounttype)Added [ACAccountType.accessGranted](https://developer.apple.com/documentation/accounts/acaccounttype/1543838-accessgranted)Added [ACAccountType.accountTypeDescription](https://developer.apple.com/documentation/accounts/acaccounttype/1543834-accounttypedescription)Added [ACAccountType.identifier](https://developer.apple.com/documentation/accounts/acaccounttype/1543833-identifier)Added [ACAccountTypeIdentifierFacebook](https://developer.apple.com/documentation/accounts/acaccounttypeidentifierfacebook)Added [ACAccountTypeIdentifierSinaWeibo](https://developer.apple.com/documentation/accounts/acaccounttypeidentifiersinaweibo)Added [ACAccountTypeIdentifierTwitter](https://developer.apple.com/documentation/accounts/acaccounttypeidentifiertwitter)ACError.hAdded [ACErrorAccessInfoInvalid](https://developer.apple.com/documentation/accounts/acerroraccessinfoinvalid)Added [ACErrorAccountAlreadyExists](https://developer.apple.com/documentation/accounts/acerrorcode/acerroraccountalreadyexists)Added [ACErrorAccountAuthenticationFailed](https://developer.apple.com/documentation/accounts/acerrorcode/acerroraccountauthenticationfailed)Added [ACErrorAccountMissingRequiredProperty](https://developer.apple.com/documentation/accounts/acerrorcode/acerroraccountmissingrequiredproperty)Added [ACErrorAccountNotFound](https://developer.apple.com/documentation/accounts/acerrorcode/acerroraccountnotfound)Added [ACErrorAccountTypeInvalid](https://developer.apple.com/documentation/accounts/acerroraccounttypeinvalid)Added [ACErrorCode](https://developer.apple.com/documentation/accounts/acerrorcode)Added [ACErrorDomain](https://developer.apple.com/documentation/accounts/acerrordomain)Added [ACErrorPermissionDenied](https://developer.apple.com/documentation/accounts/acerrorpermissiondenied)Added [ACErrorUnknown](https://developer.apple.com/documentation/accounts/acerrorcode/acerrorunknown)AccountsDefines.hAdded #def ACCOUNTS_CLASS_AVAILABLEAdded #def ACCOUNTS_EXTERN

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
