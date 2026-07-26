---
title: URL.ParseStrategy
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/parsestrategy
source_url: 'https://developer.apple.com/documentation/foundation/url/parsestrategy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/parsestrategy.json'
content_hash: 'sha256:6c118ef32ad7e216'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# URL.ParseStrategy

<sub>Structure</sub>

A parse strategy for creating URLs from formatted strings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ParseStrategy
```

## Overview

Create an explicit [ParseStrategy](parsestrategy.md) to parse multiple strings according to the same parse strategy. The following example creates a customized strategy, then applies it to multiple URL candidate strings.

```swift
let strategy = URL.ParseStrategy(
    scheme: .defaultValue("https"),
    user: .optional,
    password: .optional,
    host: .required,
    port: .optional,
    path: .required,
    query: .required,
    fragment: .optional)
let urlStrings = [
    "example.com?key1=value1", // no scheme or path
    "https://example.com?key2=value2", // no path
    "https://example.com", // no query
    "https://example.com/path?key4=value4", // complete
    "//example.com/path?key5=value5" // complete except for default-able scheme
]
let urls = urlStrings.map { try? strategy.parse($0) } // [nil, nil, nil, Optional(https://example.com/path?key4=value4), Optional(https://example.com/path?key5=value5)]
```

You don’t need to instantiate a parse strategy instance to parse a single string. Instead, use the URL initializer [init(_:strategy:)](<init(__strategy_).md>), passing in a string to parse and a customized strategy, typically created with one of the static accessors. The following example parses a URL string, with a custom strategy that provides a default value for the port component if the source string doesn’t specify one.

```swift
let urlString = "https://internal.example.com/path/to/endpoint?key=value"
let url = try? URL(urlString, strategy: .url
    .port(.defaultValue(8080))) // https://internal.example.com:8080/path/to/endpoint?key=value

```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [CustomConsumingRegexComponent](../../swift/customconsumingregexcomponent.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [ParseStrategy](../parsestrategy.md), [RegexComponent](../../swift/regexcomponent.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a URL parse strategy

- [init(scheme:user:password:host:port:path:query:fragment:)](<parsestrategy/init(scheme_user_password_host_port_path_query_fragment_).md>) — Creates a URL parse strategy with the specified component-parsing behaviors.
- [ComponentParseStrategy](parsestrategy/componentparsestrategy.md) — The strategy used to parse one component of a URL.

### Customizing strategy behavior

- [scheme(_:)](<parsestrategy/scheme(__).md>) — Modifies a parse strategy to parse a URL’s scheme component in accordance with the provided behavior.
- [user(_:)](<parsestrategy/user(__).md>) — Modifies a parse strategy to parse a URL’s user component in accordance with the provided behavior.
- [password(_:)](<parsestrategy/password(__).md>) — Modifies a parse strategy to parse a URL’s password component in accordance with the provided behavior.
- [host(_:)](<parsestrategy/host(__).md>) — Modifies a parse strategy to parse a URL’s host component in accordance with the provided behavior.
- [port(_:)](<parsestrategy/port(__).md>) — Modifies a parse strategy to parse a URL’s port component in accordance with the provided behavior.
- [path(_:)](<parsestrategy/path(__).md>) — Modifies a parse strategy to parse a URL’s path component in accordance with the provided behavior.
- [query(_:)](<parsestrategy/query(__).md>) — Modifies a parse strategy to parse a URL’s query component in accordance with the provided behavior.
- [fragment(_:)](<parsestrategy/fragment(__).md>) — Modifies a parse strategy to parse a URL’s fragment component in accordance with the provided behavior.
- [ComponentParseStrategy](parsestrategy/componentparsestrategy.md) — The strategy used to parse one component of a URL.

### Parsing strings

- [parse(_:)](<parsestrategy/parse(__).md>) — Parses a URL string in accordance with this strategy and returns the parsed value.

### Locating URLs with regular expressions

- [consuming(_:startingAt:in:)](<parsestrategy/consuming(__startingat_in_).md>) — Process the input string within the specified bounds, beginning at the given index, and return the end position (upper bound) of the match and the produced output.

### Supporting Types

- [RegexOutput](parsestrategy/regexoutput.md) — The type returned when capturing matching substrings with this strategy.

### Default Implementations

- [CustomConsumingRegexComponent Implementations](parsestrategy/customconsumingregexcomponent-implementations.md)
- [ParseStrategy Implementations](parsestrategy/parsestrategy-implementations.md)
- [RegexComponent Implementations](parsestrategy/regexcomponent-implementations.md)

## See Also

### Parsing URLs

- [parseStrategy](formatstyle/parsestrategy.md) — The parse strategy used by this format style.
