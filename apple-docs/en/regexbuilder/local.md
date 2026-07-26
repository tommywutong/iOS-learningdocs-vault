---
title: Local
framework: RegexBuilder
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/local
source_url: 'https://developer.apple.com/documentation/regexbuilder/local'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/local.json'
content_hash: 'sha256:6ecd582d55f63b8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [RegexBuilder](../regexbuilder.md)

# Local

<sub>Structure</sub>

A regex component that represents an atomic group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Local<Output>
```

## Overview

An atomic group opens a local backtracking scope which, upon successful exit, discards any remaining backtracking points from within the scope.

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [RegexComponent](../swift/regexcomponent.md)

## Topics

### Initializers

- [init(_:)](<local/init(__)-190tm.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-1pqmw.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-1z8ep.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-2682m.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-3bh2x.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-3igqu.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-3s7fi.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-53gbl.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-54x6o.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-5xekw.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-6dp02.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-75o5i.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-7an8x.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-7b0cb.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-7c8wv.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-7o3al.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-8bmi6.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-8hppy.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-8i5e6.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-8nf0w.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-8xd9f.md>) — Creates an atomic group with the given regex component.
- [init(_:)](<local/init(__)-anqj.md>) — Creates an atomic group with the given regex component.

## See Also

### Quantifiers

- [One](one.md) — A regex component that matches exactly one occurrence of its underlying component.
- [Optionally](optionally.md) — A regex component that matches zero or one occurrences of its underlying component.
- [ZeroOrMore](zeroormore.md) — A regex component that matches zero or more occurrences of its underlying component.
- [OneOrMore](oneormore.md) — A regex component that matches one or more occurrences of its underlying component.
- [Repeat](repeat.md) — A regex component that matches a selectable number of occurrences of its underlying component.
