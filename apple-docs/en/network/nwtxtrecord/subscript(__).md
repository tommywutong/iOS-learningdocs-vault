---
title: 'subscript(_:)'
framework: Network
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwtxtrecord/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwtxtrecord/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwtxtrecord/subscript%28_%3A%29.json'
content_hash: 'sha256:ef529e95d728e3ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWTXTRecord](../nwtxtrecord.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Get and set values in a TXT record dictionary, by keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(key: String) -> String? { get set }
```

## See Also

### Examining TXT Records

- [getEntry(for:)](<getentry(for_).md>) — Accesses an entry in a TXT record dictionary.
- [dictionary](dictionary.md) — The TXT record as a dictionary of strings.
