---
title: 'invokeUndefinedMethod(fromWebScript:withArguments:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/invokeundefinedmethod(fromwebscript:witharguments:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/invokeundefinedmethod(fromwebscript:witharguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/invokeundefinedmethod%28fromwebscript%3Awitharguments%3A%29.json'
content_hash: 'sha256:e8d47f3b715ff541'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# invokeUndefinedMethod(fromWebScript:withArguments:)

<sub>实例方法</sub>

处理来自脚本环境的未定义方法调用。

<sub>macOS</sub>

```swift
func invokeUndefinedMethod(fromWebScript name: String!, withArguments arguments: [Any]!) -> Any!
```

## 参数

- `name` — 未定义方法的名称。

- `arguments` — 传给未定义方法的参数。

## 返回值

调用未定义方法的结果。

## 讨论

当脚本尝试调用未直接导出到脚本环境的方法时会调用此方法。你应返回调用结果，并适当地转换为脚本环境可用的形式。

## 另请参阅

### 调用方法

- [- invokeDefaultMethodWithArguments:](<invokedefaultmethod(witharguments_).md>) — 当脚本尝试直接在暴露对象上调用方法时执行。
