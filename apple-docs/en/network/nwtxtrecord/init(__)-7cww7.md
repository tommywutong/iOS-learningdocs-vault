---
title: 'init(_:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwtxtrecord/init(_:)-7cww7'
source_url: 'https://developer.apple.com/documentation/network/nwtxtrecord/init(_:)-7cww7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwtxtrecord/init%28_%3A%29-7cww7.json'
content_hash: 'sha256:701f373b9325859b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWTXTRecord](../nwtxtrecord.md)

# init(_:)

<sub>Initializer</sub>

Create an NWTXTRecord object from a Dictionary\<String, NWTXTRecord.Entry\>.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ entryDictionary: [String : NWTXTRecord.Entry])
```

## Discussion

Invalid keys will be ignored.
