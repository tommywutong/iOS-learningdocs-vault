---
title: dispatch_workloop_create
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_workloop_create
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_workloop_create'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_workloop_create.json'
content_hash: 'sha256:9979c9e6e3845edb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_workloop_create

<sub>Function</sub>

Creates a new workloop with the specified label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_workloop_tdispatch_workloop_create(const char *label);
```

## Parameters

- `label` — A string label to attach to the queue to uniquely identify it in debugging tools such as Instruments, `sample`, stackshots, and crash reports.  Because apps, libraries, and frameworks can all create their own dispatch queues, a reverse-DNS naming style (`com.example.myqueue`) is recommended.  This parameter is optional and can be `NULL`.

## Return Value

The newly created workloop.

## Discussion

The returned workloop is active, and you may submit blocks to it immediately.

## See Also

### Creating a Dispatch Workloop

- [dispatch_workloop_create_inactive](dispatch_workloop_create_inactive.md) — Creates a new inactive workloop with the specified label.
- [dispatch_workloop_t](dispatch_workloop_t.md) — A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.
- [OS_dispatch_workloop](os_dispatch_workloop.md) — A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.
