---
title: NWTXTRecord
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwtxtrecord
source_url: 'https://developer.apple.com/documentation/network/nwtxtrecord'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwtxtrecord.json'
content_hash: 'sha256:2d4ed2a8fb7df33b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWTXTRecord

<sub>Structure</sub>

A dictionary representing a TXT record in a DNS packet.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NWTXTRecord
```

## Relationships

- **Conforms To**: [Collection](../swift/collection.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [Sequence](../swift/sequence.md)

## Topics

### Creating TXT Records

- [init(_:)](<nwtxtrecord/init(__)-566pd.md>) — Initializes a TXT record with a dictionary of strings.
- [removeEntry(key:)](<nwtxtrecord/removeentry(key_).md>) — Removes an entry from a TXT record dictionary.
- [setEntry(_:for:)](<nwtxtrecord/setentry(__for_).md>) — Sets an entry in a TXT record dictionary.
- [Entry](nwtxtrecord/entry.md) — A type of entry in a TXT record dictionary.

### Examining TXT Records

- [getEntry(for:)](<nwtxtrecord/getentry(for_).md>) — Accesses an entry in a TXT record dictionary.
- [subscript(_:)](<nwtxtrecord/subscript(__).md>) — Get and set values in a TXT record dictionary, by keys.
- [dictionary](nwtxtrecord/dictionary.md) — The TXT record as a dictionary of strings.

### Initializers

- [init(_:)](<nwtxtrecord/init(__)-30jy4.md>)
- [init(_:)](<nwtxtrecord/init(__)-69q7g.md>) — Create an NWTXTRecord object from a Dictionary\<String, Data\>.
- [init(_:)](<nwtxtrecord/init(__)-7cww7.md>) — Create an NWTXTRecord object from a Dictionary\<String, NWTXTRecord.Entry\>.

### Instance Properties

- [data](nwtxtrecord/data.md)
- [dataDictionary](nwtxtrecord/datadictionary.md) — Access the contents of an NWTXTRecord represented by a Dictionary\<String, Data\>.
- [entries](nwtxtrecord/entries.md) — Get all entries present in the TXT record.

## See Also

### Evaluating Browser Results

- [endpoint](nwbrowser/result/endpoint.md) — The discovered service endpoint.
- [interfaces](nwbrowser/result/interfaces.md) — The list of interfaces on which the service was discovered.
- [metadata](nwbrowser/result/metadata-swift.property.md) — The metadata associated with the discovered service, such as the TXT record.
- [Metadata](nwbrowser/result/metadata-swift.enum.md) — Values associated with discovered services, such as TXT records.
