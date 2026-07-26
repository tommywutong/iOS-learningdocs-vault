---
title: PredicateExpressions.StringContainsRegex
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicateexpressions/stringcontainsregex
source_url: 'https://developer.apple.com/documentation/foundation/predicateexpressions/stringcontainsregex'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicateexpressions/stringcontainsregex.json'
content_hash: 'sha256:4ba7fae5539011ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateExpressions](../predicateexpressions.md)

# PredicateExpressions.StringContainsRegex

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StringContainsRegex<Subject, Regex> where Subject : PredicateExpression, Regex : PredicateExpression, Subject.Output : BidirectionalCollection, Regex.Output : RegexComponent, Subject.Output.SubSequence == Substring
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Escapable](../../swift/escapable.md), [PredicateExpression](../predicateexpression.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [StandardPredicateExpression](../standardpredicateexpression.md)

## Topics

### Initializers

- [init(subject:regex:)](<stringcontainsregex/init(subject_regex_).md>)

### Instance Properties

- [regex](stringcontainsregex/regex.md)
- [subject](stringcontainsregex/subject.md)
