---
title: 'init(_:destination:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/link/init(_:destination:)'
source_url: 'https://developer.apple.com/documentation/swiftui/link/init(_:destination:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/link/init%28_%3Adestination%3A%29.json'
content_hash: 'sha256:4d7757a997bd737b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Link](../link.md)

# init(_:destination:)

<sub>Initializer</sub>

Creates a control, consisting of a URL and a title resource, used to navigate to a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, destination: URL)
```

## Parameters

- `titleResource` — The localized title that describes the purpose of this link.

- `destination` — The URL for the link.

## Discussion

Use [Link](../link.md) to create a control that your app uses to navigate to a URL that you provide. The example below creates a link to `example.com` and uses `Visit Example Co` as the title key to generate a link-styled view in your app:

```swift
Link("Visit Example Co",
      destination: URL(string: "https://www.example.com/")!)
```

## See Also

### Creating a link

- [init(destination:label:)](<init(destination_label_).md>) — Creates a control, consisting of a URL and a label, used to navigate to the given URL.
