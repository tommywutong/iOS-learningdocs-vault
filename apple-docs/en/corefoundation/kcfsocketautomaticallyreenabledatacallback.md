---
title: kCFSocketAutomaticallyReenableDataCallBack
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfsocketautomaticallyreenabledatacallback
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenabledatacallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfsocketautomaticallyreenabledatacallback.json'
content_hash: 'sha256:5a9cd0855945dd78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFSocketAutomaticallyReenableDataCallBack

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFSocketAutomaticallyReenableDataCallBack: CFOptionFlags { get }
```

## Discussion

When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the data callback is called every time the socket has read some data. When disabled, the data callback is called only once the next time data are read. The data callback is automatically reenabled by default.

## See Also

### Constants

- [kCFSocketAutomaticallyReenableReadCallBack](kcfsocketautomaticallyreenablereadcallback.md)
- [kCFSocketAutomaticallyReenableAcceptCallBack](kcfsocketautomaticallyreenableacceptcallback.md)
- [kCFSocketAutomaticallyReenableWriteCallBack](kcfsocketautomaticallyreenablewritecallback.md)
- [kCFSocketLeaveErrors](kcfsocketleaveerrors.md)
- [kCFSocketCloseOnInvalidate](kcfsocketcloseoninvalidate.md) — When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.
