---
title: distantFuture
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdate/distantfuture
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/distantfuture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/distantfuture.json'
content_hash: 'sha256:d866ee94e723f5be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# distantFuture

<sub>Type Property</sub>

A date object representing a date in the distant future.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var distantFuture: Date { get }
```

## Return Value

An [NSDate](../nsdate.md) object representing a date in the distant future (in terms of centuries).

## Discussion

You can pass this value when an [NSDate](../nsdate.md) object is required to have the date argument essentially ignored. For example, the [NSWindow](../../appkit/nswindow.md) method [nextEvent(matching:until:inMode:dequeue:)](<../../appkit/nswindow/nextevent(matching_until_inmode_dequeue_).md>) returns `nil` if an event specified in the event mask does not happen before the specified date. You can use the object returned by [distantFuture](distantfuture.md) as the date argument to wait indefinitely for the event to occur.

```objc
myEvent = [myWindow nextEventMatchingMask:myEventMask
    untilDate:[NSDate distantFuture]
    inMode:NSDefaultRunLoopMode
    dequeue:YES];
```

## See Also

### Getting Temporal Boundaries

- [distantPast](distantpast.md) — A date object representing a date in the distant past.
