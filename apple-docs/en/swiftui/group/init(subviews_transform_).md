---
title: 'init(subviews:transform:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/group/init(subviews:transform:)'
source_url: 'https://developer.apple.com/documentation/swiftui/group/init(subviews:transform:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/group/init%28subviews%3Atransform%3A%29.json'
content_hash: 'sha256:5c5d1f1643286c61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Group](../group.md)

# init(subviews:transform:)

<sub>Initializer</sub>

Constructs a group from the subviews of the given view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Base, Result>(subviews view: Base, @ContentBuilder transform: @escaping (SubviewsCollection) -> Result) where Content == GroupElementsOfContent<Base, Result>, Base : View, Result : View
```

## Parameters

- `view` — The view to get the subviews of.

- `transform` — A closure that constructs a view from the collection of subviews.

## Discussion

Use this initializer to create a group that gives you programmatic access to the group’s subviews. The following `CardsView` defines the group’s structure based on the set of views that you provide to it:

```swift
struct CardsView<Content: View>: View {
    var content: Content

    init(@ContentBuilder content: () -> Content) {
        self.content = content()
    }

    var body: some View {
        VStack {
            Group(subviews: content) { subviews in
                HStack {
                    if subviews.count >= 2 {
                        SecondaryCard { subview[1] }
                    }
                    if let first = subviews.first {
                        FeatureCard { first }
                    }
                    if subviews.count >= 3 {
                        SecondaryCard { subviews[2] }
                    }
                }
                if subviews.count > 3 {
                    subviews[3...]
                }
            }
        }
    }
}
```

You can use `CardsView` with its content builder-based initializer to arrange a collection of subviews:

```swift
CardsView {
    NavigationLink("What's New!") { WhatsNewView() }
    NavigationLink("Latest Hits") { LatestHitsView() }
    NavigationLink("Favorites") { FavoritesView() }
    NavigationLink("Playlists") { MyPlaylists() }
}
```

Subviews collection constructs subviews on demand, so only access the part of the collection you need to create the resulting content.

Subviews are proxies to the view they represent, which means that modifiers that you apply to the original view take effect before modifiers that you apply to the subview. SwiftUI resolves the view using the environment of its container rather than the environment of its subview proxy. Additionally, because subviews represent a single view or container, a subview might represent a view after the application of styles. As a result, applying a style to a subview might have no effect.

## See Also

### Creating a group

- [init(content:)](<init(content_).md>) — Creates a group of content.
- [init(sections:transform:)](<init(sections_transform_).md>) — Constructs a group from the sections of the given view.
