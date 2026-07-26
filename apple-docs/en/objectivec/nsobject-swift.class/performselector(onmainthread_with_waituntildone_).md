---
title: 'performSelector(onMainThread:with:waitUntilDone:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/performselector(onmainthread:with:waituntildone:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/performselector(onmainthread:with:waituntildone:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/performselector%28onmainthread%3Awith%3Awaituntildone%3A%29.json'
content_hash: 'sha256:00f09c61d165ebd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# performSelector(onMainThread:with:waitUntilDone:)

<sub>Instance Method</sub>

Invokes a method of the receiver on the main thread using the default mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performSelector(onMainThread aSelector: Selector, with arg: Any?, waitUntilDone wait: Bool)
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method to invoke. The method should not have a significant return value and should take a single argument of type id, or no arguments.

- `arg` — The argument to pass to the method when it is invoked. Pass `nil` if the method does not take an argument.

- `wait` — A Boolean that specifies whether the current thread blocks until after the specified selector is performed on the receiver on the main thread. Specify [YES](../yes.md) to block this thread; otherwise, specify [NO](../no.md) to have this method return immediately. If the current thread is also the main thread, and you specify [YES](../yes.md) for this parameter, the message is delivered and processed immediately.

## Discussion

You can use this method to deliver messages to the main thread of your application. The main thread encompasses the application’s main run loop, and is where the `NSApplication` object receives events. The message in this case is a method of the current object that you want to execute on the thread.

This method queues the message on the run loop of the main thread using the common run loop modes—that is, the modes associated with the [common](../../foundation/runloop/mode/common.md) constant. As part of its normal run loop processing, the main thread dequeues the message (assuming it is running in one of the common run loop modes) and invokes the desired method. Multiple calls to this method from the same thread cause the corresponding selectors to be queued and performed in the same order in which the calls were made.

You cannot cancel messages queued using this method. If you want the option of canceling a message on the current thread, you must use either the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) or [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) method.

### Special Considerations

This method registers with the runloop of its current context, and depends on that runloop being run on a regular basis to perform correctly. One common context where you might call this method and end up registering with a runloop that is not automatically run on a regular basis is when being invoked by a dispatch queue. If you need this type of functionality when running on a dispatch queue, you should use [dispatch_after](../../dispatch/dispatch_after.md) and related methods to get the behavior you want.

## See Also

### Sending Messages

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — Invokes a method of the receiver on the current thread using the default mode after a delay.
- [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) — Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the main thread using the specified modes.
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — Invokes a method of the receiver on the specified thread using the default mode.
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<perform(__on_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the specified thread using the specified modes.
- [- performSelectorInBackground:withObject:](<performselector(inbackground_with_).md>) — Invokes a method of the receiver on a new background thread.
- [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) — Cancels perform requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method.
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — Cancels perform requests previously registered with [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>).
