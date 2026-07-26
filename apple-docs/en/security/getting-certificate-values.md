---
title: Getting Certificate Values
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/getting-certificate-values
source_url: 'https://developer.apple.com/documentation/security/getting-certificate-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/getting-certificate-values.json'
content_hash: 'sha256:dae373220e832e75'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Certificates](certificates.md)

# Getting Certificate Values

<sub>Article</sub>

Obtain all the values associated with a certificate.

## Overview

In macOS, you can also dig deeper into the certificate content using a call to the [SecCertificateCopyValues](<seccertificatecopyvalues(______).md>) function:

**Swift**

```swift
var error: Unmanaged<CFError>?
guard let dict = SecCertificateCopyValues(certificate,nil,&error) else {
    throw error!.takeRetainedValue() as Error
}
```

**Objective-C**

```objc
CFErrorRef error = NULL;
NSDictionary* dict = (NSDictionary*)CFBridgingRelease(  // ARC takes ownership
                       SecCertificateCopyValues(certificate, NULL, &error)
                    );
if (!dict) {
    NSError *err = CFBridgingRelease(error);            // ARC takes ownership
    // Handle the error. . .
}
```

The return value is a dictionary with keys corresponding to the OID values found in [Certificate OIDs](certificate-oids.md). Each value is itself a dictionary that contains information about the certificate’s fields and extensions.
