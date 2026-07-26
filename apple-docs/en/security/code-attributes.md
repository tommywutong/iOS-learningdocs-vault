---
title: Code Attributes
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/code-attributes
source_url: 'https://developer.apple.com/documentation/security/code-attributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/code-attributes.json'
content_hash: 'sha256:6f5a36100480340f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Code Signing Services](code-signing-services.md)

# Code Attributes

<sub>API Collection</sub>

Specify these keys from the attribute dictionary when you create a static code instance.

## Overview

Use these keys in the attribute dictionary when calling the [SecStaticCodeCreateWithPathAndAttributes](<secstaticcodecreatewithpathandattributes(________).md>) function.

## Topics

### Constants

- [kSecCodeAttributeArchitecture](kseccodeattributearchitecture.md) — A key whose value is a string that indicates an architecture, such as `i386` or `x86_64`.
- [kSecCodeAttributeSubarchitecture](kseccodeattributesubarchitecture.md) — A key whose value is a string indicating a specific processor type, such as `i686` or `core2`.
- [kSecCodeAttributeBundleVersion](kseccodeattributebundleversion.md) — A key whose value indicates the bundle version.
- [kSecCodeAttributeUniversalFileOffset](kseccodeattributeuniversalfileoffset.md) — A key whose value indicates the offset of a Mach-O specific slice of a universal Mach-O file.
