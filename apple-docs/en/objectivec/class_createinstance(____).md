---
title: 'class_createInstance(_:_:)'
framework: Objective-C Runtime
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/objectivec/class_createinstance(_:_:)'
source_url: 'https://developer.apple.com/documentation/objectivec/class_createinstance(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/objectivec/class_createinstance%28_%3A_%3A%29.json'
content_hash: 'sha256:5eee7bf5fc803677'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Objective-C Runtime](../objectivec.md)

# class_createInstance(_:_:)

<sub>Function</sub>

Creates an instance of a class, allocating memory for the class in the default malloc memory zone.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func class_createInstance(_ cls: AnyClass?, _ extraBytes: Int) -> Any?
```

## Parameters

- `cls` — The class that you want to allocate an instance of.

- `extraBytes` — An integer indicating the number of extra bytes to allocate. The additional bytes can be used to store additional instance variables beyond those defined in the class definition.

## Return Value

An instance of the class `cls`.
