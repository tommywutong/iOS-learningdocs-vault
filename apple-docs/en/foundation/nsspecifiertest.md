---
title: NSSpecifierTest
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsspecifiertest
source_url: 'https://developer.apple.com/documentation/foundation/nsspecifiertest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspecifiertest.json'
content_hash: 'sha256:03dc712c11a9f4d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSpecifierTest

<sub>Class</sub>

A comparison between an object specifier and a test object.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSSpecifierTest
```

## Overview

Instances of this class represent a Boolean expression; they evaluate an object specifier and compare the resulting object to another object using a given comparison method. For more information on `NSSpecifierTest`, see the method description for its sole public method, its initializer, [- initWithObjectSpecifier:comparisonOperator:testObject:](<nsspecifiertest/init(objectspecifier_comparisonoperator_test_).md>).

When an `NSSpecifierTest` object is properly initialized, it holds two objects:

- A “value” or “test” object used as the basis of the comparison; this object can be a regular object or object specifier (such as “blue” in “words whose color is blue”).
- An object specifier evaluating to the container (“words”).

The instance also encapsulates a selector identifying the method performing this comparison. The informal protocol [NSComparisonMethods](nscomparisonmethods.md) defines a set of comparison methods useful for this purpose, while [NSScriptingComparisonMethods](../objectivec/nsscriptingcomparisonmethods.md) describes additional methods you may need to use for scripting.

The test object is compared, using the selector, against each object in the container. Specifiers in these tests usually have [containerIsObjectBeingTested](nsscriptobjectspecifier/containerisobjectbeingtested.md) invoked on their topmost container.

You should rarely need to subclass `NSSpecifierTest`.

## Relationships

- **Inherits From**: [NSScriptWhoseTest](nsscriptwhosetest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a specifier test

- [- initWithObjectSpecifier:comparisonOperator:testObject:](<nsspecifiertest/init(objectspecifier_comparisonoperator_test_).md>) — Returns a specifier test initialized to evaluate a test object against an object specified by an object specifier using a given comparison operation.

### Constants

- [TestComparisonOperation](nsspecifiertest/testcomparisonoperation.md) — These are passed to  [- initWithObjectSpecifier:comparisonOperator:testObject:](<nsspecifiertest/init(objectspecifier_comparisonoperator_test_).md>) to specify the comparison operator.

### Initializers

- [- initWithCoder:](<nsspecifiertest/init(coder_).md>)
- [init(objectSpecifier:comparisonOperator:testObject:)](<nsspecifiertest/init(objectspecifier_comparisonoperator_testobject_).md>)

## See Also

### Object Matching Tests

- [NSScriptWhoseTest](nsscriptwhosetest.md) — An abstract class that provides the basis for testing specifiers one at a time or in groups.
- [NSLogicalTest](nslogicaltest.md) — The logical combination of one or more specifier tests.
