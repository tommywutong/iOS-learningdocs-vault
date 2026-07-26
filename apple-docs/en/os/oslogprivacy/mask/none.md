---
title: OSLogPrivacy.Mask.none
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy/mask/none
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/mask/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/mask/none.json'
content_hash: 'sha256:77ddd6cddc4e5c51'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [os](../../../os.md) · [OSLogPrivacy](../../oslogprivacy.md) · [Mask](../mask.md)

# OSLogPrivacy.Mask.none

<sub>Case</sub>

An option to replace a redacted value with a generic string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case none
```

## Discussion

Use this option when you don’t want to correlate log messages with identical redacted values.

## See Also

### Privacy Mask Options

- [OSLogPrivacy.Mask.hash](hash.md) — An option to replace a redacted value with a string that contains a hashed version of the original value.
