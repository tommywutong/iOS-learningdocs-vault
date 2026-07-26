---
title: RegexComponentBuilder
framework: RegexBuilder
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/regexbuilder/regexcomponentbuilder
source_url: 'https://developer.apple.com/documentation/regexbuilder/regexcomponentbuilder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/regexbuilder/regexcomponentbuilder.json'
content_hash: 'sha256:09e0a5bf1352b883'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [RegexBuilder](../regexbuilder.md)

# RegexComponentBuilder

<sub>Enumeration</sub>

A custom parameter attribute that constructs regular expressions from closures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@resultBuilder enum RegexComponentBuilder
```

## Overview

You typically see `RegexComponentBuilder` as a parameter attribute for `Regex`- or `RegexComponent`-producing closure parameters, allowing those closures to combine multiple regular expression components. Type initializers and string algorithm methods in the RegexBuilder framework include a builder closure parameter, so that you can use regular expression components together.

## Topics

### Type Methods

- [buildBlock()](<regexcomponentbuilder/buildblock().md>)
- [buildExpression(_:)](<regexcomponentbuilder/buildexpression(__).md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-1l3rg.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-4at76.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-4hn5e.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-59bdi.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-6pyeu.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-75sld.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-79ri4.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-8v501.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-9xvwl.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-c1mb.md>)
- [buildLimitedAvailability(_:)](<regexcomponentbuilder/buildlimitedavailability(__)-d693.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-14sjx.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-1kun5.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-1l56o.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-1mvah.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-1qjvk.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-2hd06.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-2nr1l.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-2p8bg.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-2qewj.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-2r4ca.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-2rw87.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-2v43k.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-302jc.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-31uif.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-34auc.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3cwue.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3d4xq.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3fe4r.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3iyin.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3m9by.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3qdzk.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3r0w.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3rw1u.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3uzf8.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-3vbfl.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-439as.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-48ufn.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-49qyb.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-4ej74.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-4ev8q.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-4htjq.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-4qcho.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-4tecz.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-4vll5.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-4w1nu.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-560og.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-5613o.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-5l4bx.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-6ayyo.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-6j8dc.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-6jekf.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-6nfqh.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-6qrtp.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-6u75f.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-6vgmh.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-6wei8.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-78luz.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-7oi4x.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-8nuq5.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-8o64q.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-8t85z.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-90brb.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-92aur.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-94cff.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-95d7s.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-9d7nj.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-9dfaj.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-9fl4.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-9lklo.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-9ne33.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-9upqy.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-dzro.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-fss2.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-k1e8.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-krsh.md>)
- [buildPartialBlock(accumulated:next:)](<regexcomponentbuilder/buildpartialblock(accumulated_next_)-oglj.md>)
- [buildPartialBlock(first:)](<regexcomponentbuilder/buildpartialblock(first_).md>)

## See Also

### Builders

- [AlternationBuilder](alternationbuilder.md) — A custom parameter attribute that constructs regular expression alternations from closures.
