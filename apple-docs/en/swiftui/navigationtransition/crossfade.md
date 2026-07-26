---
title: crossFade
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/navigationtransition/crossfade
source_url: 'https://developer.apple.com/documentation/swiftui/navigationtransition/crossfade'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationtransition/crossfade.json'
content_hash: 'sha256:6117bdaf2b354e38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [NavigationTransition](../navigationtransition.md)

# crossFade

<sub>Type Property</sub>

A navigation transition that cross-fades between the appearing view and the disappearing view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
static var crossFade: CrossFadeNavigationTransition { get }
```

## Discussion

Specify this transition in a sheet to have it appear by fading in over the content, as opposed to moving upwards to cover content.

This example shows a sheet that appears with a cross-fade.

```swift
struct ContentView: View {
    @State private var showSheet = false

    var body: some View {
        VStack {
            Button("Show Sheet") {
                showSheet = true
            }
            .sheet(isPresented: $showSheet) {
                Text("Sheet Content")
                    .presentationDetents([.medium])
                    .navigationTransition(.crossFade)
            }
        }
    }
}
```

## See Also

### Getting built-in transitions

- [automatic](automatic.md) — A style that automatically chooses the appropriate presentation transition for the current context.
- [AutomaticNavigationTransition](../automaticnavigationtransition.md) — A style that automatically chooses the appropriate presentation transition for the current context.
- [CrossFadeNavigationTransition](../crossfadenavigationtransition.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
- [zoom(sourceID:in:)](<zoom(sourceid_in_).md>) — A navigation transition that zooms the appearing view from a given source view.
- [ZoomNavigationTransition](../zoomnavigationtransition.md) — A navigation transition that zooms the appearing view from a given source view.
