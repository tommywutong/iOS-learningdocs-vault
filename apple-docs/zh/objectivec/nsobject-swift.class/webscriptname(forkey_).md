---
title: 'webScriptName(forKey:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webscriptname(forkey:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webscriptname(forkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webscriptname%28forkey%3A%29.json'
content_hash: 'sha256:9eb6488f6f44b769'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webScriptName(forKey:)

<sub>类型方法</sub>

返回由键指定的属性的脚本环境名称。

<sub>macOS</sub>

```swift
class func webScriptName(forKey name: UnsafePointer<CChar>!) -> String!
```

## 参数

- `name` — 属性的名称。

## 返回值

用于在脚本环境中表示该属性的名称。

## 另请参阅

### 获取属性

- [+ webScriptNameForSelector:](<webscriptname(for_).md>) — 返回选择器的脚本环境名称。
- [+ isSelectorExcludedFromWebScript:](<isselectorexcluded(fromwebscript_).md>) — 返回选择器是否应从脚本环境中隐藏。
- [+ isKeyExcludedFromWebScript:](<iskeyexcluded(fromwebscript_).md>) — 返回键是否应从脚本环境中隐藏。
