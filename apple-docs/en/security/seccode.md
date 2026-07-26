---
title: SecCode
framework: Security
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccode
source_url: 'https://developer.apple.com/documentation/security/seccode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccode.json'
content_hash: 'sha256:638bac7e1dd5d622'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCode

<sub>Class</sub>

A code object representing signed code running on the system.

<sub>Mac Catalyst, macOS</sub>

```swift
class SecCode
```

## Overview

In many function calls, a value of type [SecCode](seccode.md) can be passed to a parameter that is typed as a [SecStaticCode](secstaticcode.md). In these cases, the function performs an implicit call to the [SecCodeCopyStaticCode](<seccodecopystaticcode(______).md>) function and operates on the result.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)
