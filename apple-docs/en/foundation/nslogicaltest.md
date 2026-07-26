---
title: NSLogicalTest
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslogicaltest
source_url: 'https://developer.apple.com/documentation/foundation/nslogicaltest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslogicaltest.json'
content_hash: 'sha256:c8860521adfe480b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLogicalTest

<sub>Class</sub>

The logical combination of one or more specifier tests.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSLogicalTest
```

## Overview

Instances of this class perform logical operations of `AND`, `OR`, and `NOT` on Boolean expressions represented by [NSSpecifierTest](nsspecifiertest.md) objects. These operators are equivalent to “`&&`”, “`||`”, and “`!`” in the C language.

For `AND` and `OR` operations, an `NSLogicalTest` object is typically initialized with an array containing two or more [NSSpecifierTest](nsspecifiertest.md) objects. [- isTrue](<nsscriptwhosetest/istrue().md>)—inherited from [NSScriptWhoseTest](nsscriptwhosetest.md)—evaluates the array in a manner appropriate to the logical operation. For `NOT` operations, an `NSLogicalTest` object is initialized with only one `NSSpecifierTest` object; it simply reverses the Boolean outcome of the [- isTrue](<nsscriptwhosetest/istrue().md>) method.

You don’t normally subclass `NSLogicalTest`.

## Relationships

- **Inherits From**: [NSScriptWhoseTest](nsscriptwhosetest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing a logical test

- [- initAndTestWithTests:](<nslogicaltest/init(andtestwith_).md>) — Returns an `NSLogicalTest` object initialized to perform an `AND` operation with the `NSSpecifierTest` objects in a given array.
- [- initNotTestWithTest:](<nslogicaltest/init(nottestwith_).md>) — Returns an `NSLogicalTest` object initialized to perform a `NOT` operation on the given `NSScriptWhoseTest` object.
- [- initOrTestWithTests:](<nslogicaltest/init(ortestwith_).md>) — Returns an `NSLogicalTest` object initialized to perform an `OR` operation with the `NSSpecifierTest` objects in a given array.

### Initializers

- [init(andTestWithTests:)](<nslogicaltest/init(andtestwithtests_).md>)
- [init(notTestWithTest:)](<nslogicaltest/init(nottestwithtest_).md>)
- [init(orTestWithTests:)](<nslogicaltest/init(ortestwithtests_).md>)

## See Also

### Object Matching Tests

- [NSScriptWhoseTest](nsscriptwhosetest.md) — An abstract class that provides the basis for testing specifiers one at a time or in groups.
- [NSSpecifierTest](nsspecifiertest.md) — A comparison between an object specifier and a test object.
