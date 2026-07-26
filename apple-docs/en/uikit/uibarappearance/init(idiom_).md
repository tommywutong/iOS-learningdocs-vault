---
title: 'init(idiom:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibarappearance/init(idiom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibarappearance/init(idiom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarappearance/init%28idiom%3A%29.json'
content_hash: 'sha256:5143c08d484a18e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarAppearance](../uibarappearance.md)

# init(idiom:)

<sub>Initializer</sub>

Creates a new bar appearance object that targets the specified idiom.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(idiom: UIUserInterfaceIdiom)
```

## Parameters

- `idiom` — The device idiom to target. If you specify an idiom that doesn’t make sense for the current device, this method adjusts the idiom to an appropriate value.

## Return Value

A new bar appearance object containing default values for the specified idiom.

## See Also

### Creating a custom bar appearance object

- [- initWithBarAppearance:](<init(barappearance_).md>) — Creates a new bar appearance object by copying relevant data from the specified appearance object.
- [- init](<init().md>) — Creates a new bar appearance object containing default values.
- [- initWithCoder:](<init(coder_).md>) — Creates an appearance object from data in an unarchiver.
