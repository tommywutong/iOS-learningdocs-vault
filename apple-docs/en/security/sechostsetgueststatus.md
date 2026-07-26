---
title: SecHostSetGuestStatus
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+（10.6 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/security/sechostsetgueststatus
source_url: 'https://developer.apple.com/documentation/security/sechostsetgueststatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sechostsetgueststatus.json'
content_hash: 'sha256:74f7f285ad5ff626'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecHostSetGuestStatus

<sub>Function</sub>

Updates the status and attributes of a particular guest.

<sub>Mac Catalyst, macOS</sub>

```objc
OSStatus SecHostSetGuestStatus(SecGuestRef guestRef, uint32_t status, CFDictionaryRef attributes, SecCSFlags flags);
```

## Parameters

- `guestRef` — The guest code object of the code on whose behalf this thread is acting.

- `status` — A new set of code status flags for the guest (see [SecCodeStatus](seccodestatus.md). The host must enforce the restrictions on changes to guest status: the [kSecCodeStatusValid](seccodestatus/valid.md) bit can only be cleared and the [kSecCodeStatusHard](seccodestatus/hard.md) and [kSecCodeStatusKill](seccodestatus/kill.md) flags can only be set. Pass the previous guest status to indicate that no change is desired.

- `attributes` — A key-value dictionary of attributes that can be used to identify this particular guest among all of the caller’s guests. If you include this dictionary, it completely replaces earlier-specified attributes. Pass `NULL` for this parameter if you do not want to change the attributes for this guest. Although you can specify any key-value pairs in this attributes dictionary, the keys in [Guest Attribute Dictionary Keys](guest-attribute-dictionary-keys.md) are conventionally used for this purpose.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass `kSecCSDefaultFlags` for standard behavior.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

This function must be called by a host acting in proxy mode every time the status of a guest changes so that Code Signing Services can update the information cache for that guest. The specified guest must have been created using the [SecHostCreateGuest](sechostcreateguest.md) function.
