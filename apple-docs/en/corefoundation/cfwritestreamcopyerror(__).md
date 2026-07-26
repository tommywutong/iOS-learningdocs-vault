---
title: 'CFWriteStreamCopyError(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamcopyerror(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamcopyerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamcopyerror%28_%3A%29.json'
content_hash: 'sha256:d019474ff618d9ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamCopyError(_:)

<sub>Function</sub>

Returns the error associated with a stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamCopyError(_ stream: CFWriteStream!) -> CFError!
```

## Parameters

- `stream` — The stream to examine.

## Return Value

A CFError object that describes the current problem with stream, or `NULL` if there is no error. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Examining Stream Properties

- [CFWriteStreamCanAcceptBytes](<cfwritestreamcanacceptbytes(__).md>) — Returns whether a writable stream can accept new data without blocking.
- [CFWriteStreamCopyProperty](<cfwritestreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFWriteStreamGetError](<cfwritestreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFWriteStreamGetStatus](<cfwritestreamgetstatus(__).md>) — Returns the current state of a stream.
