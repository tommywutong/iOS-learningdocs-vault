---
title: FamilyActivityPicker
framework: Family Controls
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/familycontrols/familyactivitypicker
source_url: 'https://developer.apple.com/documentation/familycontrols/familyactivitypicker'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/familycontrols/familyactivitypicker.json'
content_hash: 'sha256:b9fbd7a48dba1a8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Family Controls](../familycontrols.md)

# FamilyActivityPicker

<sub>Structure</sub>

A view in which users specify applications, web domains, and categories without revealing their choices to the app.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor @preconcurrency struct FamilyActivityPicker
```

## Overview

To prompt the user for their selection, create a binding to a [FamilyActivitySelection](familyactivityselection.md) instance, and use the binding to create a [FamilyActivityPicker](familyactivitypicker.md) instance. You can then display the picker like any SwiftUI view.

```swift
struct ExampleView: View {
    @State var selection = FamilyActivitySelection()

    var body: some View {
        VStack {
            Image(systemName: "eye")
                .font(.system(size: 76.0))
                .padding()

            FamilyActivityPicker(selection: $selection)

            Image(systemName: "hourglass")
                .font(.system(size: 76.0))
                .padding()
        }
        .onChange(of: selection) { newSelection in
            let applications = selection.applications
            let categories = selection.categories
            let webDomains = selection.webDomains
        }
    }
}
```

> [!note] Note
> A `FamilyActivityPicker` shown on a parent device only displays applications and websites from authorized child devices within the Family Sharing Group. A `FamilyActivityPicker` shown on an individually authorized device includes applications and websites from that same device.

To streamline this process, call  the [familyActivityPicker(isPresented:selection:)](<../swiftui/view/familyactivitypicker(ispresented_selection_).md>) modifier on a view in your user interface. This modifier displays the picker view as a sheet over your user interface when the `isPresented` binding is `true`.

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

When you present the `FamilyActivityPicker`, the system displays a view where the user can select categories, applications, and web domains. As soon as the user confirms their selection, the system updates the `FamilyActivitySelection` binding with the user’s selections. To protect the user’s privacy, the system uses opaque values to represent the selections.

Your app passes the selected values to the appropriate instances and methods from the [Managed Settings](../managedsettings.md) and [Device Activity](../deviceactivity.md) frameworks.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating activity pickers

- [init(selection:)](<familyactivitypicker/init(selection_).md>) — Creates a new activity picker.
- [init(headerText:footerText:selection:)](<familyactivitypicker/init(headertext_footertext_selection_).md>) — Creates a new activity picker with optional header and footer text.
- [familyActivityPicker(title:headerText:footerText:isPresented:selection:)](<../swiftui/view/familyactivitypicker(title_headertext_footertext_ispresented_selection_).md>) — Present an activity picker sheet for selecting apps and websites to manage.

### Accessing the content

- [body](familyactivitypicker/body.md) — The content of this view.

### Adding view modifiers

- [View Modifiers](familyactivitypicker-view-modifiers.md) — Apply standard modifiers to configure the family activity picker view and the views it contains.

## See Also

### Activity selections

- [FamilyActivitySelection](familyactivityselection.md) — A collection of applications, categories, and web domains selected by the user.
