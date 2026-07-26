---
title: 'startMonitoringLocationPushes(completion:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanager/startmonitoringlocationpushes(completion:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/startmonitoringlocationpushes(completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/startmonitoringlocationpushes%28completion%3A%29.json'
content_hash: 'sha256:8609b1bd3e6e994e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# startMonitoringLocationPushes(completion:)

<sub>Instance Method</sub>

Starts monitoring for the delivery of Apple Push Notification service (APNs) location pushes, and provides a device-specific token for sending pushes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func startMonitoringLocationPushes(completion: (@Sendable (Data?, (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func startMonitoringLocationPushes() async throws -> Data
```

## Parameters

- `completion` — The completion handler to call after you start monitoring location pushes. The completion handler takes the following parameters: - **`token`** — A globally unique token that identifies this device to APNs. Send this `token` to the server that you use to generate location pushes. Your server passes this `token` — unmodified — back to APNs when sending pushes. APNs device tokens are of variable length. Don’t hard-code their size. If an error occurs, `token` is `nil`. - **`error`** — If your app is unable to register for location pushes, the system sets this parameter to an error object that contains information about why it failed; otherwise it’s `nil`. The error type is [CLLocationPushServiceError](../cllocationpushserviceerror-swift.struct.md).

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func startMonitoringLocationPushes() async throws -> Data
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).

This function requests an Apple Push Notification service (APNs) token that the system uses to launch your Location Push Service Extension and deliver pushes. Devices need an Internet connection to receive the token. Your completion block receives the token if the call succeeds, otherwise it receives error information. If a compatible iPad or iPhone app calls this method when running in visionOS, the method does nothing.

To use location push notifications, your app must have the `com.apple.developer.location.push` entitlement. For more information about implementing location pushes in your app, see [Creating a location push service extension](../creating-a-location-push-service-extension.md).

## See Also

### Monitoring location push notifications

- [- stopMonitoringLocationPushes](<stopmonitoringlocationpushes().md>) — Stops monitoring for Apple Push Notification service (APNs) location pushes.
