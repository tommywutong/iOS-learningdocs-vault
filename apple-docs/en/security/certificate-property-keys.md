---
title: Certificate Property Keys
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/certificate-property-keys
source_url: 'https://developer.apple.com/documentation/security/certificate-property-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/certificate-property-keys.json'
content_hash: 'sha256:ba98730307fa9ca9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Certificates](certificates.md)

# Certificate Property Keys

<sub>API Collection</sub>

Recognize the dictionary keys that taken together define a certificate property.

## Overview

These are the keys that appear in the property dictionaries that describe a certificate. Each property dictionary includes a key for the property type, a label for the property, a localized label, and the property value itself. Many property dictionaries are in turn collected into a larger dictionary that is returned by a call to the [SecCertificateCopyValues](<seccertificatecopyvalues(______).md>) function.

## Topics

### Constants

- [kSecPropertyKeyType](ksecpropertykeytype.md) — A key whose value indicates the type of certificate property.
- [kSecPropertyKeyLabel](ksecpropertykeylabel.md) — A key whose value is the label for a certificate property.
- [kSecPropertyKeyLocalizedLabel](ksecpropertykeylocalizedlabel.md) — A key whose value is the localized label for a certificate property.
- [kSecPropertyKeyValue](ksecpropertykeyvalue.md) — A key whose value is the value for a certificate property.
