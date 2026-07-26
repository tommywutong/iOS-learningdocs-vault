---
title: Code Signing Architecture Flags
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/code-signing-architecture-flags
source_url: 'https://developer.apple.com/documentation/security/code-signing-architecture-flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/code-signing-architecture-flags.json'
content_hash: 'sha256:b600cfa523b0ce32'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Code Signing Services](code-signing-services.md)

# Code Signing Architecture Flags

<sub>API Collection</sub>

Use these supplemental flags to get static code.

## Overview

These flags supplement the flags described in [SecCSFlags](seccsflags.md). Use these additional constants with the `flags` parameter of the [SecCodeCopyStaticCode](<seccodecopystaticcode(______).md>) function.

## Topics

### Constants

- [kSecCSUseAllArchitectures](kseccsuseallarchitectures.md) — Flag for requesting all architectures.
