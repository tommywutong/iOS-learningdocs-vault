---
title: URL.FormatStyle
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/url/formatstyle
source_url: 'https://developer.apple.com/documentation/foundation/url/formatstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/formatstyle.json'
content_hash: 'sha256:c1671aca796ab04f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# URL.FormatStyle

<sub>Structure</sub>

A structure that converts between URL instances and their textual representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FormatStyle
```

## Overview

Instances of [FormatStyle](formatstyle.md) create localized, human-readable text from [URL](../url.md) instances and parse string representations of URLs into instances of [URL](../url.md).

### Formatting URLs

Use the [formatted()](<formatted().md>) method to create a string representation of a URL using the default [FormatStyle](formatstyle.md) configuration. As seen in the following example, the default style creates a string with the scheme, host, and path, but not the port or query.

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let formatted = url.formatted() // "https://www.example.com/path/to/endpoint"
```

You can specify a format style by providing an argument to the [format(_:)](<formatstyle/format(__).md>) method. The following example uses the previous URL, but preserves only the host and path.

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let style = URL.FormatStyle(scheme: .never,
                            user: .never,
                            password: .never,
                            host: .always,
                            port: .never,
                            path: .always,
                            query: .never,
                            fragment: .never)
let formatted = style.format(url) // "www.example.com/path/to/endpoint"
```

Instantiate a style when you want to format multiple URL instances with the same style. For one-time access to a default style, you can use the static accessor [url](../formatstyle/url.md) at call points that expect the [FormatStyle](formatstyle.md) type, such as the [format(_:)](<formatstyle/format(__).md>) method. This means you can write the example above as follows:

```swift
let url = URL(string:"https://www.example.com:8080/path/to/endpoint?key=value")!
let formatted = url.formatted(.url
    .scheme(.never)
    .host(.always)
    .port(.never)
    .path(.always)
    .query(.never)) // "www.example.com/path/to/endpoint"
```

This example works by taking the default style provided by [url](../formatstyle/url.md), then customizing it with calls to the style modifiers in Customizing style behavior.

### Parsing URLs

You can use [FormatStyle](formatstyle.md) to parse strings into URL values. To do this, create a [ParseStrategy](parsestrategy.md) from a format style, then call the strategy’s [parse(_:)](<parsestrategy/parse(__).md>) method.

```swift
let style = URL.FormatStyle(scheme: .always,
                            user: .never,
                            password: .never,
                            host: .always,
                            port: .always,
                            path: .always,
                            query: .always,
                            fragment: .never)
let urlString = "https://www.example.com:8080/path/to/endpoint?key=value"
let url = try? style.parseStrategy.parse(urlString)
```

### Matching regular expressions

Along with parsing URL values in strings, you can use the regular expression domain-specific language provided by Swift to match and capture URL substrings. The following example scans source input that’s expected to contain a timestamp, some whitespace, and a URL.

```swift
import RegexBuilder
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

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [FormatStyle](../formatstyle.md), [Hashable](../../swift/hashable.md), [ParseableFormatStyle](../parseableformatstyle.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating a URL format style

- [init(scheme:user:password:host:port:path:query:fragment:)](<formatstyle/init(scheme_user_password_host_port_path_query_fragment_).md>) — Creates a URL format style with the given display options.
- [ComponentDisplayOption](formatstyle/componentdisplayoption.md) — A type that indicates whether a formatted URL should include a component.
- [HostDisplayOption](formatstyle/hostdisplayoption.md) — A type that indicates whether a formatted URL should include the host component.

### Formatting URL values

- [format(_:)](<formatstyle/format(__).md>) — Formats a URL, using this style.

### Customizing style behavior

- [scheme(_:)](<formatstyle/scheme(__).md>) — Modifies a format style to display a URL’s scheme component in accordance with the provided option.
- [user(_:)](<formatstyle/user(__).md>) — Modifies a format style to display a URL’s user component in accordance with the provided option.
- [password(_:)](<formatstyle/password(__).md>) — Modifies a format style to display a URL’s password component in accordance with the provided option.
- [host(_:)](<formatstyle/host(__).md>) — Modifies a format style to display a URL’s host component in accordance with the provided option.
- [HostDisplayOption](formatstyle/hostdisplayoption.md) — A type that indicates whether a formatted URL should include the host component.
- [port(_:)](<formatstyle/port(__).md>) — Modifies a format style to display a URL’s port component in accordance with the provided option.
- [path(_:)](<formatstyle/path(__).md>) — Modifies a format style to display a URL’s path component in accordance with the provided option.
- [query(_:)](<formatstyle/query(__).md>) — Modifies a format style to display a URL’s query component in accordance with the provided option.
- [fragment(_:)](<formatstyle/fragment(__).md>) — Modifies a format style to display a URL’s fragment component in accordance with the provided option.
- [ComponentDisplayOption](formatstyle/componentdisplayoption.md) — A type that indicates whether a formatted URL should include a component.

### Parsing URLs

- [parseStrategy](formatstyle/parsestrategy.md) — The parse strategy used by this format style.
- [ParseStrategy](parsestrategy.md) — A parse strategy for creating URLs from formatted strings.

### Enumerations

- [Component](formatstyle/component.md) — An enumeration of the components of a URL, for use in creating format style options that depend on a component’s value.

### Default Implementations

- [FormatStyle Implementations](formatstyle/formatstyle-implementations.md)
- [ParseableFormatStyle Implementations](formatstyle/parseableformatstyle-implementations.md)

## See Also

### Data formatting in Swift

- [Language Introspector](../language-introspector.md) — Converts data into human-readable text using formatters and locales.
- [FormatStyle](../formatstyle.md) — A type that converts a given data type into a representation in another type, such as a string.
- [IntegerFormatStyle](../integerformatstyle.md) — A structure that converts between integer values and their textual representations.
- [FloatingPointFormatStyle](../floatingpointformatstyle.md) — A structure that converts between floating-point values and their textual representations.
- [FormatStyle](../decimal/formatstyle.md) — A structure that converts between decimal values and their textual representations.
- [ListFormatStyle](../listformatstyle.md) — A type that formats lists of items with a separator and conjunction appropriate for a given locale.
- [StringStyle](../stringstyle.md)
- [FormatStyleCapitalizationContext](../formatstylecapitalizationcontext.md) — The capitalization formatting context used when formatting dates and times.
- [Format Style Configurations](../format-style-configurations.md) — Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.
