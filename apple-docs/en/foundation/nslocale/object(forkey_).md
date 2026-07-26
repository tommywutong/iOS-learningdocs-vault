---
title: 'object(forKey:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/object(forkey:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/object(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/object%28forkey%3A%29.json'
content_hash: 'sha256:353a3aa1526232e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# object(forKey:)

<sub>Instance Method</sub>

Returns the value of the component corresponding to the specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func object(forKey key: NSLocale.Key) -> Any?
```

## Parameters

- `key` — The component for which to return the corresponding value. For possible values, see [Key](key.md).

## Return Value

The object corresponding to `key`.

## See Also

### Accessing Locale Information by Key

- [- displayNameForKey:value:](<displayname(forkey_value_).md>) — Returns the display name for the given locale component value.
- [Key](key.md) — The keys used to access components of a locale.
