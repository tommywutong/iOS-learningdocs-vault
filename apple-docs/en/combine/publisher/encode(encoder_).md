---
title: 'encode(encoder:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/encode(encoder:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/encode(encoder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/encode%28encoder%3A%29.json'
content_hash: 'sha256:6a17d8904f5561d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# encode(encoder:)

<sub>Instance Method</sub>

Encodes the output from upstream using a specified encoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode<Coder>(encoder: Coder) -> Publishers.Encode<Self, Coder> where Coder : TopLevelEncoder
```

## Parameters

- `encoder` — An encoder that implements the [TopLevelEncoder](../toplevelencoder.md) protocol.

## Return Value

A publisher that encodes received elements using a specified encoder, and publishes the resulting data.

## Discussion

Use [encode(encoder:)](<encode(encoder_).md>) with a [JSONDecoder](../../foundation/jsondecoder.md) (or a [PropertyListDecoder](../../foundation/propertylistdecoder.md) for property lists) to encode an [Encodable](../../swift/encodable.md) struct into [Data](../../foundation/data.md) that could be used to make a JSON string (or written to disk as a binary plist in the case of property lists).

In this example, a [PassthroughSubject](../passthroughsubject.md) publishes an `Article`. The [encode(encoder:)](<encode(encoder_).md>) operator encodes the properties of the `Article` struct into a new JSON string according to the [Codable](../../swift/codable.md) protocol adopted by `Article`. The operator publishes the resulting JSON string to the downstream subscriber. If the encoding operation fails, which can happen in the case of complex properties that can’t be directly transformed into JSON, the stream terminates and the error is passed to the downstream subscriber.

```swift
struct Article: Codable {
    let title: String
    let author: String
    let pubDate: Date
}

let dataProvider = PassthroughSubject<Article, Never>()
let cancellable = dataProvider
    .encode(encoder: JSONEncoder())
    .sink(receiveCompletion: { print ("Completion: \($0)") },
          receiveValue: {  data in
            guard let stringRepresentation = String(data: data, encoding: .utf8) else { return }
            print("Data received \(data) string representation: \(stringRepresentation)")
    })

dataProvider.send(Article(title: "My First Article", author: "Gita Kumar", pubDate: Date()))

// Prints: "Data received 86 bytes string representation: {"title":"My First Article","author":"Gita Kumar","pubDate":606211803.279603}"
```

## See Also

### Encoding and decoding

- [decode(type:decoder:)](<decode(type_decoder_).md>) — Decodes the output from the upstream using a specified decoder.
