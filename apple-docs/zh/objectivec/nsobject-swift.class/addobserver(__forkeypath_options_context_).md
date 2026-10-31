---
title: 'addObserver(_:forKeyPath:options:context:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/addobserver(_:forkeypath:options:context:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/addobserver(_:forkeypath:options:context:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/addobserver%28_%3Aforkeypath%3Aoptions%3Acontext%3A%29.json'
content_hash: 'sha256:a9948135507c6d34'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# addObserver(_:forKeyPath:options:context:)

<sub>实例方法</sub>

注册观察者对象，以接收相对于接收此消息的对象的键路径的 KVO 通知。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addObserver(_ observer: NSObject, forKeyPath keyPath: String, options: NSKeyValueObservingOptions = [], context: UnsafeMutableRawPointer?)
```

## 参数

- `observer` — 要注册以接收 KVO 通知的对象。观察者必须实现键值观察方法 [- observeValueForKeyPath:ofObject:change:context:](<observevalue(forkeypath_of_change_context_).md>)。

- `keyPath` — 相对于接收此消息的对象、要观察的属性的键路径。此值不得为 `nil`。

- `options` — `NSKeyValueObservingOptions` 值的组合，指定观察通知中包含的内容。可能的值参见 [NSKeyValueObservingOptions](../../foundation/nskeyvalueobservingoptions.md)。

- `context` — 在 [- observeValueForKeyPath:ofObject:change:context:](<observevalue(forkeypath_of_change_context_).md>) 中传递给 `observer` 的任意数据。

## 讨论

接收此消息的对象和 `observer` 都不会被保留。调用此方法的对象最终还必须调用 [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) 或 [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) 方法，以在参与 KVO 时取消注册观察者。

## 另请参阅

### Registering for Observation

- [- removeObserver:forKeyPath:](<removeobserver(__forkeypath_).md>) — 停止观察者对象接收相对于接收此消息的对象、由键路径指定的属性的变化通知。
- [- removeObserver:forKeyPath:context:](<removeobserver(__forkeypath_context_).md>) — 在给定上下文的情况下，停止观察者对象接收相对于接收此消息的对象、由键路径指定的属性的变化通知。
