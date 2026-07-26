---
title: SecCertificateSetPreference
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seccertificatesetpreference
source_url: 'https://developer.apple.com/documentation/security/seccertificatesetpreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccertificatesetpreference.json'
content_hash: 'sha256:cb28a669732e2a4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCertificateSetPreference

<sub>Function</sub>

Sets the preferred certificate for a specified name, key use, and date.

<sub>macOS</sub>

```objc
OSStatus SecCertificateSetPreference(SecCertificateRef certificate, CFStringRef name, uint32 keyUsage, CFDateRef date);
```

## Parameters

- `certificate` — The certificate object identifying the preferred certificate.

- `name` — A string containing an email address (RFC822) or other name with which the preferred certificate is to be associated.

- `keyUsage` — A key use value, as defined in `Security.framework/cssmtype.h`. Pass `0` if you don’t want to specify a particular key use.

- `date` — The date after which this preference is no longer valid. If supplied, the preferred certificate is changed only if this date is later than the currently saved setting. Pass `NULL` if this preference should not be restricted by date.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This function is typically used to set the preferred encryption certificate for an email recipient, either manually (when encrypting email to a recipient) or automatically upon receipt of encrypted email.

### Special Considerations

Use [SecCertificateSetPreferred](<seccertificatesetpreferred(______).md>) for new development instead.

Because this preference is stored in the default keychain, if the keychain is locked, the system asks the user for a password or other token to unlock it. This function can therefore block while waiting for user input.
