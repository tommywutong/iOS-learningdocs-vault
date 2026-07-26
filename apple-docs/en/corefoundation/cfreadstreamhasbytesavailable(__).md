---
title: 'CFReadStreamHasBytesAvailable(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamhasbytesavailable(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamhasbytesavailable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamhasbytesavailable%28_%3A%29.json'
content_hash: 'sha256:f0018158cafbedeb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamHasBytesAvailable(_:)

<sub>Function</sub>

Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamHasBytesAvailable(_ stream: CFReadStream!) -> Bool
```

## Parameters

- `stream` — The stream to examine.

## Return Value

`TRUE` if data can be read from `stream` without blocking, otherwise `FALSE`. If `stream` cannot tell if data is available without actually trying to read the data, this function returns `TRUE`.

## See Also

### Examining Stream Properties

- [CFReadStreamCopyProperty](<cfreadstreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFReadStreamGetBuffer](<cfreadstreamgetbuffer(______).md>) — Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [CFReadStreamCopyError](<cfreadstreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFReadStreamGetError](<cfreadstreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFReadStreamGetStatus](<cfreadstreamgetstatus(__).md>) — Returns the current state of a stream.
