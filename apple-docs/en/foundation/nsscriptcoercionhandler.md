---
title: NSScriptCoercionHandler
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcoercionhandler
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcoercionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcoercionhandler.json'
content_hash: 'sha256:414e343138cbb863'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSScriptCoercionHandler

<sub>Class</sub>

A mechanism for converting one kind of scripting data to another.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSScriptCoercionHandler
```

## Overview

A shared instance of this class coerces (converts) object values to objects of another class using information supplied by classes that register with it. Coercions frequently are required during key-value coding.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Accessing the application’s handler

- [+ sharedCoercionHandler](<nsscriptcoercionhandler/shared().md>) — Returns the shared `NSScriptCoercionHandler` for the application.

### Working with handlers

- [- coerceValue:toClass:](<nsscriptcoercionhandler/coercevalue(__to_).md>) — Returns an object of a given class representing a given value.
- [- registerCoercer:selector:toConvertFromClass:toClass:](<nsscriptcoercionhandler/registercoercer(__selector_toconvertfrom_to_).md>) — Registers a given object (typically a class) to handle coercions (conversions) from one given class to another.

## See Also

### NSObject Script Support

- [NSComparisonMethods](nscomparisonmethods.md) — A collection of default comparison methods useful for performing specifier tests.
- [NSScriptingComparisonMethods](../objectivec/nsscriptingcomparisonmethods.md) — A collection of methods useful for comparing script objects.
- [NSScriptKeyValueCoding](../objectivec/nsscriptkeyvaluecoding.md) — A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptObjectSpecifiers](nsscriptobjectspecifiers.md) — A collection of methods providing additional object specifier functionality.
- [NSScriptExecutionContext](nsscriptexecutioncontext.md) — The context in which the current script command is executed.
