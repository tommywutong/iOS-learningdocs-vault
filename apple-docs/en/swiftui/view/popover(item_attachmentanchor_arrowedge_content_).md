---
title: 'popover(item:attachmentAnchor:arrowEdge:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/popover(item:attachmentanchor:arrowedge:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/popover(item:attachmentanchor:arrowedge:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/popover%28item%3Aattachmentanchor%3Aarrowedge%3Acontent%3A%29.json'
content_hash: 'sha256:066465298a8f56c1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# popover(item:attachmentAnchor:arrowEdge:content:)

<sub>Instance Method</sub>

Presents a popover using the given item as a data source for the popover’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor = .rect(.bounds), arrowEdge: Edge? = nil, @ContentBuilder content: @escaping (Item) -> Content) -> some View where Item : Identifiable, Content : View

```

## Parameters

- `item` — A binding to an optional source of truth for the popover. When `item` is non-`nil`, the system passes the contents to the modifier’s closure. You use this content to populate the fields of a popover that you create that the system displays to the user. If `item` changes, the system dismisses the currently presented popover and replaces it with a new popover using the same process.

- `attachmentAnchor` — The positioning anchor that defines the attachment point of the popover. The default is [bounds](../anchor/source/bounds.md).

- `arrowEdge` — The edge of the `attachmentAnchor` that defines the location of the popover’s arrow. The default is `nil`, which results in the system allowing any arrow edge.

- `content` — A closure returning the content of the popover.

## Discussion

Use this method when you need to present a popover with content from a custom data source. The example below uses data in the `PopoverModel` structure to populate the view in the `content` closure that the popover displays to the user:

```swift
struct PopoverExample: View {
    @State private var popover: PopoverModel?

    var body: some View {
        Button("Show Popover") {
            popover = PopoverModel(message: "Custom Message")
        }
        .popover(item: $popover, arrowEdge: .bottom) { detail in
            Text("\(detail.message)")
                .padding()
        }
    }
}

struct PopoverModel: Identifiable {
    var id: String { message }
    let message: String
}
```

![A screenshot showing a popover that says Custom Message hovering](../../../../attachments/63364f288054c4ca93b99c9322d4f60e/View-popover-2@2x.png)

> [!important] Important
> Prior to iOS 18.1, the popover arrow edge was not respected. Apps that are re-compiled with the iOS 18.1 or later SDK or visionOS 2.1 or later SDK and run on iOS 18.1 or later or visionOS 2.1 or later have the arrow edge respected. On macOS, arrow edge has always been respected. Alternatively, to allow the system to choose the best orientation of the popover’s arrow, use the `View/popover(item:attachmentAnchor:content:)` variant.

### Breakthrough effect

In visionOS, most system presentations appear with a breakthrough effect by default. To change how the enclosing presentation breaks through content occluding it, use [presentationBreakthroughEffect(_:)](<presentationbreakthrougheffect(__).md>), like in the following example:

```swift
.popover(item: $popover) { detail in
    Text("\(detail.message)")
        .padding()
        .presentationBreakthroughEffect(.prominent)
}
```

## See Also

### Showing a sheet, cover, or popover

- [sheet(isPresented:onDismiss:content:)](<sheet(ispresented_ondismiss_content_).md>) — Presents a sheet when a binding to a Boolean value that you provide is true.
- [sheet(item:onDismiss:content:)](<sheet(item_ondismiss_content_).md>) — Presents a sheet using the given item as a data source for the sheet’s content.
- [fullScreenCover(isPresented:onDismiss:content:)](<fullscreencover(ispresented_ondismiss_content_).md>) — Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [fullScreenCover(item:onDismiss:content:)](<fullscreencover(item_ondismiss_content_).md>) — Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [popover(isPresented:attachmentAnchor:arrowEdge:content:)](<popover(ispresented_attachmentanchor_arrowedge_content_).md>) — Presents a popover when a given condition is true.
- [PopoverAttachmentAnchor](../popoverattachmentanchor.md) — An attachment anchor for a popover.
