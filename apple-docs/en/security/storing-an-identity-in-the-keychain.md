---
title: Storing an Identity in the Keychain
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/storing-an-identity-in-the-keychain
source_url: 'https://developer.apple.com/documentation/security/storing-an-identity-in-the-keychain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/storing-an-identity-in-the-keychain.json'
content_hash: 'sha256:b08212ad00940157'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Identities](identities.md)

# Storing an Identity in the Keychain

<sub>Article</sub>

Securely store an identity in the keychain.

## Overview

You store an identity in or retrieve an identity from a keychain much as you would a certificate, as described in [Storing a Certificate in the Keychain](storing-a-certificate-in-the-keychain.md).

Private keys have a one-to-many relationship with certificates. That is, a single private key can be paired with multiple certificates, but a given certificate corresponds to exactly one private key. As a result, the fields that distinguish one identity from another are the same as those of the certificate it contains. As a result, working with identities as keychain items is very much like working with certificates, with a few minor adjustments:

- Use [SecIdentity](secidentity.md) objects instead of [SecCertificate](seccertificate.md) objects.
- Use [kSecClassIdentity](ksecclassidentity.md) instead of [kSecClassCertificate](ksecclasscertificate.md) for the [kSecClass](ksecclass.md) attribute.
