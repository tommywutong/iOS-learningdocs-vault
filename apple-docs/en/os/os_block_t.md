---
title: os_block_t
framework: os
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/os/os_block_t
source_url: 'https://developer.apple.com/documentation/os/os_block_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/os_block_t.json'
content_hash: 'sha256:c8bddd12fd68a7b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# os_block_t

<sub>Type Alias</sub>

A block that takes no arguments and returns no value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef void (^)(void) os_block_t;
```

## Discussion

When not building with Objective-C ARC, a block object allocated on or copied to the heap must be released with a [release](../objectivec/nsobject-c.protocol/release.md) message or the `Block_release` function.

The declaration of a block literal allocates storage on the stack.

## See Also

### Memory

- [os_proc_available_memory](os_proc_available_memory.md) — Determines the amount of memory available to the current app.
- [os_function_t](os_function_t.md) — A pointer to a function.
- [os_release](os_release-c.func.md)
- [os_retain](os_retain-c.func.md)
