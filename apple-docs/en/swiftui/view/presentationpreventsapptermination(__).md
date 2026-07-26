---
title: 'presentationPreventsAppTermination(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 15.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/presentationpreventsapptermination(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/presentationpreventsapptermination(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/presentationpreventsapptermination%28_%3A%29.json'
content_hash: 'sha256:f786ea01ff70ad86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# presentationPreventsAppTermination(_:)

<sub>Instance Method</sub>

Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.

<sub>macOS</sub>

```swift
nonisolated func presentationPreventsAppTermination(_ prevents: Bool?) -> some View

```

## Discussion

SwiftUI uses the buttons in a sheet’s toolbar to determine whether a particular sheet should block termination by default. If there is a singular toolbar item with the [confirmationAction](../toolbaritemplacement/confirmationaction.md) or the [cancellationAction](../toolbaritemplacement/cancellationaction.md) placement and no other toolbar items, the sheet will not prevent termination by default.

Use this modifier to specify whether a sheet should prevent app termination. Pass `nil` to explicitly request the automatic behavior/for the inert version of this modifier. Non-nil values will override `nil`, and `true` takes precedence over `false`.

Use this modifier within the `content` argument to `View/sheet`

```swift
struct LaunchScreen: View {
  @State private var presentLogin = false
  var body: some View {
    HomeView()
      .sheet(isPresented: $presentLogin) {
        LoginView()
          // explicitly allow app termination because the
          // default behavior would resolve to `true`.
          .presentationPreventsAppTermination(false)
          .toolbar {
            ToolbarItem(placement: .cancellationAction) {
              Button("Cancel") { presentLogin = false }
            }
            ToolbarItem(placement: .confirmationAction) {
              Button("Login") {
                // Attempt login...
                presentLogin = false
              }
            }
          }
        }
    }
}
```

## See Also

### Sheet and popover configuration

- [interactiveDismissDisabled(_:)](<interactivedismissdisabled(__).md>) — Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [presentationDetents(_:)](<presentationdetents(__).md>) — Sets the available detents for the enclosing sheet.
- [presentationDetents(_:selection:)](<presentationdetents(__selection_).md>) — Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [presentationDragIndicator(_:)](<presentationdragindicator(__).md>) — Sets the visibility of the drag indicator on top of a sheet.
- [presentationBackground(_:)](<presentationbackground(__).md>) — Sets the presentation background of the enclosing sheet using a shape style.
- [presentationBackground(alignment:content:)](<presentationbackground(alignment_content_).md>) — Sets the presentation background of the enclosing sheet to a custom view.
- [presentationBackgroundInteraction(_:)](<presentationbackgroundinteraction(__).md>) — Controls whether people can interact with the view behind a presentation.
- [presentationCompactAdaptation(horizontal:vertical:)](<presentationcompactadaptation(horizontal_vertical_).md>) — Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [presentationCompactAdaptation(_:)](<presentationcompactadaptation(__).md>) — Specifies how to adapt a presentation to compact size classes.
- [presentationContentInteraction(_:)](<presentationcontentinteraction(__).md>) — Configures the behavior of swipe gestures on a presentation.
- [presentationCornerRadius(_:)](<presentationcornerradius(__).md>) — Requests that the presentation have a specific corner radius.
- [presentationSizing(_:)](<presentationsizing(__).md>) — Sets the sizing of the containing presentation.
- [presentationBreakthroughEffect(_:)](<presentationbreakthrougheffect(__).md>) — Changes the way the enclosing presentation breaks through content occluding it.
