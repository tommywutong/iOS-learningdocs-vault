---
title: NSErrorRecoveryAttempting
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nserrorrecoveryattempting
source_url: 'https://developer.apple.com/documentation/foundation/nserrorrecoveryattempting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nserrorrecoveryattempting.json'
content_hash: 'sha256:64cd9e6f9dc5aa9d'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [错误与异常](errors-and-exceptions.md) · [NSError](nserror.md)

# NSErrorRecoveryAttempting

一组提供错误恢复选项的方法。

## 概述

`NSErrorRecoveryAttempting` 非正式协议提供了一些方法，让你的 App 能够尝试从错误中恢复。当返回的 `NSError` 对象将实现此协议的对象指定为错误的 `recoveryAttempter`，并且用户选择了该错误的某个本地化恢复选项时，系统会调用这些方法。具体调用哪个方法取决于错误向用户呈现的方式。如果错误在文稿模态表单中呈现，系统会调用 [attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)](<../objectivec/nsobject-swift.class/attemptrecovery(fromerror_optionindex_delegate_didrecoverselector_contextinfo_).md>)。如果错误在 App 模态对话框中呈现，系统会调用 [attemptRecovery(fromError:optionIndex:)](<../objectivec/nsobject-swift.class/attemptrecovery(fromerror_optionindex_).md>)。

## 主题

### 尝试从错误中恢复

- [attemptRecovery(fromError:optionIndex:delegate:didRecoverSelector:contextInfo:)](<../objectivec/nsobject-swift.class/attemptrecovery(fromerror_optionindex_delegate_didrecoverselector_contextinfo_).md>) — 实现此方法，以尝试从文稿模态表单中显示的错误恢复。
- [attemptRecovery(fromError:optionIndex:)](<../objectivec/nsobject-swift.class/attemptrecovery(fromerror_optionindex_).md>) — 实现此方法，以尝试从 App 模态对话框中显示的错误恢复。

## 另请参阅

### 获取错误恢复尝试器

- [recoveryAttempter](nserror/recoveryattempter.md) — 用户信息字典中与 [NSRecoveryAttempterErrorKey](nsrecoveryattemptererrorkey.md) 键对应的对象。
