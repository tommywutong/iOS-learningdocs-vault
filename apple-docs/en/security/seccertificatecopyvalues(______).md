---
title: 'SecCertificateCopyValues(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccertificatecopyvalues(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopyvalues(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopyvalues%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:35c08a29db525934'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyValues(_:_:_:)

<sub>Function</sub>

Creates a dictionary that represents a certificate’s contents.

<sub>macOS</sub>

```swift
func SecCertificateCopyValues(_ certificate: SecCertificate, _ keys: CFArray?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary?
```

## Parameters

- `certificate` — The certificate from which values should be copied.

- `keys` — An array of string OID values, or `NULL`. If non-`NULL`, these OID values determine which values from the certificate to return. If `NULL`, all values are returned. Only OIDs that represent top-level keys in the returned dictionary can be specified. Unknown OIDs are ignored. See [Certificate OIDs](certificate-oids.md) for the list of known OIDs.

- `error` — A pointer to a [CFError](../corefoundation/cferror.md) variable where an error object is stored upon failure. If not `NULL`, the caller is responsible for checking this variable and releasing the resulting object if it exists.

## Return Value

A dictionary containing the specified values from the certificate or `NULL` if an error occurs. In Objective-C, free this dictionary with a call to the [CFRelease](../corefoundation/cfrelease.md) function when you are done with it.

## Discussion

Each entry in this dictionary is itself a dictionary with the keys described in [Certificate Property Keys](certificate-property-keys.md).
