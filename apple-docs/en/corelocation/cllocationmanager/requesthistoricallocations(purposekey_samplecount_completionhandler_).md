---
title: 'requestHistoricalLocations(purposeKey:sampleCount:completionHandler:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationmanager/requesthistoricallocations(purposekey:samplecount:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/requesthistoricallocations(purposekey:samplecount:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/requesthistoricallocations%28purposekey%3Asamplecount%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:80176a6b6213275e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# requestHistoricalLocations(purposeKey:sampleCount:completionHandler:)

<sub>Instance Method</sub>

<sub>watchOS</sub>

```swift
func requestHistoricalLocations(purposeKey: String, sampleCount: Int, completionHandler handler: @escaping @Sendable ([CLLocation], (any Error)?) -> Void)
```

<sub>watchOS</sub>

```swift
func historicalLocations(purposeKey: String, sampleCount: Int) async throws -> [CLLocation]
```

## Discussion

> [!important] Important
> You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func historicalLocations(purposeKey: String, sampleCount: Int) async throws -> [CLLocation]
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../swift/calling-objective-c-apis-asynchronously.md).
