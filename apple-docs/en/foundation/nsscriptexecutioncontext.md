---
title: NSScriptExecutionContext
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptexecutioncontext
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptexecutioncontext.json'
content_hash: 'sha256:1a7c70e3be0fd22a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSScriptExecutionContext

<sub>Class</sub>

The context in which the current script command is executed.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSScriptExecutionContext
```

## Overview

An `NSScriptExecutionContext` object is a shared instance (there is only one instance of the class) that represents the context in which the current script command is executed. `NSScriptExecutionContext` tracks global state relating to the command being executed, especially the top-level container object (that is, the container implied by a specifier object that specifies no container) used in an evaluation of an [NSScriptObjectSpecifier](nsscriptobjectspecifier.md) object.

In most cases, the top-level container for a complete series of nested object specifiers is automatically set to the application object (`NSApp`), and you can get this object with the [topLevelObject](nsscriptexecutioncontext/toplevelobject.md) method. But you can also set this top-level container to something else (using [topLevelObject](nsscriptexecutioncontext/toplevelobject.md)) if the situation warrants it.

It is unlikely that you will need to subclass `NSScriptExecutionContext`.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the current context

- [+ sharedScriptExecutionContext](<nsscriptexecutioncontext/shared().md>) — Returns the shared `NSScriptExecutionContext` instance.

### Getting and setting the container object

- [topLevelObject](nsscriptexecutioncontext/toplevelobject.md) — Sets the top-level object for an object-specifier evaluation.
- [objectBeingTested](nsscriptexecutioncontext/objectbeingtested.md) — Sets the top-level container object currently being tested in a “whose” qualifier to a given object.
- [rangeContainerObject](nsscriptexecutioncontext/rangecontainerobject.md) — Sets the top-level container object for a range-specifier evaluation to a give object.

## See Also

### NSObject Script Support

- [NSComparisonMethods](nscomparisonmethods.md) — A collection of default comparison methods useful for performing specifier tests.
- [NSScriptingComparisonMethods](../objectivec/nsscriptingcomparisonmethods.md) — A collection of methods useful for comparing script objects.
- [NSScriptKeyValueCoding](../objectivec/nsscriptkeyvaluecoding.md) — A collection of methods that provide additional capabilities for working with key-value coding.
- [NSScriptObjectSpecifiers](nsscriptobjectspecifiers.md) — A collection of methods providing additional object specifier functionality.
- [NSScriptCoercionHandler](nsscriptcoercionhandler.md) — A mechanism for converting one kind of scripting data to another.
