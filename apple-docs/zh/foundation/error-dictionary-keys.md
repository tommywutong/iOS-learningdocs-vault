---
title: 错误字典键
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/error-dictionary-keys
source_url: 'https://developer.apple.com/documentation/foundation/error-dictionary-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/error-dictionary-keys.json'
content_hash: 'sha256:73700e6e2a0b9b84'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [脚本支持](scripting-support.md) · [NSAppleScript](nsapplescript.md)

# 错误字典键

<sub>API 集合</sub>

如果 [- initWithContentsOfURL:error:](<nsapplescript/init(contentsof_error_).md>)、[- compileAndReturnError:](<nsapplescript/compileandreturnerror(__).md>)、[- executeAndReturnError:](<nsapplescript/executeandreturnerror(__).md>) 或 [- executeAppleEvent:error:](<nsapplescript/executeappleevent(__error_).md>) 的结果表示失败（分别为 `nil`、[false](../swift/false.md)、`nil` 或 `nil`），则系统会在 error 参数指向的位置放置一个指向自动释放字典的指针。错误信息字典可以包含使用以下键任意组合的条目，也可以完全不包含条目。

## 主题

### 常量

- [NSAppleScriptErrorMessage](nsapplescript/errormessage.md) — 提供错误状况详细描述的 `NSString`。
- [NSAppleScriptErrorNumber](nsapplescript/errornumber.md) — 指定错误编号的 `NSNumber`。
- [NSAppleScriptErrorAppName](nsapplescript/errorappname.md) — 指定生成错误的 App 名称的 `NSString`。
- [NSAppleScriptErrorBriefMessage](nsapplescript/errorbriefmessage.md) — 提供错误简短描述的 `NSString`。
- [NSAppleScriptErrorRange](nsapplescript/errorrange.md) — 指定范围的 `NSValue`。
