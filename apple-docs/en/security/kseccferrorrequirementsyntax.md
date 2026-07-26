---
title: kSecCFErrorRequirementSyntax
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kseccferrorrequirementsyntax
source_url: 'https://developer.apple.com/documentation/security/kseccferrorrequirementsyntax'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kseccferrorrequirementsyntax.json'
content_hash: 'sha256:6008bb9d04d42c41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecCFErrorRequirementSyntax

<sub>Global Variable</sub>

A key whose value is a string containing a compilation error generated when parsing a requirement.

<sub>Mac Catalyst, macOS</sub>

```swift
let kSecCFErrorRequirementSyntax: CFString
```

## Discussion

This key is present when a call to the [SecRequirementCreateWithStringAndErrors](<secrequirementcreatewithstringanderrors(________).md>) function results in a compilation error during the processing of the code requirement string.
