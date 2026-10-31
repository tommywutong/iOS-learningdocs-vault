---
title: 'application:delegateHandlesKey:'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.0+（11.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: '/documentation/objectivec/nsobject-swift.class/application:delegatehandleskey:'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/application:delegatehandleskey:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/application%3Adelegatehandleskey%3A.json'
content_hash: 'sha256:0b0e1b3bfbe314f0'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# application:delegateHandlesKey:

<sub>实例方法</sub>

由 Cocoa 内置脚本支持在执行 `get` 或 `set` 脚本命令期间发送，以查明委托是否能处理对指定键值键的操作。

> [!warning] 已废弃
> 请改用 [application(_:delegateHandlesKey:)](<../../appkit/nsapplicationdelegate/application(__delegatehandleskey_).md>)。

<sub>Mac Catalyst, macOS</sub>

```objc
- (BOOL) application:(NSApplication *) sender delegateHandlesKey:(NSString *) key;
```

## 参数

- `sender` — 与委托关联的 App 对象。

- `key` — 要处理的键。

## 返回值

如果你的委托处理该键，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

如果 App `sender` 的委托处理 `key` 指定的键（意味着它可以获取或设置对应该键的可脚本化属性或元素），则此方法应返回 [YES](../yes.md)。App 为其处理的每个键实现方法，方法名与键匹配。

例如，不使用 Cocoa 基于文稿的 App 架构的可脚本化 App 可以实现此方法以提供自己的文稿排序。此类 App 可能需要这样做，因为标准 App 委托期望与基于文稿的 App 协同工作。TextEdit App（其源代码随 macOS 开发者工具分发）提供了以下实现：

```objc
return [key isEqualToString:@"orderedDocuments"];
```

然后 TextEdit 在其控制器类中实现 `orderedDocuments` 方法以返回有序的文稿列表。拥有自己窗口排序的 App 可以添加对键 `orderedWindows` 的测试，以便其委托能提供自己的 `orderedWindows` 版本。

> [!important] 重要
> 对于 `get` 或 `set` 以外的脚本命令，Cocoa 脚本不会调用此方法。有关处理其他命令的信息，参见 [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164) 中的 [Script Commands](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_script_cmds/SAppsScriptCmds.html#//apple_ref/doc/uid/20001242)。

## 另请参阅

### 相关文档

- [orderedWindows](../../appkit/nsapplication/orderedwindows.md) — 按屏幕上从前到后的顺序排列的窗口对象数组。
- [orderedDocuments](../../appkit/nsapplication/ordereddocuments.md) — 按其关联窗口从前到后的顺序排列的文稿对象数组。
