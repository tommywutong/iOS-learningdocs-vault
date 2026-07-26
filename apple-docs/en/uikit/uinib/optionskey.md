---
title: UINib.OptionsKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinib/optionskey
source_url: 'https://developer.apple.com/documentation/uikit/uinib/optionskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinib/optionskey.json'
content_hash: 'sha256:3c6a1d5305ea62b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINib](../uinib.md)

# UINib.OptionsKey

<sub>Structure</sub>

Options that specify how to unarchive and instantiate the nib.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct OptionsKey
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Keys

- [UINibExternalObjects](optionskey/externalobjects.md) — The replacements for any proxy objects in the nib file.

### Initializers

- [init(rawValue:)](<optionskey/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

## See Also

### Retrieving objects from the nib file

- [- instantiateWithOwner:options:](<instantiate(withowner_options_).md>) — Unarchives and instantiates the in-memory contents of the nib object’s nib file, creating a distinct object tree and set of top-level objects.
