---
title: URL 会话后台任务取消原因
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/url-session-background-task-cancellation-reasons
source_url: 'https://developer.apple.com/documentation/foundation/url-session-background-task-cancellation-reasons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url-session-background-task-cancellation-reasons.json'
content_hash: 'sha256:ff2e84e42e42a40e'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URL Loading System error info keys](url-loading-system-error-info-keys.md)

# URL 会话后台任务取消原因

<sub>API 集合</sub>

指明系统为何取消某个后台任务的原因。

## 主题

### Cancellation reasons

- [NSURLErrorCancelledReasonBackgroundUpdatesDisabled](nsurlerrorcancelledreasonbackgroundupdatesdisabled.md) — 一个原因，表示系统因为后台任务被禁用而取消了该后台任务。
- [NSURLErrorCancelledReasonInsufficientSystemResources](nsurlerrorcancelledreasoninsufficientsystemresources.md) — 一个原因，表示系统因为缺乏足够的资源来执行该任务而取消了该后台任务。
- [NSURLErrorCancelledReasonUserForceQuitApplication](nsurlerrorcancelledreasonuserforcequitapplication.md) — 一个原因，表示系统因为用户强制退出了该应用程序而取消了该后台任务。

## 另请参阅

### Keys

- [NSURLErrorFailingURLErrorKey](nsurlerrorfailingurlerrorkey.md) — 导致某次加载失败的 URL。
- [NSURLErrorFailingURLPeerTrustErrorKey](nsurlerrorfailingurlpeertrusterrorkey.md) — 某次失败的 SSL 握手的状态。
- [NSURLErrorFailingURLStringErrorKey](nsurlerrorfailingurlstringerrorkey.md) — 导致某次加载失败的 URL。_(已废弃)_
- [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) — 错误字典中的一个键，提供取消某个后台任务的原因。
- [NSURLErrorNetworkUnavailableReasonKey](nsurlerrornetworkunavailablereasonkey.md) — 某个任务的网络不可用的原因。
- [NetworkUnavailableReason](urlerror/networkunavailablereason-swift.enum.md) — 一个枚举，列出了任务无法满足联网约束条件的各种原因。
