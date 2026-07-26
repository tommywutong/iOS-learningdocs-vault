---
title: MTLLinkedFunctions
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtllinkedfunctions
source_url: 'https://developer.apple.com/documentation/metal/mtllinkedfunctions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtllinkedfunctions.json'
content_hash: 'sha256:aae1d98781c6090c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLLinkedFunctions

<sub>Class</sub>

A set of related functions that Metal links to when necessary to create the function instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLLinkedFunctions
```

## Overview

When you create a Metal function instance using an [MTLFunctionDescriptor](mtlfunctiondescriptor.md), you specify additional functions that Metal needs to link to when it compiles and links the underlying shader code. Most often, you need to do this if your shader takes a visible function table as one or more of its arguments. For Metal to create the [MTLFunction](mtlfunction.md) instance, it needs a complete list of functions that your shader can call so that it can resolve any dependencies and generate the correct code to run on the GPU.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying related functions

- [functions](mtllinkedfunctions/functions.md) — An array of function objects to link to the new function.
- [binaryFunctions](mtllinkedfunctions/binaryfunctions.md) — An array of function objects already compiled to a binary representation to link.
- [groups](mtllinkedfunctions/groups.md) — An optional list of groups specifying which functions your shader can call at each call site.
- [privateFunctions](mtllinkedfunctions/privatefunctions.md) — An array of function objects to link to the new function, without exporting the functions publicly.

## See Also

### Specifying the function configuration

- [name](mtlfunctiondescriptor/name.md) — The name of the function to fetch from the library.
- [specializedName](mtlfunctiondescriptor/specializedname.md) — A new name for the created function object.
- [constantValues](mtlfunctiondescriptor/constantvalues.md) — The set of constant values assigned to the function constants.
- [options](mtlfunctiondescriptor/options.md) — Flags specifying how Metal should create the new function object.
- [binaryArchives](mtlfunctiondescriptor/binaryarchives.md) — The binary archives to search for a previously-compiled version of this function.
- [MTLFunctionOptions](mtlfunctionoptions.md) — Options that define how Metal compiles a GPU function.
