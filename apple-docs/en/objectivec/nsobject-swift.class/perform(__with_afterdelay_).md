---
title: 'perform(_:with:afterDelay:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/perform(_:with:afterdelay:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/perform(_:with:afterdelay:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/perform%28_%3Awith%3Aafterdelay%3A%29.json'
content_hash: 'sha256:0a80f84267d6253f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# perform(_:with:afterDelay:)

<sub>Instance Method</sub>

Invokes a method of the receiver on the current thread using the default mode after a delay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ aSelector: Selector, with anArgument: Any?, afterDelay delay: TimeInterval)
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method to invoke. The method should not have a significant return value and should take a single argument of type id, or no arguments.

- `anArgument` — The argument to pass to the method when it is invoked. Pass `nil` if the method does not take an argument.

- `delay` — The minimum time before which the message is sent. Specifying a delay of 0 does not necessarily cause the selector to be performed immediately. The selector is still queued on the thread’s run loop and performed as soon as possible.

## Discussion

This method sets up a timer to perform the `aSelector` message on the current thread’s run loop. The timer is configured to run in the default mode (`NSDefaultRunLoopMode`). When the timer fires, the thread attempts to dequeue the message from the run loop and perform the selector. It succeeds if the run loop is running and in the default mode; otherwise, the timer waits until the run loop is in the default mode.

If you want the message to be dequeued when the run loop is in a mode other than the default mode, use the [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) method instead. If you are not sure whether the current thread is the main thread, you can use the [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) or [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) method to guarantee that your selector executes on the main thread. To cancel a queued message, use the [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) or [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) method.

### Special Considerations

This method registers with the runloop of its current context, and depends on that runloop being run on a regular basis to perform correctly. One common context where you might call this method and end up registering with a runloop that is not automatically run on a regular basis is when being invoked by a dispatch queue. If you need this type of functionality when running on a dispatch queue, you should use [dispatch_after](../../dispatch/dispatch_after.md) and related methods to get the behavior you want.

## See Also

### Sending Messages

- [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) — Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — Invokes a method of the receiver on the main thread using the default mode.
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the main thread using the specified modes.
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — Invokes a method of the receiver on the specified thread using the default mode.
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<perform(__on_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the specified thread using the specified modes.
- [- performSelectorInBackground:withObject:](<performselector(inbackground_with_).md>) — Invokes a method of the receiver on a new background thread.
- [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) — Cancels perform requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method.
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — Cancels perform requests previously registered with [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>).
