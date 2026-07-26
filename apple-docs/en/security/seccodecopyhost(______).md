---
title: 'SecCodeCopyHost(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccodecopyhost(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccodecopyhost(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodecopyhost%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0fd2969a48549d5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeCopyHost(_:_:_:)

<sub>Function</sub>

Retrieves the code object for the host of specified guest code.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecCodeCopyHost(_ guest: SecCode, _ flags: SecCSFlags, _ host: UnsafeMutablePointer<SecCode?>) -> OSStatus
```

## Parameters

- `guest` — A valid code object representing code running on the system as the guest of other code.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

- `host` — On return, the code object of the host of the code specified in the `guest` parameter.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

Host code acts as the supervisor and controller of its guest code and is the ultimate authority on the dynamic validity and status of its guests.
