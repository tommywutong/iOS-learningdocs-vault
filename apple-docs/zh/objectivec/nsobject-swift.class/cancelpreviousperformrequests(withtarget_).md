---
title: 'cancelPreviousPerformRequests(withTarget:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/cancelpreviousperformrequests(withtarget:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/cancelpreviousperformrequests(withtarget:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/cancelpreviousperformrequests%28withtarget%3A%29.json'
content_hash: 'sha256:206eb976f8c88379'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# cancelPreviousPerformRequests(withTarget:)

<sub>类型方法</sub>

取消先前使用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 实例方法注册的 perform 请求。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func cancelPreviousPerformRequests(withTarget aTarget: Any)
```

## 参数

- `aTarget` — 先前使用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 实例方法注册的请求的目标。

## 讨论

具有相同目标 `aTarget` 的所有 perform 请求都会被取消。此方法仅移除当前运行循环中的 perform 请求，而非所有运行循环。

## 另请参阅

### 发送消息

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — 在延迟后使用默认模式在当前线程上调用接收者的方法。
- [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) — 在延迟后使用指定模式在当前线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — 使用默认模式在主线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — 使用指定模式在主线程上调用接收者的方法。
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — 使用默认模式在指定线程上调用接收者的方法。
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<perform(__on_with_waituntildone_modes_).md>) — 使用指定模式在指定线程上调用接收者的方法。
- [- performSelectorInBackground:withObject:](<performselector(inbackground_with_).md>) — 在新的后台线程上调用接收者的方法。
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — 取消先前使用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 注册的 perform 请求。
