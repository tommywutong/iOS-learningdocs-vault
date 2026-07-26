---
title: SecIdentitySetPreference
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/secidentitysetpreference
source_url: 'https://developer.apple.com/documentation/security/secidentitysetpreference'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secidentitysetpreference.json'
content_hash: 'sha256:e96b7a954446a9e9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecIdentitySetPreference

<sub>Function</sub>

Sets the preferred identity for the specified name and key use.

<sub>macOS</sub>

```objc
OSStatus SecIdentitySetPreference(SecIdentityRef identity, CFStringRef name, CSSM_KEYUSE keyUsage);
```

## Parameters

- `identity` — A reference to the preferred identity.

- `name` — A string containing a URI, RFC822 email address, DNS host name, or other name that uniquely identifies a service requiring this identity.

- `keyUsage` — A key use value, as defined in `Security.framework/cssmtype.h`. Pass `0` if you don’t want to specify a particular key use.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

Use [SecIdentitySetPreferred](<secidentitysetpreferred(______).md>) for new development instead.
