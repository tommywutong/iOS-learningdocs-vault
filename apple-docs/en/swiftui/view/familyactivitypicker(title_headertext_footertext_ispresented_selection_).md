---
title: 'familyActivityPicker(title:headerText:footerText:isPresented:selection:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.2+, iPadOS 26.2+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/familyactivitypicker(title:headertext:footertext:ispresented:selection:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/familyactivitypicker(title:headertext:footertext:ispresented:selection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/familyactivitypicker%28title%3Aheadertext%3Afootertext%3Aispresented%3Aselection%3A%29.json'
content_hash: 'sha256:3b1fa5dacf4402d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# familyActivityPicker(title:headerText:footerText:isPresented:selection:)

<sub>Instance Method</sub>

Present an activity picker sheet for selecting apps and websites to manage.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func familyActivityPicker(title: String?, headerText: String? = nil, footerText: String? = nil, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View

```

## Parameters

- `title` — An optional string that provides a title for the picker view.

- `headerText` — An optional string that provides text for the header of the picker view.

- `footerText` — An optional string that provides text for the footer of the picker view.

- `isPresented` — A binding that indicates whether the app presents the picker view.

- `selection` — A binding that manages the selected categories, apps, and web domains.

## Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker` with a custom title.

```swift
struct ContentView: View {
    @State private var selection = FamilyActivitySelection()
    @State private var isPresented = false

    var body: some View {
        Button("Select Activities") {
            isPresented = true
        }
        .familyActivityPicker(
            title: "Choose Apps to Limit",
            headerText: "Select apps and websites to manage",
            footerText: "These selections will be used for screen time limits",
            isPresented: $isPresented,
            selection: $selection
        )
        .onChange(of: selection) { newSelection in
            // Handle the selected activities
            print("Selected \(newSelection.applications.count) apps")
        }
    }
}
```

## See Also

### Configuring Family Sharing

- [FamilyActivityPicker](../../familycontrols/familyactivitypicker.md) — A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [familyActivityPicker(isPresented:selection:)](<familyactivitypicker(ispresented_selection_).md>) — Presents an activity picker view as a sheet.
- [familyActivityPicker(headerText:footerText:isPresented:selection:)](<familyactivitypicker(headertext_footertext_ispresented_selection_).md>) — Presents an activity picker view as a sheet.
