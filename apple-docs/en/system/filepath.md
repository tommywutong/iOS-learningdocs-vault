---
title: FilePath
framework: System
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/system/filepath
source_url: 'https://developer.apple.com/documentation/system/filepath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/system/filepath.json'
content_hash: 'sha256:4e8eedb211d1b10c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [System](../system.md)

# FilePath

<sub>Structure</sub>

Represents a location in the file system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FilePath
```

## Overview

This structure recognizes directory separators  (e.g. `/`), roots, and requires that the content terminates in a NUL (`0x0`). Beyond that, it does not give any meaning to the bytes that it contains. The file system defines how the content is interpreted; for example, by its choice of string encoding.

On construction, `FilePath` will normalize separators by removing redundant intermediary separators and stripping any trailing separators. On Windows, `FilePath` will also normalize forward slashes `/` into backslashes `\`, as preferred by the platform.

The code below creates a file path from a string literal, and then uses it to open and append to a log file:

```swift
let message: String = "This is a log message."
let path: FilePath = "/tmp/log"
let fd = try FileDescriptor.open(path, .writeOnly, options: .append)
try fd.closeAfter { try fd.writeAll(message.utf8) }
```

File paths conform to the [Equatable](../swift/equatable.md) and [Hashable](../swift/hashable.md) protocols by performing the protocols’ operations on their raw byte contents. This conformance allows file paths to be used, for example, as keys in a dictionary. However, the rules for path equivalence are file-system–specific and have additional considerations like case insensitivity, Unicode normalization, and symbolic links.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a File Path

- [init()](<filepath/init().md>) — Creates an empty, null-terminated path.
- [init(stringLiteral:)](<filepath/init(stringliteral_).md>) — Creates a file path from a string literal.

### Working with File Paths

- [length](filepath/length.md) — The length of the file path, excluding the null terminator.
- [description](filepath/description.md) — A textual representation of the file path.
- [debugDescription](filepath/debugdescription.md) — A textual representation of the file path, suitable for debugging.

### Interacting with C APIs

- [withCString(_:)](<filepath/withcstring(__).md>) — For backwards compatibility only. This function is equivalent to the preferred `withPlatformString`.

### Structures

- [Component](filepath/component.md) — Represents an individual, non-root component of a file path.
- [ComponentView](filepath/componentview.md) — A bidirectional, range replaceable collection of the non-root components that make up a file path.
- [Root](filepath/root-swift.struct.md) — Represents a root of a file path.

### Initializers

- [init(_:)](<filepath/init(__)-2gkpw.md>) — Creates a file path from a URL
- [init(_:)](<filepath/init(__)-61dsw.md>) — Creates a file path from a string.
- [init(cString:)](<filepath/init(cstring_)-2hetg.md>) _(deprecated)_
- [init(cString:)](<filepath/init(cstring_)-3xw0n.md>) _(deprecated)_
- [init(cString:)](<filepath/init(cstring_)-5igtz.md>) — For backwards compatibility only. This initializer is equivalent to the preferred `FilePath(platformString:)`. _(deprecated)_
- [init(cString:)](<filepath/init(cstring_)-8d3vx.md>) _(deprecated)_
- [init(platformString:)](<filepath/init(platformstring_)-4b3o6.md>) _(deprecated)_
- [init(platformString:)](<filepath/init(platformstring_)-5o7oh.md>) — Creates a file path by copying bytes from a null-terminated platform string.
- [init(platformString:)](<filepath/init(platformstring_)-6i5cc.md>) _(deprecated)_
- [init(platformString:)](<filepath/init(platformstring_)-8amn5.md>) — Creates a file path by copying bytes from a null-terminated platform string.
- [init(root:_:)](<filepath/init(root___)-19uu0.md>) — Create a file path from a root and a collection of components.
- [init(root:_:)](<filepath/init(root___)-19xzy.md>) — Create a file path from an optional root and a slice of another path’s components.
- [init(root:components:)](<filepath/init(root_components_).md>) — Create a file path from a root and any number of components.

### Instance Properties

- [components](filepath/components.md) — View the non-root components that make up this path.
- [extension](filepath/extension.md) — The extension of the file or directory last component.
- [isAbsolute](filepath/isabsolute.md) — Returns true if this path uniquely identifies the location of a file without reference to an additional starting location.
- [isEmpty](filepath/isempty.md) — Whether this path is empty
- [isLexicallyNormal](filepath/islexicallynormal.md) — Whether the path is in lexical-normal form, that is `.` and `..` components have been collapsed lexically (i.e. without following symlinks).
- [isRelative](filepath/isrelative.md) — Returns true if this path is not absolute (see `isAbsolute`).
- [lastComponent](filepath/lastcomponent.md) — Returns the final component of the path. Returns `nil` if the path is empty or only contains a root.
- [root](filepath/root-swift.property.md) — Returns the root of a path if there is one, otherwise `nil`.
- [stem](filepath/stem.md) — The non-extension portion of the file or directory last component.
- [string](filepath/string.md) — Creates a string by interpreting the path’s content as UTF-8 on Unix and UTF-16 on Windows.

### Instance Methods

- [append(_:)](<filepath/append(__)-66nkr.md>) — Append `components` on to the end of this path.
- [append(_:)](<filepath/append(__)-7ttzp.md>) — Append the contents of `other`, ignoring any spurious leading separators.
- [append(_:)](<filepath/append(__)-8f41n.md>) — Append a `component` on to the end of this path.
- [appending(_:)](<filepath/appending(__)-1dtn3.md>) — Non-mutating version of `append(_:String)`.
- [appending(_:)](<filepath/appending(__)-24s87.md>) — Non-mutating version of `append(_:Component)`.
- [appending(_:)](<filepath/appending(__)-60fwk.md>) — Non-mutating version of `append(_:C)`.
- [ends(with:)](<filepath/ends(with_).md>) — Returns whether `other` is a suffix of `self`, only considering whole path components.
- [lexicallyNormalize()](<filepath/lexicallynormalize().md>) — Collapse `.` and `..` components lexically (i.e. without following symlinks).
- [lexicallyNormalized()](<filepath/lexicallynormalized().md>) — Returns a copy of `self` in lexical-normal form, that is `.` and `..` components have been collapsed lexically (i.e. without following symlinks). See `lexicallyNormalize`
- [lexicallyResolving(_:)](<filepath/lexicallyresolving(__).md>) — Create a new `FilePath` by resolving `subpath` relative to `self`, ensuring that the result is lexically contained within `self`.
- [push(_:)](<filepath/push(__).md>) — If `other` does not have a root, append each component of `other`. If `other` has a root, replaces `self` with other.
- [pushing(_:)](<filepath/pushing(__).md>) — Non-mutating version of `push()`.
- [removeAll(keepingCapacity:)](<filepath/removeall(keepingcapacity_).md>) — Remove the contents of the path, keeping the null terminator.
- [removeLastComponent()](<filepath/removelastcomponent().md>) — In-place mutating variant of `removingLastComponent`.
- [removePrefix(_:)](<filepath/removeprefix(__).md>) — If `prefix` is a prefix of `self`, removes it and returns `true`. Otherwise returns `false`.
- [removingLastComponent()](<filepath/removinglastcomponent().md>) — Creates a new path with everything up to but not including `lastComponent`.
- [removingRoot()](<filepath/removingroot().md>) — Creates a new path containing just the components, i.e. everything after `root`.
- [reserveCapacity(_:)](<filepath/reservecapacity(__).md>) — Reserve enough storage space to store `minimumCapacity` platform characters.
- [starts(with:)](<filepath/starts(with_).md>) — Returns whether `other` is a prefix of `self`, only considering whole path components.
- [stat(flags:retryOnInterrupt:)](<filepath/stat(flags_retryoninterrupt_).md>) — Creates a `Stat` struct for the file referenced by this `FilePath` using the given `Flags`. _(beta)_
- [stat(followTargetSymlink:retryOnInterrupt:)](<filepath/stat(followtargetsymlink_retryoninterrupt_).md>) — Creates a `Stat` struct for the file referenced by this `FilePath`. _(beta)_
- [stat(relativeTo:flags:retryOnInterrupt:)](<filepath/stat(relativeto_flags_retryoninterrupt_).md>) — Creates a `Stat` struct for the file referenced by this `FilePath` using the given `Flags`, including a `FileDescriptor` to resolve a relative path. _(beta)_
- [withPlatformString(_:)](<filepath/withplatformstring(__).md>) — Calls the given closure with a pointer to the contents of the file path, represented as a null-terminated platform string.

### Default Implementations

- [CustomDebugStringConvertible Implementations](filepath/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](filepath/customstringconvertible-implementations.md)
- [ExpressibleByStringLiteral Implementations](filepath/expressiblebystringliteral-implementations.md)

## See Also

### Files

- [FileDescriptor](filedescriptor.md) — An abstract handle to an input or output data resource, such as a file or a socket.
- [FilePermissions](filepermissions.md) — The access permissions for a file.
