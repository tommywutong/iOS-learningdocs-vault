---
title: 'url(scheme:user:password:host:port:path:query:fragment:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/regexcomponent/url(scheme:user:password:host:port:path:query:fragment:)'
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent/url(scheme:user:password:host:port:path:query:fragment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent/url%28scheme%3Auser%3Apassword%3Ahost%3Aport%3Apath%3Aquery%3Afragment%3A%29.json'
content_hash: 'sha256:c9f6cf7fa35af184'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RegexComponent](../regexcomponent.md)

# url(scheme:user:password:host:port:path:query:fragment:)

<sub>Type Method</sub>

Creates a regex component that matches a URL substring, capturing it as a Foundation URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func url(scheme: URL.ParseStrategy.ComponentParseStrategy<String> = .required, user: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, password: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, host: URL.ParseStrategy.ComponentParseStrategy<String> = .required, port: URL.ParseStrategy.ComponentParseStrategy<Int> = .optional, path: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, query: URL.ParseStrategy.ComponentParseStrategy<String> = .optional, fragment: URL.ParseStrategy.ComponentParseStrategy<String> = .optional) -> Self
```

## Parameters

- `scheme` — A [URL.ParseStrategy.ComponentParseStrategy](../../foundation/url/parsestrategy/componentparsestrategy.md) for matching the URL scheme component.

- `user` — A [URL.ParseStrategy.ComponentParseStrategy](../../foundation/url/parsestrategy/componentparsestrategy.md) for matching the user component.

- `password` — A [URL.ParseStrategy.ComponentParseStrategy](../../foundation/url/parsestrategy/componentparsestrategy.md) for matching the password component.

- `host` — A [URL.ParseStrategy.ComponentParseStrategy](../../foundation/url/parsestrategy/componentparsestrategy.md) for matching the host component.

- `port` — A [URL.ParseStrategy.ComponentParseStrategy](../../foundation/url/parsestrategy/componentparsestrategy.md) for matching the port component.

- `path` — A [URL.ParseStrategy.ComponentParseStrategy](../../foundation/url/parsestrategy/componentparsestrategy.md) for matching the path component.

- `query` — A [URL.ParseStrategy.ComponentParseStrategy](../../foundation/url/parsestrategy/componentparsestrategy.md) for matching the query component.

- `fragment` — A [URL.ParseStrategy.ComponentParseStrategy](../../foundation/url/parsestrategy/componentparsestrategy.md) for matching the fragment component.

## Return Value

A `RegexComponent` that matches a URL.

## Discussion

All the parameters to this method take a [URL.ParseStrategy.ComponentParseStrategy](../../foundation/url/parsestrategy/componentparsestrategy.md) value to configure the matching behavior for one component of the URL. The three possible values are:

- [URL.ParseStrategy.ComponentParseStrategy.required](../../foundation/url/parsestrategy/componentparsestrategy/required.md) — The URL component needs to be present for matching to succeed.
- [URL.ParseStrategy.ComponentParseStrategy.optional](../../foundation/url/parsestrategy/componentparsestrategy/optional.md) — The URL component doesn’t need to be present for matching to succeed.
- [URL.ParseStrategy.ComponentParseStrategy.defaultValue(_:)](<../../foundation/url/parsestrategy/componentparsestrategy/defaultvalue(__).md>) — If the URL component is absent, the captured URL contains the provided default value for the component.

The following example creates a [Regex](../regex.md) that matches a URL, when it contains a scheme and a host. It then matches against a source string that contains a date formatted in the `en_US` locale, some whitespace, and a valid URL. The regex defines a default value for the port with [URL.ParseStrategy.ComponentParseStrategy.defaultValue(_:)](<../../foundation/url/parsestrategy/componentparsestrategy/defaultvalue(__).md>), and because the source URL doesn’t include a port, the captured URL adds it.

```swift
let source = "7/31/2022, 5:15:12 AM  https://www.example.com/productList?query=slushie"
let matcher = Regex {
    One(.dateTime(date: .numeric,
                  time: .standard,
                  locale: Locale(identifier: "en_US"),
                  timeZone: TimeZone(identifier: "PST")!))
    OneOrMore(.horizontalWhitespace)
    Capture {
        One(.url(scheme: .required,
                 user: .optional,
                 password: .optional,
                 host: .required,
                 port: .defaultValue(8088),
                 path: .optional,
                 query: .optional,
                 fragment: .optional))
    }
}
guard let match = source.firstMatch(of: matcher) else { return }
let url = match.1 // url = https://www.example.com:8088/productList?query=slushie
```
