---
title: 'navigationLinkIndicatorVisibility(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/navigationlinkindicatorvisibility(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/navigationlinkindicatorvisibility(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/navigationlinkindicatorvisibility%28_%3A%29.json'
content_hash: 'sha256:eab303728ada023b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# navigationLinkIndicatorVisibility(_:)

<sub>Instance Method</sub>

Configures whether navigation links show a disclosure indicator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency func navigationLinkIndicatorVisibility(_ visibility: Visibility) -> some View

```

## Discussion

If you need to detect whether the navigation disclosure indicator should be shown for the current view, read the [navigationLinkIndicatorVisibility](../environmentvalues/navigationlinkindicatorvisibility.md) environment value.

The following example hides the indicator for all links in the list. The indicator can be hidden for a specific link by placing the modifier on the `NavigationLink` itself.

```swift
struct NoIndicatorLink: View {
    var body: some View {
        NavigationStack {
            List {
                NavigationLink("See detail") {
                    Text("Detail view")
                }
            }
            .navigationLinkIndicatorVisibility(.hidden)
        }
    }
}
```

> [!important] Important
> Setting the link indicator visibility to `.visible` is only supported for navigation links contained in a `List` built with the Xcode 16 SDKs and earlier. Current releases support setting the indicator visibility to `.visible` regardless of whether the link is within a list.

## See Also

### Navigation stacks and columns

- [navigationDestination(for:destination:)](<navigationdestination(for_destination_).md>) — Associates a destination view with a presented data type for use within a navigation stack.
- [navigationDestination(isPresented:destination:)](<navigationdestination(ispresented_destination_).md>) — Associates a destination view with a binding that can be used to push the view onto a [NavigationStack](../navigationstack.md).
- [navigationDestination(item:destination:)](<navigationdestination(item_destination_).md>) — Associates a destination view with a bound value for use within a navigation stack or navigation split view
- [navigationSplitViewColumnWidth(_:)](<navigationsplitviewcolumnwidth(__).md>) — Sets a fixed, preferred width for the column containing this view.
- [navigationSplitViewColumnWidth(min:ideal:max:)](<navigationsplitviewcolumnwidth(min_ideal_max_).md>) — Sets a flexible, preferred width for the column containing this view.
- [navigationTransition(_:)](<navigationtransition(__).md>) — Sets the navigation transition style for this view.
