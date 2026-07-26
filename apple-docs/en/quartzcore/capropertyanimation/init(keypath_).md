---
title: 'init(keyPath:)'
framework: Core Animation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/capropertyanimation/init(keypath:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/capropertyanimation/init(keypath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/capropertyanimation/init%28keypath%3A%29.json'
content_hash: 'sha256:6412fe161ce9dd2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAPropertyAnimation](../capropertyanimation.md)

# init(keyPath:)

<sub>Initializer</sub>

Creates and returns an `CAPropertyAnimation` instance for the specified key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(keyPath path: String?)
```

## Parameters

- `path` — The key path of the property to be animated.

## Return Value

A new instance of `CAPropertyAnimation` with the key path set to `keyPath`.
