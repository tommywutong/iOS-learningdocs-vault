---
title: GenerateKey
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_spi_csp_funcs-c.struct/generatekey
source_url: 'https://developer.apple.com/documentation/security/cssm_spi_csp_funcs-c.struct/generatekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_spi_csp_funcs-c.struct/generatekey.json'
content_hash: 'sha256:b80d08c5e084591c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [cssm_spi_csp_funcs](../cssm_spi_csp_funcs-c.struct.md)

# GenerateKey

<sub>Instance Property</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(long, unsigned long long, const struct cssm_context *, unsigned int, unsigned int, const struct cssm_data *, const struct cssm_resource_control_context *, struct cssm_key *, unsigned long long) GenerateKey;
```
