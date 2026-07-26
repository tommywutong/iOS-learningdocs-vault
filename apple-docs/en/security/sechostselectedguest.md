---
title: SecHostSelectedGuest
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sechostselectedguest
source_url: 'https://developer.apple.com/documentation/security/sechostselectedguest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sechostselectedguest.json'
content_hash: 'sha256:069cbcb6bf9b214c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecHostSelectedGuest

<sub>Function</sub>

Retrieves the handle for the guest currently selected for the calling thread.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecHostSelectedGuest(SecCSFlags flags, SecGuestRef *guestRef);
```

## Parameters

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

- `guestRef` — On return, the guest code object of the current selected guest for the calling thread. If no guest is active on this thread (that is, the thread is acting for the host), the value returned is [kSecNoGuest](ksecnoguest.md).

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

This function may be called in either dynamic hosting mode or proxy hosting mode. If the host has more than one guest, it can set a different selected guest for each thread.
