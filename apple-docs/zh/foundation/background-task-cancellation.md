---
title: 后台任务取消
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/background-task-cancellation
source_url: 'https://developer.apple.com/documentation/foundation/background-task-cancellation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/background-task-cancellation.json'
content_hash: 'sha256:b14bbe69813daf33'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Foundation](../foundation.md) · [URL Loading System](url-loading-system.md) · [URLSession](urlsession.md)

# 后台任务取消

<sub>API 集合</sub>

指明后台任务取消原因的常量。

## 概述

这些值与 [NSError](nserror.md) 对象的 `userInfo` 字典中的 [NSURLErrorBackgroundTaskCancelledReasonKey](nsurlerrorbackgroundtaskcancelledreasonkey.md) 键配合使用。

## 主题

### 取消原因

- [NSURLErrorCancelledReasonBackgroundUpdatesDisabled](nsurlerrorcancelledreasonbackgroundupdatesdisabled.md) — 表示系统因后台任务被停用而取消后台任务的原因。
- [NSURLErrorCancelledReasonInsufficientSystemResources](nsurlerrorcancelledreasoninsufficientsystemresources.md) — 表示系统因没有足够资源执行任务而取消后台任务的原因。
- [NSURLErrorCancelledReasonUserForceQuitApplication](nsurlerrorcancelledreasonuserforcequitapplication.md) — 表示系统因用户强制退出 App 而取消后台任务的原因。

## 另请参阅

### 处理错误

- [URL 会话错误字典键](url-session-error-dictionary-keys.md) — 与 URL 会话和任务返回的错误对象配合使用的键。
