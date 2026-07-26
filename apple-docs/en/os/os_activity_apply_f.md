---
title: os_activity_apply_f
framework: os
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_activity_apply_f
source_url: 'https://developer.apple.com/documentation/os/os_activity_apply_f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_activity_apply_f.json'
content_hash: 'sha256:2ef7f5567cefb321'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_activity_apply_f

<sub>Function</sub>

Execute a function using a given activity object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void os_activity_apply_f(os_activity_t activity, void *context, os_function_t function);
```

## Parameters

- `activity` — An activity object. You can alternatively pass one of the global activity constants, such as [OS_ACTIVITY_NONE](os_activity_none.md) or [OS_ACTIVITY_CURRENT](os_activity_current.md).

- `context` — A context to pass to the function. This may be `NULL`.

- `function` — A function to call within the context of the given activity. This function must match the signature defined by [os_function_t](os_function_t.md).

## See Also

### Executing an Activity

- [os_activity_apply](os_activity_apply.md) — Execute a block using a given activity object.
