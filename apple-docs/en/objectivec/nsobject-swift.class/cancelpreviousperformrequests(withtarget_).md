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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Objective-C Runtime](../../objectivec.md) · [NSObject](../nsobject-swift.class.md)

# cancelPreviousPerformRequests(withTarget:)

<sub>Type Method</sub>

Cancels perform requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func cancelPreviousPerformRequests(withTarget aTarget: Any)
```

## Parameters

- `aTarget` — The target for requests previously registered with the [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) instance method.

## Discussion

All perform requests having the same target `aTarget` are canceled. This method removes perform requests only in the current run loop, not all run loops.

## See Also

### Sending Messages

- [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>) — Invokes a method of the receiver on the current thread using the default mode after a delay.
- [- performSelector:withObject:afterDelay:inModes:](<perform(__with_afterdelay_inmodes_).md>) — Invokes a method of the receiver on the current thread using the specified modes after a delay.
- [- performSelectorOnMainThread:withObject:waitUntilDone:](<performselector(onmainthread_with_waituntildone_).md>) — Invokes a method of the receiver on the main thread using the default mode.
- [- performSelectorOnMainThread:withObject:waitUntilDone:modes:](<performselector(onmainthread_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the main thread using the specified modes.
- [- performSelector:onThread:withObject:waitUntilDone:](<perform(__on_with_waituntildone_).md>) — Invokes a method of the receiver on the specified thread using the default mode.
- [- performSelector:onThread:withObject:waitUntilDone:modes:](<perform(__on_with_waituntildone_modes_).md>) — Invokes a method of the receiver on the specified thread using the specified modes.
- [- performSelectorInBackground:withObject:](<performselector(inbackground_with_).md>) — Invokes a method of the receiver on a new background thread.
- [+ cancelPreviousPerformRequestsWithTarget:selector:object:](<cancelpreviousperformrequests(withtarget_selector_object_).md>) — Cancels perform requests previously registered with [- performSelector:withObject:afterDelay:](<perform(__with_afterdelay_).md>).
