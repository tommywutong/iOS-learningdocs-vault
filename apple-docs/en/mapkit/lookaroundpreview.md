---
title: LookAroundPreview
framework: MapKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/mapkit/lookaroundpreview
source_url: 'https://developer.apple.com/documentation/mapkit/lookaroundpreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/lookaroundpreview.json'
content_hash: 'sha256:f31561bfc6732079'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md)

# LookAroundPreview

<sub>Structure</sub>

A view that provides a Look Around preview for a specific geographic location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct LookAroundPreview
```

## Overview

Use a `LookAroundPreview` to create preview imagery for a specific geographic location on the map that you can place in your view. In the following example, a travel recommendations app displays and styles a stack of Look Around previews it generates from an array of `ItineraryItem` structures that contain the location’s title and Look Around scene:

```swift
    struct LookAroundPreviewsView: View {
        let itinerary: [ItineraryItem]
        var body: some View {
            ScrollView {
                LazyVStack {
                    ForEach(itinerary) { item in
                        LookAroundPreview(initialScene: item.lookAroundScene)
                            .frame(height: 128)
                            .overlay(alignment: .bottomTrailing) {
                                Text(item.title)
                                    .font(.caption)
                                    .foregroundColor(.white)
                                    .padding()
                            }
                    }
                }
            }
        }
    }
```

To display a Look Around viewer a person can explore, apply a `lookAroundViewer` view modifier to a specific view, then add a control the user interacts with to display the Look Around viewer. In the following example, the `lookAroundViewer` view modifier observes a binding to Boolean value to determine whether to display the Look Around viewer.

```swift
    var lookAroundScene: MKLookAroundScene?

    @State private var isLookingAround: Bool = false

    var body: some View {
        MyInterestingView()
            .lookAroundViewer(isPresented: $isLookingAround, initialScene: lookAroundScene)
            .toolbar {
                ToolbarItem {
                    Button(action: { lookingAround = true }) {
                        Image(systemName: "binoculars")
                }
            }
        }   
    }
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating a Look Around preview

- [init(initialScene:allowsNavigation:showsRoadLabels:pointsOfInterest:badgePosition:)](<lookaroundpreview/init(initialscene_allowsnavigation_showsroadlabels_pointsofinterest_badgeposition_).md>) — Creates a Look Around preview with an initial scene, navigation, road label, points of interest, and badge position you specify.
- [init(scene:allowsNavigation:showsRoadLabels:pointsOfInterest:badgePosition:)](<lookaroundpreview/init(scene_allowsnavigation_showsroadlabels_pointsofinterest_badgeposition_).md>) — Creates a Look Around preview with a binding to a scene, navigation, road label, points of interest, and badge position you specify.
