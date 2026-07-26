---
title: 'init(outputType:failure:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/fail/init(outputtype:failure:)'
source_url: 'https://developer.apple.com/documentation/combine/fail/init(outputtype:failure:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/fail/init%28outputtype%3Afailure%3A%29.json'
content_hash: 'sha256:cb5029485bee4714'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Fail](../fail.md)

# init(outputType:failure:)

<sub>Initializer</sub>

Creates publisher with the given output type, that immediately terminates with the specified failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(outputType: Output.Type, failure: Failure)
```

## Parameters

- `outputType` — The output type exposed by this publisher.

- `failure` — The failure to send when terminating the publisher.

## Discussion

Use this initializer to create a `Fail` publisher that can work with subscribers or publishers that expect a given output type.

## See Also

### Creating a fail publisher

- [init(error:)](<init(error_).md>) — Creates a publisher that immediately terminates with the specified failure.
