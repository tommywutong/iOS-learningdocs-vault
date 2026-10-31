---
title: os_activity_label_useraction
framework: os
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_label_useraction
source_url: 'https://developer.apple.com/documentation/os/os_activity_label_useraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_label_useraction.json'
content_hash: 'sha256:e241e4bbca7b1e44'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# os_activity_label_useraction

<sub>宏</sub>

为 AppKit 或 UIKit 自动生成的活动添加标签。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define os_activity_label_useraction(label)
```

## 参数

- `label` — 描述用户操作意图的 C 字符串。描述必须是调用方可执行文件或库内的常量字符串。

## 讨论

当 AppKit 或 UIKit 执行由用户发起的操作时，各框架会在调用到 `IBAction` 方法之前，自动创建一个活动来捕获该操作的日志。调用此方法，可将更高层级的语义操作与底层的 AppKit 或 UIKit 操作关联起来。例如，当用户选择某个菜单项时，你可以将该菜单项预期的操作关联上去，如下面的示例所示：

```objc
os_activity_label_useraction("New mail message");
os_activity_label_useraction("Empty trash");
```

你必须在 AppKit 或 UIKit 所调用的 `IBAction` 方法作用域内调用此函数。请在该操作作用域的靠前位置调用此函数，并在创建任何子活动之前完成调用。

## 另请参阅

### 创建活动

- [os_activity_initiate](os_activity_initiate.md) — 使用所提供的 block 同步执行一个新活动。
- [os_activity_initiate_f](os_activity_initiate_f.md) — 使用所提供的函数同步执行一个新活动。
- [os_activity_create](os_activity_create.md) — 创建一个新的活动对象。
- [os_activity_flag_t](os_activity_flag_t.md) — 在创建活动时调整行为的标志。
