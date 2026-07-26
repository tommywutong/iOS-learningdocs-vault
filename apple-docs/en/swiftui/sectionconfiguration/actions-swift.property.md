---
title: actions
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sectionconfiguration/actions-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/sectionconfiguration/actions-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sectionconfiguration/actions-swift.property.json'
content_hash: 'sha256:39eefceb4dace697'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SectionConfiguration](../sectionconfiguration.md)

# actions

<sub>Instance Property</sub>

Custom actions associated with a section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var actions: SectionConfiguration.Actions { get }
```

## Discussion

This property provides programmatic access to the actions defined on a [Section](../section.md). If no actions were specified, the collection will be empty. The following `MailboxView` will put actions into an overflow menu if there are too many to display inline.

```swift
struct MailboxView<Content: View>: View {
    var content: Content

    init(@ContentBuilder content: () -> Content) {
        self.content = content()
    }

    var body: some View {
        ForEach(sections: content) { section in
            HStack {
                section.header
                Spacer()
                Group(subviews: section.actions) { actions in
                    if actions.count > 2 {
                        actions[0]
                        // Place the extras in an overflow menu.
                        Menu("Actions", systemImage: "plus") {
                            actions[1...]
                        }
                    } else {
                        actions
                    }
                }
            }
            section.content
        }
    }
}
```

You can then use actions in `MailboxView` without considering overflow.

```swift
MailboxView {
    Section("iCloud") {
        Label("Receipts", systemImage: "folder")
        Label("Mailing Lists", systemImage: "folder")
    }
    .sectionActions {
        Button("New", systemImage: "folder.badge.plus") {}
        Button("Edit", systemImage: "folder.badge.gearshape") {}
        Button("Delete", systemImage: "folder.badge.minus") {}
    }
}
```
