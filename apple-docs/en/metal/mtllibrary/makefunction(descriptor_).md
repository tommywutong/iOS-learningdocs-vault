---
title: 'makeFunction(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllibrary/makefunction(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/makefunction(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/makefunction%28descriptor%3A%29.json'
content_hash: 'sha256:bc6d270620493366'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# makeFunction(descriptor:)

<sub>Instance Method</sub>

Synchronously creates an object representing a shader function, using the specified descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeFunction(descriptor: MTLFunctionDescriptor) throws -> any MTLFunction
```

## Parameters

- `descriptor` — The description of the function object to create.

## Return Value

A new [MTLFunction](../mtlfunction.md) instance if the method finds the function in the library; otherwise Swift throws an error and Objective-C returns `nil`.

## See Also

### Creating shader function instances

- [- newFunctionWithName:](<makefunction(name_).md>) — Creates an instance that represents a shader function in the library.
- [- newFunctionWithName:constantValues:completionHandler:](<makefunction(name_constantvalues_completionhandler_).md>) — Asynchronously creates a specialized shader function.
- [- newFunctionWithName:constantValues:error:](<makefunction(name_constantvalues_).md>) — Synchronously creates a specialized shader function.
- [- newFunctionWithDescriptor:completionHandler:](<makefunction(descriptor_completionhandler_).md>) — Asynchronously creates an object representing a shader function, using the specified descriptor.
