---
title: 'init(requiringSecureCoding:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nskeyedarchiver/init(requiringsecurecoding:)'
source_url: 'https://developer.apple.com/documentation/foundation/nskeyedarchiver/init(requiringsecurecoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nskeyedarchiver/init%28requiringsecurecoding%3A%29.json'
content_hash: 'sha256:612791af531d2e3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSKeyedArchiver](../nskeyedarchiver.md)

# init(requiringSecureCoding:)

<sub>Initializer</sub>

Creates an archiver to encode data, and optionally disables secure coding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(requiringSecureCoding requiresSecureCoding: Bool)
```

## Parameters

- `requiresSecureCoding` — A Boolean value indicating whether all encoded objects must conform to [NSSecureCoding](../nssecurecoding.md).

## Discussion

To prevent the possibility of encoding an object that [NSKeyedUnarchiver](../nskeyedunarchiver.md) can’t decode, set `requiresSecureCoding` to [true](../../swift/true.md) whenever possible. This ensures that all encoded objects conform to [NSSecureCoding](../nssecurecoding.md).

> [!note] Note
> Enabling secure coding doesn’t change the output format of the archive. This means that you can encode archives with secure coding enabled, and decode them later with secure coding disabled.

## See Also

### Related Documentation

- [requiresSecureCoding](requiressecurecoding.md) — Indicates whether the archiver requires all archived classes to resist object substitution attacks.

### Creating a Keyed Archiver

- [- init](<init().md>) — Initializes an archiver to encode data. _(deprecated)_
- [- initForWritingWithMutableData:](<init(forwritingwith_).md>) — Initializes an archiver to encode data into a given a mutable-data object. _(deprecated)_
