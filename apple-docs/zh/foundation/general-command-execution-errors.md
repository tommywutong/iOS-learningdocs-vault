---
title: NSScriptCommand——常规命令执行错误
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/general-command-execution-errors
source_url: 'https://developer.apple.com/documentation/foundation/general-command-execution-errors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/general-command-execution-errors.json'
content_hash: 'sha256:750cd06072ce2772'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [脚本支持](scripting-support.md) · [NSScriptCommand](nsscriptcommand.md)

# NSScriptCommand——常规命令执行错误

<sub>API 集合</sub>

`NSScriptCommand` 使用以下错误码表示常规命令执行问题：

## 主题

### 常量

- [NSNoScriptError](nsnoscripterror.md) — 没有错误。
- [NSReceiverEvaluationScriptError](nsreceiverevaluationscripterror.md) — 找不到由命令的直接参数指定的一个或多个对象。
- [NSKeySpecifierEvaluationScriptError](nskeyspecifierevaluationscripterror.md) — 找不到由键指定的一个或多个对象（适用于支持键说明符的命令）。
- [NSArgumentEvaluationScriptError](nsargumentevaluationscripterror.md) — 找不到由参数指定的对象。
- [NSReceiversCantHandleCommandScriptError](nsreceiverscanthandlecommandscripterror.md) — 接收方不支持发送给它们的命令。
- [NSRequiredArgumentsMissingScriptError](nsrequiredargumentsmissingscripterror.md) — 缺少一个或多个参数。
- [NSArgumentsWrongScriptError](nsargumentswrongscripterror.md) — 一个或多个参数类型错误，或由于其他原因而无效。
- [NSUnknownKeyScriptError](nsunknownkeyscripterror.md) — 发生无法识别的错误；这表明 App 的脚本支持中存在错误。
- [NSInternalScriptError](nsinternalscripterror.md) — 发生无法识别的内部错误；这表明 App 的脚本支持中存在错误。
- [NSOperationNotSupportedForKeyScriptError](nsoperationnotsupportedforkeyscripterror.md) — 脚本命令的实现发出错误信号。
- [NSCannotCreateScriptCommandError](nscannotcreatescriptcommanderror.md) — 无法创建脚本命令；收到无效或无法识别的 Apple event。
