---
title: 'appEntityIdentifier(forSelectionType:identifier:)'
framework: AppIntents
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/appentityidentifier(forselectiontype:identifier:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/appentityidentifier(forselectiontype:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/appentityidentifier%28forselectiontype%3Aidentifier%3A%29.json'
content_hash: 'sha256:951d88a27394671b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# appEntityIdentifier(forSelectionType:identifier:)

<sub>Instance Method</sub>

Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func appEntityIdentifier<I>(forSelectionType itemType: I.Type = I.self, identifier: @escaping @Sendable (I) -> EntityIdentifier?) -> some View where I : Hashable

```

## Discussion

Use this modifier to make app entities that describe data in a list discoverable by Apple Intelligence and Siri. This provides additional context to the system when the list appears onscreen and people scroll through it.

The following example associates a [List](../list.md) view that displays books with an app entity for each book in the list.

```swift
struct BookListView: View {
   let books: [Book]
   @State private var selection = Set<Book.ID>()
   var body: some View {
       List(selection: $selection) {
           ForEach(books) { book in
               BookView(book.name)
           }
       }
       .appEntityIdentifier(forSelectionType: Book.ID.self) { bookId in
           EntityIdentifier(for: Book.self, identifier: bookId)
       }
   }
 }
```

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [App Intents](../../appintents.md).

## See Also

### App intents

- [appEntityIdentifier(_:)](<appentityidentifier(__).md>) — Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [appEntityUIElements(_:)](<appentityuielements(__).md>) — Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.
- [onAppIntentExecution(_:perform:)](<onappintentexecution(__perform_).md>) — Registers a handler to invoke in response to the specified app intent that your app receives.
- [shortcutsLinkStyle(_:)](<shortcutslinkstyle(__).md>) — Sets the given style for ShortcutsLinks within the view hierarchy
- [siriTipViewStyle(_:)](<siritipviewstyle(__).md>) — Sets the given style for SiriTipView within the view hierarchy
