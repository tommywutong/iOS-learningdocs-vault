---
title: dispatch_data_apply
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_data_apply
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_data_apply'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_data_apply.json'
content_hash: 'sha256:cc445784b61af6c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_data_apply

<sub>Function</sub>

Traverses the memory of a dispatch data object and executes custom code on each region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern bool dispatch_data_apply(dispatch_data_t data, dispatch_data_applier_t applier);
```

## Parameters

- `data` — The dispatch object whose memory you want to use.

- `applier` — The block to run on each contiguous memory region of `data`.

## Return Value

A Boolean indicating whether the traversal completed successfully. Typically, this value is `true` if the applier block was executed on all of the regions or there was nothing to traverse. If it is `false`, it means the block terminated the traversal early.

## Discussion

For each contiguous memory region, this function creates a temporary dispatch data object and passes it to the specified applier function. This new object, plus the other parameters to the block, provide direct access to the specific memory region being examined. Once the applier block returns, the temporary dispatch data object is released. (The original object in the `data` parameter is not touched.)

> [!note] Note
> If the dispatch data object has zero length, the applier block is not called.

## See Also

### Applying Changes to the Data

- [dispatch_data_applier_t](dispatch_data_applier_t.md) — A block to invoke for every contiguous memory region in a data object.
