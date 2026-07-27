---
title: 解读异常信息
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/reading-an-exception-message
source_url: 'https://developer.apple.com/documentation/xcode/reading-an-exception-message'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/reading-an-exception-message.json'
content_hash: 'sha256:5102c9c6849cfe6f'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [使用崩溃报告和设备日志诊断问题](diagnosing-issues-using-crash-reports-and-device-logs.md) · [识别常见崩溃的原因](identifying-the-cause-of-common-crashes.md)

# 解读异常信息

<sub>文章</sub>

了解并处理 App 崩溃的常见原因。

## 概述

框架会检测与使用其 API 相关的常见错误，并在错误发生时引发异常。如果 App 没有处理这些错误（例如，未通过调用 [NSSetUncaughtExceptionHandler(_:)](<../foundation/nssetuncaughtexceptionhandler(__).md>) 安装异常处理程序），App 就会崩溃。操作系统会记录一份崩溃报告，其中包含 App 崩溃时的状态信息。

以下各节分别说明使用框架 API 时的常见错误，以及 App 遇到这些情况时崩溃报告中出现的异常信息。对于每种情况，崩溃报告中的异常线程栈回溯都会显示 App 在代码中崩溃的位置。有关更多信息，请参阅[分析崩溃报告](analyzing-a-crash-report.md)。

### 处理因向集合添加空对象而导致的崩溃

`Foundation` 的集合类（例如 [NSArray](../foundation/nsarray.md)、它的可变子类 [NSMutableArray](../foundation/nsmutablearray.md)），以及对应的 `CoreFoundation` 类型（例如 [CFArray](../corefoundation/cfarray.md)），都不能包含 `nil` 值。此外，字典集合（[NSDictionary](../foundation/nsdictionary.md)、[NSMutableDictionary](../foundation/nsmutabledictionary.md)、[CFDictionary](../corefoundation/cfdictionary.md)）不能包含 `nil` 键。如果 App 向可变集合添加 `nil`，App 会崩溃，并且崩溃报告中会包含类似以下示例的异常信息：

```
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '*** -[__NSArrayM insertObject:atIndex:]: object cannot be nil'
```

如果需要向 `Foundation` 或 `CoreFoundation` 集合类添加一个表示缺少任何有效值的对象，请使用 [null](../foundation/nsnull/null.md) 或 [kCFNull](../corefoundation/kcfnull.md)。否则，请在将对象添加到集合之前测试其值，如果对象为 `nil`，则不要添加。

### 处理因在要求非空参数的 API 中使用空对象而导致的崩溃

许多 API 要求参数非 `nil`，如果收到 `nil` 则会抛出异常。例如，[addAttribute(_:value:range:)](<../foundation/nsmutableattributedstring/addattribute(__value_range_).md>) 要求其 `name` 和 `value` 均非 `nil`。如果 App 向属性字符串添加 `nil` 属性（attribute），App 会崩溃，并且崩溃报告中会包含类似以下示例的异常信息：

```
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: 'NSConcreteMutableAttributedString addAttribute:value:range:: nil value'
```

请确定一个合适的非 `nil` 值作为替代；否则，请避免设置该属性。

要求非 `nil` 参数的 API 包含可空性标注，你也可以为自己的方法、block 和函数添加可空性标注。当你在要求非 `nil` 对象的场合使用可能为 `nil` 的对象时，编译器会检测到这种情况并发出警告。有关更多信息，请参阅[在 Objective-C API 中指定可空性](../swift/designating-nullability-in-objective-c-apis.md)。

### 处理因向类或对象发送无法识别的选择器而导致的崩溃

你通常会通过在源代码中写入方法名称，向 Objective-C 类和对象发送消息；例如，键入 `[myAttributedString addAttribute:aName value:aValue range:aRange];` 来发送 [addAttribute(_:value:range:)](<../foundation/nsmutableattributedstring/addattribute(__value_range_).md>)。在某些情况下，你会动态构造方法名称（也称为_选择器（selector）_），并将其发送给类或对象。常见示例是在 Storyboard 文件中将控制器方法的名称设为操作。如果接收消息的对象或类不响应该选择器，也无法将其转发给另一个对象，App 就会崩溃，并且崩溃报告中会包含类似以下示例的异常信息：

```
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[__NSCFBoolean insertObject:atIndex:]: unrecognized selector sent to instance 0x1e75db6c0'
```

检查方法选择器的拼写是否正确，包括用于指示每个实参的冒号。验证接收对象的类是否实现了请求的方法，或是否将其转发给实现该方法的对象。

### 处理因在不可变集合或序列中插入、替换或删除对象而导致的崩溃

每种常见的 `Foundation` 集合都有一个不可变类（例如 [NSArray](../foundation/nsarray.md)）和一个对应的可变子类（例如 [NSMutableArray](../foundation/nsmutablearray.md)）。这些 Objective-C 类可与对应的 `CoreFoundation` 类型 [CFArray](../corefoundation/cfarray.md) 和 [CFMutableArray](../corefoundation/cfmutablearray.md) 互换。尝试更改不可变集合的内容（例如追加对象）是错误行为。如果 App 尝试更改不可变集合的内容，App 会崩溃，并且崩溃报告中会包含类似以下示例的异常信息：

