---
title: 'controlSize(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 10.15+, tvOS 15.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/controlsize(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/controlsize(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/controlsize%28_%3A%29.json'
content_hash: 'sha256:0e4b3a1f23c0faea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# controlSize(_:)

<sub>Instance Method</sub>

Sets the size for controls within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func controlSize(_ controlSize: ControlSize) -> some View

```

## Parameters

- `controlSize` — One of the control sizes specified in the [ControlSize](../controlsize.md) enumeration.

## Discussion

Use `controlSize(_:)` to override the system default size for controls in this view. In this example, a view displays several typical controls at `.mini`, `.small` and `.regular` sizes.

```swift
struct ControlSize: View {
    var body: some View {
        VStack {
            MyControls(label: "Mini")
                .controlSize(.mini)
            MyControls(label: "Small")
                .controlSize(.small)
            MyControls(label: "Regular")
                .controlSize(.regular)
        }
        .padding()
        .frame(width: 450)
        .border(Color.gray)
    }
}

struct MyControls: View {
    var label: String
    @State private var value = 3.0
    @State private var selected = 1
    var body: some View {
        HStack {
            Text(label + ":")
            Picker("Selection", selection: $selected) {
                Text("option 1").tag(1)
                Text("option 2").tag(2)
                Text("option 3").tag(3)
            }
            Slider(value: $value, in: 1...10)
            Button("OK") { }
        }
    }
}
```

![A screenshot showing several controls of various](../../../../attachments/accf80df231061eac66e07e5377e0d31/SwiftUI-View-controlSize@2x.png)

## See Also

### Sizing controls

- [controlSize](../environmentvalues/controlsize.md) — The size to apply to controls within a view.
- [ControlSize](../controlsize.md) — The size classes, like regular or small, that you can apply to controls within a view.
