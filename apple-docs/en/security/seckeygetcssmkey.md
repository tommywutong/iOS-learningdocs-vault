---
title: SecKeyGetCSSMKey
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/seckeygetcssmkey
source_url: 'https://developer.apple.com/documentation/security/seckeygetcssmkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeygetcssmkey.json'
content_hash: 'sha256:24078e08afb088af'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyGetCSSMKey

<sub>Function</sub>

Retrieves a pointer to the `CSSM_KEY` structure containing the key stored in a keychain item.

<sub>macOS</sub>

```objc
OSStatus SecKeyGetCSSMKey(SecKeyRef key, const CSSM_KEY **cssmKey);
```

## Parameters

- `key` — A keychain key item object.

- `cssmKey` — A pointer to a `CSSM_KEY` structure for the specified key. You should not modify or free this data, because it is owned by the system.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

The `CSSM_KEY` structure is used to represent keys in CSSM and is used as an input value to several CSSM functions. The `CSSM_KEY` structure is valid until the keychain item object is released.
