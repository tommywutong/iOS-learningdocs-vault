---
title: CFRunLoopObserver
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfrunloopobserver
source_url: 'https://developer.apple.com/documentation/corefoundation/cfrunloopobserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfrunloopobserver.json'
content_hash: 'sha256:4f9b62c87714cc4c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFRunLoopObserver

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFRunLoopObserver
```

## Overview

A CFRunLoopObserver provides a general means to receive callbacks at different points within a running run loop. In contrast to sources, which fire when an asynchronous event occurs, and timers, which fire when a particular time passes, observers fire at special locations within the execution of the run loop, such as before sources are processed or before the run loop goes to sleep, waiting for an event to occur. Observers can be either one-time events or repeated every time through the run loop’s loop.

Each run loop observer can be registered in only one run loop at a time, although it can be added to multiple run loop modes within that run loop.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### CFRunLoopObserver Miscellaneous Functions

- [CFRunLoopObserverCreateWithHandler](<cfrunloopobservercreatewithhandler(__________).md>) — Creates a CFRunLoopObserver object with a block-based handler.
- [CFRunLoopObserverCreate](<cfrunloopobservercreate(____________).md>) — Creates a CFRunLoopObserver object with a function callback.
- [CFRunLoopObserverDoesRepeat](<cfrunloopobserverdoesrepeat(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver repeats.
- [CFRunLoopObserverGetActivities](<cfrunloopobservergetactivities(__).md>) — Returns the run loop stages during which an observer runs.
- [CFRunLoopObserverGetContext](<cfrunloopobservergetcontext(____).md>) — Returns the context information for a CFRunLoopObserver object.
- [CFRunLoopObserverGetOrder](<cfrunloopobservergetorder(__).md>) — Returns the ordering parameter for a CFRunLoopObserver object.
- [CFRunLoopObserverGetTypeID](<cfrunloopobservergettypeid().md>) — Returns the type identifier for the CFRunLoopObserver opaque type.
- [CFRunLoopObserverInvalidate](<cfrunloopobserverinvalidate(__).md>) — Invalidates a CFRunLoopObserver object, stopping it from ever firing again.
- [CFRunLoopObserverIsValid](<cfrunloopobserverisvalid(__).md>) — Returns a Boolean value that indicates whether a CFRunLoopObserver object is valid and able to fire.

### Callbacks

- [CFRunLoopObserverCallBack](cfrunloopobservercallback.md) — Callback invoked when a CFRunLoopObserver object is fired.

### Data Types

- [CFRunLoopObserverContext](cfrunloopobservercontext.md) — A structure that contains program-defined data and callbacks with which you can configure a CFRunLoopObserver object’s behavior.

### Constants

- [CFRunLoopActivity](cfrunloopactivity.md) — Run loop activity stages in which run loop observers can be scheduled.

## See Also

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
