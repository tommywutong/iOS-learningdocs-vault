---
title: 'withMutation(of:keyPath:_:)'
framework: Observation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/observation/observationregistrar/withmutation(of:keypath:_:)'
source_url: 'https://developer.apple.com/documentation/observation/observationregistrar/withmutation(of:keypath:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observationregistrar/withmutation%28of%3Akeypath%3A_%3A%29.json'
content_hash: 'sha256:2fedd69101745e91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Observation](../../observation.md) · [ObservationRegistrar](../observationregistrar.md)

# withMutation(of:keyPath:_:)

<sub>Instance Method</sub>

Identifies mutations to the transactions registered for observers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func withMutation<Subject, Member, T>(of subject: Subject, keyPath: KeyPath<Subject, Member>, _ mutation: () throws -> T) rethrows -> T where Subject : Observable
```

## Parameters

- `subject` — An instance of an observable type.

- `keyPath` — The key path of an observed property.

## Discussion

This method calls [willSet(_:keyPath:)](<willset(__keypath_).md>) before the mutation. Then it calls [didSet(_:keyPath:)](<didset(__keypath_).md>) after the mutation.

## See Also

### Identifying transactional access

- [access(_:keyPath:)](<access(__keypath_).md>) — Registers access to a specific property for observation.
