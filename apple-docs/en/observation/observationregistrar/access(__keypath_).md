---
title: 'access(_:keyPath:)'
framework: Observation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/observation/observationregistrar/access(_:keypath:)'
source_url: 'https://developer.apple.com/documentation/observation/observationregistrar/access(_:keypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observationregistrar/access%28_%3Akeypath%3A%29.json'
content_hash: 'sha256:4c2a2a15826dfedd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Observation](../../observation.md) · [ObservationRegistrar](../observationregistrar.md)

# access(_:keyPath:)

<sub>Instance Method</sub>

Registers access to a specific property for observation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func access<Subject, Member>(_ subject: Subject, keyPath: KeyPath<Subject, Member>) where Subject : Observable
```

## Parameters

- `subject` — An instance of an observable type.

- `keyPath` — The key path of an observed property.

## See Also

### Identifying transactional access

- [withMutation(of:keyPath:_:)](<withmutation(of_keypath___).md>) — Identifies mutations to the transactions registered for observers.
