---
title: CFRunLoopObserverGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopobservergettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopobservergettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopobservergettypeid%28%29.json'
content_hash: 'sha256:623f239d1ff27928'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopObserverGetTypeID()

<sub>Function</sub>

Returns the type identifier for the CFRunLoopObserver opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopObserverGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFRunLoopObserver opaque type.

## See Also

### CFRunLoopObserver Miscellaneous Functions

- [CFRunLoopObserverCreateWithHandler](<cfrunloopobservercreatewithhandler(__________).md>) — Creates a CFRunLoopObserver object with a block-based handler.
- [CFRunLoopObserverCreate](<cfrunloopobservercreate(____________).md>) — Creates a CFRunLoopObserver object with a function callback.
- [CFRunLoopObserverDoesRepeat](<cfrunloopobserverdoesrepeat(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver repeats.
- [CFRunLoopObserverGetActivities](<cfrunloopobservergetactivities(__).md>) — Returns the run loop stages during which an observer runs.
- [CFRunLoopObserverGetContext](<cfrunloopobservergetcontext(____).md>) — Returns the context information for a CFRunLoopObserver object.
- [CFRunLoopObserverGetOrder](<cfrunloopobservergetorder(__).md>) — Returns the ordering parameter for a CFRunLoopObserver object.
- [CFRunLoopObserverInvalidate](<cfrunloopobserverinvalidate(__).md>) — Invalidates a CFRunLoopObserver object, stopping it from ever firing again.
- [CFRunLoopObserverIsValid](<cfrunloopobserverisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.
