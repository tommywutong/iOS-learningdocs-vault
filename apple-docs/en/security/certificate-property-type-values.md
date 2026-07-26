---
title: Certificate Property Type Values
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/certificate-property-type-values
source_url: 'https://developer.apple.com/documentation/security/certificate-property-type-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/certificate-property-type-values.json'
content_hash: 'sha256:3df9bbf4ab4182c2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Certificate, Key, and Trust Services](certificate-key-and-trust-services.md) · [Certificates](certificates.md)

# Certificate Property Type Values

<sub>API Collection</sub>

Recognize the possible certificate property types.

## Overview

These are the possible values that may be assigned to the [kSecPropertyKeyType](ksecpropertykeytype.md) key in each of the property dictionaries returned by a call to the [SecCertificateCopyValues](<seccertificatecopyvalues(______).md>) function.

## Topics

### Constants

- [kSecPropertyTypeWarning](ksecpropertytypewarning.md) — A key whose value is a string describing a trust evaluation warning.
- [kSecPropertyTypeSuccess](ksecpropertytypesuccess.md) — A key whose value is a string describing a trust evaluation success.
- [kSecPropertyTypeSection](ksecpropertytypesection.md) — A key whose value is a string describing the name of a field in the certificate (`CFSTR("Subject Name")`, for example).
- [kSecPropertyTypeData](ksecpropertytypedata.md) — A key whose value is a data object.
- [kSecPropertyTypeString](ksecpropertytypestring.md) — A key whose value is a string.
- [kSecPropertyTypeURL](ksecpropertytypeurl.md) — Specifies a key whose value is a URL.
- [kSecPropertyTypeDate](ksecpropertytypedate.md) — Specifies a key whose value is a string containing a date (or a string listing the bytes of an invalid date).
- [kSecPropertyTypeArray](ksecpropertytypearray.md) — Specifies a key whose value is an array.
- [kSecPropertyTypeNumber](ksecpropertytypenumber.md) — Specifies a key whose value is a number.
- [kSecPropertyTypeTitle](ksecpropertytypetitle.md) — Specifies a key whose value is a string containing the title (display name) of the certificate.
- [kSecPropertyTypeError](ksecpropertytypeerror.md) — Specifies a key whose value is a string containing the reason for a trust evaluation failure.
