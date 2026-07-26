---
title: NSScriptWhoseTest
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptwhosetest
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptwhosetest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptwhosetest.json'
content_hash: 'sha256:1ab77ecde223f174'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSScriptWhoseTest

<sub>Class</sub>

An abstract class that provides the basis for testing specifiers one at a time or in groups.

<sub>Mac Catalyst, macOS</sub>

```swift
class NSScriptWhoseTest
```

## Overview

`NSScriptWhoseTest` is an abstract class whose sole method is [- isTrue](<nsscriptwhosetest/istrue().md>). Two concrete subclasses of `NSScriptWhoseTest` generate objects representing Boolean expressions comparing one object with another and objects representing multiple Boolean expressions connected by logical operators (`OR`, `AND`, `NOT`). These classes are, respectively, [NSSpecifierTest](nsspecifiertest.md) and [NSLogicalTest](nslogicaltest.md). In evaluating itself, an [NSWhoseSpecifier](nswhosespecifier.md) invokes the [- isTrue](<nsscriptwhosetest/istrue().md>) method of its “test” object.

You shouldn’t need to subclass `NSScriptWhoseTest`, and you should rarely need to subclass one of its subclasses.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [NSLogicalTest](nslogicaltest.md), [NSSpecifierTest](nsspecifiertest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Evaluating a test

- [- isTrue](<nsscriptwhosetest/istrue().md>) — Returns a Boolean value that indicates whether the test represented by the receiver evaluates to true.

### Initializers

- [- init](<nsscriptwhosetest/init().md>)
- [- initWithCoder:](<nsscriptwhosetest/init(coder_).md>)

## See Also

### Object Matching Tests

- [NSSpecifierTest](nsspecifiertest.md) — A comparison between an object specifier and a test object.
- [NSLogicalTest](nslogicaltest.md) — The logical combination of one or more specifier tests.
