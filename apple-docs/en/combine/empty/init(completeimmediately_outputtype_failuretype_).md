---
title: 'init(completeImmediately:outputType:failureType:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/empty/init(completeimmediately:outputtype:failuretype:)'
source_url: 'https://developer.apple.com/documentation/combine/empty/init(completeimmediately:outputtype:failuretype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/empty/init%28completeimmediately%3Aoutputtype%3Afailuretype%3A%29.json'
content_hash: 'sha256:e5e4562f2b60e1f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Empty](../empty.md)

# init(completeImmediately:outputType:failureType:)

<sub>Initializer</sub>

Creates an empty publisher with the given completion behavior and output and failure types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(completeImmediately: Bool = true, outputType: Output.Type, failureType: Failure.Type)
```

## Parameters

- `completeImmediately` — A Boolean value that indicates whether the publisher should immediately finish.

- `outputType` — The output type exposed by this publisher.

- `failureType` — The failure type exposed by this publisher.

## Discussion

Use this initializer to connect the empty publisher to subscribers or other publishers that have specific output and failure types.

## See Also

### Creating an empty publisher

- [init(completeImmediately:)](<init(completeimmediately_).md>) — Creates an empty publisher.