```
*** Terminating app due to uncaught exception 'NSInternalInconsistencyException', reason: '-[__NSCFArray insertObject:atIndex:]: mutating method sent to immutable object'
```

如果需要修改与其他代码共享的集合，原始集合的来源需要初始化一个可变集合。如果需要更改原始集合的本地副本，而原始集合保持不可变，请使用 `-mutableCopy` 创建可变的本地版本。否则，请移除修改集合的代码。

> [!note] 注意
> 导致此异常的常见原因是错误地互换 `Foundation` 和 `CoreFoundation` 集合类，例如使用 `(__bridge NSMutableArray *)` 将 `CFArrayRef` 转换为 Objective-C。使用免费桥接来互换 `Foundation` 和 `CoreFoundation` 集合类时，请确保 Objective-C 变量的桥接类型与对应 `CoreFoundation` 类型相匹配，包括它们的可变性。

### 处理因使用越界索引、范围或位置而导致的崩溃

接受表示有序集合或序列中对象或其他数据位置的参数的 API，如果该位置超出所包含集合的范围，就会引发异常。接受表示序列中一段值范围的参数的 API，如果范围起点或终点超出所包含集合，也会引发异常。

> [!note] 注意
> 特殊值 [NSNotFound](../foundation/nsnotfound-4qp9h.md) 并非用于表示集合或序列中的位置；如果在代码中以这种方式使用它，将导致越界异常。

如果 App 尝试访问集合或序列范围之外的内容，App 会崩溃，并且崩溃报告中会包含类似以下示例的异常信息：

```
*** Terminating app due to uncaught exception 'NSRangeException', reason: '*** -[__NSArrayM objectAtIndex:]: index 12 beyond bounds [0 .. 0]'
```

在从空数组中请求特定索引处对象这一特殊情况下，异常信息类似以下示例：

```
*** Terminating app due to uncaught exception 'NSRangeException', reason: '*** -[__NSArray0 objectAtIndex:]: index 12 beyond bounds for empty array'
```

检查 App 使用的集合大小值是否为最新值，并确认计算位置或范围的代码是否正确。

### 处理因请求超出整数类型范围的范围而导致的崩溃

[NSRange](../foundation/nsrange-c.struct.md) 结构体的位置和长度使用同一种类型（[NSUInteger](../objectivec/nsuinteger.md)），集合类也使用此类型表示集合中的索引。创建的范围终点可能超出使用该范围的集合能够表示为索引的值。当集合或序列检测到这种情况时，App 会崩溃，并且崩溃报告中会包含类似以下示例的异常信息：

```
*** Terminating app due to uncaught exception 'NSRangeException', reason: '*** -[NSConcreteMutableData subdataWithRange:]: range {20, 18446744073709551605} causes integer overflow'
```

检查 App 使用的集合大小值是否为最新值，并确认计算范围的代码是否正确。

### 处理因错误初始化字典而导致的崩溃

使用初始化器方法 [init(objects:forKeys:)](<../foundation/nsdictionary/init(objects_forkeys_).md>) 初始化 [NSDictionary](../foundation/nsdictionary.md) 或 [NSMutableDictionary](../foundation/nsmutabledictionary.md) 时，必须提供数量相同的键和对象。如果提供的数组长度不同，App 会崩溃，并且崩溃报告中会包含类似以下示例的异常信息：

```
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '*** -[NSDictionary initWithObjects:forKeys:]: count of objects (1) differs from count of keys (2)'
```

检查代码，以确定传入的哪个数组（键数组还是对象数组）有误。

### 处理因尝试编码或解码不可编码对象而导致的崩溃

要使用 [NSCoder](../foundation/nscoder.md) 序列化或反序列化对象，无论是将其存储在文件中，还是发送到另一个进程或通过网络发送，该对象都必须遵循 [NSCoding](../foundation/nscoding.md)。如果 App 尝试编码或解码不遵循 `NSCoding` 的对象，App 会崩溃，并且崩溃报告中会包含类似以下示例的异常信息：

```
*** Terminating app due to uncaught exception 'NSInvalidArgumentException', reason: '-[MyClass encodeWithCoder:]: unrecognized selector sent to instance 0x600002090040'
```

请将该对象替换为遵循 `NSCoding` 的对象，或为该对象的类或该类的分类添加 `NSCoding` 遵循关系。

> [!note] 注意
> 尽管 `NSArray` 和 `NSDictionary` 等集合类可编码，但集合中的每个对象也必须遵循 `NSCoding`，集合才能正确编码自身。

## 另请参阅

### 运行时错误

- [处理 Swift 运行时错误导致的崩溃](addressing-crashes-from-swift-runtime-errors.md) — 识别 Swift 运行时错误的迹象，并处理运行时错误导致的崩溃。
- [处理语言异常崩溃](addressing-language-exception-crashes.md) — 识别语言异常的迹象，并处理未捕获语言异常导致的崩溃。
