---
title: CFSocket 标志
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
translated: true
---

> 导航： [技术](../technologies.md) · [Core Foundation](../corefoundation.md) · [CFSocket](cfsocket.md)

# CFSocket 标志

<sub>API 集合</sub>

可在 CFSocket 对象上设置以控制其行为的标志。

## 概述

CFSocket 对象的标志通过 [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) 设置。要立即启用或禁用回调，请使用 [CFSocketEnableCallBacks](<cfsocketenablecallbacks(____).md>) 和 [CFSocketDisableCallBacks](<cfsocketdisablecallbacks(____).md>)。

## 主题

### 常量

- [kCFSocketAutomaticallyReenableReadCallBack](kcfsocketautomaticallyreenablereadcallback.md)
- [kCFSocketAutomaticallyReenableAcceptCallBack](kcfsocketautomaticallyreenableacceptcallback.md)
- [kCFSocketAutomaticallyReenableDataCallBack](kcfsocketautomaticallyreenabledatacallback.md)
- [kCFSocketAutomaticallyReenableWriteCallBack](kcfsocketautomaticallyreenablewritecallback.md)
- [kCFSocketLeaveErrors](kcfsocketleaveerrors.md)
- [kCFSocketCloseOnInvalidate](kcfsocketcloseoninvalidate.md) — 使用 [CFSocketSetSocketFlags](<cfsocketsetsocketflags(____).md>) 启用时，与 CFSocket 对象关联的原生套接字（native socket）会在 CFSocket 对象失效时关闭。禁用时，原生套接字保持打开。默认启用此选项。

## 另请参阅

### 常量

- [CFSocketCallBackType](cfsocketcallbacktype.md) — 可导致 CFSocket 对象的回调函数被调用的套接字活动类型。
- [CFSocketError](cfsocketerror.md) — 许多 CFSocket 函数的错误码。
