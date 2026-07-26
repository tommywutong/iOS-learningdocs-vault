---
title: 'CFReadStreamGetBuffer(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamgetbuffer(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamgetbuffer(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamgetbuffer%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:aafb457d4e76ecec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamGetBuffer(_:_:_:)

<sub>Function</sub>

Returns a pointer to a stream’s internal buffer of unread data, if possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamGetBuffer(_ stream: CFReadStream!, _ maxBytesToRead: CFIndex, _ numBytesRead: UnsafeMutablePointer<CFIndex>!) -> UnsafePointer<UInt8>!
```

## Parameters

- `stream` — The stream to examine.

- `maxBytesToRead` — The maximum number of bytes to read. If greater than `0`, `maxBytesToRead` limits the number of bytes read; if `0` or less, all available bytes are read.

- `numBytesRead` — On return, contains the length of returned buffer. If `stream` is not open or has encountered an error, `numBytesRead` is set to `-1`.

## Return Value

A pointer to the internal buffer of unread data for `stream`, if possible; `NULL` otherwise. The buffer is good only until the next stream operation called on the stream. You should neither change the contents of the returned buffer nor attempt to deallocate the buffer; it is still owned by the stream. The bytes returned in the buffer are considered read from the stream.

## See Also

### Examining Stream Properties

- [CFReadStreamCopyProperty](<cfreadstreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFReadStreamCopyError](<cfreadstreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFReadStreamGetError](<cfreadstreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFReadStreamGetStatus](<cfreadstreamgetstatus(__).md>) — Returns the current state of a stream.
- [CFReadStreamHasBytesAvailable](<cfreadstreamhasbytesavailable(__).md>) — Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.
