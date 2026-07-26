---
title: 'makeIntersectionFunction(descriptor:completionHandler:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllibrary/makeintersectionfunction(descriptor:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/makeintersectionfunction(descriptor:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/makeintersectionfunction%28descriptor%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:5a8d287e7ea8344f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# makeIntersectionFunction(descriptor:completionHandler:)

<sub>Instance Method</sub>

Asynchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIntersectionFunction(descriptor: MTLIntersectionFunctionDescriptor, completionHandler: @escaping @Sendable ((any MTLFunction)?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeIntersectionFunction(descriptor: MTLIntersectionFunctionDescriptor) async throws -> any MTLFunction
```

## See Also

### Creating intersection function instances

- [- newIntersectionFunctionWithDescriptor:error:](<makeintersectionfunction(descriptor_).md>) — Synchronously creates an object representing a ray-tracing intersection function, using the specified descriptor.
