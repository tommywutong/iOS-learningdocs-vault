---
title: PredicateCodableConfiguration
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/predicatecodableconfiguration
source_url: 'https://developer.apple.com/documentation/foundation/predicatecodableconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicatecodableconfiguration.json'
content_hash: 'sha256:5b8d848d63c1a917'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PredicateCodableConfiguration

<sub>Structure</sub>

A specification of the expected types and key paths found in an archived predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PredicateCodableConfiguration
```

## Overview

Use this configuration when encoding and decoding a predicate to restrict what that predicate can contain.  If a predicate contains data types or keypaths that aren’t allowed by the configuration, the encoding or decoding process throws an error.

```swift
var configuration = PredicateCodableConfiguration.standardConfiguration
configuration.allowType(Message.self, identifier: "MyApp.Message")
configuration.allowType(Person.self, identifier: "MyApp.Person")
configuration.allowKeyPath(\Message.sender, identifier: "MyApp.Message.sender")
configuration.allowKeyPath(\Person.firstName, identifier: "MyApp.Person.firstName")
configuration.allowKeyPath(\Person.lastName, identifier: "MyApp.Person.lastName")

struct MyRequest: Codable {
    let predicate: Predicate<Message>
    
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)
        try container.encode(predicate, forKey: .predicate, configuration: configuration)
    }
    
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)
        predicate = try container.decode(Predicate<Message>.self, forKey: .predicate, configuration: configuration)
    }
}
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a configuration

- [init()](<predicatecodableconfiguration/init().md>)
- [standardConfiguration](predicatecodableconfiguration/standardconfiguration.md)

### Allowing types and key paths

- [allow(_:)](<predicatecodableconfiguration/allow(__).md>)
- [allowKeyPathsForPropertiesProvided(by:recursive:)](<predicatecodableconfiguration/allowkeypathsforpropertiesprovided(by_recursive_).md>)
- [allowPartialType(_:identifier:)](<predicatecodableconfiguration/allowpartialtype(__identifier_).md>)
- [allowType(_:identifier:)](<predicatecodableconfiguration/allowtype(__identifier_).md>)

### Disallowing types and key paths

- [disallowKeyPathsForPropertiesProvided(by:recursive:)](<predicatecodableconfiguration/disallowkeypathsforpropertiesprovided(by_recursive_).md>)
- [disallowPartialType(_:)](<predicatecodableconfiguration/disallowpartialtype(__).md>)
- [disallowType(_:)](<predicatecodableconfiguration/disallowtype(__).md>)

### Instance Methods

- [allowKeyPath(_:identifier:)](<predicatecodableconfiguration/allowkeypath(__identifier_).md>)
- [disallowKeyPath(_:)](<predicatecodableconfiguration/disallowkeypath(__).md>)

## See Also

### Filltering

- [Predicate](predicate.md) — A logical condition used to test a set of input values for searching or filtering.
- [PredicateError](predicateerror.md) — An error thrown while evaluating a predicate.
- [PredicateCodableKeyPathProviding](predicatecodablekeypathproviding.md) — A type that provides the expected key paths found in an archived predicate.
- [PredicateExpression](predicateexpression.md) — A component expression that makes up part of a predicate.
- [StandardPredicateExpression](standardpredicateexpression.md) — A component expression that makes up part of a predicate, and that’s supported by the standard predicate type.
- [PredicateExpressions](predicateexpressions.md) — The expressions that make up a predicate.
- [PredicateBindings](predicatebindings.md) — A mapping from a predicates’s input variables to their values.
- [NSPredicate](nspredicate.md) — A definition of logical conditions for constraining a search for a fetch or for in-memory filtering.
- [NSExpression](nsexpression.md) — An expression for use in a comparison predicate.
- [NSComparisonPredicate](nscomparisonpredicate.md) — A specialized predicate for comparing expressions.
- [NSCompoundPredicate](nscompoundpredicate.md) — A specialized predicate that evaluates logical combinations of other predicates.
