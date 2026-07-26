---
title: dispatch_workloop_create_inactive
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_workloop_create_inactive
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_workloop_create_inactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_workloop_create_inactive.json'
content_hash: 'sha256:945b72bddaece05d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_workloop_create_inactive

<sub>Function</sub>

Creates a new inactive workloop with the specified label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_workloop_tdispatch_workloop_create_inactive(const char *label);
```

## Parameters

- `label` — A string label to attach to the queue to uniquely identify it in debugging tools such as Instruments, `sample`, stackshots, and crash reports.  Because apps, libraries, and frameworks can all create their own dispatch queues, a reverse-DNS naming style (`com.example.myqueue`) is recommended. This parameter is optional and can be `NULL`.

## Return Value

The newly created workloop.

## Discussion

Use this function when you want to change the default behavior of the workloop before activating it. For example, use this method if you call [dispatch_set_qos_class_floor](dispatch_set_qos_class_floor.md) to configure the minimum quality of service level.

After configuring the workloop, you must call [dispatch_activate](<dispatchobject/activate().md>) before submitting any blocks to it. If you submit blocks to an inactive workloop, the system terminates the current process.

## See Also

### Creating a Dispatch Workloop

- [dispatch_workloop_create](dispatch_workloop_create.md) — Creates a new workloop with the specified label.
- [dispatch_workloop_t](dispatch_workloop_t.md) — A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.
- [OS_dispatch_workloop](os_dispatch_workloop.md) — A dispatch queue that prioritizes the execution of tasks based on their quality-of-service level.
