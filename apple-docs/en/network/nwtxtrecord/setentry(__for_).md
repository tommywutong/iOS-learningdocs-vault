---
title: 'setEntry(_:for:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwtxtrecord/setentry(_:for:)'
source_url: 'https://developer.apple.com/documentation/network/nwtxtrecord/setentry(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwtxtrecord/setentry%28_%3Afor%3A%29.json'
content_hash: 'sha256:8acc29a94ae491a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWTXTRecord](../nwtxtrecord.md)

# setEntry(_:for:)

<sub>Instance Method</sub>

Sets an entry in a TXT record dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func setEntry(_ entry: NWTXTRecord.Entry, for key: String) -> Bool
```

## See Also

### Creating TXT Records

- [init(_:)](<init(__)-566pd.md>) — Initializes a TXT record with a dictionary of strings.
- [removeEntry(key:)](<removeentry(key_).md>) — Removes an entry from a TXT record dictionary.
- [Entry](entry.md) — A type of entry in a TXT record dictionary.
