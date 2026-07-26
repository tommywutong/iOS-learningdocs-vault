---
title: Input and Output
framework: Swift
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/input-and-output
source_url: 'https://developer.apple.com/documentation/swift/input-and-output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/input-and-output.json'
content_hash: 'sha256:73b1e0e2977ee7d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md) · [Swift Standard Library](swift-standard-library.md)

# Input and Output

<sub>API Collection</sub>

Print values to the console, read from and write to text streams, and use command line arguments.

## Topics

### Text Output

- [print(_:separator:terminator:)](<print(__separator_terminator_).md>) — Writes the textual representations of the given items into the standard output.
- [print(_:separator:terminator:to:)](<print(__separator_terminator_to_).md>) — Writes the textual representations of the given items into the given output stream.

### Command Line Input

- [CommandLine](commandline.md) — Command-line arguments for the current process.
- [readLine(strippingNewline:)](<readline(strippingnewline_).md>) — Returns a string read from standard input through the end of the current line or until EOF is reached.

### Streams

- [TextOutputStream](textoutputstream.md) — A type that can be the target of text-streaming operations.
- [TextOutputStreamable](textoutputstreamable.md) — A source of text-streaming operations.

## See Also

### Programming Tasks

- [Debugging and Reflection](debugging-and-reflection.md) — Fortify your code with runtime checks, and examine your values’ runtime representation.
- [Macros](macros.md) — Generate boilerplate code and perform other compile-time operations.
- [Concurrency](concurrency.md) — Perform asynchronous and parallel operations.
- [Key-Path Expressions](key-path-expressions.md) — Use key-path expressions to access properties dynamically.
- [Manual Memory Management](manual-memory-management.md) — Allocate and manage memory manually.
- [Type Casting and Existential Types](type-casting-and-existential-types.md) — Perform casts between types or represent values of any type.
- [C Interoperability](c-interoperability.md) — Use imported C types or call C variadic functions.
- [Operator Declarations](operator-declarations.md) — Work with prefix, postfix, and infix operators.
