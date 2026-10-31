---
title: 'perform(_:on:with:waitUntilDone:modes:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/perform(_:on:with:waituntildone:modes:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/perform(_:on:with:waituntildone:modes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/perform%28_%3Aon%3Awith%3Awaituntildone%3Amodes%3A%29.json'
content_hash: 'sha256:6858dbadc77c9c43'
translated: true
---

> 导航： [技术](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# perform(_:on:with:waitUntilDone:modes:)

<sub>实例方法</sub>

使用指定模式在指定线程上调用接收者的方法。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)
```

## 参数

- `aSelector` — 标识要调用的方法的 [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48)。它不应有显著的返回值，且应接受单个类型为 id 的参数，或不接受参数。

- `thr` — 在其上执行 `aSelector` 的线程。此线程表示目标线程。

- `arg` — 调用方法时传入的参数。若方法不接受参数，则传入 `nil`。

- `wait` — 指定当前线程是否阻塞，直到在指定线程上对接收者执行指定选择器之后。指定 [YES](../yes.md) 以阻塞此线程；否则指定 [NO](../no.md) 以使此方法立即返回。若当前线程与目标线程相同，且为此参数指定 [YES](../yes.md)，则选择器会立即执行。若指定 [NO](../no.md)，此方法会将该消息入队并立即返回，无论线程是否相同。

- `array` — 标识允许执行指定选择器的模式的字符串数组。此数组必须至少包含一个字符串。若为此参数指定 `nil` 或空数组，此方法会返回而不执行指定选择器。有关运行循环模式的信息，请参阅 [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i) 中的 [Run Loops](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html#//apple_ref/doc/uid/10000057i-CH16)。

## 讨论

你可以使用此方法向应用程序中的其他线程传递消息。此情况下的消息是当前对象的方法，你希望在目标线程上执行该方法。

此方法使用 `array` 参数中指定的运行循环模式将消息排入目标线程的运行循环。作为其正常运行循环处理的一部分，目标线程会将该消息出队（假定它正在指定模式之一中运行）并调用所需方法。

你无法取消使用此方法排队的消息。若希望可以选择取消当前线程上的消息，则必须改用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 或 [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) 方法。

### 特殊注意事项

此方法向其当前上下文的运行循环注册，并依赖于该运行循环定期运行才能正确执行。你可能会调用此方法并最终向不会自动定期运行的运行循环注册的一个常见上下文是由调度队列调用时。若在调度队列上运行时需要此类功能，应使用 [dispatch_after](../../dispatch/dispatch_after.md) 及相关方法来获得所需行为。

## 另请参阅

### 发送消息

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — 在延迟后使用默认模式在当前线程上调用接收者的方法。
- [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) — 在延迟后使用指定模式在当前线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — 使用默认模式在主线程上调用接收者的方法。
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — 使用指定模式在主线程上调用接收者的方法。
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — 使用默认模式在指定线程上调用接收者的方法。
- [- performSelectorInBackground:withObject:](<performselector(inbackground_with_).md>) — 在新的后台线程上调用接收者的方法。
- [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) — 取消先前使用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 实例方法注册的 perform 请求。
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — 取消先前使用 [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) 注册的 perform 请求。
