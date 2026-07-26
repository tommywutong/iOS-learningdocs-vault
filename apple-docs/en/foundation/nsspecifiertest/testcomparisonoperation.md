---
title: NSSpecifierTest.TestComparisonOperation
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsspecifiertest/testcomparisonoperation
source_url: 'https://developer.apple.com/documentation/foundation/nsspecifiertest/testcomparisonoperation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspecifiertest/testcomparisonoperation.json'
content_hash: 'sha256:8bea8300a703bb46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpecifierTest](../nsspecifiertest.md)

# NSSpecifierTest.TestComparisonOperation

<sub>Enumeration</sub>

These are passed to  [- initWithObjectSpecifier:comparisonOperator:testObject:](<init(objectspecifier_comparisonoperator_test_).md>) to specify the comparison operator.

<sub>Mac Catalyst, macOS</sub>

```swift
enum TestComparisonOperation
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [NSEqualToComparison](testcomparisonoperation/equal.md) — Binary comparison operator that results in true if the two objects are equal.
- [NSLessThanOrEqualToComparison](testcomparisonoperation/lessthanorequal.md) — Binary comparison operator that results in true if the value of the test object is equal to or less than the value of the other object.
- [NSLessThanComparison](testcomparisonoperation/lessthan.md) — Binary comparison operator that results in true if the value of the test object is less than the value of the other object.
- [NSGreaterThanOrEqualToComparison](testcomparisonoperation/greaterthanorequal.md) — Binary comparison operator that results in true if the value of the test object is greater than or equal to the value of the other object.
- [NSGreaterThanComparison](testcomparisonoperation/greaterthan.md) — Binary comparison operator that results in true if the value of the test object is greater than the value of the other object.
- [NSBeginsWithComparison](testcomparisonoperation/beginswith.md) — Binary containment operator that results in true if the test object is a list or string that matches the beginning of the other object (which is also a list or string).
- [NSEndsWithComparison](testcomparisonoperation/endswith.md) — Binary containment operator that results in true if the test object is a list or string that matches the end of the other object (which is also a list or string).
- [NSContainsComparison](testcomparisonoperation/contains.md) — Binary containment operator that results in true if the test object is a list or string that matches the other object (which is also a list or string) at any location.

### Initializers

- [init(rawValue:)](<testcomparisonoperation/init(rawvalue_).md>)
