---
title: Creating an Identity
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/creating-an-identity
source_url: 'https://developer.apple.com/documentation/security/creating-an-identity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/creating-an-identity.json'
content_hash: 'sha256:0b17899ef3d31cce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Identities](identities.md)

# Creating an Identity

<sub>Article</sub>

Create an identity from a certificate and private key.

## Overview

In macOS, you can create an identity as a combination of a certificate and a private key. You begin by obtaining a certificate reference in one of the ways described in [Getting a Certificate](getting-a-certificate.md). You then supply that reference to the [SecIdentityCreateWithCertificate](<secidentitycreatewithcertificate(______).md>) function:

**Swift**

```swift
let certificate: SecCertificate = <# a certificate #>
var identity: SecIdentity?
let status = SecIdentityCreateWithCertificate(nil, certificate, &identity)
guard status == errSecSuccess else { throw <# an error #> }
```

**Objective-C**

```objc
SecCertificateRef certificate = <# a certificate #>;
SecIdentityRef identity = NULL;
OSStatus status =
    SecIdentityCreateWithCertificate(NULL,   // Default keychain search list
                                     certificate,
                                     &identity);
if (status != errSecSuccess) { <# Handle error #> }
else                         { <# Use identity #> }
 
if (identity) { CFRelease(identity); }  // After you are done with it
```

The function attempts to locate the corresponding private key in the default keychain list or in the keychain or keychains that you specify as the first argument. If it succeeds, as indicated by the status result, it populates the identity reference with a pointer to a newly created identity object. Otherwise, the identity reference remains empty.

To persist a copy of the identity for later use, store it in the keychain, as described in [Storing an Identity in the Keychain](storing-an-identity-in-the-keychain.md).

In Objective-C, when you are done with the identity, you are responsible for freeing the object’s memory. In Swift, the system manages the object’s memory automatically, releasing it when the object goes out of scope.
