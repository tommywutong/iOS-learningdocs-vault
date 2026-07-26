---
title: 'write(to:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/data/write(to:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/data/write(to:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/data/write%28to%3Aoptions%3A%29.json'
content_hash: 'sha256:47901f69940cafbe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Data](../data.md)

# write(to:options:)

<sub>Instance Method</sub>

Writes the contents of the data buffer to a location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func write(to url: URL, options: Data.WritingOptions = []) throws
```

## Parameters

- `url` — The location to write the data into.

- `options` — Options for writing the data. Default value is `[]`.

## See Also

### Reading and Writing Data

- [ReadingOptions](readingoptions.md) — Options to control the reading of data from a URL.
- [WritingOptions](writingoptions.md) — Options to control the writing of data to a URL.
