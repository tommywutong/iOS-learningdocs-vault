---
title: 'private(mask:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/oslogprivacy/private(mask:)'
source_url: 'https://developer.apple.com/documentation/os/oslogprivacy/private(mask:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogprivacy/private%28mask%3A%29.json'
content_hash: 'sha256:8e6cecbdf71cb618'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogPrivacy](../oslogprivacy.md)

# private(mask:)

<sub>Type Method</sub>

Returns a privacy structure that marks an interpolated value as private, and customizes the display of redacted values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func `private`(mask: OSLogPrivacy.Mask) -> OSLogPrivacy
```

## Parameters

- `mask` — A mask that determines whether the system replaces a redacted value with a generic string or a string from a hash of the redacted value.

## Return Value

A privacy object that redacts a value.

## See Also

### Creating a Custom Privacy Mask

- [auto(mask:)](<auto(mask_).md>) — Returns a privacy structure that determines whether to redact or show values according to their type, and customizes the display of redacted values.
- [sensitive(mask:)](<sensitive(mask_).md>) — Returns a privacy structure that marks an interpolated value as sensitive, and customizes the display of redacted values.
- [Mask](mask.md) — A mask that establishes how the system displays a redacted value in a log message.
