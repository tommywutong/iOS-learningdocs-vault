---
title: 'performSelector(inBackground:with:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/performselector(inbackground:with:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/performselector(inbackground:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/performselector%28inbackground%3Awith%3A%29.json'
content_hash: 'sha256:0d9d823ba0428464'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# performSelector(inBackground:with:)

<sub>实例方法</sub>

在新的后台线程上调用接收者的方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performSelector(inBackground aSelector: Selector, with arg: Any?)
```

## 参数

- `aSelector` — 标识要调用的方法的 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。该方法不应有显著的返回结果，且应接受单个类型为 id 的参数，或根本不接受参数。

- `arg` — 调用方法时传入的参数。若方法不接受参数，则传入 `nil`。

## 讨论

此方法在应用中创建新线程；若应用尚未进入多线程模式，则会进入该模式。由 `aSelector` 表示的方法必须像为程序中任何其他新线程一样设置线程环境。有关如何配置和运行线程的更多信息，请参见 [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i)。

## 另请参阅

### 发送消息

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — 在延迟后使用默认模式在当前线程上调用接收者的方法。
- [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) — 在延迟后使用指定模式在当前线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — 使用默认模式在主线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — 使用指定模式在主线程上调用接收者的方法。
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — 使用默认模式在指定线程上调用接收者的方法。
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<perform(__on_with_waituntildone_modes_).md>) — 使用指定模式在指定线程上调用接收者的方法。
- [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) — 取消先前使用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 实例方法注册的 perform 请求。
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — 取消先前使用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 注册的 perform 请求。
