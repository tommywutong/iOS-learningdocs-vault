---
title: CFSocket Flags
framework: Core Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/1560944-cfsocket-flags
source_url: 'https://developer.apple.com/documentation/corefoundation/1560944-cfsocket-flags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/1560944-cfsocket-flags.json'
content_hash: 'sha256:d8dcbf5f7fddbbf2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFSocket](cfsocket.md)

# CFSocket Flags

<sub>API Collection</sub>

Flags that can be set on a CFSocket object to control its behavior.

## Overview

The flags for a CFSocket object are set with [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>). To immediately enable or disable a callback, use [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) and [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>).

## Topics

### Constants

- [kCFSocketAutomaticallyReenableReadCallBack](kcfsocketautomaticallyreenablereadcallback.md)
- [kCFSocketAutomaticallyReenableAcceptCallBack](kcfsocketautomaticallyreenableacceptcallback.md)
- [kCFSocketAutomaticallyReenableDataCallBack](kcfsocketautomaticallyreenabledatacallback.md)
- [kCFSocketAutomaticallyReenableWriteCallBack](kcfsocketautomaticallyreenablewritecallback.md)
- [kCFSocketLeaveErrors](kcfsocketleaveerrors.md)
- [kCFSocketCloseOnInvalidate](kcfsocketcloseoninvalidate.md) — When enabled using [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.

## See Also

### Constants

- [CFSocketCallBackType](cfsocketcallbacktype.md) — Types of socket activity that can cause the callback function of a CFSocket object to be called.
- [CFSocketError](cfsocketerror.md) — Error codes for many CFSocket functions.
