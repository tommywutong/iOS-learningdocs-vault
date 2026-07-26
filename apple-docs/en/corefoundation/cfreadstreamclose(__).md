---
title: 'CFReadStreamClose(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfreadstreamclose(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfreadstreamclose(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfreadstreamclose%28_%3A%29.json'
content_hash: 'sha256:a03823c829daae0b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFReadStreamClose(_:)

<sub>Function</sub>

Closes a readable stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFReadStreamClose(_ stream: CFReadStream!)
```

## Parameters

- `stream` — The stream to close.

## Discussion

This function terminates the flow of bytes and releases any system resources required by the stream. The stream is removed from any run loops in which it was scheduled. Once closed, the stream cannot be reopened.

## See Also

### Opening and Closing a Read Stream

- [CFReadStreamOpen](<cfreadstreamopen(__).md>) — Opens a stream for reading.
