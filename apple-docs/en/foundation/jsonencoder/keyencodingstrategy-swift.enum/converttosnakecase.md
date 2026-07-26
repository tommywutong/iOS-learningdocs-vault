---
title: JSONEncoder.KeyEncodingStrategy.convertToSnakeCase
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum/converttosnakecase
source_url: 'https://developer.apple.com/documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum/converttosnakecase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/jsonencoder/keyencodingstrategy-swift.enum/converttosnakecase.json'
content_hash: 'sha256:a27e2de211e7816d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [JSONEncoder](../../jsonencoder.md) · [KeyEncodingStrategy](../keyencodingstrategy-swift.enum.md)

# JSONEncoder.KeyEncodingStrategy.convertToSnakeCase

<sub>Case</sub>

A key encoding strategy that converts camel-case keys to snake-case keys.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case convertToSnakeCase
```

## Discussion

Camel-case and snake-case are two common approaches for combining words when naming parts of an API. The Swift [API Design Guidelines](https://swift.org/documentation/api-design-guidelines/#general-conventions) recommend using camel-case names. Some JSON APIs adopt snake-case; use this strategy when you encounter such an API.

This strategy uses [uppercaseLetters](../../characterset/uppercaseletters.md) and [lowercaseLetters](../../characterset/lowercaseletters.md) to determine the boundaries between words, and the [systemLocale](../../nslocale/system.md) locale when converting uppercase letters to lowercase letters.

This strategy follows these steps to convert key names to snake-case:

1. Split the name into words, preserving leading or trailing underscores.
2. Insert an underscore between each word.
3. Convert the resulting string to lowercase.

The following examples show the result of applying this strategy:

- **`feeFiFoFum`** — Converts to: `fee_fi_fo_fum`
- **`fee_fi_fo_fum`** — Converts to: `fee_fi_fo_fum`
- **`xmlContents`** — Converts to: `xml_contents`

The example below shows how properties on the `OlympicEventResult` structure convert to snake-case when encoded as keys in a JSON object.

```swift
struct OlympicEventResult: Codable {
    var goldWinner: String
    var silverWinner: String
    var bronzeWinner: String
}

let marathonResult = OlympicEventResult(goldWinner: "Light", silverWinner: "Sound", bronzeWinner: "Unladen Swallow")

let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
let encodeAndPrint = { print(String(data: try! encoder.encode(marathonResult), encoding: .utf8)!) }

encoder.keyEncodingStrategy = .convertToSnakeCase
encodeAndPrint()

/* Prints:
{
  "bronze_winner" : "Unladen Swallow",
  "gold_winner" : "Light",
  "silver_winner" : "Sound"
}
*/
```

## See Also

### Related Documentation

- [JSONDecoder.KeyDecodingStrategy.convertFromSnakeCase](../../jsondecoder/keydecodingstrategy-swift.enum/convertfromsnakecase.md) — A key decoding strategy that converts snake-case keys to camel-case keys.

### Built-in Encoding

- [JSONEncoder.KeyEncodingStrategy.useDefaultKeys](usedefaultkeys.md) — A key encoding strategy that doesn’t change key names during encoding.
