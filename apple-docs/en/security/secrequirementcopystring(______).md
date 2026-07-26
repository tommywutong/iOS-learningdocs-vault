---
title: 'SecRequirementCopyString(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secrequirementcopystring(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secrequirementcopystring(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secrequirementcopystring%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e47abd5f1dbaf1e2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecRequirementCopyString(_:_:_:)

<sub>Function</sub>

Converts a code requirement object into text form.

<sub>Mac Catalyst, macOS</sub>

```swift
func SecRequirementCopyString(_ requirement: SecRequirement, _ flags: SecCSFlags, _ text: UnsafeMutablePointer<CFString?>) -> OSStatus
```

## Parameters

- `requirement` — A valid code requirement object.

- `flags` — Optional flags; see [SecCSFlags](seccsflags.md) for possible values. Pass [kSecCSDefaultFlags](seccsflags/kseccsdefaultflags.md) for standard behavior.

- `text` — On return, a text representation of the code requirement.

## Return Value

A result code. See [Code Signing Services Result Codes](code-signing-services-result-codes.md).

## Discussion

If you use the [SecRequirementCreateWithString](<secrequirementcreatewithstring(______).md>) or [SecRequirementCreateWithStringAndErrors](<secrequirementcreatewithstringanderrors(________).md>) function to create a code requirement object from a text string and later use the [SecRequirementCopyString](<secrequirementcopystring(______).md>) function to convert the object back to a string, the reconstituted text may differ in formatting, contain different source comments, and perform its validation functions in different order from the original. However, it is guaranteed that that the reconstituted text is functionally identical to the original. That is, recompiling the text using [SecRequirementCreateWithString](<secrequirementcreatewithstring(______).md>) will produce a code requirement object that behaves identically to the first one you created.
