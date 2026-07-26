---
title: 'workoutPreview(_:isPresented:)'
framework: WorkoutKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 15.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/workoutpreview(_:ispresented:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/workoutpreview(_:ispresented:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/workoutpreview%28_%3Aispresented%3A%29.json'
content_hash: 'sha256:674629c40bcc0e5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# workoutPreview(_:isPresented:)

<sub>Instance Method</sub>

Presents a preview of the workout contents as a modal sheet

<sub>iOS, iPadOS, Mac Catalyst, macOS, watchOS</sub>

```swift
nonisolated func workoutPreview(_ workout: WorkoutPlan, isPresented: Binding<Bool>) -> some View

```

## Parameters

- `workout` — The `WorkoutContainer` the preview displays

- `isPresented` — A binding to a Boolean value that determines whether to present the preview

## Discussion

```swift
struct WorkoutPreviewer: View {
    let workout: WorkoutPlan
    @State var presented: Bool = false
    var body: some View {
        Button {
            isPresented = true
        } label: {
            WorkoutContainerView(workout)
        }
        .workoutPreview(workout, isPresented: $presented)
    }
}
```

## See Also

### Accessing health data

- [healthDataAccessRequest(store:objectType:predicate:trigger:completion:)](<healthdataaccessrequest(store_objecttype_predicate_trigger_completion_).md>) — Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [healthDataAccessRequest(store:readTypes:trigger:completion:)](<healthdataaccessrequest(store_readtypes_trigger_completion_).md>) — Requests permission to read the specified HealthKit data types.
- [healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)](<healthdataaccessrequest(store_sharetypes_readtypes_trigger_completion_).md>) — Requests permission to save and read the specified HealthKit data types.
