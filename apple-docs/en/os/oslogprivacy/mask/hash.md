---
title: OSLogPrivacy.Mask.hash
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy/mask/hash
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/mask/hash'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/mask/hash.json'
content_hash: 'sha256:18b1ebe20bfe84fb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [os](../../../os.md) · [OSLogPrivacy](../../oslogprivacy.md) · [Mask](../mask.md)

# OSLogPrivacy.Mask.hash

<sub>Case</sub>

An option to replace a redacted value with a string that contains a hashed version of the original value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case hash
```

## Discussion

Use this option when you want to hide potentially sensitive data in log messages, but still want to know when two or more log messages contain the same hidden value. An [OSLogPrivacy](../../oslogprivacy.md) structure with this option generates a hash string for a redacted value. The system displays that hash string as part of the log message, making it possible for you to compare log messages with the same value.

## See Also

### Privacy Mask Options

- [OSLogPrivacy.Mask.none](none.md) — An option to replace a redacted value with a generic string.
