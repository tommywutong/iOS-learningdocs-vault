---
title: 'CFWriteStreamCanAcceptBytes(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamcanacceptbytes(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamcanacceptbytes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamcanacceptbytes%28_%3A%29.json'
content_hash: 'sha256:824a945482db814b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamCanAcceptBytes(_:)

<sub>Function</sub>

Returns whether a writable stream can accept new data without blocking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamCanAcceptBytes(_ stream: CFWriteStream!) -> Bool
```

## Parameters

- `stream` — The stream to examine.

## Return Value

`true` if data can be written to `stream` without blocking, `false` otherwise. If `stream` cannot tell if data can be written without actually trying to write the data, this function returns `true`.

## See Also

### Examining Stream Properties

- [CFWriteStreamCopyProperty](<cfwritestreamcopyproperty(____).md>) — Returns the value of a property for a stream.
- [CFWriteStreamCopyError](<cfwritestreamcopyerror(__).md>) — Returns the error associated with a stream.
- [CFWriteStreamGetError](<cfwritestreamgeterror(__).md>) — Returns the error status of a stream. _(deprecated)_
- [CFWriteStreamGetStatus](<cfwritestreamgetstatus(__).md>) — Returns the current state of a stream.
