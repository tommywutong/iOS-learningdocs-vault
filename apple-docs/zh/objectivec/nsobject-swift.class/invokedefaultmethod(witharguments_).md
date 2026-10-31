---
title: 'invokeDefaultMethod(withArguments:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/invokedefaultmethod(witharguments:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/invokedefaultmethod(witharguments:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/invokedefaultmethod%28witharguments%3A%29.json'
content_hash: 'sha256:ef10b367c6f1df4d'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# invokeDefaultMethod(withArguments:)

<sub>实例方法</sub>

当脚本尝试直接在暴露对象上调用方法时执行。

<sub>macOS</sub>

```swift
func invokeDefaultMethod(withArguments arguments: [Any]!) -> Any!
```

## 参数

- `arguments` — 要传递给默认方法的参数。

## 返回值

调用默认方法的结果。

## 另请参阅

### 调用方法

- [- invokeUndefinedMethodFromWebScript:withArguments:](<invokeundefinedmethod(fromwebscript_witharguments_).md>) — 处理来自脚本环境的未定义方法调用。
