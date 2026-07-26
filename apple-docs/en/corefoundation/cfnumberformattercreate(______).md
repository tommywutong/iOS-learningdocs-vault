---
title: 'CFNumberFormatterCreate(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattercreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattercreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattercreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:58458b8d9670dff2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterCreate(_:_:_:)

<sub>Function</sub>

Creates a new CFNumberFormatter object, localized to the given locale, which will format numbers to the given style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterCreate(_ allocator: CFAllocator!, _ locale: CFLocale!, _ style: CFNumberFormatterStyle) -> CFNumberFormatter!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `locale` — A locale to use for localization. If `NULL`, the function uses the default system locale. Use [CFLocaleCopyCurrent](<cflocalecopycurrent().md>) to specify the locale of the current user.

- `style` — A number style. See [Number Formatter Styles](number-formatter-styles.md) for possible values.

## Return Value

A new number formatter, localized to the given locale, which will format numbers using the given style. Returns `NULL` if there was a problem creating the formatter. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).
