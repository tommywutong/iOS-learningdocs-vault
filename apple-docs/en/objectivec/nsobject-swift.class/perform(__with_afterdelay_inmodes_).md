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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# perform(_:with:afterDelay:inModes:)

<sub>Instance Method</sub>

Invokes a method of the receiver on the current thread using the specified modes after a delay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval, inModes modes: [RunLoop.Mode])
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method to invoke. The method should not have a significant return value and should take a single argument of type id, or no arguments.

- `anArgument` — The argument to pass to the method when it is invoked. Pass `nil` if the method does not take an argument.

- `delay` — The minimum time before which the message is sent. Specifying a delay of 0 does not necessarily cause the selector to be performed immediately. The selector is still queued on the thread’s run loop and performed as soon as possible.

- `modes` — An array of strings that identify the modes to associate with the timer that performs the selector. This array must contain at least one string. If you specify `nil` or an empty array for this parameter, this method returns without performing the specified selector. For information about run loop modes, see [Run Loops](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/RunLoopManagement/RunLoopManagement.html#//apple_ref/doc/uid/10000057i-CH16) in [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i).

## Discussion

This method sets up a timer to perform the `aSelector` message on the current thread’s run loop. The timer is configured to run in the modes specified by the `modes` parameter. When the timer fires, the thread attempts to dequeue the message from the run loop and perform the selector. It succeeds if the run loop is running and in one of the specified modes; otherwise, the timer waits until the run loop is in one of those modes.

If you want the message to be dequeued when the run loop is in a mode other than the default mode, use the [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) method instead. If you are not sure whether the current thread is the main thread, you can use the [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) or [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) method to guarantee that your selector executes on the main thread. To cancel a queued message, use the [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) or [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) method.

### Special Considerations

This method registers with the runloop of its current context, and depends on that runloop being run on a regular basis to perform correctly. One common context where you might call this method and end up registering with a runloop that is not automatically run on a regular basis is when being invoked by a dispatch queue. If you need this type of functionality when running on a dispatch queue, you should use [dispatch_after](../../dispatch/dispatch_after.md) and related methods to get the behavior you want.

## See Also

### Related Documentation

- [invalidate()](<../../foundation/timer/invalidate().md>) — Stops the timer from ever firing again and requests its removal from its run loop.
- [add(_:forMode:)](<../../foundation/runloop/add(__formode_)-392ag.md>) — Registers a given timer with a given input mode.

### Sending Messages

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — Invokes a method of the receiver on the current thread using the default mode after a delay.
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — Invokes a method of the receiver on the main thread using the default mode.
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the main thread using the specified modes.
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — Invokes a method of the receiver on the specified thread using the default mode.
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<perform(__on_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the specified thread using the specified modes.
- [- performSelectorInBackground:withObject:](<performselector(inbackground_with_).md>) — Invokes a method of the receiver on a new background thread.
- [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) — Cancels perform requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method.
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — Cancels perform requests previously registered with [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>).
