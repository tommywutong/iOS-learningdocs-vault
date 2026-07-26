---
title: 'writeOutput(data:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/writeoutput(data:)-ydvk'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/writeoutput(data:)-ydvk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/writeoutput%28data%3A%29-ydvk.json'
content_hash: 'sha256:9702ff7c1ff38be5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# writeOutput(data:)

<sub>Instance Method</sub>

Sends arbitrary output data from your protocol to the next protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func writeOutput(data: Data)
```

## See Also

### Writing Output

- [parseOutput(minimumIncompleteLength:maximumLength:parse:)](<parseoutput(minimumincompletelength_maximumlength_parse_).md>) — Examines the content of output data while inside your output handler.
- [writeOutputNoCopy(length:)](<writeoutputnocopy(length_).md>) — Sends a specific number of bytes from a message while inside your output handler.
- [passThroughOutput()](<passthroughoutput().md>) — Indicates that your protocol no longer needs to handle output data.
