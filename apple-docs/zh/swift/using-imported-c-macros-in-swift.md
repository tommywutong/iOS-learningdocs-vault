---
title: 在 Swift 中使用导入的 C 宏
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-imported-c-macros-in-swift
source_url: 'https://developer.apple.com/documentation/swift/using-imported-c-macros-in-swift'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-imported-c-macros-in-swift.json'
content_hash: 'sha256:8f4570ee93c88b5b'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [导入的 C 与 Objective-C API](imported-c-and-objective-c-apis.md)

# 在 Swift 中使用导入的 C 宏

<sub>文章</sub>

将导入的 C 宏用作常量。

## 概述

Swift 会自动把用 `#define` 指令声明的简单、类似常量的宏导入为全局常量。当宏对字符串、浮点数或整数值使用字面量，或者在字面量或先前定义的宏之间使用 `+`、`-`、`>` 和 `==` 等运算符时，宏就会被导入。下面的示例在一个 C 头文件中定义了一些简单宏：

```occ
#define FADE_ANIMATION_DURATION 0.35
#define VERSION_STRING "2.2.10.0a"
#define MAX_RESOLUTION 1268

#define HALF_RESOLUTION (MAX_RESOLUTION / 2)
#define IS_HIGH_RES (MAX_RESOLUTION > 1024)
```

导入到 Swift 后，上例中的宏等价于以下常量声明：

```swift
let FADE_ANIMATION_DURATION = 0.35
let VERSION_STRING = "2.2.10.0a"
let MAX_RESOLUTION = 1268

let HALF_RESOLUTION = 634
let IS_HIGH_RES = true
```

### 用函数和泛型代替复杂宏

比简单常量定义更复杂的 C 宏在 Swift 中没有对应物。在 C 和 Objective-C 中使用复杂宏，是为了避开类型检查约束，或者避免重复输入大量样板代码。然而，宏会让调试和重构变得困难。在 Swift 中，你可以使用函数和泛型来毫无妥协地实现同样的效果。

## 另请参阅

### C API

- [Using Imported C Structs and Unions in Swift](using-imported-c-structs-and-unions-in-swift.md) — 了解 Swift 如何表示导入的 C 结构体与联合体，包括带位域（bitfield）和未命名字段的类型。
- [Using Imported C Functions in Swift](using-imported-c-functions-in-swift.md) — 了解如何调用在 C 头文件中声明的导入函数。
