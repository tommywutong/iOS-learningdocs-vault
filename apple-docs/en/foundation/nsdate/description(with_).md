---
title: 'description(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdate/description(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdate/description(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdate/description%28with%3A%29.json'
content_hash: 'sha256:b631e0b9274f1f4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSDate](../nsdate.md)

# description(with:)

<sub>Instance Method</sub>

Returns a string representation of the date using the given locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func description(with locale: Any?) -> String
```

## Parameters

- `locale` — An `NSLocale` object. If you pass `nil`, `NSDate` formats the date in the same way as the [description](description.md) property. In OS X v10.4 and earlier, this parameter was an `NSDictionary` object. If you pass in an `NSDictionary` object in OS X v10.5, `NSDate` uses the default user locale—the same as if you passed in `[NSLocale currentLocale].`

## Return Value

A string representation of the receiver, using the given locale, or if the locale argument is `nil`, in the international format `YYYY-MM-DD HH:MM:SS ±HHMM`, where `±HHMM` represents the time zone offset in hours and minutes from UTC (for example, “`2001-03-24 10:45:32 +0600`”)

## Discussion

In OS X v10.4 and earlier, `localeDictionary` is an `NSDictionary` object containing locale data. To use the user’s preferences, you can use `[[NSUserDefaults standardUserDefaults] dictionaryRepresentation].`

## See Also

### Describing Dates

- [description](description.md) — A string representation of the date object.
- [customPlaygroundQuickLook](customplaygroundquicklook.md) — A custom playground Quick Look for this object. _(deprecated)_
