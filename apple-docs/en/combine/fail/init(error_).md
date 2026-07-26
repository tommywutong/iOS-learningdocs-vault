---
title: 'init(error:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/fail/init(error:)'
source_url: 'https://developer.apple.com/documentation/combine/fail/init(error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/fail/init%28error%3A%29.json'
content_hash: 'sha256:495437271adcfc5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Fail](../fail.md)

# init(error:)

<sub>Initializer</sub>

Creates a publisher that immediately terminates with the specified failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(error: Failure)
```

## Parameters

- `error` — The failure to send when terminating the publisher.

## See Also

### Creating a fail publisher

- [init(outputType:failure:)](<init(outputtype_failure_).md>) — Creates publisher with the given output type, that immediately terminates with the specified failure.
