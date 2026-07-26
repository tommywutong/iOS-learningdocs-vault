---
title: 'CFWriteStreamClose(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfwritestreamclose(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfwritestreamclose(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfwritestreamclose%28_%3A%29.json'
content_hash: 'sha256:c14be1644aa884fa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFWriteStreamClose(_:)

<sub>Function</sub>

Closes a writable stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFWriteStreamClose(_ stream: CFWriteStream!)
```

## Parameters

- `stream` — The stream to close.

## Discussion

This function terminates the flow of bytes and releases any system resources required by the stream. The stream is removed from any run loops in which it was scheduled. Once closed, the stream cannot be reopened.

## See Also

### Opening and Closing a Stream

- [CFWriteStreamOpen](<cfwritestreamopen(__).md>) — Opens a stream for writing.
