---
title: 'init(objectSpecifier:comparisonOperator:test:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspecifiertest/init(objectspecifier:comparisonoperator:test:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspecifiertest/init(objectspecifier:comparisonoperator:test:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspecifiertest/init%28objectspecifier%3Acomparisonoperator%3Atest%3A%29.json'
content_hash: 'sha256:5a1acb2e3c16076c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpecifierTest](../nsspecifiertest.md)

# init(objectSpecifier:comparisonOperator:test:)

<sub>Initializer</sub>

Returns a specifier test initialized to evaluate a test object against an object specified by an object specifier using a given comparison operation.

<sub>Mac Catalyst, macOS</sub>

```swift
init(objectSpecifier obj1: NSScriptObjectSpecifier?, comparisonOperator compOp: NSSpecifierTest.TestComparisonOperation, test obj2: Any?)
```

## Parameters

- `obj1` — An object specifier.

- `compOp` — The comparison operation.

- `obj2` — The object against which to evaluate the object specified by `obj1`.

## Return Value

A specifier test initialized to evaluate (`obj2`) against an object specified by `obj1` using the comparison operation `compOp`.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
