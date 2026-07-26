---
title: 'SecRequirementCopyData(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secrequirementcopydata(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secrequirementcopydata(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secrequirementcopydata%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:299b5a0499fa1ce2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecRequirementCopyData(_:_:_:)

<sub>Function</sub>

Extracts a binary form of a code requirement from a code requirement object.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecRequirementCopyData(_ requirement: SecRequirement, _ flags: SecCSFlags, _ data: UnsafeMutablePointer<CFData?>) -> OSStatus
```

## Parameters

- `requirement` — A valid code requirement object.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

- `data` — On return, the code requirement in the form of a binary blob.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

You can extract the binary blob from the [CFData](../corefoundation/cfdata.md) object and store it in any form you wish. Use of this function is the only publicly supported way to get such a data blob. You can use the [SecRequirementCreateWithData](<secrequirementcreatewithdata(______).md>) function to convert it back to a code requirement object.
