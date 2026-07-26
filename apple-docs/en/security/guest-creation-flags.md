---
title: Guest Creation Flags
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/guest-creation-flags
source_url: 'https://developer.apple.com/documentation/security/guest-creation-flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/guest-creation-flags.json'
content_hash: 'sha256:92e7a1632602317f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Code Signing Services](code-signing-services.md)

# Guest Creation Flags

<sub>API Collection</sub>

Use these supplemental flags to create a guest object.

## Overview

These flags supplement the flags described in [SecCSFlags](seccsflags.md). Use these additional constants with the flags parameter of the [SecHostCreateGuest](sechostcreateguest.md) function.

## Topics

### Constants

- [kSecCSDedicatedHost](kseccsdedicatedhost.md) — Declares dedicated hosting for the given host.
- [kSecCSGenerateGuestHash](kseccsgenerateguesthash.md) — Ask the host to generate the unique binary identifier ([kSecCodeInfoUnique](kseccodeinfounique.md)) from the copy on disk at the path given.
