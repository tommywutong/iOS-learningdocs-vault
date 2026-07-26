---
title: Video Subscriber Account
framework: Video Subscriber Account
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.14+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/videosubscriberaccount
source_url: 'https://developer.apple.com/documentation/videosubscriberaccount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/videosubscriberaccount.json'
content_hash: 'sha256:78dd63de866c4a5c'
translated: false
---

> Navigation: [Technologies](technologies.md)

# Video Subscriber Account

<sub>Framework</sub>

Support TV provider and Apple TV app functionality.

## Overview

`VideoSubscriberAccount` provides APIs to help you create apps that require secure communication with a TV provider’s authentication service. The framework also informs the Apple TV app about whether someone has a subscription and the details of that subscription.

## Topics

### Essentials

- [Video Subscriber Account updates](updates/videosubscriberaccount.md) — Learn about important changes in Video Subscriber Account.

### TV provider authentication

- [VSAccountManager](videosubscriberaccount/vsaccountmanager.md) — The object that coordinates your app’s authentication requests with a TV provider’s authentication service.

### TV app integration

- [VSAppleSubscription](videosubscriberaccount/vsapplesubscription-swift.struct.md) — An Apple streaming service customer and their subscriptions.
- [VSSubscriptionRegistrationCenter](videosubscriberaccount/vssubscriptionregistrationcenter.md) — An object that stores subscription information that the system provides to the Apple TV app.
- [VSAccountApplicationProvider](videosubscriberaccount/vsaccountapplicationprovider.md) — An object to display app-specific providers in your app.

### User account management

- [Signing people in to their media accounts automatically](videosubscriberaccount/signing-people-in-to-media-apps-automatically.md) — Implement single sign-on for media-streaming apps by managing a sign-in token on a person’s Apple Account.
- [VSUserAccountManager](videosubscriberaccount/vsuseraccountmanager.md) — The object that coordinates your app’s user account actions.
- [VSUserAccount](videosubscriberaccount/vsuseraccount-swift.struct.md) — An object that represents a user’s account.

### Errors

- [VSErrorDomain](videosubscriberaccount/vserrordomain.md) — The domain for all errors in the framework.
- [VSErrorInfoKeySAMLResponse](videosubscriberaccount/vserrorinfokeysamlresponse.md) — The subscription provider’s SAML error response.
- [VSErrorInfoKeySAMLResponseStatus](videosubscriberaccount/vserrorinfokeysamlresponsestatus.md) — The subscription provider’s SAML error-response status code.
- [VSErrorInfoKeyAccountProviderResponse](videosubscriberaccount/vserrorinfokeyaccountproviderresponse.md) — The account provider’s error-response object.
- [VSErrorInfoKeyUnsupportedProviderIdentifier](videosubscriberaccount/vserrorinfokeyunsupportedprovideridentifier.md) — The identifier of the unsupported subscription provider.
- [VSError](videosubscriberaccount/vserror.md) — Error information in the framework error domain.
- [Code](videosubscriberaccount/vserror/code.md) — Error codes in the framework error domain.

### Deprecated

- [VSSubscription](videosubscriberaccount/vssubscription.md) — An object that describes a subscriber’s access to content. _(deprecated)_
