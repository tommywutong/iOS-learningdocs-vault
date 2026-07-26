---
title: 'handleInput(framer:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframerimplementation/handleinput(framer:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframerimplementation/handleinput(framer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframerimplementation/handleinput%28framer%3A%29.json'
content_hash: 'sha256:67819af5ef1204dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolFramerImplementation](../nwprotocolframerimplementation.md)

# handleInput(framer:)

<sub>Instance Method</sub>

Notifies your protocol that new inbound data is available to parse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func handleInput(framer: NWProtocolFramer.Instance) -> Int
```

## See Also

### Handling Data

- [handleOutput(framer:message:messageLength:isComplete:)](<handleoutput(framer_message_messagelength_iscomplete_).md>) — Notifies your protocol about a new outbound message.
