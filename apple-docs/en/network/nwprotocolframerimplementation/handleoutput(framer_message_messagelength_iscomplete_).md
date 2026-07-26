---
title: 'handleOutput(framer:message:messageLength:isComplete:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframerimplementation/handleoutput(framer:message:messagelength:iscomplete:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframerimplementation/handleoutput(framer:message:messagelength:iscomplete:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframerimplementation/handleoutput%28framer%3Amessage%3Amessagelength%3Aiscomplete%3A%29.json'
content_hash: 'sha256:788398932de142ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWProtocolFramerImplementation](../nwprotocolframerimplementation.md)

# handleOutput(framer:message:messageLength:isComplete:)

<sub>Instance Method</sub>

Notifies your protocol about a new outbound message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func handleOutput(framer: NWProtocolFramer.Instance, message: NWProtocolFramer.Message, messageLength: Int, isComplete: Bool)
```

## Parameters

- `framer` — The framer instance associated with the connection.

- `message` — The framer message passed by the application.

- `messageLength` — The length of the message content being sent.

- `isComplete` — A boolean indicating if this the last chunk of a message.

## Discussion

The output handler is your opportunity to encapsulate or encode a signle application message. You should write any output using [writeOutput(data:)](<../nwprotocolframer/instance/writeoutput(data_)-ydvk.md>) or [writeOutputNoCopy(length:)](<../nwprotocolframer/instance/writeoutputnocopy(length_).md>) before returning from the output handler. If you do not write a message, the application message will be discarded.

## See Also

### Handling Data

- [handleInput(framer:)](<handleinput(framer_).md>) — Notifies your protocol that new inbound data is available to parse.
