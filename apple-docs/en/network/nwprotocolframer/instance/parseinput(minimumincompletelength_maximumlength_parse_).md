---
title: 'parseInput(minimumIncompleteLength:maximumLength:parse:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/parseinput(minimumincompletelength:maximumlength:parse:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/parseinput(minimumincompletelength:maximumlength:parse:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/parseinput%28minimumincompletelength%3Amaximumlength%3Aparse%3A%29.json'
content_hash: 'sha256:7155755b4b73c849'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# parseInput(minimumIncompleteLength:maximumLength:parse:)

<sub>Instance Method</sub>

Examines the content of input data while in your input handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func parseInput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool
```

## Parameters

- `minimumIncompleteLength` — The minimum number of bytes that should be delivered to the parse completion.

- `maximumLength` — The maximum number of bytes that should be delivered to the parse completion.

- `parse` — A completion handler that will be called inline to examine a region of bytes. This will contain the buffer that matches the constraints, and a boolean indicating if this buffer represents the end of a message.

## Return Value

Returns true if the requested length was available to parse, or false if the conditions could not be met.

## See Also

### Delivering Input

- [deliverInput(data:message:isComplete:)](<deliverinput(data_message_iscomplete_).md>) — Delivers an inbound message containing arbitrary data from your protocol to the application.
- [deliverInputNoCopy(length:message:isComplete:)](<deliverinputnocopy(length_message_iscomplete_).md>) — Delivers an inbound message containing a specific number of next received bytes.
- [passThroughInput()](<passthroughinput().md>) — Indicates that your protocol no longer needs to handle input data.
