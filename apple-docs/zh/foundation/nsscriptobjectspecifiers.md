---
title: NSScriptObjectSpecifiers
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifiers
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifiers.json'
content_hash: 'sha256:9c03d9f04a5a40f5'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [脚本支持](scripting-support.md)

# NSScriptObjectSpecifiers

一组提供额外对象说明符功能的方法。

## 概述

这些方法允许可编写脚本的对象在 App 中为自身提供完全指定的对象说明符。它们还允许对象容器自行执行说明符求值。

如需全面了解对象说明符（包括示例代码），请参阅 [Cocoa 脚本指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)中的[对象说明符](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_object_specifiers/SAppsObjectSpecifiers.html#//apple_ref/doc/uid/TP40002164-CH3)。

## 主题

### 使用对象说明符

- [objectSpecifier](../objectivec/nsobject-swift.class/objectspecifier.md) — 返回接收者的对象说明符。
- [indicesOfObjects(byEvaluatingObjectSpecifier:)](<../objectivec/nsobject-swift.class/indicesofobjects(byevaluatingobjectspecifier_).md>) — 返回指定容器对象的索引。

## 另请参阅

### 相关文档

- [Cocoa 脚本指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### NSObject 脚本支持

- [NSComparisonMethods](nscomparisonmethods.md) — 一组默认比较方法，可用于执行说明符测试。
- [NSScriptingComparisonMethods](../objectivec/nsscriptingcomparisonmethods.md) — 一组用于比较脚本对象的方法。
- [NSScriptKeyValueCoding](../objectivec/nsscriptkeyvaluecoding.md) — 一组为键值编码提供额外功能的方法。
- [NSScriptCoercionHandler](nsscriptcoercionhandler.md) — 将一种脚本数据转换为另一种脚本数据的机制。
- [NSScriptExecutionContext](nsscriptexecutioncontext.md) — 执行当前脚本命令的上下文。
