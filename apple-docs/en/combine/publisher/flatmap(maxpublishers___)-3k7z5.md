---
title: 'flatMap(maxPublishers:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/flatmap(maxpublishers:_:)-3k7z5'
source_url: 'https://developer.apple.com/documentation/combine/publisher/flatmap(maxpublishers:_:)-3k7z5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/flatmap%28maxpublishers%3A_%3A%29-3k7z5.json'
content_hash: 'sha256:c47a47cd775e6f7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# flatMap(maxPublishers:_:)

<sub>Instance Method</sub>

Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flatMap<T, P>(maxPublishers: Subscribers.Demand = .unlimited, _ transform: @escaping (Self.Output) -> P) -> Publishers.FlatMap<P, Self> where T == P.Output, P : Publisher, Self.Failure == P.Failure
```

## Parameters

- `maxPublishers` — Specifies the maximum number of concurrent publisher subscriptions, or [unlimited](../subscribers/demand/unlimited.md) if unspecified.

- `transform` — A closure that takes an element as a parameter and returns a publisher that produces elements of that type.

## Return Value

A publisher that transforms elements from an upstream  publisher into a publisher of that element’s type.

## Discussion

Combine‘s `flatMap(maxPublishers:_:)` operator performs a similar function to the [flatMap(_:)](<../../swift/sequence/flatmap(__)-jo2y.md>) operator in the Swift standard library, but turns the elements from one kind of publisher into a new publisher that is sent to subscribers. Use `flatMap(maxPublishers:_:)` when you want to create a new series of events for downstream subscribers based on the received value. The closure creates the new [Publisher](../publisher.md) based on the received value. The new [Publisher](../publisher.md) can emit more than one event, and successful completion of the new [Publisher](../publisher.md) does not complete the overall stream. Failure of the new [Publisher](../publisher.md) causes the overall stream to fail.

In the example below, a [PassthroughSubject](../passthroughsubject.md) publishes `WeatherStation` elements. The `flatMap(maxPublishers:_:)` receives each element, creates a [URL](../../foundation/url.md) from it, and produces a new [URLSession.DataTaskPublisher](../../foundation/urlsession/datataskpublisher.md), which will publish the data loaded from that [URL](../../foundation/url.md).

```swift
public struct WeatherStation {
    public let stationID: String
}

var weatherPublisher = PassthroughSubject<WeatherStation, URLError>()

cancellable = weatherPublisher.flatMap { station -> URLSession.DataTaskPublisher in
    let url = URL(string:"https://weatherapi.example.com/stations/\(station.stationID)/observations/latest")!
    return URLSession.shared.dataTaskPublisher(for: url)
}
.sink(
    receiveCompletion: { completion in
        // Handle publisher completion (normal or error).
    },
    receiveValue: {
        // Process the received data.
    }
 )

weatherPublisher.send(WeatherStation(stationID: "KSFO")) // San Francisco, CA
weatherPublisher.send(WeatherStation(stationID: "EGLC")) // London, UK
weatherPublisher.send(WeatherStation(stationID: "ZBBB")) // Beijing, CN
```

## See Also

### Republishing elements by subscribing to new publishers

- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-qxf.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-hyb0.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-4of8w.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [switchToLatest()](<switchtolatest()-453ht.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-1c51y.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-20v3t.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-9eb3r.md>) — Republishes elements sent by the most recently received publisher.
