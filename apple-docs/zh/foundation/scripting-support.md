---
title: 脚本支持
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/scripting-support
source_url: 'https://developer.apple.com/documentation/foundation/scripting-support'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scripting-support.json'
content_hash: 'sha256:2837e31ed4305ed5'
translated: true
---

> 导航：[技术](../technologies.md) · [Foundation](../foundation.md)

# 脚本支持

<sub>API 集合</sub>

允许用户使用 AppleScript 和其他自动化技术控制你的 App，或从 App 内运行脚本。

## 主题

### 脚本执行

- [NSAppleScript](nsapplescript.md) — 提供加载、编译和执行脚本能力的对象。

### Apple 事件处理

- [NSAppleEventDescriptor](nsappleeventdescriptor.md) — Apple 事件描述符数据类型的包装器。
- [NSAppleEventManager](nsappleeventmanager.md) — 为特定类型的 Apple 事件注册处理程序例程并将事件分派给这些处理程序的机制。

### 脚本命令

- [NSScriptCommand](nsscriptcommand.md) — 一条自包含的脚本语句。
- [NSQuitCommand](nsquitcommand.md) — 退出指定 App 的命令。
- [NSSetCommand](nssetcommand.md) — 将一个或多个特性（attribute）或关系设为一个或多个值的命令。
- [NSMoveCommand](nsmovecommand.md) — 移动一个或多个可编写脚本对象的命令。
- [NSCreateCommand](nscreatecommand.md) — 创建可编写脚本对象的命令。
- [NSDeleteCommand](nsdeletecommand.md) — 删除可编写脚本对象的命令。
- [NSExistsCommand](nsexistscommand.md) — 确定可编写脚本对象是否存在的命令。
- [NSGetCommand](nsgetcommand.md) — 从可编写脚本对象中获取值或对象的命令。
- [NSCloneCommand](nsclonecommand.md) — 克隆一个或多个可编写脚本对象的命令。
- [NSCountCommand](nscountcommand.md) — 对指定对象容器中指定类的对象数量进行计数的命令。
- [NSCloseCommand](nsclosecommand.md) — 关闭一个或多个可编写脚本对象的命令。

### 对象说明符

- [NSScriptObjectSpecifier](nsscriptobjectspecifier.md) — 用于表示自然语言表达式的抽象类。
- [NSPropertySpecifier](nspropertyspecifier.md) — 简单特性值、一对一关系或对多关系全部元素的说明符。
- [NSPositionalSpecifier](nspositionalspecifier.md) — 容器中相对于另一对象的插入点说明符。
- [NSRandomSpecifier](nsrandomspecifier.md) — 集合中任意对象的说明符；如果不是一对多关系，则为唯一对象的说明符。
- [NSRangeSpecifier](nsrangespecifier.md) — 容器中某一对象范围的说明符。
- [NSUniqueIDSpecifier](nsuniqueidspecifier.md) — 通过唯一 ID 指定集合（或容器）中对象的说明符。
- [NSWhoseSpecifier](nswhosespecifier.md) — 指示集合中符合某个条件的每个对象的说明符。
- [NSNameSpecifier](nsnamespecifier.md) — 通过名称指定集合（或容器）中对象的说明符。
- [NSMiddleSpecifier](nsmiddlespecifier.md) — 指示集合中间对象的说明符；如果不是一对多关系，则指示唯一对象。
- [NSIndexSpecifier](nsindexspecifier.md) — 表示集合（或容器）中具有某个索引号的对象的说明符。
- [NSRelativeSpecifier](nsrelativespecifier.md) — 通过对象相对于另一对象的位置指示集合中对象的说明符。

### 脚本字典描述

- [NSScriptSuiteRegistry](nsscriptsuiteregistry.md) — App 运行时脚本化信息的顶层存储库。
- [NSScriptClassDescription](nsscriptclassdescription.md) — macOS App 支持的可编写脚本类。
- [NSClassDescription](nsclassdescription.md) — 提供查询某个类的关系和属性（property）所需接口的抽象类。
- [NSScriptCommandDescription](nsscriptcommanddescription.md) — macOS App 支持的脚本命令。

### 对象匹配测试

- [NSScriptWhoseTest](nsscriptwhosetest.md) — 为逐个或成组测试说明符提供基础的抽象类。
- [NSSpecifierTest](nsspecifiertest.md) — 对象说明符与测试对象之间的比较。
- [NSLogicalTest](nslogicaltest.md) — 一个或多个说明符测试的逻辑组合。

### NSObject 脚本支持

- [NSComparisonMethods](nscomparisonmethods.md) — 一组默认比较方法，可用于执行说明符测试。
- [NSScriptingComparisonMethods](../objectivec/nsscriptingcomparisonmethods.md) — 一组用于比较脚本对象的方法。
- [NSScriptKeyValueCoding](../objectivec/nsscriptkeyvaluecoding.md) — 一组为键值编码提供额外功能的方法。
- [NSScriptObjectSpecifiers](nsscriptobjectspecifiers.md) — 一组提供额外对象说明符功能的方法。
- [NSScriptCoercionHandler](nsscriptcoercionhandler.md) — 将一种脚本数据转换为另一种脚本数据的机制。
- [NSScriptExecutionContext](nsscriptexecutioncontext.md) — 执行当前脚本命令的上下文。

## 另请参阅

### App 支持

- [任务管理](task-management.md) — 管理 App 的工作及其与 Handoff 和“快捷指令”等系统服务的交互方式。
- [资源](resources.md) — 访问与你的 App 捆绑在一起的资源及其他数据。
- [通知](notifications.md) — 用于广播信息和订阅广播的设计模式。
- [App 扩展支持](app-extension-support.md) — 管理 App 扩展与托管它的 App 之间的交互。
- [错误与异常](errors-and-exceptions.md) — 响应与 API 交互时出现的问题，并微调 App 以改善调试体验。
