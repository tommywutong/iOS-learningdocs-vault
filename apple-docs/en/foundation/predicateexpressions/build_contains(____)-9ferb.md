---
title: 'build_contains(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicateexpressions/build_contains(_:_:)-9ferb'
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/build_contains(_:_:)-9ferb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/build_contains%28_%3A_%3A%29-9ferb.json'
content_hash: 'sha256:777d3fd77af289e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# build_contains(_:_:)

<sub>Type Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func build_contains<Subject, Regex>(_ subject: Subject, _ regex: Regex) -> PredicateExpressions.StringContainsRegex<Subject, Regex> where Subject : PredicateExpression, Regex : PredicateExpression, Subject.Output : BidirectionalCollection, Regex.Output : RegexComponent, Subject.Output.SubSequence == Substring
```
