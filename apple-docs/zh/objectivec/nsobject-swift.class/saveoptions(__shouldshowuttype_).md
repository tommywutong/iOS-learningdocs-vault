---
title: 'saveOptions(_:shouldShowUTType:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/saveoptions(_:shouldshowuttype:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/saveoptions(_:shouldshowuttype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/saveoptions%28_%3Ashouldshowuttype%3A%29.json'
content_hash: 'sha256:0e97f28718b39b66'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# saveOptions(_:shouldShowUTType:)

<sub>实例方法</sub>

调用以确定是否应在存储面板中显示指定的统一类型标识符。

<sub>macOS</sub>

```swift
func saveOptions(_ saveOptions: IKSaveOptions!, shouldShowUTType utType: String!) -> Bool
```

## 参数

- `saveOptions` — 调用该委托的 `IKSaveOptions` 实例。

- `utType` — 要测试的统一类型标识符。

## 返回值

若应在存储选项中显示指定类型则为 [YES](../yes.md)，否则为 [NO](../no.md)。
