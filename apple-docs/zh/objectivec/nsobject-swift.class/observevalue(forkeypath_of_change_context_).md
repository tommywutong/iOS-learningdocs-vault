---
title: 'observeValue(forKeyPath:of:change:context:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/observevalue(forkeypath:of:change:context:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/observevalue(forkeypath:of:change:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/observevalue%28forkeypath%3Aof%3Achange%3Acontext%3A%29.json'
content_hash: 'sha256:5d8bbe549114a7fb'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# observeValue(forKeyPath:of:change:context:)

<sub>实例方法</sub>

当相对于被观察对象的指定键路径处的值已更改时，通知观察对象。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func observeValue(forKeyPath keyPath: String?, of object: Any?, change: [NSKeyValueChangeKey : Any]?, context: UnsafeMutableRawPointer?)
```

## 参数

- `keyPath` — 相对于 `object`、已更改值的键路径。

- `object` — 键路径 `keyPath` 的源对象。

- `change` — 描述相对于 `object` 的键路径 `keyPath` 处属性值已发生更改的字典。条目在 `Change Dictionary Keys` 中说明。

- `context` — 注册观察者以接收键值观察通知时提供的值。

## 讨论

若要让 `object` 开始为 `keyPath` 处的值发送更改通知消息，请向其发送 [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) 消息，并指定应接收这些消息的观察对象。完成观察后，尤其是在观察对象被释放之前，请向被观察对象发送 [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) 或 [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) 消息以取消注册观察者，并停止发送更改通知消息。
