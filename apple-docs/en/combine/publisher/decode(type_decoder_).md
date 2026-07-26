---
title: 'decode(type:decoder:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/decode(type:decoder:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/decode(type:decoder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/decode%28type%3Adecoder%3A%29.json'
content_hash: 'sha256:8f8b19001fdf77ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# decode(type:decoder:)

<sub>Instance Method</sub>

Decodes the output from the upstream using a specified decoder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func decode<Item, Coder>(type: Item.Type, decoder: Coder) -> Publishers.Decode<Self, Item, Coder> where Item : Decodable, Coder : TopLevelDecoder, Self.Output == Coder.Input
```

## Parameters

- `type` — The encoded data to decode into a struct that conforms to the [Decodable](../../swift/decodable.md) protocol.

- `decoder` — A decoder that implements the [TopLevelDecoder](../topleveldecoder.md) protocol.

## Return Value

A publisher that decodes a given type using a specified decoder and publishes the result.

## Discussion

Use [decode(type:decoder:)](<decode(type_decoder_).md>) with a [JSONDecoder](../../foundation/jsondecoder.md) (or a [PropertyListDecoder](../../foundation/propertylistdecoder.md) for property lists) to decode data received from a [URLSession.DataTaskPublisher](../../foundation/urlsession/datataskpublisher.md) or other data source using the [Decodable](../../swift/decodable.md) protocol.

In this example, a [PassthroughSubject](../passthroughsubject.md) publishes a JSON string. The JSON decoder parses the string, converting its fields according to the [Decodable](../../swift/decodable.md) protocol implemented by `Article`, and successfully populating a new `Article`. The [Decode](../publishers/decode.md) publisher then publishes the `Article` to the downstream. If a decoding operation fails, which happens in the case of missing or malformed data in the source JSON string, the stream terminates and passes the error to the downstream subscriber.

```swift
struct Article: Codable {
    let title: String
    let author: String
    let pubDate: Date
}

let dataProvider = PassthroughSubject<Data, Never>()
cancellable = dataProvider
    .decode(type: Article.self, decoder: JSONDecoder())
    .sink(receiveCompletion: { print ("Completion: \($0)")},
          receiveValue: { print ("value: \($0)") })

dataProvider.send(Data("{\"pubDate\":1574273638.575666, \"title\" : \"My First Article\", \"author\" : \"Gita Kumar\" }".utf8))

// Prints: ".sink() data received Article(title: "My First Article", author: "Gita Kumar", pubDate: 2050-11-20 18:13:58 +0000)"
```

## See Also

### Encoding and decoding

- [encode(encoder:)](<encode(encoder_).md>) — Encodes the output from upstream using a specified encoder.
