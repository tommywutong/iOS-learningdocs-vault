---
title: SecKeyGetCredentials
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeygetcredentials
source_url: 'https://developer.apple.com/documentation/security/seckeygetcredentials'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeygetcredentials.json'
content_hash: 'sha256:da3fa3dd5e5beeeb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyGetCredentials

<sub>Function</sub>

Returns an access credential for a key.

<sub>macOS</sub>

```objc
OSStatus SecKeyGetCredentials(SecKeyRef keyRef, CSSM_ACL_AUTHORIZATION_TAG operation, SecCredentialType credentialType, const CSSM_ACCESS_CREDENTIALS **outCredentials);
```

## Parameters

- `keyRef` — The key for which you want an access credential.

- `operation` — The type of operation to be performed with this key. Possible values are listed under “Authorization tag types” in `Security.framework/cssmtype.h`.

- `credentialType` — The type of credential requested. See [SecCredentialType](seccredentialtype.md) for possible values.

- `outCredentials` — On return, points to an access credential for the specified key. This pointer remains valid until the key reference is released. Do not attempt to modify or free this data.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

An access credential is required as an input to a number of CSSM functions.
