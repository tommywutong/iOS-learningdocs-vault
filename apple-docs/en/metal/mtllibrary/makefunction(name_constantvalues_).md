---
title: 'makeFunction(name:constantValues:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtllibrary/makefunction(name:constantvalues:)'
source_url: 'https://developer.apple.com/documentation/metal/mtllibrary/makefunction(name:constantvalues:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllibrary/makefunction%28name%3Aconstantvalues%3A%29.json'
content_hash: 'sha256:9481c7625585f780'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLLibrary](../mtllibrary.md)

# makeFunction(name:constantValues:)

<sub>Instance Method</sub>

Synchronously creates a specialized shader function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeFunction(name: String, constantValues: MTLFunctionConstantValues) throws -> any MTLFunction
```

## Parameters

- `name` — The name of the specialized function.

- `constantValues` — The set of constant values for the function constants. The compiler can’t compile the function if any value is invalid for the function constants it requires.

## Return Value

A new [MTLFunction](../mtlfunction.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Function constant values are first looked up by their index, then by their name. The compiler ignores any values that don’t correspond to a function constant in the named function, and doesn’t generate errors or warnings.

## See Also

### Creating shader function instances

- [- newFunctionWithName:](<makefunction(name_).md>) — Creates an instance that represents a shader function in the library.
- [- newFunctionWithName:constantValues:completionHandler:](<makefunction(name_constantvalues_completionhandler_).md>) — Asynchronously creates a specialized shader function.
- [- newFunctionWithDescriptor:completionHandler:](<makefunction(descriptor_completionhandler_).md>) — Asynchronously creates an object representing a shader function, using the specified descriptor.
- [- newFunctionWithDescriptor:error:](<makefunction(descriptor_).md>) — Synchronously creates an object representing a shader function, using the specified descriptor.
