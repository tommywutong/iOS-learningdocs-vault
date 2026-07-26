---
title: auto
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy/auto
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/auto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/auto.json'
content_hash: 'sha256:7c5459ce3729ffd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogPrivacy](../oslogprivacy.md)

# auto

<sub>Type Property</sub>

The standard option to let the system determine whether to redact or display a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var auto: OSLogPrivacy { get }
```

## Discussion

Use this option to apply the default rules for redacting or showing interpolated values. When it redacts a value, the system displays a generic string in place of the value. If you want to correlate log messages that contain the same value, use the [auto(mask:)](<auto(mask_).md>) function to create a structure with the [OSLogPrivacy.Mask.hash](mask/hash.md) mask.

## See Also

### Getting the Privacy Options

- [private](private.md) — The standard option to always redact the interpolated value.
- [public](public.md) — The standard option to always show the interpolated value.
- [sensitive](sensitive.md) — The option to always redact interpolated values that contain sensitive information.
