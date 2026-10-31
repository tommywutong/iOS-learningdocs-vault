---
title: 'perform(_:with:afterDelay:inModes:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/perform(_:with:afterdelay:inmodes:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/perform(_:with:afterdelay:inmodes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/perform%28_%3Awith%3Aafterdelay%3Ainmodes%3A%29.json'
content_hash: 'sha256:24a060eac2d66966'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# perform(_:with:afterDelay:inModes:)

<sub>实例方法</sub>

延迟后使用指定模式在当前线程上调用接收者的方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoop.Mode])
```

## 参数

- `aSelector` — 标识要调用的方法的 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。该方法不应有显著的返回结果，且应接受单个类型为 id 的参数，或根本不接受参数。

- `anArgument` — 调用方法时传入的参数。若方法不接受参数，则传入 `nil`。

- `delay` — 发送消息之前的最短时间。指定延迟为 0 并不一定会导致立即执行选择器。选择器仍会排入该线程的运行循环，并尽快执行。

- `modes` — 标识要与执行选择器的计时器关联的模式的字符串数组。此数组必须至少包含一个字符串。若为此参数指定 `nil` 或空数组，此方法会返回而不执行指定选择器。有关运行循环模式的信息，请参阅 [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i) 中的 [Run Loops](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html#//apple_ref/doc/uid/10000057i-CH16)。

## 讨论

此方法设置一个计时器，以在当前线程的运行循环上执行 `aSelector` 消息。该计时器配置为在 `modes` 参数指定的模式中运行。当计时器触发时，线程尝试从运行循环中将该消息出队并执行选择器。若运行循环正在运行且处于指定模式之一，则成功；否则，计时器会等待，直到运行循环处于那些模式之一。

若希望在运行循环处于默认模式以外的模式时将消息出队，请改用 [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) 方法。若不确定当前线程是否为主线程，可以使用 [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) 或 [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) 方法来保证选择器在主线程上执行。要取消排队的消息，请使用 [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) 或 [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) 方法。

### 特殊注意事项

此方法向其当前上下文的运行循环注册，并依赖于该运行循环定期运行才能正确执行。你可能会调用此方法并最终向不会自动定期运行的运行循环注册的一个常见上下文是由调度队列调用时。若在调度队列上运行时需要此类功能，应使用 [dispatch_after](../../dispatch/dispatch_after.md) 及相关方法来获得所需行为。

## 另请参阅

### 相关文档

- [invalidate()](<../../foundation/timer/invalidate().md>) — 停止计时器再次触发，并请求将其从其运行循环中移除。
- [add(_:forMode:)](<../../foundation/runloop/add(__formode_)-392ag.md>) — 将给定计时器注册到给定输入模式。

### 发送消息

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — 在延迟后使用默认模式在当前线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — 使用默认模式在主线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — 使用指定模式在主线程上调用接收者的方法。
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — 使用默认模式在指定线程上调用接收者的方法。
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<perform(__on_with_waituntildone_modes_).md>) — 使用指定模式在指定线程上调用接收者的方法。
- [- performSelectorInBackground:withObject:](<performselector(inbackground_with_).md>) — 在新的后台线程上调用接收者的方法。
- [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) — 取消先前使用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 实例方法注册的 perform 请求。
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — 取消先前使用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 注册的 perform 请求。
