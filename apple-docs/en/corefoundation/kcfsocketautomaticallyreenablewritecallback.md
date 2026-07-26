---
title: kCFSocketAutomaticallyReenableWriteCallBack
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfsocketautomaticallyreenablewritecallback
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenablewritecallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfsocketautomaticallyreenablewritecallback.json'
content_hash: 'sha256:f57925124b6eab40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFSocketAutomaticallyReenableWriteCallBack

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFSocketAutomaticallyReenableWriteCallBack: CFOptionFlags { get }
```

## Discussion

When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the write callback is called every time more data can be written to the socket. When disabled, the write callback is called only the next time data can be written. The write callback is not automatically reenabled by default.

## See Also

### Constants

- [kCFSocketAutomaticallyReenableReadCallBack](kcfsocketautomaticallyreenablereadcallback.md)
- [kCFSocketAutomaticallyReenableAcceptCallBack](kcfsocketautomaticallyreenableacceptcallback.md)
- [kCFSocketAutomaticallyReenableDataCallBack](kcfsocketautomaticallyreenabledatacallback.md)
- [kCFSocketLeaveErrors](kcfsocketleaveerrors.md)
- [kCFSocketCloseOnInvalidate](kcfsocketcloseoninvalidate.md) — When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.
