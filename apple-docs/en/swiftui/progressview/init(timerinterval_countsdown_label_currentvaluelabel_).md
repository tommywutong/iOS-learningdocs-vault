---
title: 'init(timerInterval:countsDown:label:currentValueLabel:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/progressview/init(timerinterval:countsdown:label:currentvaluelabel:)'
source_url: 'https://developer.apple.com/documentation/swiftui/progressview/init(timerinterval:countsdown:label:currentvaluelabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressview/init%28timerinterval%3Acountsdown%3Alabel%3Acurrentvaluelabel%3A%29.json'
content_hash: 'sha256:afd2362574a318c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressView](../progressview.md)

# init(timerInterval:countsDown:label:currentValueLabel:)

<sub>Initializer</sub>

Creates a progress view for showing continuous progress as time passes, with descriptive and current progress labels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(timerInterval: ClosedRange<Date>, countsDown: Bool = true, @ContentBuilder label: () -> Label, @ContentBuilder currentValueLabel: () -> CurrentValueLabel)
```

## Parameters

- `timerInterval` — The date range over which the view should progress.

- `countsDown` — A Boolean value that determines whether the view empties or fills as time passes. If `true` (the default), the view empties.

- `label` — An optional view that describes the purpose of the progress view.

- `currentValueLabel` — A view that displays the current value of the timer.

## Discussion

Use this initializer to create a view that shows continuous progress within a date range. The following example initializes a progress view with a range of `start...end`, where `start` is 30 seconds in the past and `end` is 90 seconds in the future. As a result, the progress view begins at 25 percent complete. This example also provides custom views for a descriptive label (Progress) and a current value label that shows the date range.

```swift
struct ContentView: View {
    let start = Date().addingTimeInterval(-30)
    let end = Date().addingTimeInterval(90)

    var body: some View {
        ProgressView(timerInterval: start...end,
                     countsDown: false) {
            Text("Progress")
        } currentValueLabel: {
            Text(start...end)
         }
     }
}
```

![A horizontal bar that represents progress, partially filled in from](../../../../attachments/7afea2bc36293b26400c634e5e9ef856/ProgressView-6-macOS@2x.png)

By default, the progress view empties as time passes from the start of the date range to the end, but you can use the `countsDown` parameter to create a progress view that fills as time passes, as the above example demonstrates.

> [!note] Note
> Date-relative progress views, such as those created with this initializer, don’t support custom styles.

## See Also

### Create a progress view spanning a date range

- [init(timerInterval:countsDown:)](<init(timerinterval_countsdown_).md>) — Creates a progress view for showing continuous progress as time passes.
- [init(timerInterval:countsDown:label:)](<init(timerinterval_countsdown_label_).md>) — Creates a progress view for showing continuous progress as time passes, with a descriptive label.
