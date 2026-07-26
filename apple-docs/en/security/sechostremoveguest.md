---
title: SecHostRemoveGuest
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sechostremoveguest
source_url: 'https://developer.apple.com/documentation/security/sechostremoveguest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sechostremoveguest.json'
content_hash: 'sha256:4ff618d0abf69714'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecHostRemoveGuest

<sub>Function</sub>

Removes a guest from a host.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecHostRemoveGuest(SecGuestRef host, SecGuestRef guest, SecCSFlags flags);
```

## Parameters

- `host` — The guest code object of the host of the guest. You cannot specify a host of a host here except in the case of a dedicated host. For a dedicated host, the dedicated host is automatically substituted for its guest. See [kSecCSDedicatedHost](kseccsdedicatedhost.md) for a discussion of dedicated hosts.

- `guest` — The guest code object for the guest whose guest relationship you wish to terminate.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

This function removes all memory of the guest-host relationship from the Code Signing Services hosting system. You cannot remove a dedicated guest. The specified guest must have been created using the [SecHostCreateGuest](sechostcreateguest.md) function. If you remove a guest that is also a host, all of the guest’s guests are removed, recursively, as well, even if one or more of those guests are dedicated hosts.

## See Also

### Related Documentation

- [SecHostCreateGuest](sechostcreateguest.md) — Creates a new guest and describes its initial properties. _(deprecated)_
