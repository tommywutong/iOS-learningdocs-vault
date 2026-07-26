---
title: dispatch_debug
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+（6.0 起废弃）, iPadOS 4.0+（6.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.6+（10.9 起废弃）, tvOS, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/dispatch/dispatch_debug
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_debug'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_debug.json'
content_hash: 'sha256:f7833fc007e7b479'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_debug

<sub>Function</sub>

Programmatically logs debug information about a dispatch object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_debug(dispatch_object_t object, const char *message, ...);
```

## Parameters

- `object` — The object to introspect.

- `message` — The message to log above and beyond the introspection, in the form of a printf-style format string. The content of this message is appended to the log message separated by a colon, like this: “{_dispatch_object_information_}: _message_”.

## Discussion

Debug information is logged to the Console log.  This information can be useful as a debugging tool to view the internal state (current reference count, suspension count, etc.) of a dispatch object at the time the [dispatch_debug](dispatch_debug.md) function is called.

## See Also

### Functions

- [dispatch_get_current_queue](<dispatch_get_current_queue().md>) — Returns the queue on which the currently executing block is running.
- [dispatch_debugv](<dispatch_debugv(______).md>)
