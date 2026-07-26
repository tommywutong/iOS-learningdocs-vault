---
title: Observable()
framework: Observation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/observation/observable()
source_url: 'https://developer.apple.com/documentation/observation/observable()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observable%28%29.json'
content_hash: 'sha256:3761ced1df395d8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Observation](../observation.md)

# Observable()

<sub>Macro</sub>

Defines and implements conformance of the Observable protocol.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@attached(member, names: named(_$observationRegistrar), named(access), named(withMutation), named(shouldNotifyObservers)) @attached(memberAttribute) @attached(extension, conformances: Observable) macro Observable()
```

## Overview

This macro adds observation support to a custom type and conforms the type to the [Observable](observable.md) protocol. For example, the following code applies the `Observable` macro to the type `Car` making it observable:

```swift
@Observable 
class Car {
   var name: String = ""
   var needsRepairs: Bool = false

   init(name: String, needsRepairs: Bool = false) {
       self.name = name
       self.needsRepairs = needsRepairs
   }
}
```

## See Also

### Observable conformance

- [Observable](observable.md) — A type that emits notifications to observers when underlying data changes.
