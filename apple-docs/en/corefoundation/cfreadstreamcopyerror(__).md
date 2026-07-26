---
title: 'CFReadStreamCopyError(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamcopyerror(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamcopyerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamcopyerror%28_%3A%29.json'
content_hash: 'sha256:9a3d31abb808f92c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamCopyError(_:)

<sub>Function</sub>

Returns the error associated with a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamCopyError(_ stream: CFReadStream!) -> CFError!
```

## Parameters

- `stream` — The stream to examine.

## Return Value

A CFError object that describes the current problem with stream, or `NULL` if there is no error. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Examining Stream Properties

- [CFReadStreamCopyProperty](<cfreadstreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFReadStreamGetBuffer](<cfreadstreamgetbuffer(______).md>) — Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [CFReadStreamGetError](<cfreadstreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFReadStreamGetStatus](<cfreadstreamgetstatus(__).md>) — Returns the current state of a stream.
- [CFReadStreamHasBytesAvailable](<cfreadstreamhasbytesavailable(__).md>) — Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.
