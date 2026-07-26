---
title: pipe
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nspipe/pipe
source_url: 'https://developer.apple.com/documentation/foundation/nspipe/pipe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nspipe/pipe.json'
content_hash: 'sha256:a061e28d5bd3f9e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Pipe](../pipe.md)

# pipe

<sub>Type Method</sub>

Returns an `NSPipe` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (NSPipe *) pipe;
```

## Return Value

An initialized `NSPipe` object. Returns `nil` if the method encounters errors while attempting to create the pipe or the `NSFileHandle` objects that serve as endpoints of the pipe.
