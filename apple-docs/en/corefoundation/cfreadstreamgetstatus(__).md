---
title: 'CFReadStreamGetStatus(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamgetstatus(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamgetstatus(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamgetstatus%28_%3A%29.json'
content_hash: 'sha256:2b7bb9bd55692719'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamGetStatus(_:)

<sub>Function</sub>

Returns the current state of a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamGetStatus(_ stream: CFReadStream!) -> CFStreamStatus
```

## Parameters

- `stream` — The stream to examine.

## Return Value

The current state of `stream`. See [CFStreamStatus](cfstreamstatus.md) for the list of possible states.

## See Also

### Examining Stream Properties

- [CFReadStreamCopyProperty](<cfreadstreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFReadStreamGetBuffer](<cfreadstreamgetbuffer(______).md>) — Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [CFReadStreamCopyError](<cfreadstreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFReadStreamGetError](<cfreadstreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFReadStreamHasBytesAvailable](<cfreadstreamhasbytesavailable(__).md>) — Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.
