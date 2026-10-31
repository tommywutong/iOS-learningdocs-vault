---
title: 'composedString(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/composedstring(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/composedstring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/composedstring%28_%3A%29.json'
content_hash: 'sha256:a345ab2365e54e69'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# composedString(_:)

<sub>实例方法</sub>

返回当前的组合字符串。

<sub>macOS</sub>

```swift
func composedString(_ sender: Any!) -> Any!
```

## 参数

- `sender` — 请求该字符串的客户端对象。

## 返回值

当前的组合字符串，可以是 `NSString` 或 `NSAttributedString` 对象。返回的对象应为自动释放对象。

## 讨论

组合字符串是指输入法通常维护的缓冲区，用于镜像活动行内区域中包含的文本。之所以称为组合字符串，是因为输入法通过转换用户输入的字符来组合该字符串。此外，使用“组合字符串”这一术语更容易区分输入法缓冲区与用户看到的活动行内区域中的文本。
