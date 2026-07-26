---
title: 'familyActivityPicker(headerText:footerText:isPresented:selection:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/familyactivitypicker(headertext:footertext:ispresented:selection:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/familyactivitypicker(headertext:footertext:ispresented:selection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/familyactivitypicker%28headertext%3Afootertext%3Aispresented%3Aselection%3A%29.json'
content_hash: 'sha256:74c633b1edf83b17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# familyActivityPicker(headerText:footerText:isPresented:selection:)

<sub>Instance Method</sub>

Presents an activity picker view as a sheet.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency func familyActivityPicker(headerText: String? = nil, footerText: String? = nil, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View

```

## Parameters

- `headerText` — An optional string that provides text for the header of the picker view.

- `footerText` — An optional string that provides text for the footer of the picker view.

- `isPresented` — A binding that indicates whether the app presents the picker view.

- `selection` — A binding that manages the user-selected categories, apps, and web domains.

## Discussion

Use this view modifier to present a `FamilyControls/FamilyActivityPicker`.

## See Also

### Configuring Family Sharing

- [FamilyActivityPicker](../../familycontrols/familyactivitypicker.md) — A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [familyActivityPicker(isPresented:selection:)](<familyactivitypicker(ispresented_selection_).md>) — Presents an activity picker view as a sheet.
- [familyActivityPicker(title:headerText:footerText:isPresented:selection:)](<familyactivitypicker(title_headertext_footertext_ispresented_selection_).md>) — Present an activity picker sheet for selecting apps and websites to manage.
