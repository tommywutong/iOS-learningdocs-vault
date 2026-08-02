---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Swift/VideoSubscriberAccount.html
archived_at: '2026-07-18T02:58:02.414594Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# VideoSubscriberAccount Changes for Swift

### VideoSubscriberAccount (Added)

Added VSAccountAccessStatus [enum]Added VSAccountAccessStatus.deniedAdded VSAccountAccessStatus.grantedAdded VSAccountAccessStatus.notDeterminedAdded VSAccountAccessStatus.restrictedAdded VSAccountManagerAdded VSAccountManager.checkAccessStatus(options: [VSCheckAccessOption : Any], completionHandler: (VSAccountAccessStatus, Error?) -> Swift.Void)Added VSAccountManager.delegateAdded VSAccountManager.enqueue(_: VSAccountMetadataRequest, completionHandler: (VSAccountMetadata?, Error?) -> Swift.Void) -> VSAccountManagerResultAdded VSAccountManagerDelegateAdded VSAccountManagerDelegate.accountManager(_: VSAccountManager, dismiss: UIViewController)Added VSAccountManagerDelegate.accountManager(_: VSAccountManager, present: UIViewController)Added VSAccountManagerResultAdded VSAccountManagerResult.cancel()Added VSAccountMetadataAdded VSAccountMetadata.accountProviderIdentifierAdded VSAccountMetadata.authenticationExpirationDateAdded VSAccountMetadata.samlAttributeQueryResponseAdded VSAccountMetadata.verificationDataAdded VSAccountMetadataRequestAdded VSAccountMetadataRequest.attributeNamesAdded VSAccountMetadataRequest.channelIdentifierAdded VSAccountMetadataRequest.forceAuthenticationAdded VSAccountMetadataRequest.includeAccountProviderIdentifierAdded VSAccountMetadataRequest.includeAuthenticationExpirationDateAdded VSAccountMetadataRequest.isInterruptionAllowedAdded VSAccountMetadataRequest.localizedVideoTitleAdded VSAccountMetadataRequest.supportedAccountProviderIdentifiersAdded VSAccountMetadataRequest.verificationTokenAdded VSCheckAccessOption [struct]Added VSCheckAccessOption.init(rawValue: String)Added VSCheckAccessOption.promptAdded VSError [struct]Added VSError.accessNotGrantedAdded VSError.init(_nsError: NSError)Added VSError.invalidVerificationTokenAdded VSError.providerRejectedAdded VSError.serviceTemporarilyUnavailableAdded VSError.unsupportedProviderAdded VSError.userCancelledAdded VSError.Code [enum]Added VSError.Code.accessNotGrantedAdded VSError.Code.invalidVerificationTokenAdded VSError.Code.providerRejectedAdded VSError.Code.serviceTemporarilyUnavailableAdded VSError.Code.unsupportedProviderAdded VSError.Code.userCancelledAdded VSErrorDomainAdded VSErrorInfoKeySAMLResponseAdded VSErrorInfoKeySAMLResponseStatusAdded VSErrorInfoKeyUnsupportedProviderIdentifier

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
