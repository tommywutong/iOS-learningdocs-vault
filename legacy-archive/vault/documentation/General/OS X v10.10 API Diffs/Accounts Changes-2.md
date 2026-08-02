---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/Accounts.html
archived_at: '2026-07-15T07:34:48.609271Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# Accounts Changes

## Accounts (Added)

Added ACAccountAdded ACAccount.accountDescriptionAdded ACAccount.accountTypeAdded ACAccount.init(accountType: ACAccountType!)Added ACAccount.credentialAdded ACAccount.identifierAdded ACAccount.usernameAdded ACAccountCredentialAdded ACAccountCredential.init(OAuth2Token: String!, refreshToken: String!, expiryDate: NSDate!)Added ACAccountCredential.init(OAuthToken: String!, tokenSecret: String!)Added ACAccountCredential.oauthTokenAdded ACAccountCredentialRenewResult [enum]Added ACAccountCredentialRenewResult.FailedAdded ACAccountCredentialRenewResult.RejectedAdded ACAccountCredentialRenewResult.RenewedAdded ACAccountStoreAdded ACAccountStore.accountTypeWithAccountTypeIdentifier(String!) -> ACAccountType!Added ACAccountStore.accountWithIdentifier(String!) -> ACAccount!Added ACAccountStore.accountsAdded ACAccountStore.accountsWithAccountType(ACAccountType!) -> [AnyObject]!Added ACAccountStore.removeAccount(ACAccount!, withCompletionHandler: ACAccountStoreRemoveCompletionHandler!)Added ACAccountStore.renewCredentialsForAccount(ACAccount!, completion: ACAccountStoreCredentialRenewalHandler!)Added ACAccountStore.requestAccessToAccountsWithType(ACAccountType!, options:[NSObject: AnyObject]!, completion: ACAccountStoreRequestAccessCompletionHandler!)Added ACAccountStore.saveAccount(ACAccount!, withCompletionHandler: ACAccountStoreSaveCompletionHandler!)Added ACAccountTypeAdded ACAccountType.accessGrantedAdded ACAccountType.accountTypeDescriptionAdded ACAccountType.identifierAdded ACErrorCode [struct]Added ACErrorCode.init(_: UInt32)Added ACErrorCode.valueAdded ACAccountStoreCredentialRenewalHandlerAdded ACAccountStoreDidChangeNotificationAdded ACAccountStoreRemoveCompletionHandlerAdded ACAccountStoreRequestAccessCompletionHandlerAdded ACAccountStoreSaveCompletionHandlerAdded ACAccountTypeIdentifierFacebookAdded ACAccountTypeIdentifierLinkedInAdded ACAccountTypeIdentifierSinaWeiboAdded ACAccountTypeIdentifierTencentWeiboAdded ACAccountTypeIdentifierTwitterAdded ACErrorAccessDeniedByProtectionPolicyAdded ACErrorAccessInfoInvalidAdded ACErrorAccountAlreadyExistsAdded ACErrorAccountAuthenticationFailedAdded ACErrorAccountMissingRequiredPropertyAdded ACErrorAccountNotFoundAdded ACErrorAccountTypeInvalidAdded ACErrorClientPermissionDeniedAdded ACErrorCredentialNotFoundAdded ACErrorDomainAdded ACErrorFetchCredentialFailedAdded ACErrorInvalidClientBundleIDAdded ACErrorPermissionDeniedAdded ACErrorRemoveCredentialFailedAdded ACErrorStoreCredentialFailedAdded ACErrorUnknownAdded ACErrorUpdatingNonexistentAccountAdded ACFacebookAppIdKeyAdded ACFacebookAudienceEveryoneAdded ACFacebookAudienceFriendsAdded ACFacebookAudienceKeyAdded ACFacebookAudienceOnlyMeAdded ACFacebookPermissionsKeyAdded ACLinkedInAppIdKeyAdded ACLinkedInPermissionsKeyAdded ACTencentWeiboAppIdKey

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
