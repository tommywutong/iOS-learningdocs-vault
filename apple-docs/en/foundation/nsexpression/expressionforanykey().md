---
title: expressionForAnyKey()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsexpression/expressionforanykey()
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/expressionforanykey()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/expressionforanykey%28%29.json'
content_hash: 'sha256:bafd1e80203a3fd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# expressionForAnyKey()

<sub>Type Method</sub>

Creates an expression that represents any key for a Spotlight query.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func expressionForAnyKey() -> NSExpression
```

## Return Value

A new expression that represents any key for a Spotlight query.

## See Also

### Creating an Expression for a Value

- [+ expressionForConstantValue:](<init(forconstantvalue_).md>) — Creates an expression that represents a specified constant value.
- [+ expressionForEvaluatedObject](<expressionforevaluatedobject().md>) — Creates an expression that represents the object you’re evaluating.
- [+ expressionForKeyPath:](<init(forkeypath_)-1aqf5.md>) — Creates an expression that invokes the value function with a specified key path.
- [+ expressionForVariable:](<init(forvariable_).md>) — Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [init(forKeyPath:)](<init(forkeypath_)-98by.md>) — Creates an expression using a key path you specify.
