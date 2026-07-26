---
title: 'healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+, watchOS 10.2+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/healthdataaccessrequest(store:sharetypes:readtypes:trigger:completion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/healthdataaccessrequest(store:sharetypes:readtypes:trigger:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/healthdataaccessrequest%28store%3Asharetypes%3Areadtypes%3Atrigger%3Acompletion%3A%29.json'
content_hash: 'sha256:49ebdb79f3177404'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)

<sub>Instance Method</sub>

Requests permission to save and read the specified HealthKit data types.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
@preconcurrency nonisolated func healthDataAccessRequest(store: HKHealthStore, shareTypes: Set<HKSampleType>, readTypes: Set<HKObjectType>? = nil, trigger: some Equatable, completion: @escaping @Sendable (Result<Bool, any Error>) -> Void) -> some View

```

## Parameters

- `store` — The HealthKit store where you’re requesting authorization.

- `shareTypes` — A set containing the data types you want to share. This set can contain any concrete subclass of the [HKSampleType](../../healthkit/hksampletype.md) class (any of the [HKQuantityType](../../healthkit/hkquantitytype.md), [HKCategoryType](../../healthkit/hkcategorytype.md), [HKWorkoutType](../../healthkit/hkworkouttype.md), or [HKCorrelationType](../../healthkit/hkcorrelationtype.md) classes). If the user grants permission, your app can create and save these data types to the HealthKit store.

- `readTypes` — An optional set containing the data types you want to read. This set can contain any concrete subclass of the [HKObjectType](../../healthkit/hkobjecttype.md) class (any of the [HKCharacteristicType](../../healthkit/hkcharacteristictype.md), [HKQuantityType](../../healthkit/hkquantitytype.md), [HKCategoryType](../../healthkit/hkcategorytype.md), [HKWorkoutType](../../healthkit/hkworkouttype.md), or [HKCorrelationType](../../healthkit/hkcorrelationtype.md) classes ). If the user grants permission, your app can read these data types from the HealthKit store.

- `trigger` — A value used to trigger the request. This value must be a [State](../state.md) variable. Any change to the variable triggers a request.

- `completion` — A block that the system calls after the request is complete. The system passes the result parameter.

## Discussion

HealthKit performs these requests asynchronously when you modify the trigger’s value. If you call this method with a new data type (a type of data that the user hasn’t previously granted or denied permission for in this app), the system automatically displays the authorization sheet when you modify the trigger’s value. The authorization sheet lists all the requested permissions. After the user finishes responding, HealthKit calls the completion block on a background queue. If the user has already chosen to grant or prohibit access to all of the types specified, HealthKit calls the completion when you modify the trigger without prompting the user.

Each data type has two separate permissions, one to read it and one to share it. You can make a single request, and include all the data types your app needs.

**Requesting access on launch**

```swift
@State private var trigger = false

var body: some Scene {
    WindowGroup {
        ContentView(enabled: $accessRequested)
            .healthDataAccessRequest(store: store,
                                     shareTypes: healthDataTypes,
                                     readTypes: healthDataTypes,
                                     trigger: trigger) { result in
                switch result {

                case .success(_):
                    accessRequested = true
                case .failure(let error):
                    // Handle the error here.
                    fatalError("*** An error occurred while requesting authentication: \(error) ***")
                }

                logger.debug("Authorization request complete.")
            }
            .onAppear() {
                trigger.toggle()
            }
    }
}
```

**Full Swift file**

```swift
import SwiftUI
import HealthKit
import HealthKitUI
import os

let healthDataTypes: Set = [
    HKQuantityType.workoutType(),
    HKQuantityType(.heartRate),
    HKQuantityType(.activeEnergyBurned),
    HKQuantityType(.basalEnergyBurned),
    HKQuantityType(.distanceWalkingRunning),
    HKQuantityType(.stepCount)
]

private let logger = Logger(subsystem: "example.com.MyWorkoutApp",
                            category: "iOS App")

@main
struct MyApp: App {

    @State private var accessRequested = false
    @State private var trigger = false

    let store = HKHealthStore()

    var body: some Scene {
        WindowGroup {
            ContentView(enabled: $accessRequested)
                .healthDataAccessRequest(store: store,
                                         shareTypes: healthDataTypes,
                                         readTypes: healthDataTypes,
                                         trigger: trigger) { result in
                    switch result {

                    case .success(_):
                        accessRequested = true
                    case .failure(let error):
                        // Handle the error here.
                        fatalError("*** An error occurred while requesting authentication: \(error) ***")
                    }

                    logger.debug("Authorization request complete.")
                }
                .onAppear() {
                    trigger.toggle()
                }
        }
    }
}
```

Customize the messages displayed on the permissions sheet by setting the following keys:

- [NSHealthShareUsageDescription](../../bundleresources/information-property-list/nshealthshareusagedescription.md) customizes the message for reading data.
- [NSHealthUpdateUsageDescription](../../bundleresources/information-property-list/nshealthupdateusagedescription.md) customizes the message for writing data.

> [!warning] Warning
> You must set the usage keys, or your app crashes when you request authorization.

Set these keys in the Target Properties list on the app’s Info tab.

After users set the permissions for your app, they can always change them using either the Settings or the Health app. Your app appears in the Health app’s Sources tab, even if the user didn’t allow permission to read or share data.

## See Also

### Accessing health data

- [healthDataAccessRequest(store:objectType:predicate:trigger:completion:)](<healthdataaccessrequest(store_objecttype_predicate_trigger_completion_).md>) — Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [healthDataAccessRequest(store:readTypes:trigger:completion:)](<healthdataaccessrequest(store_readtypes_trigger_completion_).md>) — Requests permission to read the specified HealthKit data types.
- [workoutPreview(_:isPresented:)](<workoutpreview(__ispresented_).md>) — Presents a preview of the workout contents as a modal sheet
