---
title: levelOfDetail
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/levelofdetail
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/levelofdetail'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/levelofdetail.json'
content_hash: 'sha256:df8648b2850d7579'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# levelOfDetail

<sub>Instance Property</sub>

The level of detail the view is recommended to have.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var levelOfDetail: LevelOfDetail { get set }
```

## Discussion

Read from the environment with

```swift
@Environment(\.levelOfDetail) var levelOfDetail
```

To customize your view based on recommended level of detail, read the environment value using the `.levelOfDetail` key and apply that to change your view.

```swift
var body: some View {
     switch levelOfDetail {
     case .default:
         VStack {
            NewsTitleView()
            NewsBodyView()
         }
     case .simplified:
         NewsImageOverview()
     }
}
```

> [!note] Note
> The levelOfDetail can be determined by different factors depending on the platforms.
