---
title: 'healthDataAccessRequest(store:objectType:predicate:trigger:completion:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/healthdataaccessrequest(store:objecttype:predicate:trigger:completion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/healthdataaccessrequest(store:objecttype:predicate:trigger:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/healthdataaccessrequest%28store%3Aobjecttype%3Apredicate%3Atrigger%3Acompletion%3A%29.json'
content_hash: 'sha256:f83f7913fb1a3702'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# healthDataAccessRequest(store:objectType:predicate:trigger:completion:)

<sub>Instance Method</sub>

Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@preconcurrency nonisolated func healthDataAccessRequest(store: HKHealthStore, objectType: HKObjectType, predicate: NSPredicate? = nil, trigger: some Equatable, completion: @escaping @Sendable (Result<Bool, any Error>) -> Void) -> some View

```

## Parameters

- `store` — The HealthKit store where you’re requesting authorization.

- `objectType` — The data type you want to read. This type must be a type that requires per-object authorization.

- `predicate` — An optional predicate that further restricts the objects of interest.

- `trigger` — A value used to trigger the request. This value must be a [State](../state.md) variable. Any change to the variable triggers a request.

- `completion` — A block that the system calls after the request is complete. The system passes the result parameter.

## Discussion

Some samples require per-object authorization. For these samples, people can select which ones your app can read on a sample-by-sample basis. By default, your app can read any of the per-object authorization samples that it has saved to the HealthKit store; however, you may not always have access to those samples. People can update the authorization status for any of these samples at any time.

Your app can begin by setting up the request in SwiftUI.

```swift
@State private var trigger = false
let store = HKHealthStore()

var body: some Scene {
    WindowGroup {
        ContentView(enabled: $accessRequested)
            .healthDataAccessRequest(store: store,
                                     objectType: .visionPrescriptionType(),
                                     predicate: nil,
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
    }
}
```

Next, query for any samples that it already has permission to read.

```swift
// Read the newest prescription from the HealthKit store.
let queryDescriptor = HKSampleQueryDescriptor(predicates: [.visionPrescription()],
                                              sortDescriptors: [SortDescriptor(\.startDate, order: .reverse)],
                                              limit: 1)

let prescription: HKVisionPrescription

do {
    guard let result = try await queryDescriptor.result(for: store).first else {
        print("*** No prescription found. ***")
        return
    }

    prescription = result
} catch {
    // Handle the error here.
    fatalError("*** An error occurred while reading the most recent vision prescriptions: \(error.localizedDescription) ***")
}
```

Based on the results, you can then decide whether you need to request authorization for additional samples. Modify the trigger’s value to prompt someone to modify the samples your app has access to read.

```swift
// Request authorization for additional samples.
trigger.toggle()
```

> [!important] Important
> Using the [healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)](<healthdataaccessrequest(store_sharetypes_readtypes_trigger_completion_).md>) method to request read access to any data types that require per-object authorization fails with an [errorInvalidArgument](../../healthkit/hkerror/errorinvalidargument.md) error.

When your app calls this method, HealthKit displays an authorization sheet that asks for permission to read the samples that match the predicate and object type. The person using your app can then select individual samples to share with your app. The system always asks for permission, regardless of whether the user previously granted it.

People can individually enable each of the prescriptions. After they respond, the system calls the callback handler on an arbitrary background queue.

## See Also

### Accessing health data

- [healthDataAccessRequest(store:readTypes:trigger:completion:)](<healthdataaccessrequest(store_readtypes_trigger_completion_).md>) — Requests permission to read the specified HealthKit data types.
- [healthDataAccessRequest(store:shareTypes:readTypes:trigger:completion:)](<healthdataaccessrequest(store_sharetypes_readtypes_trigger_completion_).md>) — Requests permission to save and read the specified HealthKit data types.
- [workoutPreview(_:isPresented:)](<workoutpreview(__ispresented_).md>) — Presents a preview of the workout contents as a modal sheet
