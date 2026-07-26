---
title: 'CFRunLoopObserverInvalidate(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopobserverinvalidate(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopobserverinvalidate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopobserverinvalidate%28_%3A%29.json'
content_hash: 'sha256:27567a875d0ff36e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopObserverInvalidate(_:)

<sub>Function</sub>

Invalidates a CFRunLoopObserver object, stopping it from ever firing again.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopObserverInvalidate(_ observer: CFRunLoopObserver!)
```

## Parameters

- `observer` — The run loop observer to invalidate.

## Discussion

Once invalidated, `observer` will never fire and call its callback function again. This function automatically removes `observer` from all run loop modes in which it had been added. The memory is not deallocated unless the run loop held the only reference to `observer`.

## See Also

### CFRunLoopObserver Miscellaneous Functions

- [CFRunLoopObserverCreateWithHandler](<cfrunloopobservercreatewithhandler(__________).md>) — Creates a CFRunLoopObserver object with a block-based handler.
- [CFRunLoopObserverCreate](<cfrunloopobservercreate(____________).md>) — Creates a CFRunLoopObserver object with a function callback.
- [CFRunLoopObserverDoesRepeat](<cfrunloopobserverdoesrepeat(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver repeats.
- [CFRunLoopObserverGetActivities](<cfrunloopobservergetactivities(__).md>) — Returns the run loop stages during which an observer runs.
- [CFRunLoopObserverGetContext](<cfrunloopobservergetcontext(____).md>) — Returns the context information for a CFRunLoopObserver object.
- [CFRunLoopObserverGetOrder](<cfrunloopobservergetorder(__).md>) — Returns the ordering parameter for a CFRunLoopObserver object.
- [CFRunLoopObserverGetTypeID](<cfrunloopobservergettypeid().md>) — Returns the type identifier for the CFRunLoopObserver opaque type.
- [CFRunLoopObserverIsValid](<cfrunloopobserverisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.
