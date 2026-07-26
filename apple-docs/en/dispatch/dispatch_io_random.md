---
title: DISPATCH_IO_RANDOM
framework: Dispatch
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_random
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_random'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_random.json'
content_hash: 'sha256:6d06cc8fc357dc7c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_IO_RANDOM

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var DISPATCH_IO_RANDOM: Int32 { get }
```

## Discussion

The channel represents a random access file. Read and write operations may be performed concurrently with a channel of this type. Offsets are interpreted relative to the file pointer position that is current at the time the channel is created. After channel creation, the file pointer position of the file descriptor is indeterminate until channel relinquishes control of the file descriptor, at which time the position is reset to its initial value.

The file descriptor for a channel of this type must be seekable. If it is not, attempting to create a channel of this type for the descriptor will result in an error.

## See Also

### Initializing the Type

- [DISPATCH_IO_STREAM](dispatch_io_stream.md)
