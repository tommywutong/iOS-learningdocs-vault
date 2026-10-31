---
title: 'isSelectorExcluded(fromWebScript:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/isselectorexcluded(fromwebscript:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isselectorexcluded(fromwebscript:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/isselectorexcluded%28fromwebscript%3A%29.json'
content_hash: 'sha256:a3ea2200609712ab'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# isSelectorExcluded(fromWebScript:)

<sub>类型方法</sub>

返回选择器是否应从脚本环境中隐藏。

<sub>macOS</sub>

```swift
class func isSelectorExcluded(fromWebScript selector: Selector!) -> Bool
```

## 参数

- `selector` — 选择器。

## 返回值

若应由 `aSelector` 指定的选择器对脚本环境隐藏，则为 [YES](../yes.md)；否则为 [NO](../no.md)。

## 讨论

只有参数和返回类型有效的方法才会导出到 WebKit JavaScript 环境。有效类型为 Objective-C 对象和标量。默认值为 [YES](../yes.md)。

## 另请参阅

### 获取属性

- [+ webScriptNameForKey:](<webscriptname(forkey_).md>) — 返回由键指定的属性的脚本环境名称。
- [+ webScriptNameForSelector:](<webscriptname(for_).md>) — 返回选择器的脚本环境名称。
- [+ isKeyExcludedFromWebScript:](<iskeyexcluded(fromwebscript_).md>) — 返回键是否应从脚本环境中隐藏。
