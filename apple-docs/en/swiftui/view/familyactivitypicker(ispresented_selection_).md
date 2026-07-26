---
title: 'familyActivityPicker(isPresented:selection:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/familyactivitypicker(ispresented:selection:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/familyactivitypicker(ispresented:selection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/familyactivitypicker%28ispresented%3Aselection%3A%29.json'
content_hash: 'sha256:7d8ca3e89c15bafd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# familyActivityPicker(isPresented:selection:)

<sub>Instance Method</sub>

Presents an activity picker view as a sheet.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View

```

## Parameters

- `isPresented` — A binding that indicates whether the app presents the picker view.

- `selection` — A binding that manages the user-selected categories, apps, and web domains.

## Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker`.

```swift
struct ExampleView: View {
    @State var selection = FamilyActivitySelection()
    @State var isPresented = false

   var body: some View {
       Button("Present FamilyActivityPicker") { isPresented = true }
       .familyActivityPicker(isPresented: $isPresented,
                             selection: $selection)
       .onChange(of: selection) { newSelection in
           let applications = selection.applications
           let categories = selection.categories
           let webDomains = selection.webDomains
       }
   }
}
```

## See Also

### Configuring Family Sharing

- [FamilyActivityPicker](../../familycontrols/familyactivitypicker.md) — A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [familyActivityPicker(headerText:footerText:isPresented:selection:)](<familyactivitypicker(headertext_footertext_ispresented_selection_).md>) — Presents an activity picker view as a sheet.
- [familyActivityPicker(title:headerText:footerText:isPresented:selection:)](<familyactivitypicker(title_headertext_footertext_ispresented_selection_).md>) — Present an activity picker sheet for selecting apps and websites to manage.
