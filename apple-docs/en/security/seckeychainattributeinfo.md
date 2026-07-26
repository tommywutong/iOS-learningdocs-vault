---
title: SecKeychainAttributeInfo
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainattributeinfo
source_url: 'https://developer.apple.com/documentation/security/seckeychainattributeinfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainattributeinfo.json'
content_hash: 'sha256:df8cbee7c1e617df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainAttributeInfo

<sub>Structure</sub>

A structure that represents an attribute.

<sub>macOS</sub>

```swift
struct SecKeychainAttributeInfo
```

## Overview

Each tag and format item form a pair. Use [SecKeychainAttributeInfoForItemID](<seckeychainattributeinfoforitemid(______).md>) to obtain the structure for a given keychain item, and [SecKeychainFreeAttributeInfo](<seckeychainfreeattributeinfo(__).md>) to release that structure’s memory when you are done with it. Use an instance of this structure in a call to the [SecKeychainItemCopyAttributesAndData](<seckeychainitemcopyattributesanddata(____________).md>) function to specify the attributes of a keychain item to retrieve.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Instance Properties

- [count](seckeychainattributeinfo/count.md) — The number of tag-format pairs in the respective arrays.
- [format](seckeychainattributeinfo/format.md) — A pointer to the first attribute format in the array.
- [tag](seckeychainattributeinfo/tag.md) — A pointer to the first attribute tag in the array.

### Initializers

- [init(count:tag:format:)](<seckeychainattributeinfo/init(count_tag_format_).md>) — Creates a new attribute information structure.
