---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/VideoSubscriberAccount.html
archived_at: '2026-07-18T02:55:00.037380Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# VideoSubscriberAccount Changes for Objective-C

### VideoSubscriberAccount (Added)

#### VideoSubscriberAccountDefines.h (Added)

Added #def VS_EXPORTAdded #def VS_EXTERN

#### VideoSubscriberAccountErrors.h (Added)

Added VSErrorCodeAdded VSErrorCodeAccessNotGrantedAdded VSErrorCodeInvalidVerificationTokenAdded VSErrorCodeProviderRejectedAdded VSErrorCodeServiceTemporarilyUnavailableAdded VSErrorCodeUnsupportedProviderAdded VSErrorCodeUserCancelledAdded VSErrorDomainAdded VSErrorInfoKeySAMLResponseAdded VSErrorInfoKeySAMLResponseStatusAdded VSErrorInfoKeyUnsupportedProviderIdentifier

#### VSAccountManager.h (Added)

Added VSAccountManagerAdded -[VSAccountManager checkAccessStatusWithOptions:completionHandler:]Added VSAccountManager.delegateAdded -[VSAccountManager enqueueAccountMetadataRequest:completionHandler:]Added VSAccountManagerDelegateAdded -[VSAccountManagerDelegate accountManager:dismissViewController:]Added -[VSAccountManagerDelegate accountManager:presentViewController:]Added VSAccountAccessStatusAdded VSAccountAccessStatusDeniedAdded VSAccountAccessStatusGrantedAdded VSAccountAccessStatusNotDeterminedAdded VSAccountAccessStatusRestrictedAdded VSCheckAccessOptionAdded VSCheckAccessOptionPrompt

#### VSAccountManagerResult.h (Added)

Added VSAccountManagerResultAdded -[VSAccountManagerResult cancel]

#### VSAccountMetadata.h (Added)

Added VSAccountMetadataAdded VSAccountMetadata.accountProviderIdentifierAdded VSAccountMetadata.authenticationExpirationDateAdded VSAccountMetadata.SAMLAttributeQueryResponseAdded VSAccountMetadata.verificationData

#### VSAccountMetadataRequest.h (Added)

Added VSAccountMetadataRequestAdded VSAccountMetadataRequest.attributeNamesAdded VSAccountMetadataRequest.channelIdentifierAdded VSAccountMetadataRequest.forceAuthenticationAdded VSAccountMetadataRequest.includeAccountProviderIdentifierAdded VSAccountMetadataRequest.includeAuthenticationExpirationDateAdded VSAccountMetadataRequest.interruptionAllowedAdded VSAccountMetadataRequest.localizedVideoTitleAdded VSAccountMetadataRequest.supportedAccountProviderIdentifiersAdded VSAccountMetadataRequest.verificationToken

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
