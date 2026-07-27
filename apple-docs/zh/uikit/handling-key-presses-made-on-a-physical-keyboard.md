---
title: 处理物理键盘上的按键操作
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/handling-key-presses-made-on-a-physical-keyboard
source_url: 'https://developer.apple.com/documentation/uikit/handling-key-presses-made-on-a-physical-keyboard'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/handling-key-presses-made-on-a-physical-keyboard.json'
content_hash: 'sha256:917a067d913e759f'
translated: true
---

> 导航：[Technologies](../technologies.md) · [UIKit](../uikit.md) · [键盘与输入](keyboards-and-input.md)

# 处理物理键盘上的按键操作

<sub>文章</sub>

检测用户按下并释放物理键盘上按键的时刻。

## 概述

在 iOS App 以及使用 Mac Catalyst 构建的 Mac App 中，系统会通过向活跃 App 的响应者链中的响应者对象发送按压事件，来报告用户在物理键盘上做出的按键操作。

响应者链是一系列相互连接的 [UIResponder](uiresponder.md) 对象，例如 [UIViewController](https://developer.apple.com/library/archive/releasenotes/General/RN-iPhoneSDK-3/index.html#//apple_ref/doc/uid/TP40008407-CH1-SW19) 和 [UIApplication](uiapplication.md)，它们要么处理某个事件，要么将处理该事件的责任转交给 App 中的其他响应者。要详细了解响应者与响应者链，请参阅[使用响应者和响应者链处理事件](using-responders-and-the-responder-chain-to-handle-events.md)。

### 检测按键操作

要检测用户在物理键盘上做出的按键操作，请在你 App 的某个响应者对象（例如 App 委托或主视图控制器）中重写 [- pressesBegan:withEvent:](<uiresponder/pressesbegan(__with_).md>)。

要确定用户按下了哪个键，请遍历这组按压操作，检查每次按压的 [key](uipress/key.md) 属性。使用 [charactersIgnoringModifiers](uikey/charactersignoringmodifiers.md) 来确定该键的文本值，以及响应者是否应该处理这次按键操作。如果响应者不处理该按键操作，请在超类上调用 [- pressesBegan:withEvent:](<uiresponder/pressesbegan(__with_).md>)，将按压事件发送给活跃响应者链中的下一个响应者。

例如，以下代码清单处理用户按下左箭头键或右箭头键的情况。

```swift
// Handle someone pressing a key on a physical keyboard.
override func pressesBegan(_ presses: Set<UIPress>, 
                           with event: UIPressesEvent?) {
    
    var didHandleEvent = false
    
    for press in presses {
        
        // Get the pressed key.
        guard let key = press.key else { continue }
        
        if key.charactersIgnoringModifiers == UIKeyCommand.inputLeftArrow {
            // Someone pressed the left arrow key.
            // Respond to the key-press event.
            didHandleEvent = true
        }
        if key.charactersIgnoringModifiers == UIKeyCommand.inputRightArrow {
            // Someone pressed the right arrow key.
            // Respond to the key-press event.
            didHandleEvent = true
        }
    }
    
    if didHandleEvent == false {
        // If someone presses a key that you're not handling,
        // pass the event to the next responder.
        super.pressesBegan(presses, with: event)
    }
}
```

### 检测按键释放

重写响应者的 [- pressesEnded:withEvent:](<uiresponder/pressesended(__with_).md>) 方法，以检测用户释放某个键的时刻。要获取有关该键的信息，做法与检测按键操作时相同：检查 `presses` 集合中每次按压的 [key](uipress/key.md) 属性。例如，以下代码清单处理用户释放左箭头键或右箭头键的情况。

```swift
// Handle someone releasing a key on a physical keyboard.
override func pressesEnded(_ presses: Set<UIPress>, with event: UIPressesEvent?) {
    
    var didHandleEvent = false
    
    
    for press in presses {
        
        // Get the released key.
        guard let key = press.key else { continue }
        
        
        if key.charactersIgnoringModifiers == UIKeyCommand.inputLeftArrow {
            // Someone released the left arrow key.
            // Respond to the event.
            didHandleEvent = true
        }
        if key.charactersIgnoringModifiers == UIKeyCommand.inputRightArrow {
            // Someone released the right arrow key.
            // Respond to the event.
            didHandleEvent = true
        }
    }
    
    if didHandleEvent == false {
        // If someone releases a key that you're not handling,
        // pass the event to the next responder.
        super.pressesEnded(presses, with: event)
    }
}
```

## 另请参阅

### 物理键盘

- [使用键盘导览 App 的用户界面](navigating-an-app-s-user-interface-using-a-keyboard.md) — 在 iPad App 和使用 Mac Catalyst 构建的 App 中，使用键盘和可获得焦点的 UI 元素在用户界面元素之间导览。
- [为你的 App 添加硬件键盘支持](adding-hardware-keyboard-support-to-your-app.md) — 通过处理原始键盘事件、编写自定键盘快捷键，以及配合手势识别器使用，增强与你 App 的交互。
- [UIKey](uikey.md) — 一个提供键盘按键状态信息的对象。
- [UIKeyboardHIDUsage](uikeyboardhidusage.md) — 一组用于标识 USB 键盘按键的 HID 使用代码。
