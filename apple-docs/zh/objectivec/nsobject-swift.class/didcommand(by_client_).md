---
title: 'didCommand(by:client:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/didcommand(by:client:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/didcommand(by:client:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/didcommand%28by%3Aclient%3A%29.json'
content_hash: 'sha256:0b3ffaef1bf8a224'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# didCommand(by:client:)

<sub>实例方法</sub>

处理由用户操作（例如键入某些键或按下鼠标按钮）生成的命令。

<sub>macOS</sub>

```swift
func didCommand(by aSelector: Selector!, client sender: Any!) -> Bool
```

## 参数

- `aSelector` — 与按键事件关联的操作。选择器可以是输入法键与操作字典中指定的操作（即特定于输入法的操作），也可以是 `NSResponder` 操作方法之一，例如 `insertNewline:` 或 `deleteBackward:`。根据定义，此类操作方法不返回值。

- `sender` — 发送按键事件的客户端对象。

## 返回值

若命令已处理则为 [YES](../yes.md)；若未处理则为 [NO](../no.md)。若未处理，事件会传递给客户端。

## 讨论

当系统将按键事件绑定到操作方法时会调用此方法。若实现此方法，应在实际调用操作方法之前测试是否适合调用，因为调用操作方法意味着你同意处理该命令。假设你实现了某个版本的 `insertNewline:`，它会终止转换会话并向客户端发送已完全转换的文本。但如果转换缓冲区为空，你希望应用程序接收触发调用 `insertNewline:` 的回车键。此时，在调用 `didCommandBySelector:client:` 时，应在调用你的 `insertNewline:` 实现之前测试缓冲区。若缓冲区为空，返回 [NO](../no.md) 以表示回车键应继续传递给应用程序。若缓冲区非空，则调用 `insertNewline:`，然后作为 `didCommandBySelector:client:` 的结果返回 [YES](../yes.md)。

## 另请参阅

### 相关文档

- [- inputText:client:](<inputtext(__client_).md>) — 处理未映射到操作方法的按键按下事件。
