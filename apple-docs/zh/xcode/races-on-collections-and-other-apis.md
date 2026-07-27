---
title: 集合及其他 API 中的数据争用
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/races-on-collections-and-other-apis
source_url: 'https://developer.apple.com/documentation/xcode/races-on-collections-and-other-apis'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/races-on-collections-and-other-apis.json'
content_hash: 'sha256:3fb3acce4c703c1b'
translated: true
---

> 导航：[技术](../technologies.md) · [Xcode](../xcode.md) · [调试](debugging.md) · [尽早诊断内存、线程和崩溃问题](diagnosing-memory-thread-and-crash-issues-early.md)

# 集合及其他 API 中的数据争用

<sub>文章</sub>

检测一个线程访问可变对象、而另一个线程正在写入该对象的情况。

## 概述

在 Xcode 9 及更高版本中，Thread Sanitizer 会检测对 [Foundation](../foundation.md) 和 [Core Foundation](../corefoundation.md) 框架 API 的不安全线程访问。此功能适用于以下集合类型：

- [NSMutableArray](../foundation/nsmutablearray.md)
- [NSMutableDictionary](../foundation/nsmutabledictionary.md)
- [CFMutableArray](../corefoundation/cfmutablearray.md)
- [CFMutableDictionary](../corefoundation/cfmutabledictionary.md)

### 可变数组中的数据争用（data race）

在以下示例中，代码在一个线程中枚举可变数组，同时从另一个线程写入该数组，而没有同步访问：

**Swift**

```swift
let array: NSMutableArray = []
var sum: Int = 0
// 在线程 #1 上执行
for value in array {
    sum += value as! Int
}
// 在线程 #2 上执行
array.add(42)
```

**Objective-C**

```objc
NSMutableArray *array = [NSMutableArray new];
NSInteger sum = 0;
// 在线程 #1 上执行
for (id value in array) {  
    sum += [value integerValue];
} 
// 在线程 #2 上执行
[array addObject:@42];
```

#### 解决方案

使用 [Dispatch](../dispatch.md) API 协调多个线程对 `array` 的访问。

### 可变字典中的数据争用

在以下示例中，代码在一个线程中枚举可变字典，同时从另一个线程写入该字典，而没有同步访问：

```swift
let dictionary: NSMutableDictionary = [:]
var sum: Int = 0
// 在线程 #1 上执行
for key in dictionary.keyEnumerator() {
    sum += dictionary[key] as! Int
}
// 在线程 #2 上执行
dictionary["forty-two"] = 42
```

**Objective-C**

```objc
NSMutableDictionary *dictionary = [NSMutableDictionary new];
NSInteger sum = 0;
// 在线程 #1 上执行
for (id key in dictionary) {
    sum += [dictionary[key] integerValue];
}
// 在线程 #2 上执行
dictionary[@"forty-two"] = @42;
```

#### 解决方案

使用 [Dispatch](../dispatch.md) API 协调多个线程对 `dictionary` 的访问。

## 另请参阅

### Thread Sanitizer

- [数据争用](data-races.md) — 检测多个线程对可变状态的未同步访问。
- [Swift 访问争用](swift-access-races.md) — 检测 Swift 中多个线程对可变状态的未同步访问。
- [未初始化的互斥锁](uninitialized-mutexes.md) — 检测使用未初始化互斥锁的情况。
- [线程泄漏](thread-leaks.md) — 检测使用后未关闭线程的情况。
