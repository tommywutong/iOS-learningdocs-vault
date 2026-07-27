---
title: URL 加载系统的错误信息键
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/url-loading-system-error-info-keys
source_url: 'https://developer.apple.com/documentation/foundation/url-loading-system-error-info-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url-loading-system-error-info-keys.json'
content_hash: 'sha256:ea59e257204bfa68'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md)

# URL 加载系统的错误信息键

<sub>API 集合</sub>

识别 URL 加载 API 产生的错误对象的 user info 字典中的这些键。

## 概述

这些键仅存在于 [NSURLErrorDomain](nsurlerrordomain.md) 中。

## 主题

### 键

- [NSURLErrorFailingURLErrorKey](nsurlerrorfailingurlerrorkey.md) — 导致加载失败的 URL。
- [NSURLErrorFailingURLPeerTrustErrorKey](nsurlerrorfailingurlpeertrusterrorkey.md) — 失败的 SSL 握手的状态。
- [NSURLErrorFailingURLStringErrorKey](nsurlerrorfailingurlstringerrorkey.md) — 导致加载失败的 URL。 _(已废弃)_
- [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) — 错误字典中提供取消后台任务原因的一个键。
- [URL Session Background Task Cancellation Reasons](url-session-background-task-cancellation-reasons.md) — 表明系统为何取消某个后台任务的原因。
- [NSURLErrorNetworkUnavailableReasonKey](nsurlerrornetworkunavailablereasonkey.md) — 某个任务的网络不可用的原因。
- [NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md) — 一个枚举，说明某个任务为何无法满足网络限制条件的原因。

### 已废弃

- [NSErrorFailingURLStringKey](nserrorfailingurlstringkey.md) — 导致错误的 URL。 _(已废弃)_

## 另请参阅

### 错误

- [URLError](urlerror.md) — URL 加载 API 返回的错误代码。
