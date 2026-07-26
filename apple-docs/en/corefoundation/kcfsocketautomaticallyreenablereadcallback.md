---
title: kCFSocketAutomaticallyReenableReadCallBack
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfsocketautomaticallyreenablereadcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenablereadcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfsocketautomaticallyreenablereadcallback.json'
content_hash: 'sha256:16c640b9da2c9413'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFSocketAutomaticallyReenableReadCallBack

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFSocketAutomaticallyReenableReadCallBack: CFOptionFlags { get }
```

## Discussion

When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the read callback is called every time the sockets has data to be read. When disabled, the read callback is called only once the next time data are available. The read callback is automatically reenabled by default.

## See Also

### Constants

- [kCFSocketAutomaticallyReenableAcceptCallBack](kcfsocketautomaticallyreenableacceptcallback.md)
- [kCFSocketAutomaticallyReenableDataCallBack](kcfsocketautomaticallyreenabledatacallback.md)
- [kCFSocketAutomaticallyReenableWriteCallBack](kcfsocketautomaticallyreenablewritecallback.md)
- [kCFSocketLeaveErrors](kcfsocketleaveerrors.md)
- [kCFSocketCloseOnInvalidate](kcfsocketcloseoninvalidate.md) — When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.
