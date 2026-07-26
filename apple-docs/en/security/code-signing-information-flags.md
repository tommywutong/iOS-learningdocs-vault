---
title: Code Signing Information Flags
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/code-signing-information-flags
source_url: 'https://developer.apple.com/documentation/security/code-signing-information-flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/code-signing-information-flags.json'
content_hash: 'sha256:53900ab0199b822b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Code Signing Services](code-signing-services.md)

# Code Signing Information Flags

<sub>API Collection</sub>

Use these supplemental flags to retrieve signing information.

## Overview

Use these constants with the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to specify what type of information to return. See [Signing Information Dictionary Keys](signing-information-dictionary-keys.md) for more information about the information returned.

## Topics

### Constants

- [kSecCSInternalInformation](kseccsinternalinformation.md) — Internal code signing information.
- [kSecCSSigningInformation](kseccssigninginformation.md) — Cryptographic signing information.
- [kSecCSRequirementInformation](kseccsrequirementinformation.md) — Code requirements—including the designated requirement—embedded in the code.
- [kSecCSDynamicInformation](kseccsdynamicinformation.md) — Dynamic validity information about running code.
- [kSecCSContentInformation](kseccscontentinformation.md) — More information about the file system contents making up the signed code on disk.
- [kSecCSSkipResourceDirectory](kseccsskipresourcedirectory.md) — Suppress validating the resource directory.
- [kSecCSCalculateCMSDigest](kseccscalculatecmsdigest.md)
