---
title: Storing a DER-Encoded X.509 Certificate
framework: Security
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/storing-a-der-encoded-x-509-certificate
source_url: 'https://developer.apple.com/documentation/security/storing-a-der-encoded-x-509-certificate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/storing-a-der-encoded-x-509-certificate.json'
content_hash: 'sha256:df478d2660a81cab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Certificates](certificates.md)

# Storing a DER-Encoded X.509 Certificate

<sub>Article</sub>

Import and export a certificate from a file.

## Overview

Certificates are not secret and you often want to share them to disseminate a public key, but [SecCertificate](seccertificate.md) is an opaque type that you can’t distribute directly. Instead, you create a Distinguished Encoding Rules (DER) encoded data representation of the certificate using the [SecCertificateCopyData](<seccertificatecopydata(__).md>) function:

**Swift**

```swift
let certificate = <# a certificate #>
let certData = SecCertificateCopyData(certificate) as Data
```

**Objective-C**

```objc
SecCertificateRef certificate = <# a certificate #>;
NSData* certData = (NSData*)CFBridgingRelease( // ARC takes ownership
                       SecCertificateCopyData(certificate)
                    );
```

You might send this data object over a network connection or store it in a `.cer` file:

**Swift**

```swift
certData.write(to: <# a URL #>)
```

**Objective-C**

```objc
[certData writeToURL:<# a URL #> atomically:YES];
```

When you receive such a data object, you use the [SecCertificateCreateWithData](<seccertificatecreatewithdata(____).md>) function to reverse the process:

**Swift**

```swift
let certificate = SecCertificateCreateWithData(nil, certData as CFData)
```

**Objective-C**

```objc
SecCertificateRef certificate =
    SecCertificateCreateWithData(NULL, (__bridge CFDataRef)certData);
		 
if (certificate)  { CFRelease(certificate); } // After you are done with it
```

By leaving the first argument empty, you rely on the default allocator to allocate memory for the certificate. Note that in Objective-C, you call [CFRelease](../corefoundation/cfrelease.md) to free the certificate’s memory when you are done with it. In Swift, the system manages the object’s memory automatically.
