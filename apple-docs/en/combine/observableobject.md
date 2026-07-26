---
title: ObservableObject
framework: Combine
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/observableobject
source_url: 'https://developer.apple.com/documentation/combine/observableobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/observableobject.json'
content_hash: 'sha256:6a10049ea1826b3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Combine](../combine.md)

# ObservableObject

<sub>Protocol</sub>

A type of object with a publisher that emits before the object has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ObservableObject : AnyObject
```

## Overview

By default an [ObservableObject](observableobject.md) synthesizes an [objectWillChange](observableobject/objectwillchange.md) publisher that emits the changed value before any of its `@Published` properties changes.

```swift
class Contact: ObservableObject {
    @Published var name: String
    @Published var age: Int

    init(name: String, age: Int) {
        self.name = name
        self.age = age
    }

    func haveBirthday() -> Int {
        age += 1
        return age
    }
}

let john = Contact(name: "John Appleseed", age: 24)
cancellable = john.objectWillChange
    .sink { _ in
        print("\(john.age) will change")
}
print(john.haveBirthday())
// Prints "24 will change"
// Prints "25"
```

## Topics

### Publishing changes

- [objectWillChange](observableobject/objectwillchange.md) — A publisher that emits before the object has changed.
- [ObjectWillChangePublisher](observableobject/objectwillchangepublisher.md) — The type of publisher that emits before the object has changed.

## See Also

### Observable Objects

- [ObservableObjectPublisher](observableobjectpublisher.md) — A publisher that publishes changes from observable objects.
