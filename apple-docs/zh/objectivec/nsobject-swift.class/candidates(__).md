---
title: 'candidates(_:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/candidates(_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/candidates(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/candidates%28_%3A%29.json'
content_hash: 'sha256:f6ba1f749866ec7c'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# candidates(_:)

<sub>实例方法</sub>

返回候选数组。

<sub>macOS</sub>

```swift
func candidates(_ sender: Any!) -> [Any]!
```

## 参数

- `sender` — 请求候选的客户端对象。

## 返回值

候选数组。返回的数组应为自动释放对象。

## 讨论

输入法应查找其当前的组合字符串，并返回该组合字符串可能映射到的候选字符串列表。
