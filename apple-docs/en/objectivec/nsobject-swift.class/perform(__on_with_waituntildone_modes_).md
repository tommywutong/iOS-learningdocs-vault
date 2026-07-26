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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# perform(_:on:with:waitUntilDone:modes:)

<sub>Instance Method</sub>

Invokes a method of the receiver on the specified thread using the specified modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector, on thr: Thread, with arg: Any?, waitUntilDone wait: Bool, modes array: [String]?)
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method to invoke. It should not have a significant return value and should take a single argument of type id, or no arguments.

- `thr` — The thread on which to execute `aSelector`. This thread represents the target thread.

- `arg` — The argument to pass to the method when it is invoked. Pass `nil` if the method does not take an argument.

- `wait` — A Boolean that specifies whether the current thread blocks until after the specified selector is performed on the receiver on the specified thread. Specify [YES](../yes.md) to block this thread; otherwise, specify [NO](../no.md) to have this method return immediately. If the current thread and target thread are the same, and you specify [YES](../yes.md) for this parameter, the selector is performed immediately. If you specify [NO](../no.md), this method queues the message and returns immediately, regardless of whether the threads are the same or different.

- `array` — An array of strings that identifies the modes in which it is permissible to perform the specified selector. This array must contain at least one string. If you specify `nil` or an empty array for this parameter, this method returns without performing the specified selector. For information about run loop modes, see [Run Loops](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html#//apple_ref/doc/uid/10000057i-CH16) in [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i).

## Discussion

You can use this method to deliver messages to other threads in your application. The message in this case is a method of the current object that you want to execute on the target thread.

This method queues the message on the run loop of the target thread using the run loop modes specified in the `array` parameter. As part of its normal run loop processing, the target thread dequeues the message (assuming it is running in one of the specified modes) and invokes the desired method.

You cannot cancel messages queued using this method. If you want the option of canceling a message on the current thread, you must use either the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) or [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) method instead.

### Special Considerations

This method registers with the runloop of its current context, and depends on that runloop being run on a regular basis to perform correctly. One common context where you might call this method and end up registering with a runloop that is not automatically run on a regular basis is when being invoked by a dispatch queue. If you need this type of functionality when running on a dispatch queue, you should use [dispatch_after](../../dispatch/dispatch_after.md) and related methods to get the behavior you want.

## See Also

### Sending Messages

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — Invokes a method of the receiver on the current thread using the default mode after a delay.
- [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) — Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — Invokes a method of the receiver on the main thread using the default mode.
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the main thread using the specified modes.
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — Invokes a method of the receiver on the specified thread using the default mode.
- [- performSelectorInBackground:withObject:](<performselector(inbackground_with_).md>) — Invokes a method of the receiver on a new background thread.
- [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) — Cancels perform requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method.
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — Cancels perform requests previously registered with [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>).
