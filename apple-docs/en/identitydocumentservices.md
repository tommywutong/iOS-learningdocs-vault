---
title: IdentityDocumentServices
framework: IdentityDocumentServices
symbol_kind: module
role: collection
role_heading: Framework
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/identitydocumentservices
source_url: 'https://developer.apple.com/documentation/identitydocumentservices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/identitydocumentservices.json'
content_hash: 'sha256:3df97637ea876325'
translated: false
---

> Navigation: [Technologies](technologies.md)

# IdentityDocumentServices

<sub>Framework</sub>

Share mobile documents using the Digital Credentials API.

## Overview

Identity Document Services enables the presentment of identity documents on device and web browser support for the Digital Credentials API.

![A conceptual image that shows a small identity document and a rectangular web page.](../../attachments/fe83fe395f5f3bb1f92833a0c1798345/identity-document-services-hero~dark@2x.png)

Once authorized, a person can select your app during a identity documents request, where they can authorize the presentment of identification through a UI you create with [IdentityDocumentServicesUI](identitydocumentservicesui.md).

This framework also enables web browsers to implement the presentment flow for the Digital Credentials API. With web browser support, a person can present identity documents locally on their device or remotely on another device using the same iCloud account. Identity documents can include documents such as a driver’s license or identity card.

## Topics

### Essentials

- [Requesting a mobile document on the web](identitydocumentservices/requesting-a-mobile-document-on-the-web.md) — Send a request for mobile document information for apps installed on a device.
- [Implementing as an identity document provider](identitydocumentservices/implenting-as-an-identity-document-provider.md) — Add your app as an option for mobile document web presentment.
- [Verifying a mobile document from a passport](identitydocumentservices/verifying-a-mobile-document-from-a-passport.md) — Validate a response from mobile document information derived from a passport.

### Registering as an identity document provider

- [IdentityDocumentProviderRegistrationStore](identitydocumentservices/identitydocumentproviderregistrationstore.md) — A store that notifies the system which documents an app has available for presentment.
- [IdentityDocumentRegistration](identitydocumentservices/identitydocumentregistration.md) — A protocol that defines an identity document registration.
- [MobileDocumentRegistration](identitydocumentservices/mobiledocumentregistration.md) — A type you use to register mobile documents.

### Implementing the web presentment flow into your browser

- [IdentityDocumentWebPresentmentRawRequestValidator](identitydocumentservices/identitydocumentwebpresentmentrawrequestvalidator.md) — A type that contains functions for validating the incoming web presentment raw request.
- [IdentityDocumentWebPresentmentRequest](identitydocumentservices/identitydocumentwebpresentmentrequest.md) — A closed protocol that indicates that the system uses this object to perform an identity document web presentment
- [ISO18013MobileDocumentRequest](identitydocumentservices/iso18013mobiledocumentrequest.md) — A type that represents an incoming ISO 18013-5 mobile document request.
- [IdentityDocumentWebPresentmentResponse](identitydocumentservices/identitydocumentwebpresentmentresponse.md) — A closed protocol that indicates that the system uses this object to represent a web presentment response.
- [ISO18013MobileDocumentResponse](identitydocumentservices/iso18013mobiledocumentresponse.md) — A type representing the document response from a web presentment request.
- [IdentityDocumentWebPresentmentRawRequest](identitydocumentservices/identitydocumentwebpresentmentrawrequest.md) — A struct that defines the type that represents a raw web presentment request.

### Structures

- [IdentityDocumentPresentmentError](identitydocumentservices/identitydocumentpresentmenterror.md) — An error type that is thrown from the identity document web presentment controller.
