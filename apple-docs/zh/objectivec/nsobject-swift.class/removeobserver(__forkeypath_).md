---
title: 'removeObserver(_:forKeyPath:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/removeobserver(_:forkeypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/removeobserver%28_%3Aforkeypath%3A%29.json'
content_hash: 'sha256:99cb80f30604b824'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# removeObserver(_:forKeyPath:)

<sub>实例方法</sub>

停止观察者对象接收与接收此消息的对象相关的、由键路径指定的属性的更改通知。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeObserver(_ observer: NSObject, forKeyPath keyPath: String)
```

## 参数

- `observer` — 要移除的观察者对象。

- `keyPath` — 相对于接收此消息的对象的键路径，`observer` 已注册以接收该键路径的 KVO 更改通知。

## 讨论

对先前未注册为观察者的 `object` 调用 [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) 是错误的。

请务必在 [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) 中指定的任何对象被释放之前调用此方法（或 [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>)）。

## 另请参阅

### Registering for Observation

- [- addObserver:forKeyPath:options:context:](<addobserver(__forkeypath_options_context_).md>) — 注册观察者对象，以接收相对于接收此消息的对象的键路径的 KVO 通知。
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — 在给定上下文的情况下，停止观察者对象接收相对于接收此消息的对象、由键路径指定的属性的变化通知。
