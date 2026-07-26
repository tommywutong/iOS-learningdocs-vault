---
title: NWTXTRecord.Entry
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwtxtrecord/entry
source_url: 'https://developer.apple.com/documentation/network/nwtxtrecord/entry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwtxtrecord/entry.json'
content_hash: 'sha256:84dbf6dbb2b64892'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWTXTRecord](../nwtxtrecord.md)

# NWTXTRecord.Entry

<sub>Enumeration</sub>

A type of entry in a TXT record dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Entry
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Entry Types

- [NWTXTRecord.Entry.none](entry/none.md) — The key is not mapped to any value.
- [NWTXTRecord.Entry.empty](entry/empty.md) — The key is mapped to an empty value.
- [NWTXTRecord.Entry.string(_:)](<entry/string(__).md>) — The key is mapped to a string.

### Enumeration Cases

- [NWTXTRecord.Entry.data(_:)](<entry/data(__).md>)

### Initializers

- [init(_:)](<entry/init(__).md>)

### Instance Properties

- [data](entry/data.md)

## See Also

### Creating TXT Records

- [init(_:)](<init(__)-566pd.md>) — Initializes a TXT record with a dictionary of strings.
- [removeEntry(key:)](<removeentry(key_).md>) — Removes an entry from a TXT record dictionary.
- [setEntry(_:for:)](<setentry(__for_).md>) — Sets an entry in a TXT record dictionary.
