---
title: 'webScriptName(for:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/webscriptname(for:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/webscriptname(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/webscriptname%28for%3A%29.json'
content_hash: 'sha256:32ce4609256a9af9'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# webScriptName(for:)

<sub>类型方法</sub>

返回选择器的脚本环境名称。

<sub>macOS</sub>

```swift
class func webScriptName(for selector: Selector!) -> String!
```

## 参数

- `selector` — 选择器。

## 返回值

用于在脚本环境中表示选择器的名称。

## 讨论

确保返回的名称对于调用此方法的脚本是唯一的是你的责任。若此方法返回 `nil` 或你未实现它，则选择器的默认名称按如下方式构造：

- Objective-C 选择器中的冒号（”:”）替换为下划线（”_”）。
- Objective-C 选择器中的下划线前缀美元符号（”$”）。
- Objective-C 选择器中的美元符号前缀另一个美元符号。

下表显示了如何构造默认名称的示例：

| Objective-C selector | Default script name for selector |
|---|---|
| `setFlag:` | `setFlag_` |
| `setFlag:forKey:withAttributes:` | `setFlag_forKey_withAttributes_` |
| `propertiesForExample_Object:` | `propertiesForExample$_Object_` |
| `set_$_forKey:withDictionary:` | `set$_$$_$_forKey_withDictionary_` |

由于方法名称的默认构造可能因其 Objective-C 名称而令人困惑，你应实现此方法并返回更易读的名称。

## 另请参阅

### 获取属性

- [+ webScriptNameForKey:](<webscriptname(forkey_).md>) — 返回由键指定的属性的脚本环境名称。
- [+ isSelectorExcludedFromWebScript:](<isselectorexcluded(fromwebscript_).md>) — 返回选择器是否应从脚本环境中隐藏。
- [+ isKeyExcludedFromWebScript:](<iskeyexcluded(fromwebscript_).md>) — 返回键是否应从脚本环境中隐藏。
