---
title: 'isKeyExcluded(fromWebScript:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/iskeyexcluded(fromwebscript:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/iskeyexcluded(fromwebscript:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/iskeyexcluded%28fromwebscript%3A%29.json'
content_hash: 'sha256:2b7a403fba21c1be'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isKeyExcluded(fromWebScript:)

<sub>类型方法</sub>

返回键是否应从脚本环境中隐藏。

<sub>macOS</sub>

```swift
class func isKeyExcluded(fromWebScript name: UnsafePointer<CChar>!) -> Bool
```

## 参数

- `name` — 属性的名称。

## 返回值

若应由 `name` 指定的属性对脚本环境隐藏，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

默认值为 [YES](../yes.md)。

## 另请参阅

### 获取属性

- [+ webScriptNameForKey:](<webscriptname(forkey_).md>) — 返回由键指定的属性的脚本环境名称。
- [+ webScriptNameForSelector:](<webscriptname(for_).md>) — 返回选择器的脚本环境名称。
- [+ isSelectorExcludedFromWebScript:](<isselectorexcluded(fromwebscript_).md>) — 返回选择器是否应从脚本环境中隐藏。
