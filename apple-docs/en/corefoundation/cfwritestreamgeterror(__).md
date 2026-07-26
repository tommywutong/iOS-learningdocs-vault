---
title: 'CFWriteStreamGetError(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfwritestreamgeterror(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamgeterror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamgeterror%28_%3A%29.json'
content_hash: 'sha256:e84896e84bca23b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamGetError(_:)

<sub>Function</sub>

Returns the error status of a stream.

> [!warning] Deprecated
> Use [CFWriteStreamCopyError](<cfwritestreamcopyerror(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamGetError(_ stream: CFWriteStream!) -> CFStreamError
```

## Parameters

- `stream` — The stream to examine.

## Return Value

The error status of `stream` returned in a CFStreamError structure.

## See Also

### Examining Stream Properties

- [CFWriteStreamCanAcceptBytes](<cfwritestreamcanacceptbytes(__).md>) — Returns whether a writable stream can accept new data without blocking.
- [CFWriteStreamCopyProperty](<cfwritestreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFWriteStreamCopyError](<cfwritestreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFWriteStreamGetStatus](<cfwritestreamgetstatus(__).md>) — Returns the current state of a stream.
