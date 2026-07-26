---
title: 'CFReadStreamGetError(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfreadstreamgeterror(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamgeterror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamgeterror%28_%3A%29.json'
content_hash: 'sha256:aeb8b7e032628d89'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamGetError(_:)

<sub>Function</sub>

Returns the error status of a stream.

> [!warning] Deprecated
> Use [CFReadStreamCopyError](<cfreadstreamcopyerror(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamGetError(_ stream: CFReadStream!) -> CFStreamError
```

## Parameters

- `stream` — The stream to examine.

## Return Value

The error status of `stream` returned in a [CFStreamError](cfstreamerror.md) structure.

## Discussion

The error field is `0` if no error has occurred. If the error field is not `0`, the `domain` field contains a code that identifies the domain in which the value of the `error` field should be interpreted.

## See Also

### Examining Stream Properties

- [CFReadStreamCopyProperty](<cfreadstreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFReadStreamGetBuffer](<cfreadstreamgetbuffer(______).md>) — Returns a pointer to a stream’s internal buffer of unread data, if possible.
- [CFReadStreamCopyError](<cfreadstreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFReadStreamGetStatus](<cfreadstreamgetstatus(__).md>) — Returns the current state of a stream.
- [CFReadStreamHasBytesAvailable](<cfreadstreamhasbytesavailable(__).md>) — Returns a Boolean value that indicates whether a readable stream has data that can be read without blocking.
