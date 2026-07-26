---
title: Identities
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/identities
source_url: 'https://developer.apple.com/documentation/security/identities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/identities.json'
content_hash: 'sha256:f3d2e2e6b055560d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md)

# Identities

<sub>API Collection</sub>

Combine certificates and cryptographic keys into identities.

## Overview

An identity consists of a private key packaged with the certificate that contains and vouches for the corresponding public key. You use the certificate, key, and trust services API to create an identity from a private key and its certificate, or to import an identity from a password-protected PKCS #12 file. You then use the API to extract the key and certificate from the identity. You can also use the keychain services API to store the identity to or retrieve it from a keychain, much as you would the certificate or key by itself.

## Topics

### Essentials

- [Creating an Identity](creating-an-identity.md) — Create an identity from a certificate and private key.
- [Storing an Identity in the Keychain](storing-an-identity-in-the-keychain.md) — Securely store an identity in the keychain.
- [SecIdentityCreateWithCertificate](<secidentitycreatewithcertificate(______).md>) — Creates a new identity for a certificate and its associated private key.
- [SecIdentity](secidentity.md) — An abstract Core Foundation-type object representing an identity.
- [SecIdentityGetTypeID](<secidentitygettypeid().md>) — Returns the unique identifier of the opaque type to which an identity object belongs.

### Identity Import

- [Importing an Identity](importing-an-identity.md) — Learn how to import an identity from file.
- [SecPKCS12Import](<secpkcs12import(______).md>) — Returns the identities and certificates in a PKCS #12-formatted blob.
- [Keychain Import and Export Options](keychain-import-and-export-options.md) — Use these constants when you pass dictionary-based arguments to import and export functions.
- [PKCS #12 Import Item Keys](pkcs-12-import-item-keys.md) — Recognized the dictionary keys returned by an import operation.

### Identity Components

- [Parsing an Identity](parsing-an-identity.md) — Extract the private key and certificate from an identity.
- [SecIdentityCopyCertificate](<secidentitycopycertificate(____).md>) — Retrieves a certificate associated with an identity.
- [SecIdentityCopyPrivateKey](<secidentitycopyprivatekey(____).md>) — Retrieves the private key associated with an identity.

### System Identities

- [SecIdentityCopySystemIdentity](<secidentitycopysystemidentity(______).md>) — Obtains the system identity associated with a specified domain.
- [SecIdentitySetSystemIdentity](<secidentitysetsystemidentity(____).md>) — Assigns the system identity to be associated with a specified domain.
- [System Identity Domains](system-identity-domains.md) — Set or obtain a system identity for domains.

### Identity Naming

- [SecIdentitySetPreferred](<secidentitysetpreferred(______).md>) — Sets the identity that should be preferred for the specified name and key use.
- [SecIdentityCopyPreferred](<secidentitycopypreferred(______).md>) — Retrieves the preferred identity for the specified name and key use.

### Identity Search

- [SecIdentitySearch](secidentitysearch.md) — Contains information about an identity search.

### Creating an Identity for Local Network TLS

- [Creating an Identity for Local Network TLS](../network/creating-an-identity-for-local-network-tls.md) — Learn how to create and use a digital identity in your application for local network TLS.
