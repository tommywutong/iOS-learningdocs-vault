---
title: 'init(forKeyPath:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(forkeypath:)-98by'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(forkeypath:)-98by'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28forkeypath%3A%29-98by.json'
content_hash: 'sha256:948841ee648165bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(forKeyPath:)

<sub>Initializer</sub>

Creates an expression using a key path you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init<Root, Value>(forKeyPath keyPath: KeyPath<Root, Value>)
```

## Parameters

- `keyPath` — The key path that the new expression evaluates.

## See Also

### Creating an Expression for a Value

- [+ expressionForConstantValue:](<init(forconstantvalue_).md>) — Creates an expression that represents a specified constant value.
- [+ expressionForEvaluatedObject](<expressionforevaluatedobject().md>) — Creates an expression that represents the object you’re evaluating.
- [+ expressionForKeyPath:](<init(forkeypath_)-1aqf5.md>) — Creates an expression that invokes the value function with a specified key path.
- [+ expressionForVariable:](<init(forvariable_).md>) — Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [+ expressionForAnyKey](<expressionforanykey().md>) — Creates an expression that represents any key for a Spotlight query.
