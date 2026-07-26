---
title: 'cancelPreviousPerformRequests(withTarget:selector:object:)'
framework: Objective-C Runtime
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/nsobject-swift.class/cancelpreviousperformrequests(withtarget:selector:object:)'
source_url: 'https://developer.apple.com/documentation/objectivec/nsobject-swift.class/cancelpreviousperformrequests(withtarget:selector:object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/nsobject-swift.class/cancelpreviousperformrequests%28withtarget%3Aselector%3Aobject%3A%29.json'
content_hash: 'sha256:2f600ee11f04e231'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# cancelPreviousPerformRequests(withTarget:selector:object:)

<sub>Type Method</sub>

Cancels perform requests previously registered with [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func cancelPreviousPerformRequests(withTarget aTarget: Any, selector aSelector: Selector, object anArgument: Any?)
```

## Parameters

- `aTarget` — The target for requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method

- `aSelector` — The [Selector](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Selector.html#//apple_ref/doc/uid/TP40008195-CH48) for requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method.

- `anArgument` — The argument for requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method. Argument equality is determined using [- isEqual:](<../nsobjectprotocol/isequal(__).md>), so the value need not be the same object that was passed originally. Pass `nil` to match a request for `nil` that was originally passed as the argument.

## Discussion

All perform requests are canceled that have the same target as `aTarget`, argument as `anArgument`, and selector as `aSelector`. This method removes perform requests only in the current run loop, not all run loops.

## See Also

### Sending Messages

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — Invokes a method of the receiver on the current thread using the default mode after a delay.
- [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) — Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — Invokes a method of the receiver on the main thread using the default mode.
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the main thread using the specified modes.
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — Invokes a method of the receiver on the specified thread using the default mode.
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<perform(__on_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the specified thread using the specified modes.
- [- performSelectorInBackground:withObject:](<performselector(inbackground_with_).md>) — Invokes a method of the receiver on a new background thread.
- [+ cancelPreviousPerformRequestsWithTarget:](<cancelpreviousperformrequests(withtarget_).md>) — Cancels perform requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method.
