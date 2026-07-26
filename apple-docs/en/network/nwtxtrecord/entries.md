---
title: entries
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwtxtrecord/entries
source_url: 'https://developer.apple.com/documentation/network/nwtxtrecord/entries'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwtxtrecord/entries.json'
content_hash: 'sha256:40feb576397d0b80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWTXTRecord](../nwtxtrecord.md)

# entries

<sub>Instance Property</sub>

Get all entries present in the TXT record.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var entries: [String : NWTXTRecord.Entry] { get }
```

## Return Value

A dictionary representing all entries in the TXT record, preserving original key case.
