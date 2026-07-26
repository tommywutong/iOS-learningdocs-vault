---
title: switchToLatest()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publisher/switchtolatest()-453ht
source_url: 'https://developer.apple.com/documentation/combine/publisher/switchtolatest()-453ht'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/switchtolatest%28%29-453ht.json'
content_hash: 'sha256:c3f2d64c5134d964'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# switchToLatest()

<sub>Instance Method</sub>

Republishes elements sent by the most recently received publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Self>
```

## Discussion

This operator works with an upstream publisher of publishers, flattening the stream of elements to appear as if they were coming from a single stream of elements. It switches the inner publisher as new ones arrive but keeps the outer publisher constant for downstream subscribers.

For example, given the type `AnyPublisher<URLSession.DataTaskPublisher, NSError>`, calling `switchToLatest()` results in the type `SwitchToLatest<(Data, URLResponse), URLError>`. The downstream subscriber sees a continuous stream of `(Data, URLResponse)` elements from what looks like a single [URLSession.DataTaskPublisher](../../foundation/urlsession/datataskpublisher.md) even though the elements are coming from different upstream publishers.

When this operator receives a new publisher from the upstream publisher, it cancels its previous subscription. Use this feature to prevent earlier publishers from performing unnecessary work, such as creating network request publishers from frequently updating user interface publishers.

The following example updates a [PassthroughSubject](../passthroughsubject.md) with a new value every `0.1` seconds. A [map(_:)](<map(__)-99evh.md>) operator receives the new value and uses it to create a new [URLSession.DataTaskPublisher](../../foundation/urlsession/datataskpublisher.md). By using the `switchToLatest()` operator, the downstream sink subscriber receives the `(Data, URLResponse)` output type from the data task publishers, rather than the [URLSession.DataTaskPublisher](../../foundation/urlsession/datataskpublisher.md) type produced by the [map(_:)](<map(__)-99evh.md>) operator. Furthermore, creating each new data task publisher cancels the previous data task publisher.

```swift
let subject = PassthroughSubject<Int, Never>()
cancellable = subject
    .setFailureType(to: URLError.self)
    .map() { index -> URLSession.DataTaskPublisher in
        let url = URL(string: "https://example.org/get?index=\(index)")!
        return URLSession.shared.dataTaskPublisher(for: url)
    }
    .switchToLatest()
    .sink(receiveCompletion: { print("Complete: \($0)") },
          receiveValue: { (data, response) in
            guard let url = response.url else { print("Bad response."); return }
            print("URL: \(url)")
    })

for index in 1...5 {
    DispatchQueue.main.asyncAfter(deadline: .now() + TimeInterval(index/10)) {
        subject.send(index)
    }
}

// Prints "URL: https://example.org/get?index=5"
```

The exact behavior of this example depends on the value of `asyncAfter` and the speed of the network connection. If the delay value is longer, or the network connection is fast, the earlier data tasks may complete before `switchToLatest()` can cancel them. If this happens, the output includes multiple URLs whose tasks complete before cancellation.

## See Also

### Republishing elements by subscribing to new publishers

- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-3k7z5.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-qxf.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-hyb0.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [flatMap(maxPublishers:_:)](<flatmap(maxpublishers___)-4of8w.md>) — Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [switchToLatest()](<switchtolatest()-1c51y.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-20v3t.md>) — Republishes elements sent by the most recently received publisher.
- [switchToLatest()](<switchtolatest()-9eb3r.md>) — Republishes elements sent by the most recently received publisher.
