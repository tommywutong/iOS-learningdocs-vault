---
title: 'writeOutputNoCopy(length:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwprotocolframer/instance/writeoutputnocopy(length:)'
source_url: 'https://developer.apple.com/documentation/network/nwprotocolframer/instance/writeoutputnocopy(length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwprotocolframer/instance/writeoutputnocopy%28length%3A%29.json'
content_hash: 'sha256:ea143838df6f7093'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [NWProtocolFramer](../../nwprotocolframer.md) · [Instance](../instance.md)

# writeOutputNoCopy(length:)

<sub>Instance Method</sub>

Sends a specific number of bytes from a message while inside your output handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func writeOutputNoCopy(length: Int) throws
```

## See Also

### Writing Output

- [parseOutput(minimumIncompleteLength:maximumLength:parse:)](<parseoutput(minimumincompletelength_maximumlength_parse_).md>) — Examines the content of output data while inside your output handler.
- [writeOutput(data:)](<writeoutput(data_)-ydvk.md>) — Sends arbitrary output data from your protocol to the next protocol.
- [passThroughOutput()](<passthroughoutput().md>) — Indicates that your protocol no longer needs to handle output data.
