---
title: expressionForEvaluatedObject()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression/expressionforevaluatedobject()
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/expressionforevaluatedobject()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/expressionforevaluatedobject%28%29.json'
content_hash: 'sha256:a67af5b79da73378'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# expressionForEvaluatedObject()

<sub>Type Method</sub>

Creates an expression that represents the object you’re evaluating.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func expressionForEvaluatedObject() -> NSExpression
```

## Return Value

A new expression that represents the object being evaluated.

## See Also

### Creating an Expression for a Value

- [+ expressionForConstantValue:](<init(forconstantvalue_).md>) — Creates an expression that represents a specified constant value.
- [+ expressionForKeyPath:](<init(forkeypath_)-1aqf5.md>) — Creates an expression that invokes the value function with a specified key path.
- [+ expressionForVariable:](<init(forvariable_).md>) — Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [init(forKeyPath:)](<init(forkeypath_)-98by.md>) — Creates an expression using a key path you specify.
- [+ expressionForAnyKey](<expressionforanykey().md>) — Creates an expression that represents any key for a Spotlight query.
