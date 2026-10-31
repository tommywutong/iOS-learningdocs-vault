---
title: 'indicesOfObjects(byEvaluatingObjectSpecifier:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst, macOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/indicesofobjects(byevaluatingobjectspecifier:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/indicesofobjects(byevaluatingobjectspecifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/indicesofobjects%28byevaluatingobjectspecifier%3A%29.json'
content_hash: 'sha256:9dfa9eaad45f7e49'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# indicesOfObjects(byEvaluatingObjectSpecifier:)

<sub>实例方法</sub>

返回指定容器对象的索引。

<sub>Mac Catalyst, macOS</sub>

```swift
func indicesOfObjects(byEvaluatingObjectSpecifier specifier: NSScriptObjectSpecifier) -> [NSNumber]?
```

## 参数

- `specifier` — 用于获取其索引的容器对象的对象指定符。

## 返回值

由 `NSNumber` 对象组成的从零开始的数组，用于标识匹配 `specifier` 的容器对象的从零开始的索引；若未找到匹配对象则为 `nil`。

## 讨论

希望自行求值某些指定符的容器应实现此方法。若此方法返回 `nil`，对象指定符将继续自行求值，因此仅当你需要该行为或发生错误时应返回 `nil`。若此方法返回数组，对象指定符将使用其中的 `NSNumber` 对象作为索引。因此，若你求值指定符且没有匹配对象，应返回空数组，而不是 `nil`。若只找到一个对象，仍应将其索引放在数组中返回。返回仅含单个索引且该索引为 –1 的数组会被解释为表示所有对象。

有关示例实现，请参阅 [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164) 中 [Object Specifiers](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_object_specifiers/SAppsObjectSpecifiers.html#//apple_ref/doc/uid/TP40002164-CH3) 的“Implementing Object Specifiers”。
