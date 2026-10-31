---
title: awakeFromNib()
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/objectivec/nsobject-swift.class/awakefromnib()
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/awakefromnib()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/awakefromnib%28%29.json'
content_hash: 'sha256:5600fbec1f2f319d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# awakeFromNib()

<sub>实例方法</sub>

在从 Interface Builder 归档或 nib 文件加载后，使接收者准备好提供服务。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func awakeFromNib()
```

## 讨论

nib 加载基础结构会向从 nib 归档重新创建的每个对象发送 `awakeFromNib` 消息，但仅在归档中的所有对象都已加载并初始化之后。当对象收到 `awakeFromNib` 消息时，保证其所有出口和操作连接都已建立。

必须调用 `awakeFromNib` 的 `super` 实现，以便父类有机会执行其所需的任何额外初始化。虽然此方法的默认实现不做任何事，但许多 UIKit 类提供了非空实现。你可以在自己的 `awakeFromNib` 方法中的任意时刻调用 `super` 实现。

> [!note] 注意
> 在 Interface Builder 的测试模式下，此消息也会发送给从已加载的 Interface Builder 插件实例化的对象。因为插件链接到包含对象定义代码的框架，Interface Builder 能够在存在时调用它们的 `awakeFromNib` 方法。对于你为 Xcode 项目创建的自定义对象则并非如此。Interface Builder 仅知道这些对象已定义的出口和操作；它无法访问它们的实际代码。

在实例化过程中，归档中的每个对象都会被解档，然后使用适合其类型的方法进行初始化。符合 [NSCoding](../../foundation/nscoding.md) 协议的对象（包括 [UIView](../../uikit/uiview.md) 和 [UIViewController](../../uikit/uiviewcontroller.md) 的所有子类）使用其 `initWithCoder:` 方法进行初始化。所有不符合 `NSCoding` 协议的对象使用其 `init` 方法进行初始化。在所有对象都已实例化并初始化之后，nib 加载代码会重新建立所有这些对象的出口和操作连接，然后调用这些对象的 `awakeFromNib` 方法。有关 nib 加载过程中所遵循步骤的更多详细信息，请参见 Resource Programming Guide 中的 Nib Files。

> [!important] 重要
> 由于从归档实例化对象的顺序无法保证，初始化方法不应向层次结构中的其他对象发送消息。可在 `awakeFromNib` 方法中安全地向其他对象发送消息。

通常，你会为需要在设计时无法完成的额外设置的对象实现 `awakeFromNib`。例如，你可能会使用此方法自定义任何控件的默认配置，以匹配用户偏好设置或其他控件中的值。你也可能使用它将各个控件恢复到应用的某个先前状态。

## 另请参阅

### 相关文档

- [- awakeAfterUsingCoder:](<awakeafter(using_).md>) — 由子类重写，以便用另一对象替代已解码并随后收到此消息的对象。
- [+ initialize](<initialize().md>) — 在类收到第一条消息之前对其进行初始化。
- [init(coder:)](<../../foundation/nscoding/init(coder_).md>) — 根据给定解档器中的数据初始化接收者。
