---
title: WrapKey
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_spi_csp_funcs-c.struct/wrapkey
source_url: 'https://developer.apple.com/documentation/security/cssm_spi_csp_funcs-c.struct/wrapkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_spi_csp_funcs-c.struct/wrapkey.json'
content_hash: 'sha256:b0274fb5c81802f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [cssm_spi_csp_funcs](../cssm_spi_csp_funcs-c.struct.md)

# WrapKey

<sub>Instance Property</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(long, unsigned long long, const struct cssm_context *, const struct cssm_access_credentials *, const struct cssm_key *, const struct cssm_data *, struct cssm_key *, unsigned long long) WrapKey;
```
