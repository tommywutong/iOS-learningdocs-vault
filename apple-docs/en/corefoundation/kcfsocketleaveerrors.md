---
title: kCFSocketLeaveErrors
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfsocketleaveerrors
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfsocketleaveerrors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfsocketleaveerrors.json'
content_hash: 'sha256:465df8a12bd1344d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFSocketLeaveErrors

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var kCFSocketLeaveErrors: CFOptionFlags { get }
```

## Discussion

Normally, the CFNetwork stack calls getsockopt(2) macOS Developer Tools Manual Page to read the error code from the socket prior to calling your write callback. This also has the effect of clearing any pending errors on the socket.

If this flag is set, this call is skipped so that you can check for specific socket errors in your write callback.

## See Also

### Constants

- [kCFSocketAutomaticallyReenableReadCallBack](kcfsocketautomaticallyreenablereadcallback.md)
- [kCFSocketAutomaticallyReenableAcceptCallBack](kcfsocketautomaticallyreenableacceptcallback.md)
- [kCFSocketAutomaticallyReenableDataCallBack](kcfsocketautomaticallyreenabledatacallback.md)
- [kCFSocketAutomaticallyReenableWriteCallBack](kcfsocketautomaticallyreenablewritecallback.md)
- [kCFSocketCloseOnInvalidate](kcfsocketcloseoninvalidate.md) — When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.
