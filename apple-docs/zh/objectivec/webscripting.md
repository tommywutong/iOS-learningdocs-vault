---
title: WebScripting
framework: Objective-C Runtime
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/objectivec/webscripting
source_url: 'https://developer.apple.com/documentation/objectivec/webscripting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/webscripting.json'
content_hash: 'sha256:21d132a2f61568f2'
translated: true
---

> 导航：[Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md) · [NSObject](nsobject-swift.class.md)

# WebScripting

<sub>API 集合</sub>

`WebScripting` 是一个非正式协议，定义了一些方法，类可以实现这些方法将其接口导出到诸如 JavaScript 之类的 WebScript 环境。

## 概述

并非所有属性和方法都会默认导出到 JavaScript。对象需要实现下文描述的类方法，来指定要导出的属性和方法。此外，如果某个方法的返回类型及其所有参数都不是 Objective-C 对象或标量，那么该方法就不会被导出。

作为 Objective-C 对象的方法参数和返回类型，会被转换为脚本环境中相应的类型。例如：

- `nil` 会被转换为 undefined。
- `NSNumber` 对象会被转换为 JavaScript 数字。
- `NSString` 对象会被转换为 JavaScript 字符串。
- `NSArray` 对象会被映射为特殊的只读数组。
- `NSNull` 会被转换为 JavaScript 的 `null`。
- `WebUndefined` 会被转换为 undefined。
- `WebScriptObject` 的实例会为脚本环境解包。

所有其他类的实例在传递给脚本之前都会被包装，并在返回 Objective-C 时解包。`int` 和 `char` 这类基础类型会在 JavaScript 中被转换为数字类型。

对对象特性（如实例变量）的访问由键值编码（KVC）管理。KVC 方法 `setValue:forKey:` 和 `valueForKey:` 用于从脚本环境访问对象的特性。此外，脚本环境可以尝试任意数量的、未被你的类导出的特性请求或方法调用。你可以通过重写键值编码协议中的 `setValue:forUndefinedKey:` 和 `valueForUndefinedKey:` 方法来管理这些请求。

可以通过向相关的 `WebScriptObject` 实例发送 [throwException(_:)](<../webkit/webscriptobject/throwexception(__).md>) 消息，从脚本环境中引发异常。引发异常的方法必须在脚本调用的作用域内。

## 主题

### Getting attributes

- [+ webScriptNameForKey:](<nsobject-swift.class/webscriptname(forkey_).md>) — 返回由键指定的特性在脚本环境中的名称。
- [+ webScriptNameForSelector:](<nsobject-swift.class/webscriptname(for_).md>) — 返回某个选择器（selector）在脚本环境中的名称。
- [+ isSelectorExcludedFromWebScript:](<nsobject-swift.class/isselectorexcluded(fromwebscript_).md>) — 返回某个选择器是否应对脚本环境隐藏。
- [+ isKeyExcludedFromWebScript:](<nsobject-swift.class/iskeyexcluded(fromwebscript_).md>) — 返回某个键是否应对脚本环境隐藏。

### Invoking methods

- [- invokeDefaultMethodWithArguments:](<nsobject-swift.class/invokedefaultmethod(witharguments_).md>) — 当脚本尝试直接在某个已暴露的对象上调用方法时执行。
- [- invokeUndefinedMethodFromWebScript:withArguments:](<nsobject-swift.class/invokeundefinedmethod(fromwebscript_witharguments_).md>) — 处理来自脚本环境的未定义方法调用。

### Finalizing

- [- finalizeForWebScript](<nsobject-swift.class/finalizeforwebscript().md>) — 在脚本环境重置时执行清理工作。

## 另请参阅

### 相关文档

- [WebKit Objective-C Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/DisplayWebContent.html#//apple_ref/doc/uid/10000164i)
