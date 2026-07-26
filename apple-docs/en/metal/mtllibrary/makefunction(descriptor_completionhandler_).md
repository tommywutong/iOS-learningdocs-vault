---
title: 'makeFunction(descriptor:completionHandler:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllibrary/makefunction(descriptor:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/makefunction(descriptor:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/makefunction%28descriptor%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:a69b4c0452e6d7ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# makeFunction(descriptor:completionHandler:)

<sub>Instance Method</sub>

Asynchronously creates an object representing a shader function, using the specified descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeFunction(descriptor: MTLFunctionDescriptor, completionHandler: @escaping @Sendable ((any MTLFunction)?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeFunction(descriptor: MTLFunctionDescriptor) async throws -> any MTLFunction
```

## Parameters

- `descriptor` — The description of the function object to create.

- `completionHandler` — A Swift closure or an Objective-C block that Metal calls after it creates the function.

## See Also

### Creating shader function instances

- [- newFunctionWithName:](<makefunction(name_).md>) — Creates an instance that represents a shader function in the library.
- [- newFunctionWithName:constantValues:completionHandler:](<makefunction(name_constantvalues_completionhandler_).md>) — Asynchronously creates a specialized shader function.
- [- newFunctionWithName:constantValues:error:](<makefunction(name_constantvalues_).md>) — Synchronously creates a specialized shader function.
- [- newFunctionWithDescriptor:error:](<makefunction(descriptor_).md>) — Synchronously creates an object representing a shader function, using the specified descriptor.
