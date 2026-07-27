---
title: NSComparisonMethods
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscomparisonmethods
source_url: 'https://developer.apple.com/documentation/foundation/nscomparisonmethods'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscomparisonmethods.json'
content_hash: 'sha256:001083b52c264088'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md) · [脚本支持](scripting-support.md)

# NSComparisonMethods

一组用于执行说明符测试的默认比较方法。

## 概述

如果你的可脚本化对象需要为脚本编程目的执行比较，则可能需要实现 NSScriptingComparisonMethods 中声明的一些方法。`NSObject` 为其中许多方法提供的默认实现适用于实现了单个比较方法的对象，该方法的选择器（selector）、签名和描述与以下内容匹配：

```objc
- (NSComparisonResult)compare:(id)object;
```

如果接收者小于 `object`，此方法应返回 `NSOrderedAscending`；如果接收者大于 `object`，则返回 `NSOrderedDescending`；如果接收者与 `object` 相等，则返回 `NSOrderedSame`。例如，`NSString` 没有实现此非正式协议中声明的大多数方法，但 `NSString` 对象仍能正确处理符合此协议的消息，因为 `NSString` 实现了满足必要要求的 `compare:` 方法。Cocoa 还为 `NSDate`、`NSDecimalNumber` 和 `NSValue` 类提供了适当的 `compare:` 方法实现。

## 主题

### 执行比较

- [doesContain(_:)](<../objectivec/nsobject-swift.class/doescontain(__).md>) — 返回一个布尔值，指示接收者是否包含给定对象。
- [isCaseInsensitiveLike(_:)](<../objectivec/nsobject-swift.class/iscaseinsensitivelike(__).md>) — 返回一个布尔值，指示忽略接收者中的字符大小写时，接收者是否被视为与给定字符串“相似”。
- [isEqual(to:)](<../objectivec/nsobject-swift.class/isequal(to_).md>) — 返回一个布尔值，指示接收者是否等于另一个给定对象。
- [isGreaterThan(_:)](<../objectivec/nsobject-swift.class/isgreaterthan(__).md>) — 返回一个布尔值，指示接收者是否大于另一个给定对象。
- [isGreaterThanOrEqual(to:)](<../objectivec/nsobject-swift.class/isgreaterthanorequal(to_).md>) — 返回一个布尔值，指示接收者是否大于或等于另一个给定对象。
- [isLessThan(_:)](<../objectivec/nsobject-swift.class/islessthan(__).md>) — 返回一个布尔值，指示接收者是否小于另一个给定对象。
- [isLessThanOrEqual(to:)](<../objectivec/nsobject-swift.class/islessthanorequal(to_).md>) — 返回一个布尔值，指示接收者是否小于或等于另一个给定对象。
- [isLike(_:)](<../objectivec/nsobject-swift.class/islike(__).md>) — 返回一个布尔值，指示接收者是否与另一个给定对象“相似”。
- [isNotEqual(to:)](<../objectivec/nsobject-swift.class/isnotequal(to_).md>) — 返回一个布尔值，指示接收者是否不等于另一个给定对象。

## 另请参阅

### 相关文档

- [Cocoa 脚本编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### NSObject 脚本支持

- [NSScriptingComparisonMethods](../objectivec/nsscriptingcomparisonmethods.md) — 一组用于比较脚本对象的方法。
- [NSScriptKeyValueCoding](../objectivec/nsscriptkeyvaluecoding.md) — 一组为使用键值编码提供额外功能的方法。
- [NSScriptObjectSpecifiers](nsscriptobjectspecifiers.md) — 一组提供额外对象说明符功能的方法。
- [NSScriptCoercionHandler](nsscriptcoercionhandler.md) — 一种将一种脚本数据转换为另一种的机制。
- [NSScriptExecutionContext](nsscriptexecutioncontext.md) — 执行当前脚本命令的上下文。
