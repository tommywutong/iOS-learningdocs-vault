---
title: 'init(forKeyPath:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsexpression/init(forkeypath:)-1aqf5'
source_url: 'https://developer.apple.com/documentation/foundation/nsexpression/init(forkeypath:)-1aqf5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsexpression/init%28forkeypath%3A%29-1aqf5.json'
content_hash: 'sha256:697491ed185aaa2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSExpression](../nsexpression.md)

# init(forKeyPath:)

<sub>Initializer</sub>

Creates an expression that invokes the value function with a specified key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(forKeyPath keyPath: String)
```

## Parameters

- `keyPath` — The key path that the new expression should evaluate.

## Return Value

A new expression that invokes [value(forKeyPath:)](<../../objectivec/nsobject-swift.class/value(forkeypath_).md>) with `keyPath`.

## See Also

### Creating an Expression for a Value

- [+ expressionForConstantValue:](<init(forconstantvalue_).md>) — Creates an expression that represents a specified constant value.
- [+ expressionForEvaluatedObject](<expressionforevaluatedobject().md>) — Creates an expression that represents the object you’re evaluating.
- [+ expressionForVariable:](<init(forvariable_).md>) — Creates an expression that extracts a value from the variable bindings dictionary for a specified key.
- [init(forKeyPath:)](<init(forkeypath_)-98by.md>) — Creates an expression using a key path you specify.
- [+ expressionForAnyKey](<expressionforanykey().md>) — Creates an expression that represents any key for a Spotlight query.
