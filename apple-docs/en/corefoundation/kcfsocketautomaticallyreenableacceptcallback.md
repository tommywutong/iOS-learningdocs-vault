---
title: kCFSocketAutomaticallyReenableAcceptCallBack
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfsocketautomaticallyreenableacceptcallback
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenableacceptcallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfsocketautomaticallyreenableacceptcallback.json'
content_hash: 'sha256:dbc491fa4a986675'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFSocketAutomaticallyReenableAcceptCallBack

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFSocketAutomaticallyReenableAcceptCallBack: CFOptionFlags { get }
```

## Discussion

When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the accept callback is called every time someone connects to your socket. When disabled, the accept callback is called only once the next time a new socket connection is accepted. The accept callback is automatically reenabled by default.

## See Also

### Constants

- [kCFSocketAutomaticallyReenableReadCallBack](kcfsocketautomaticallyreenablereadcallback.md)
- [kCFSocketAutomaticallyReenableDataCallBack](kcfsocketautomaticallyreenabledatacallback.md)
- [kCFSocketAutomaticallyReenableWriteCallBack](kcfsocketautomaticallyreenablewritecallback.md)
- [kCFSocketLeaveErrors](kcfsocketleaveerrors.md)
- [kCFSocketCloseOnInvalidate](kcfsocketcloseoninvalidate.md) — When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.
