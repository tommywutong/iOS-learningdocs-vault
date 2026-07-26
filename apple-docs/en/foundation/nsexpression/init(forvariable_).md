---
title: 'init(forVariable:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(forvariable:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(forvariable:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28forvariable%3A%29.json'
content_hash: 'sha256:93f64c9c84734d59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(forVariable:)

<sub>Initializer</sub>

Creates an expression that extracts a value from the variable bindings dictionary for a specified key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forVariable string: String)
```

## Parameters

- `string` — The key for the variable to extract from the variable bindings dictionary.

## Return Value

A new expression that extracts from the variable bindings dictionary the value for the key `string`.

## See Also

### Creating an Expression for a Value

- [+ expressionForConstantValue:](<init(forconstantvalue_).md>) — Creates an expression that represents a specified constant value.
- [+ expressionForEvaluatedObject](<expressionforevaluatedobject().md>) — Creates an expression that represents the object you’re evaluating.
- [+ expressionForKeyPath:](<init(forkeypath_)-1aqf5.md>) — Creates an expression that invokes the value function with a specified key path.
- [init(forKeyPath:)](<init(forkeypath_)-98by.md>) — Creates an expression using a key path you specify.
- [+ expressionForAnyKey](<expressionforanykey().md>) — Creates an expression that represents any key for a Spotlight query.
