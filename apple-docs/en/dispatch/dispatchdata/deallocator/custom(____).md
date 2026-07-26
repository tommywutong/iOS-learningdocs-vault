---
title: 'DispatchData.Deallocator.custom(_:_:)'
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchdata/deallocator/custom(_:_:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchdata/deallocator/custom(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchdata/deallocator/custom%28_%3A_%3A%29.json'
content_hash: 'sha256:3ff0e79666f53fca'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchData](../../dispatchdata.md) · [Deallocator](../deallocator.md)

# DispatchData.Deallocator.custom(_:_:)

<sub>Case</sub>

Use a custom deallocator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency case custom(DispatchQueue?, @Sendable () -> Void)
```

## See Also

### Deallocators

- [DispatchData.Deallocator.free](free.md) — Use `free` to deallocate memory.
- [DispatchData.Deallocator.unmap](unmap.md) — Use `munmap` to deallocate memory.
