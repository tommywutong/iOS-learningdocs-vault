---
title: 使用委托自定对象行为
framework: Swift
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/using-delegates-to-customize-object-behavior
source_url: 'https://developer.apple.com/documentation/swift/using-delegates-to-customize-object-behavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/using-delegates-to-customize-object-behavior.json'
content_hash: 'sha256:2709725258c86411'
translated: true
---

> 导航：[技术](../technologies.md) · [Swift](../swift.md) · [Cocoa 设计模式](cocoa-design-patterns.md)

# 使用委托自定对象行为

<sub>文章</sub>

代表委托方响应事件。

## 概述

你使用委托与 Cocoa 对象交互，这些对象会把 App 中的事件告知你。

### 采用委托协议

Cocoa API 通常会提供包含委托方法的协议。当事件发生时——例如用户调整窗口大小——作为委托方的类会检测到该事件，并在你指定为委托的类上调用委托方法。委托方法可以自定 App 响应事件的方式。

下面的示例采用 [NSWindowDelegate](../appkit/nswindowdelegate.md) 协议并实现其 [window(_:willUseFullScreenContentSize:)](<../appkit/nswindowdelegate/window(__willusefullscreencontentsize_).md>) 方法：

```swift
class MyDelegate: NSObject, NSWindowDelegate {
    func window(_ window: NSWindow, willUseFullScreenContentSize proposedSize: NSSize) -> NSSize {
        return proposedSize
    }
}
```

### 检查委托是否存在

Cocoa 委托模式不要求委托必须被实例化。如果你不需要响应事件，就不需要创建委托。在调用对象委托上的方法之前，请确保委托不是 `nil`。

下面的示例创建一个 [NSWindow](../appkit/nswindow.md)，并使用可选链在向委托发送消息之前检查窗口的委托是否存在。

```swift
let myWindow = NSWindow(
    contentRect: NSRect(x: 0, y: 0, width: 5120, height: 2880),
    styleMask: .fullScreen,
    backing: .buffered,
    defer: false
)

myWindow.delegate = MyDelegate()
if let fullScreenSize = myWindow.delegate?.window(myWindow, willUseFullScreenContentSize: mySize) {
    print(NSStringFromSize(fullScreenSize))
}
```

## 另请参阅

### 常用模式

- [在 Swift 中使用键值观察](using-key-value-observing-in-swift.md) — 把其他对象属性的变化通知给对象。
- [使用单例管理共享资源](managing-a-shared-resource-using-a-singleton.md) — 使用单一的共享类实例来提供对共享资源的访问。
- [关于导入的 Cocoa 错误参数](about-imported-cocoa-error-parameters.md) — 了解 Cocoa 错误参数如何被转换为 Swift 的抛出方法。
- [在 Swift 中处理 Cocoa 错误](handling-cocoa-errors-in-swift.md) — 抛出和捕获使用 Cocoa 错误类型的错误。
