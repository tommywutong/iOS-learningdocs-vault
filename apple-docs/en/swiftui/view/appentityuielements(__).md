---
title: 'appEntityUIElements(_:)'
framework: AppIntents
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/appentityuielements(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/appentityuielements(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/appentityuielements%28_%3A%29.json'
content_hash: 'sha256:9381421cfcbbfbf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# appEntityUIElements(_:)

<sub>Instance Method</sub>

Provides the system with additional context to make a custom view’s content discoverable by Apple Intelligence and Siri.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func appEntityUIElements(_ provider: @escaping @MainActor (AppEntityUIElementsContext) -> [AppEntityUIElement]) -> some View

```

## Parameters

- `provider` — A closure to set up and return a list of elements that provide context to Apple Intelligence. The order of the returned elements isn’t relevant.

## Discussion

For standard SwiftUI views, you provide onscreen content and context to Apple Intelligence with the [appEntityIdentifier(_:)](<appentityidentifier(__).md>) modifier, making your app entities discoverable when your view appears on screen.

To make content that appears in custom views to Apple Intelligence, use `AppEntityUIElement` structures that act as wrappers for your app entities to provide the system with additional context.

The folowing example shows how a note taking app might provide context to Apple Intelligence for one of its custom views. Its app entity code describes a sticky note. The entity’s `bounds` property provides the system with additional spatial context, enabling it to better understand how a view and its content relate to other views on the screen.

```swift
import AppIntents
import SwiftUI

struct StickyNote: AppEntity {
    var bounds: CGRect
    let colorFill: Color

    let id = UUID()
    let displayRepresentation = DisplayRepresentation(title: "StickyNote")
    static var typeDisplayRepresentation = TypeDisplayRepresentation(stringLiteral: "StickyNote")

    static var defaultQuery = StickyNoteQuery()

    init(bounds: CGRect, colorFill: Color) {
        self.bounds = bounds
        self.colorFill = colorFill
    }
}

struct StickyNoteQuery: EntityQuery {
    func entities(for identifiers: [StickyNote.ID]) async throws -> [StickyNote] {
        // Code to return the queried entities.
    }
}
```

When drawing the view, the app uses the `appEntityUIElements(_:)` API to associate the view’s element with the app entity:

```swift
struct NoteBoardView: View {
    // A collection of app entities with information about the custom view's drawing behavir; for example the view's `.bounds`.
    @State var stickyNotes: [StickyNote]

    var body: some View {
        Canvas { context, size in
            stickyNotes.forEach { note in
                context.fill(
                    Path(
                        roundedRect: note.bounds,
                        cornerSize: .zero
                    ),
                    with: .color(note.colorFill)
                )
            }
        }
        .appEntityUIElements { context in
               stickyNotes.compactMap { note in
                   let includeNote = context.requests.contains { request in
                       switch request {
                           case .visible(let rect):
                               return note.frame.intersects(rect)
                           case .selected:
                               return note.isSelected
                           @unknown default:
                               return false
                       }
                   }
                   guard includeNote else {
                       return nil
                   }
                   return AppEntityUIElement(
                       identifier: EntityIdentifier(
                           for: StickyNote.self,
                           identifier: note.id
                       ),
                       bounds: note.frame,
                       state: State(isSelected: note.isSelected)
                   )
               }
        }
    }
}
```

For more information, refer to doc:providing-contextual-cues-to-Apple-Intelligence-and-Siri and [App Intents](../../appintents.md).

## See Also

### App intents

- [appEntityIdentifier(_:)](<appentityidentifier(__).md>) — Associates a SwiftUI view with an app entity to make its content discoverable by Apple Intelligence and Siri.
- [appEntityIdentifier(forSelectionType:identifier:)](<appentityidentifier(forselectiontype_identifier_).md>) — Associates the items in a SwiftUI list view with app entities to make them discoverable by Apple Intelligence and Siri.
- [onAppIntentExecution(_:perform:)](<onappintentexecution(__perform_).md>) — Registers a handler to invoke in response to the specified app intent that your app receives.
- [shortcutsLinkStyle(_:)](<shortcutslinkstyle(__).md>) — Sets the given style for ShortcutsLinks within the view hierarchy
- [siriTipViewStyle(_:)](<siritipviewstyle(__).md>) — Sets the given style for SiriTipView within the view hierarchy
