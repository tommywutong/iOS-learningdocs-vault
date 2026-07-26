---
title: OSLogPrivacy.Mask
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy/mask
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/mask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/mask.json'
content_hash: 'sha256:da4c73f9a9d46ac1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogPrivacy](../oslogprivacy.md)

# OSLogPrivacy.Mask

<sub>Enumeration</sub>

A mask that establishes how the system displays a redacted value in a log message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Mask
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### Privacy Mask Options

- [OSLogPrivacy.Mask.hash](mask/hash.md) — An option to replace a redacted value with a string that contains a hashed version of the original value.
- [OSLogPrivacy.Mask.none](mask/none.md) — An option to replace a redacted value with a generic string.

## See Also

### Creating a Custom Privacy Mask

- [auto(mask:)](<auto(mask_).md>) — Returns a privacy structure that determines whether to redact or show values according to their type, and customizes the display of redacted values.
- [private(mask:)](<private(mask_).md>) — Returns a privacy structure that marks an interpolated value as private, and customizes the display of redacted values.
- [sensitive(mask:)](<sensitive(mask_).md>) — Returns a privacy structure that marks an interpolated value as sensitive, and customizes the display of redacted values.
