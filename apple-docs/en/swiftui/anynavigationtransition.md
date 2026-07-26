---
title: AnyNavigationTransition
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/anynavigationtransition
source_url: 'https://developer.apple.com/documentation/swiftui/anynavigationtransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anynavigationtransition.json'
content_hash: 'sha256:d097555b3803a56a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# AnyNavigationTransition

<sub>Structure</sub>

A type-erasing navigation transition that allows for providing any navigation transition value dynamically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AnyNavigationTransition
```

## Overview

Use this navigation transition when you need to dynamically configure the transition of your content. For example, you could use this in a [sheet(isPresented:onDismiss:content:)](<view/sheet(ispresented_ondismiss_content_).md>) modifier to dynamically configure how the sheet transitions in and out.

This example shows a sheet that uses a different transition based on model state.

```swift
struct ContentView: View {
    @State private var showSheet = false
    @Environment(Model.self) var model

    var body: some View {
        VStack {
            Button("Show Sheet") {
                showSheet = true
            }
            .sheet(isPresented: $showSheet) {
                let transition = model.useCrossDissolve
                    ? AnyNavigationTransition(.crossFade)
                    : AnyNavigationTransition(.automatic)
                Text("Sheet Content")
                    .presentationDetents([.medium])
                    .navigationTransition(transition)
            }
        }
    }
}
```

## Relationships

- **Conforms To**: [NavigationTransition](navigationtransition.md)

## Topics

### Initializers

- [init(_:)](<anynavigationtransition/init(__).md>) _(beta)_

## See Also

### Defining navigation transitions

- [navigationTransition(_:)](<view/navigationtransition(__).md>) — Sets the navigation transition style for this view.
- [NavigationTransition](navigationtransition.md) — A type that defines the transition to use when navigating to a view.
- [CrossFadeNavigationTransition](crossfadenavigationtransition.md) — A navigation transition that cross-fades between the appearing view and the disappearing view. _(beta)_
