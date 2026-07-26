---
title: 'CFRunLoopObserverGetOrder(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopobservergetorder(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopobservergetorder(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopobservergetorder%28_%3A%29.json'
content_hash: 'sha256:a61a0f8418984a68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopObserverGetOrder(_:)

<sub>Function</sub>

Returns the ordering parameter for a CFRunLoopObserver object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopObserverGetOrder(_ observer: CFRunLoopObserver!) -> CFIndex
```

## Parameters

- `observer` — The run loop observer to examine.

## Return Value

The ordering parameter for `observer`. When multiple observers are scheduled in the same run loop mode and stage, this value determines the order (from small to large) in which the observers are called.

## See Also

### CFRunLoopObserver Miscellaneous Functions

- [CFRunLoopObserverCreateWithHandler](<cfrunloopobservercreatewithhandler(__________).md>) — Creates a CFRunLoopObserver object with a block-based handler.
- [CFRunLoopObserverCreate](<cfrunloopobservercreate(____________).md>) — Creates a CFRunLoopObserver object with a function callback.
- [CFRunLoopObserverDoesRepeat](<cfrunloopobserverdoesrepeat(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver repeats.
- [CFRunLoopObserverGetActivities](<cfrunloopobservergetactivities(__).md>) — Returns the run loop stages during which an observer runs.
- [CFRunLoopObserverGetContext](<cfrunloopobservergetcontext(____).md>) — Returns the context information for a CFRunLoopObserver object.
- [CFRunLoopObserverGetTypeID](<cfrunloopobservergettypeid().md>) — Returns the type identifier for the CFRunLoopObserver opaque type.
- [CFRunLoopObserverInvalidate](<cfrunloopobserverinvalidate(__).md>) — Invalidates a CFRunLoopObserver object, stopping it from ever firing again.
- [CFRunLoopObserverIsValid](<cfrunloopobserverisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.
