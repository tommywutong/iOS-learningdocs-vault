---
title: SecKeychainAttribute
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeychainattribute
source_url: 'https://developer.apple.com/documentation/security/seckeychainattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeychainattribute.json'
content_hash: 'sha256:0a624c4acec0c96a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeychainAttribute

<sub>Structure</sub>

A structure that holds a single keychain attribute.

<sub>macOS</sub>

```swift
struct SecKeychainAttribute
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md)

## Topics

### Instance Properties

- [data](seckeychainattribute/data.md) — A pointer to the attribute data.
- [length](seckeychainattribute/length.md) — The length of the buffer pointed to by data.
- [tag](seckeychainattribute/tag.md) — A 4-byte attribute tag.

### Initializers

- [init()](<seckeychainattribute/init().md>)
- [init(tag:length:data:)](<seckeychainattribute/init(tag_length_data_).md>)
