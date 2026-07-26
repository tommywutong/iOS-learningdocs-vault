---
title: 'CFWriteStreamGetStatus(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamgetstatus(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamgetstatus(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamgetstatus%28_%3A%29.json'
content_hash: 'sha256:2fa825231b83b04e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamGetStatus(_:)

<sub>Function</sub>

Returns the current state of a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamGetStatus(_ stream: CFWriteStream!) -> CFStreamStatus
```

## Parameters

- `stream` — The stream to examine.

## Return Value

The current state of `stream`. See [CFStreamStatus](cfstreamstatus.md) for the list of possible states.

## See Also

### Examining Stream Properties

- [CFWriteStreamCanAcceptBytes](<cfwritestreamcanacceptbytes(__).md>) — Returns whether a writable stream can accept new data without blocking.
- [CFWriteStreamCopyProperty](<cfwritestreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFWriteStreamCopyError](<cfwritestreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFWriteStreamGetError](<cfwritestreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
