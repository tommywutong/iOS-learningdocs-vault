---
title: 'SecRequirementCreateWithData(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secrequirementcreatewithdata(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secrequirementcreatewithdata(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secrequirementcreatewithdata%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:57bf7043afc48517'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecRequirementCreateWithData(_:_:_:)

<sub>Function</sub>

Creates a code requirement object from the binary form of a code requirement.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecRequirementCreateWithData(_ data: CFData, _ flags: SecCSFlags, _ requirement: UnsafeMutablePointer<SecRequirement?>) -> OSStatus
```

## Parameters

- `data` — A binary blob created earlier from a valid code requirement object by calling the [SecRequirementCopyData](<secrequirementcopydata(______).md>) function.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

- `requirement` — On return, contains a code requirement object that behaves identically to the one from which the data blob was obtained.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

You can use the [SecRequirementCopyData](<secrequirementcopydata(______).md>) function to convert a code requirement object to a binary blob, and store the blob in any form you wish. When you are ready to use the code requirement in another function call, you can use the [SecRequirementCreateWithData](<secrequirementcreatewithdata(______).md>) function to convert it back to a code requirement object.
