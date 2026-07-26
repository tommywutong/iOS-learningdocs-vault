---
title: 'init(timerInterval:countsDown:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/progressview/init(timerinterval:countsdown:)'
source_url: 'https://developer.apple.com/documentation/swiftui/progressview/init(timerinterval:countsdown:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/progressview/init%28timerinterval%3Acountsdown%3A%29.json'
content_hash: 'sha256:ad4ed430b28bbaf4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ProgressView](../progressview.md)

# init(timerInterval:countsDown:)

<sub>Initializer</sub>

Creates a progress view for showing continuous progress as time passes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(timerInterval: ClosedRange<Date>, countsDown: Bool = true)
```

## Parameters

- `timerInterval` — The date range over which the view progresses.

- `countsDown` — If `true` (the default), the view empties as time passes.

## Discussion

Use this initializer to create a view that shows continuous progress within a date range. The following example initializes a progress view with a range of `start...end`, where `start` is 30 seconds in the past and `end` is 90 seconds in the future. As a result, the progress view begins at 25 percent complete.

```swift
struct ContentView: View {
    let start = Date().addingTimeInterval(-30)
    let end = Date().addingTimeInterval(90)

    var body: some View {
        ProgressView(timerInterval: start...end
                     countsDown: false)
    }
}
```

![A horizontal bar that represents progress, partially filled in from](../../../../attachments/ae9d9e19ddc35cebb304375cd9f41ff2/ProgressView-8-macOS@2x.png)

By default, the progress view empties as time passes from the start of the date range to the end, but you can use the `countsDown` parameter to create a progress view that fills as time passes, as the above example demonstrates.

The progress view provided by this initializer omits a descriptive label and provides a text label that automatically updates to describe the current time remaining. To provide custom views for these labels, use [init(value:total:label:currentValueLabel:)](<init(value_total_label_currentvaluelabel_).md>) instead.

> [!note] Note
> Date-relative progress views, such as those created with this initializer, don’t support custom styles.

## See Also

### Create a progress view spanning a date range

- [init(timerInterval:countsDown:label:)](<init(timerinterval_countsdown_label_).md>) — Creates a progress view for showing continuous progress as time passes, with a descriptive label.
- [init(timerInterval:countsDown:label:currentValueLabel:)](<init(timerinterval_countsdown_label_currentvaluelabel_).md>) — Creates a progress view for showing continuous progress as time passes, with descriptive and current progress labels.
