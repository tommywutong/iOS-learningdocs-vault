---
title: SecCertificateCopyPreference
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seccertificatecopypreference
source_url: 'https://developer.apple.com/documentation/security/seccertificatecopypreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatecopypreference.json'
content_hash: 'sha256:2cd51e03a1cf06d1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateCopyPreference

<sub>Function</sub>

Retrieves the preferred certificate for the specified name and key use.

<sub>macOS</sub>

```objc
OSStatus SecCertificateCopyPreference(CFStringRef name, uint32 keyUsage, SecCertificateRef*certificate);
```

## Parameters

- `name` — A string containing an email address (RFC822) or other name for which a preferred certificate is requested.

- `keyUsage` — A key use value, as defined in `Security.framework/cssmtype.h`. Pass `0` to ignore this parameter.

- `certificate` — On return, a reference to the preferred certificate, or `NULL` if none was found. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release this object when you are finished with it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function is typically used to obtain the preferred encryption certificate for an email recipient.

### Special Considerations

Use [SecCertificateCopyPreferred](<seccertificatecopypreferred(____).md>) for new development instead.
