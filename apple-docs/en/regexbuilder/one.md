---
title: One
framework: RegexBuilder
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/one
source_url: 'https://developer.apple.com/documentation/regexbuilder/one'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/one.json'
content_hash: 'sha256:2de44bc21c38742e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [RegexBuilder](../regexbuilder.md)

# One

<sub>Structure</sub>

A regex component that matches exactly one occurrence of its underlying component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct One<Output>
```

## Relationships

- **Conforms To**: [RegexComponent](../swift/regexcomponent.md)

## Topics

### Initializers

- [init(_:)](<one/init(__).md>) — Creates a regex component that matches the given component exactly once.

## See Also

### Quantifiers

- [Optionally](optionally.md) — A regex component that matches zero or one occurrences of its underlying component.
- [ZeroOrMore](zeroormore.md) — A regex component that matches zero or more occurrences of its underlying component.
- [OneOrMore](oneormore.md) — A regex component that matches one or more occurrences of its underlying component.
- [Repeat](repeat.md) — A regex component that matches a selectable number of occurrences of its underlying component.
- [Local](local.md) — A regex component that represents an atomic group.
