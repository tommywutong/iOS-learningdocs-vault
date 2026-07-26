---
title: 'SecCodeMapMemory(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/seccodemapmemory(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/seccodemapmemory(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccodemapmemory%28_%3A_%3A%29.json'
content_hash: 'sha256:90fc1ceef7b8131b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCodeMapMemory(_:_:)

<sub>Function</sub>

Asks the kernel to accept the signing information currently attached to a code object and uses it to validate memory page-ins.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecCodeMapMemory(_ code: SecStaticCode, _ flags: SecCSFlags) -> OSStatus
```

## Parameters

- `code` — A code or static code object representing the signed code whose main executable should be subject to page-in validation. If you provide a code object, the function processes it in the same manner as the  [SecCodeCopyStaticCode](<seccodecopystaticcode(______).md>) function—that is, whether you provide a code object or a static code object, the function actually takes the signature from the code on disk.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

This function is for the use of code hosts that use memory mapping to manage their own code. The kernel takes the signing information attached to the code on disk specified by the `code` parameter and attaches it to the memory object. After that, it uses the signature to validate memory page-ins, updating the dynamic validity status accordingly. You can use the [SecCodeCopySigningInformation](<seccodecopysigninginformation(______).md>) function to check the code’s dynamic validity status. The attachment of the signature to the memory object affects all processes that have the main executable of this code mapped.
