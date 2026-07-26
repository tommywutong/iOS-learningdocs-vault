---
title: 'parseOutput(minimumIncompleteLength:maximumLength:parse:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/parseoutput(minimumincompletelength:maximumlength:parse:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/parseoutput(minimumincompletelength:maximumlength:parse:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/parseoutput%28minimumincompletelength%3Amaximumlength%3Aparse%3A%29.json'
content_hash: 'sha256:23784fa0efd5120d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# parseOutput(minimumIncompleteLength:maximumLength:parse:)

<sub>Instance Method</sub>

Examines the content of output data while inside your output handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func parseOutput(minimumIncompleteLength: Int, maximumLength: Int, parse: (UnsafeMutableRawBufferPointer?, Bool) -> Int) -> Bool
```

## Parameters

- `minimumIncompleteLength` — The minimum number of bytes that should be delivered to the parse completion.

- `maximumLength` — The maximum number of bytes that should be delivered to the parse completion.

- `parse` — A completion handler that will be called inline to examine a region of bytes. This will contain the buffer that matches the constraints, and a boolean indicating if this buffer represents the end of a message.

## Return Value

Returns true if the requested length was available to parse, or false if the conditions could not be met.

## See Also

### Writing Output

- [writeOutput(data:)](<writeoutput(data_)-ydvk.md>) — Sends arbitrary output data from your protocol to the next protocol.
- [writeOutputNoCopy(length:)](<writeoutputnocopy(length_).md>) — Sends a specific number of bytes from a message while inside your output handler.
- [passThroughOutput()](<passthroughoutput().md>) — Indicates that your protocol no longer needs to handle output data.
