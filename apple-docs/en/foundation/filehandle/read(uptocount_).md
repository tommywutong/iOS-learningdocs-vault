---
title: 'read(upToCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, macOS 10.15.4+, tvOS 13.4+, visionOS 1.0+, watchOS 6.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/read(uptocount:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/read(uptocount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/read%28uptocount%3A%29.json'
content_hash: 'sha256:46c708ed3c7bbde2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# read(upToCount:)

<sub>Instance Method</sub>

Reads data synchronously up to the specified number of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func read(upToCount count: Int) throws -> Data?
```

## Parameters

- `count` — The number of bytes to read from the file handle.

## Return Value

The data available through the receiver up to a maximum of `length` bytes, or the maximum size that can be represented by an [NSData](../nsdata.md) object, whichever is the smaller.

## Discussion

If the handle represents a file, this method returns the data obtained by reading `length` bytes starting at the current file pointer. If `length` bytes aren’t available, this method returns the data from the current file pointer to the end of the file. If the handle is a communications channel, the method reads up to `length` bytes from the channel. Returns an empty [NSData](../nsdata.md) object if the handle is at the file’s end or if the communications channel returns an end-of-file indicator.

This method throws an error if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

## See Also

### Reading from a file handle synchronously

- [availableData](availabledata.md) — The data currently available in the receiver.
- [readToEnd()](<readtoend().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes.
