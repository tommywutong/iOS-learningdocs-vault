---
title: 'tabViewSearchActivation(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/tabviewsearchactivation(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/tabviewsearchactivation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/tabviewsearchactivation%28_%3A%29.json'
content_hash: 'sha256:ae180b4e424be93a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# tabViewSearchActivation(_:)

<sub>Instance Method</sub>

Configures the activation and deactivation behavior of search in the search tab.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
nonisolated func tabViewSearchActivation(_ activation: TabSearchActivation) -> some View

```

## Discussion

Use this modifier on a [TabView](../tabview.md) to change how search activation is handled. The exact activation behavior is determined by the [TabSearchActivation](../tabsearchactivation.md) you pass to this modifier:

```swift
struct TabExampleView: View {
    @State private var text: String = ""

    var body: some View {
        TabView {
            Tab("Books", systemImage: "book") {
                BooksTab()
            }
            Tab(role: .search) {
                NavigationStack {
                    SearchContent()
                }
            }
        }
        .searchable(text: $text)
        .tabViewSearchActivation(.searchTabSelection)
    }
}
```

By default, search is only activated and deactivated by the user.

## See Also

### Tab views

- [defaultAdaptableTabBarPlacement(_:)](<defaultadaptabletabbarplacement(__).md>) — Specifies the default placement for the tabs in a tab view using the adaptable sidebar style.
- [defaultTabBarPlacement(_:)](<defaulttabbarplacement(__).md>) — Specifies the preferred placement for the tabs of a [TabView](../tabview.md) in the [sidebarAdaptable](../tabviewstyle/sidebaradaptable.md) style on platforms where the tab bar cannot adapt between different representations, and only one representation can be shown. _(beta)_
- [sectionActions(content:)](<sectionactions(content_).md>) — Adds custom actions to a section.
- [tabBarMinimizeBehavior(_:)](<tabbarminimizebehavior(__).md>) — Sets the behavior for tab bar minimization.
- [tabViewBottomAccessory(content:)](<tabviewbottomaccessory(content_).md>) — Places a view as the bottom accessory of the tab view.
- [tabViewBottomAccessory(isEnabled:content:)](<tabviewbottomaccessory(isenabled_content_).md>) — Places a view as the bottom accessory of the tab view. Use this modifier to dynamically show and hide the accessory view.
- [tabViewCustomization(_:)](<tabviewcustomization(__).md>) — Specifies the customizations to apply to the sidebar representation of the tab view.
- [tabViewSidebarHeader(content:)](<tabviewsidebarheader(content_).md>) — Adds a custom header to the sidebar of a tab view.
- [tabViewSidebarFooter(content:)](<tabviewsidebarfooter(content_).md>) — Adds a custom footer to the sidebar of a tab view.
- [tabViewSidebarBottomBar(content:)](<tabviewsidebarbottombar(content_).md>) — Adds a custom bottom bar to the sidebar of a tab view.
