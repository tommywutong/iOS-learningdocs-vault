---
title: 'init(type:path:oflag:mode:queue:cleanupHandler:)'
framework: Dispatch
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchio/init(type:path:oflag:mode:queue:cleanuphandler:)-25rlb'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchio/init(type:path:oflag:mode:queue:cleanuphandler:)-25rlb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchio/init%28type%3Apath%3Aoflag%3Amode%3Aqueue%3Acleanuphandler%3A%29-25rlb.json'
content_hash: 'sha256:2d360c4c5571a8da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchIO](../dispatchio.md)

# init(type:path:oflag:mode:queue:cleanupHandler:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(type: DispatchIO.StreamType, path: UnsafePointer<Int8>, oflag: Int32, mode: mode_t, queue: DispatchQueue, cleanupHandler: @escaping (Int32) -> Void)
```
