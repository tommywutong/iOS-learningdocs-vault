---
title: NSDictionaryOfVariableBindings
framework: UIKit
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdictionaryofvariablebindings
source_url: 'https://developer.apple.com/documentation/uikit/nsdictionaryofvariablebindings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdictionaryofvariablebindings.json'
content_hash: 'sha256:9565805d592be47c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSDictionaryOfVariableBindings

<sub>Macro</sub>

Creates a dictionary wherein the keys are string representations of the corresponding values’ variable names.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
#define NSDictionaryOfVariableBindings(...)
```

## Discussion

This macro is particularly useful when creating Auto Layout constraints. For example, the following code creates the dictionary `{ @"button1" = button1, @"button2" = button2 }`.

```objc
NSDictionary *viewsDictionary = NSDictionaryOfVariableBindings(button1, button2);
```

## See Also

### Constraints

- [Positioning content within layout margins](positioning-content-within-layout-margins.md) — Position views so that they aren’t crowded by other content.
- [Positioning content relative to the safe area](positioning-content-relative-to-the-safe-area.md) — Position views so that they aren’t obstructed by other content.
- [NSLayoutConstraint](nslayoutconstraint.md) — The relationship between two user interface objects that must be satisfied by the constraint-based layout system.
- [UILayoutSupport](uilayoutsupport.md) — A set of methods that provide layout support and access to layout anchors.
