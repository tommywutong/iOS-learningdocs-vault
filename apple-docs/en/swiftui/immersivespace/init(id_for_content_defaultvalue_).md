---
title: 'init(id:for:content:defaultValue:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/immersivespace/init(id:for:content:defaultvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/immersivespace/init(id:for:content:defaultvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/immersivespace/init%28id%3Afor%3Acontent%3Adefaultvalue%3A%29.json'
content_hash: 'sha256:7462da2cbde1c7be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ImmersiveSpace](../immersivespace.md)

# init(id:for:content:defaultValue:)

<sub>Initializer</sub>

Creates the immersive space associated with an identifier for a specified type of presented data, and a default value, if the data is not set.

<sub>visionOS</sub>

```swift
nonisolated init(id: String, for type: Data.Type = Data.self, @ImmersiveSpaceContentBuilder content: @escaping (Binding<Data>) -> Content, defaultValue: @escaping () -> Data)
```

## Parameters

- `id` — A string that uniquely identifies the immersive space. Ensure that identifiers are unique among the immersive spaces in your app.

- `type` — The type of presented data this immersive space accepts.

- `content` — An immersive space content builder that defines the content for each instance of the immersive space. The closure receives a binding to the value that you pass to the [openImmersiveSpace](../environmentvalues/openimmersivespace.md) action when you call that action to open an immersive space. The system automatically persists and restores the value of this binding during state restoration.

- `defaultValue` — A closure that returns a value that SwiftUI presents when it doesn’t receive one from you, like when you call the [openImmersiveSpace](../environmentvalues/openimmersivespace.md) action without providing a value.

## Discussion

The space uses the specified content builder to form the content. Your app invokes this initializer when it presents a value of the specified `type` using the [openImmersiveSpace](../environmentvalues/openimmersivespace.md) action.

## See Also

### Providing default data to an immersive space

- [init(for:content:defaultValue:)](<init(for_content_defaultvalue_).md>) — Creates an immersive space.
