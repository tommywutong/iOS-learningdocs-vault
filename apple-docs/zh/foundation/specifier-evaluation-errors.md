---
title: NSScriptObjectSpecifier — 说明符求值错误
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/specifier-evaluation-errors
source_url: 'https://developer.apple.com/documentation/foundation/specifier-evaluation-errors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/specifier-evaluation-errors.json'
content_hash: 'sha256:77e5181052de0c39'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [脚本支持](scripting-support.md) · [NSScriptObjectSpecifier](nsscriptobjectspecifier.md)

# NSScriptObjectSpecifier — 说明符求值错误

<sub>API 集合</sub>

`NSScriptObjectSpecifier` 为求值说明符时出现的特定问题提供以下错误码常量：

## 主题

### 常量

- [NSNoSpecifierError](nsnospecifiererror.md) — 未遇到错误。
- [NSNoTopLevelContainersSpecifierError](nsnotoplevelcontainersspecifiererror.md) — 有人以 `nil` 调用了 `evaluate`。
- [NSContainerSpecifierError](nscontainerspecifiererror.md) — 求值容器说明符时出错。
- [NSUnknownKeySpecifierError](nsunknownkeyspecifiererror.md) — 接收者无法识别该键。
- [NSInvalidIndexSpecifierError](nsinvalidindexspecifiererror.md) — 索引越界。
- [NSInternalSpecifierError](nsinternalspecifiererror.md) — 其他内部错误。
- [NSOperationNotSupportedForKeySpecifierError](nsoperationnotsupportedforkeyspecifiererror.md) — 尝试对某个键执行不受支持的操作。
