---
title: 'CFRunLoopObserverGetActivities(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopobservergetactivities(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopobservergetactivities(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopobservergetactivities%28_%3A%29.json'
content_hash: 'sha256:b73a7bfb9d99e6bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopObserverGetActivities(_:)

<sub>Function</sub>

Returns the run loop stages during which an observer runs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopObserverGetActivities(_ observer: CFRunLoopObserver!) -> CFOptionFlags
```

## Parameters

- `observer` — The run loop observer to examine.

## Return Value

A bitwise-OR combination of all the run loop stages in which `observer` is called. See [CFRunLoopActivity](cfrunloopactivity.md) for the list of stages.

## See Also

### CFRunLoopObserver Miscellaneous Functions

- [CFRunLoopObserverCreateWithHandler](<cfrunloopobservercreatewithhandler(__________).md>) — Creates a CFRunLoopObserver object with a block-based handler.
- [CFRunLoopObserverCreate](<cfrunloopobservercreate(____________).md>) — Creates a CFRunLoopObserver object with a function callback.
- [CFRunLoopObserverDoesRepeat](<cfrunloopobserverdoesrepeat(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver repeats.
- [CFRunLoopObserverGetContext](<cfrunloopobservergetcontext(____).md>) — Returns the context information for a CFRunLoopObserver object.
- [CFRunLoopObserverGetOrder](<cfrunloopobservergetorder(__).md>) — Returns the ordering parameter for a CFRunLoopObserver object.
- [CFRunLoopObserverGetTypeID](<cfrunloopobservergettypeid().md>) — Returns the type identifier for the CFRunLoopObserver opaque type.
- [CFRunLoopObserverInvalidate](<cfrunloopobserverinvalidate(__).md>) — Invalidates a CFRunLoopObserver object, stopping it from ever firing again.
- [CFRunLoopObserverIsValid](<cfrunloopobserverisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.
