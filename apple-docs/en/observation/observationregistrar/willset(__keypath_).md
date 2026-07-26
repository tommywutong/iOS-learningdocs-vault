---
title: 'willSet(_:keyPath:)'
framework: Observation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/observation/observationregistrar/willset(_:keypath:)'
source_url: 'https://developer.apple.com/documentation/observation/observationregistrar/willset(_:keypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/observation/observationregistrar/willset%28_%3Akeypath%3A%29.json'
content_hash: 'sha256:80213135ae0a78a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Observation](../../observation.md) · [ObservationRegistrar](../observationregistrar.md)

# willSet(_:keyPath:)

<sub>Instance Method</sub>

A property observation called before setting the value of the subject.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willSet<Subject, Member>(_ subject: Subject, keyPath: KeyPath<Subject, Member>) where Subject : Observable
```

## Parameters

- `subject` — An instance of an observable type.

- `keyPath` — The key path of an observed property.

## See Also

### Receiving change notifications

- [didSet(_:keyPath:)](<didset(__keypath_).md>) — A property observation called after setting the value of the subject.
