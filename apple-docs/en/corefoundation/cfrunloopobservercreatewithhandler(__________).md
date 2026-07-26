---
title: 'CFRunLoopObserverCreateWithHandler(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfrunloopobservercreatewithhandler(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopobservercreatewithhandler(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopobservercreatewithhandler%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:2c6de8751eb68bcf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopObserverCreateWithHandler(_:_:_:_:_:)

<sub>Function</sub>

Creates a CFRunLoopObserver object with a block-based handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFRunLoopObserverCreateWithHandler(_ allocator: CFAllocator!, _ activities: CFOptionFlags, _ repeats: Bool, _ order: CFIndex, _ block: ((CFRunLoopObserver?, CFRunLoopActivity) -> Void)!) -> CFRunLoopObserver!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `activities` — Set of flags identifying the activity stages of the run loop during which the observer is called. See [CFRunLoopActivity](cfrunloopactivity.md)for the list of stages. To have the observer called at multiple stages in the run loop, combine the [CFRunLoopActivity](cfrunloopactivity.md) values using the bitwise-OR operator.

- `repeats` — A flag identifying whether the observer is called only once or every time through the run loop. If `repeats` is `false`, the observer is invalidated after it is called once, even if the observer was scheduled to be called at multiple stages within the run loop.

- `order` — A priority index indicating the order in which run loop observers are processed. When multiple run loop observers are scheduled in the same activity stage in a given run loop mode, the observers are processed in increasing order of this parameter. Pass 0 unless there is a reason to do otherwise.

- `block` — The block invoked when the observer runs. The block takes two arguments: - **`observer`** — The run loop observer that is firing. - **`activity`** — The current activity stage of the run loop.

## Return Value

The new CFRunLoopObserver object. Ownership follows the Create Rule described in [Ownership Policy](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148).

## Discussion

The run loop observer is not automatically added to a run loop. To add the observer to a run loop, use [CFRunLoopAddObserver](<cfrunloopaddobserver(______).md>). An observer can be registered to only one run loop, although it can be added to multiple run loop modes within that run loop.

## See Also

### CFRunLoopObserver Miscellaneous Functions

- [CFRunLoopObserverCreate](<cfrunloopobservercreate(____________).md>) — Creates a CFRunLoopObserver object with a function callback.
- [CFRunLoopObserverDoesRepeat](<cfrunloopobserverdoesrepeat(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver repeats.
- [CFRunLoopObserverGetActivities](<cfrunloopobservergetactivities(__).md>) — Returns the run loop stages during which an observer runs.
- [CFRunLoopObserverGetContext](<cfrunloopobservergetcontext(____).md>) — Returns the context information for a CFRunLoopObserver object.
- [CFRunLoopObserverGetOrder](<cfrunloopobservergetorder(__).md>) — Returns the ordering parameter for a CFRunLoopObserver object.
- [CFRunLoopObserverGetTypeID](<cfrunloopobservergettypeid().md>) — Returns the type identifier for the CFRunLoopObserver opaque type.
- [CFRunLoopObserverInvalidate](<cfrunloopobserverinvalidate(__).md>) — Invalidates a CFRunLoopObserver object, stopping it from ever firing again.
- [CFRunLoopObserverIsValid](<cfrunloopobserverisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.
