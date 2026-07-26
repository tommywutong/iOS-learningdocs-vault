---
title: Macros
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/macros
source_url: 'https://developer.apple.com/documentation/swift/macros'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/macros.json'
content_hash: 'sha256:53388320837587b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# Macros

<sub>API Collection</sub>

Generate boilerplate code and perform other compile-time operations.

## Topics

### Essentials

- [Applying Macros](applying-macros.md) — Use macros to generate repetitive code at compile time.

### Getting Source Location Information

- [file()](<file().md>) — Produces the path to the file in which it appears.
- [fileID()](<fileid().md>) — Produces a unique identifier for the source file in which the macro appears.
- [filePath()](<filepath().md>) — Produces the complete path to the file in which the macro appears.
- [function()](<function().md>) — Produces the name of the declaration in which it appears.
- [line()](<line().md>) — Produces the line number on which it appears.
- [column()](<column().md>) — Produces the column number in which the macro begins.

### Generating Compile-Time Diagnostics

- [warning(_:)](<warning(__).md>) — Produces the given warning message during compilation.
- [error(_:)](<error(__).md>) — Emits the given message as a fatal error and terminates the compilation process.

### Writing Custom Macros

- [externalMacro(module:type:)](<externalmacro(module_type_).md>) — Specifies the module and type name for a macro’s implementation.

### Accessing the Dynamic Shared Object Handle

- [dsohandle()](<dsohandle().md>) — Produces the dynamic shared object (DSO) handle in use where the macro appears.

## See Also

### Programming Tasks

- [Input and Output](input-and-output.md) — Print values to the console, read from and write to text streams, and use command line arguments.
- [Debugging and Reflection](debugging-and-reflection.md) — Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Concurrency](concurrency.md) — Perform asynchronous and parallel operations.
- [Key-Path Expressions](key-path-expressions.md) — Use key-path expressions to access properties dynamically.
- [Manual Memory Management](manual-memory-management.md) — Allocate and manage memory manually.
- [Type Casting and Existential Types](type-casting-and-existential-types.md) — Perform casts between types or represent values of any type.
- [C Interoperability](c-interoperability.md) — Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md) — Work with prefix, postfix, and infix operators.
