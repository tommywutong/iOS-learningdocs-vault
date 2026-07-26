---
title: 'makeIntersectionFunction(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllibrary/makeintersectionfunction(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/makeintersectionfunction(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/makeintersectionfunction%28descriptor%3A%29.json'
content_hash: 'sha256:ac21c06b0cc64365'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# makeIntersectionFunction(descriptor:)

<sub>Instance Method</sub>

Synchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIntersectionFunction(descriptor: MTLIntersectionFunctionDescriptor) throws -> any MTLFunction
```

## See Also

### Creating intersection function instances

- [- newIntersectionFunctionWithDescriptor:completionHandler:](<makeintersectionfunction(descriptor_completionhandler_).md>) — Asynchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.
