---
title: public
framework: os
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogprivacy/public
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/public'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/public.json'
content_hash: 'sha256:b6ca0fc772e27f4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogPrivacy](../oslogprivacy.md)

# public

<sub>Type Property</sub>

The standard option to always show the interpolated value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var `public`: OSLogPrivacy { get }
```

## See Also

### Getting the Privacy Options

- [auto](auto.md) — The standard option to let the system determine whether to redact or display a value.
- [private](private.md) — The standard option to always redact the interpolated value.
- [sensitive](sensitive.md) — The option to always redact interpolated values that contain sensitive information.
