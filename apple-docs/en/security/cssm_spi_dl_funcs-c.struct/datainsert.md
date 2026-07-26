---
title: DataInsert
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.0+（10.7 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/cssm_spi_dl_funcs-c.struct/datainsert
source_url: 'https://developer.apple.com/documentation/security/cssm_spi_dl_funcs-c.struct/datainsert'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cssm_spi_dl_funcs-c.struct/datainsert.json'
content_hash: 'sha256:dd0227eac70c6ab2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [cssm_spi_dl_funcs](../cssm_spi_dl_funcs-c.struct.md)

# DataInsert

<sub>Instance Property</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct cssm_dl_db_handle, unsigned int, const struct cssm_db_record_attribute_data *, const struct cssm_data *, struct cssm_db_unique_record **) DataInsert;
```
