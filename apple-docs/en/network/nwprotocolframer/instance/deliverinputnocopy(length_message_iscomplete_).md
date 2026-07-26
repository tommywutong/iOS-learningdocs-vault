---
title: 'deliverInputNoCopy(length:message:isComplete:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/deliverinputnocopy(length:message:iscomplete:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/deliverinputnocopy(length:message:iscomplete:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/deliverinputnocopy%28length%3Amessage%3Aiscomplete%3A%29.json'
content_hash: 'sha256:bef7f15043ec459f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# deliverInputNoCopy(length:message:isComplete:)

<sub>Instance Method</sub>

Delivers an inbound message containing a specific number of next received bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func deliverInputNoCopy(length: Int, message: NWProtocolFramer.Message, isComplete: Bool) -> Bool
```

## See Also

### Delivering Input

- [parseInput(minimumIncompleteLength:maximumLength:parse:)](<parseinput(minimumincompletelength_maximumlength_parse_).md>) — Examines the content of input data while in your input handler.
- [deliverInput(data:message:isComplete:)](<deliverinput(data_message_iscomplete_).md>) — Delivers an inbound message containing arbitrary data from your protocol to the application.
- [passThroughInput()](<passthroughinput().md>) — Indicates that your protocol no longer needs to handle input data.
