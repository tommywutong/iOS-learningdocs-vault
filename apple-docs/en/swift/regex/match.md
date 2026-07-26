---
title: Regex.Match
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regex/match
source_url: 'https://developer.apple.com/documentation/swift/regex/match'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regex/match.json'
content_hash: 'sha256:c28f52ebaa0def13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Regex](../regex.md)

# Regex.Match

<sub>Structure</sub>

The result of matching a regular expression against a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct Match
```

## Overview

A `Match` forwards API to the `Output` generic parameter, providing direct access to captures.

## Topics

### Initializers

- [init(_:)](<match/init(__).md>) — Creates a regular expression match with a dynamic capture list from the given match.

### Instance Properties

- [output](match/output.md) — The output produced from the match operation.
- [range](match/range.md) — The range of the overall match.

### Subscripts

- [subscript(_:)](<match/subscript(__)-9bzv4.md>) — Accesses the capture with the specified name, if a capture with that name exists.
- [subscript(_:)](<match/subscript(__)-vbin.md>) — Accesses this match’s capture by the given reference.
- [subscript(dynamicMember:)](<match/subscript(dynamicmember_).md>) — Accesses a capture by its name or number.
