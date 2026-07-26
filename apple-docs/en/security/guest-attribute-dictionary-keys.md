---
title: Guest Attribute Dictionary Keys
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/guest-attribute-dictionary-keys
source_url: 'https://developer.apple.com/documentation/security/guest-attribute-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/guest-attribute-dictionary-keys.json'
content_hash: 'sha256:3f38e21ba16da34f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Code Signing Services](code-signing-services.md)

# Guest Attribute Dictionary Keys

<sub>API Collection</sub>

Specify attributes of guest code.

## Overview

Use these keys in the dictionary you supply as the `attributes` parameter to the [SecHostCreateGuest](sechostcreateguest.md), [SecHostSetGuestStatus](sechostsetgueststatus.md), and [SecCodeCopyGuestWithAttributes](<seccodecopyguestwithattributes(________).md>) functions.

## Topics

### Constants

- [kSecGuestAttributeArchitecture](ksecguestattributearchitecture.md) — A key whose value is a number representing the CPU type under which the guest code is designed to run.
- [kSecGuestAttributeAudit](ksecguestattributeaudit.md)
- [kSecGuestAttributeCanonical](ksecguestattributecanonical.md) — A key whose value is the guest code object for that guest.
- [kSecGuestAttributeDynamicCode](ksecguestattributedynamiccode.md)
- [kSecGuestAttributeDynamicCodeInfoPlist](ksecguestattributedynamiccodeinfoplist.md)
- [kSecGuestAttributeHash](ksecguestattributehash.md) — A key whose value is a data object containing the SHA-1 hash of the code directory.
- [kSecGuestAttributeMachPort](ksecguestattributemachport.md) — Not implemented.
- [kSecGuestAttributePid](ksecguestattributepid.md) — A key whose value is an integer of type `pid_t` representing a process ID (PID), usually of the kernel’s guest.
- [kSecGuestAttributeSubarchitecture](ksecguestattributesubarchitecture.md) — A key whose value is a number representing the CPU subtype under which the guest code is designed to run.
