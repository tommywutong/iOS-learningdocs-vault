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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# performSelector(inBackground:with:)

<sub>Instance Method</sub>

Invokes a method of the receiver on a new background thread.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performSelector(inBackground aSelector: Selector, with arg: Any?)
```

## Parameters

- `aSelector` — A [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) that identifies the method to invoke. The method should not have a significant return value and should take a single argument of type id, or no arguments.

- `arg` — The argument to pass to the method when it is invoked. Pass `nil` if the method does not take an argument.

## Discussion

This method creates a new thread in your application, putting your application into multithreaded mode if it was not already. The method represented by `aSelector` must set up the thread environment just as you would for any other new thread in your program. For more information about how to configure and run threads, see [Threading Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Multithreading/Introduction/Introduction.html#//apple_ref/doc/uid/10000057i).

## See Also

### Sending Messages

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — Invokes a method of the receiver on the current thread using the default mode after a delay.
- [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) — Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — Invokes a method of the receiver on the main thread using the default mode.
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the main thread using the specified modes.
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — Invokes a method of the receiver on the specified thread using the default mode.
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<perform(__on_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the specified thread using the specified modes.
- [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) — Cancels perform requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method.
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — Cancels perform requests previously registered with [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>).
