---
title: AlternationBuilder
framework: RegexBuilder
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/alternationbuilder
source_url: 'https://developer.apple.com/documentation/regexbuilder/alternationbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/alternationbuilder.json'
content_hash: 'sha256:a932e7daea66517c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [RegexBuilder](../regexbuilder.md)

# AlternationBuilder

<sub>Structure</sub>

A custom parameter attribute that constructs regular expression alternations from closures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder struct AlternationBuilder
```

## Overview

When you use a `ChoiceOf` initializer, the initializer’s closure parameter has an `AlternationBuilder` attribute, allowing you to provide multiple regular expression statements as alternatives.

## Topics

### Type Methods

- [buildExpression(_:)](<alternationbuilder/buildexpression(__).md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-1jq94.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-1oadq.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-1vk92.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-20ao.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-28nze.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-2afed.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-2q3in.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-2yatq.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-30m9e.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-3571v.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-38zc3.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-39yml.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-3a1qj.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-3ascd.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-3b47j.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-3eldc.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-3ibe4.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-3nzbh.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-3rkqj.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-3wkc9.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-42jgz.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-46i6m.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-4jwp3.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-4nz0t.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-4q1xd.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-53xav.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-576fa.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-57987.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-5afat.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-5fcrr.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-5me97.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-5qva.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-5wwt0.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6074o.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-653ta.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6842g.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6anqe.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6hkv5.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6nfpu.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6pfu4.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6tz5g.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6vjm9.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6vp0.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6x6gg.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-6yu9n.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-70usl.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-71zj2.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-7ihw4.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-7jsg7.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-815py.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-8a7vx.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-8dd0v.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-8e0ap.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-8pz3c.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-90yht.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-9f39x.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-9g62e.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-9k7s0.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-9op0h.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-9s1co.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-b6ks.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-klfl.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-o7ny.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-q4oo.md>)
- [buildPartialBlock(accumulated:next:)](<alternationbuilder/buildpartialblock(accumulated_next_)-toh7.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-1kh7h.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-271vl.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-3f6z3.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-520tx.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-5qbok.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-63ah5.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-6mjz0.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-6vt65.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-7jdle.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-c2a6.md>)
- [buildPartialBlock(first:)](<alternationbuilder/buildpartialblock(first_)-uy7q.md>)

## See Also

### Builders

- [RegexComponentBuilder](regexcomponentbuilder.md) — A custom parameter attribute that constructs regular expressions from closures.
