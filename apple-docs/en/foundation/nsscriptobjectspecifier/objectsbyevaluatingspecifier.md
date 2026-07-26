---
title: objectsByEvaluatingSpecifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptobjectspecifier/objectsbyevaluatingspecifier
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptobjectspecifier/objectsbyevaluatingspecifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptobjectspecifier/objectsbyevaluatingspecifier.json'
content_hash: 'sha256:1b673049cfad4495'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptObjectSpecifier](../nsscriptobjectspecifier.md)

# objectsByEvaluatingSpecifier

<sub>Instance Property</sub>

Returns the actual object represented by the nested series of object specifiers.

<sub>Mac Catalyst, macOS</sub>

```swift
var objectsByEvaluatingSpecifier: Any? { get }
```

## Return Value

The actual object represented by the nested series of object specifiers.

## Discussion

Recursively obtains the next container in a nested series of object specifiers until it reaches the top-level container specifier (which is either an [NSWhoseSpecifier](../nswhosespecifier.md) or the application object), after which it begins evaluating each object specifier ([- objectsByEvaluatingWithContainers:](<objectsbyevaluating(withcontainers_).md>)) going in the opposite direction (top-level to innermost) as it unwinds from the stack. Returns the actual object represented by the nested series of object specifiers. Returns `nil` if a container specifier could not be evaluated or if no top-level container specifier could be found. Thus `nil` can be a valid value or can indicate an error; you can use [evaluationErrorNumber](evaluationerrornumber.md) to determine if and which error occurred and [evaluationErrorSpecifier](evaluationerror.md) to find the container specifier responsible for the error. In the normal course of command processing, this method is invoked by an `NSScriptCommand` object’s [evaluatedArguments](../nsscriptcommand/evaluatedarguments.md) and [evaluatedReceivers](../nsscriptcommand/evaluatedreceivers.md) methods, which take as message receiver the innermost object specifier.

## See Also

### Evaluating an object specifier

- [- indicesOfObjectsByEvaluatingWithContainer:count:](<indicesofobjectsbyevaluating(withcontainer_count_).md>) — This primitive method must be overridden by subclasses to return a pointer to an array of indices identifying objects in the key of a given container that are identified by the receiver of the message.
- [- objectsByEvaluatingWithContainers:](<objectsbyevaluating(withcontainers_).md>) — Returns the actual object or objects specified by the receiver as evaluated in the context of given container object.
