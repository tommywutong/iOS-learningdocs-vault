---
title: Locale
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/locale/'
original_language: en
published: 2012-09-03
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:a1ac6f4cc814fc93'
translated: false
---

> 原文：[Locale](https://nshipster.com/locale/)　·　NSHipster (Mattt)

# [Locale](https://nshipster.com/locale/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  November 28^th, 2018 ([revised](https://github.com/nshipster/articles/commits/master/2012-09-03-locale.md))

> “You take delight not in a city’s seven or seventy wonders,   
>  but in the answer it gives to a question of yours.” Italo Calvino, _Invisible Cities_

Localization (l10n) is the process of adapting your application for a specific market, or locale. Internationalization (i18n) is the process of preparing your app to be localized. Internationalization is a _necessary_, but not _sufficient_ condition for localization. And whether or not you decide to localize your app for other markets, it’s always a good idea to do everything with internationalization in mind.

The hardest thing about internationalization _(aside from saying the word itself)_ is learning how to think outside of your cultural context. Unless you’ve had the privilege to travel or to meet people from other places, you may not even be aware that things could _be_ any other way. But when you venture out into the world, everything from the price of bread to the letters in the alphabet to the numbers of hours in a day — all of that is up in the air.

It can be absolutely overwhelming without a guide. Fortunately for us, we have `Locale` to show us the ways of the world.

---

Foundation’s `Locale` type encapsulates the linguistic and cultural conventions of a user, which include:

- Language and Orthography
- Text Direction and Layout
- Keyboards and Input Methods
- Collation Ordering
- Personal Name Formatting
- Calendar and Date Formatting
- Currency and Number Formatting
- Units and Measurement Formatting
- Use of Symbols, Colors, and Iconography

`Locale` objects are often used as parameters for methods that perform localized operations like sorting a list of strings or formatting a date. Most of the time, you’ll access the `Locale.current` type property to use the user’s current locale.

```
import Foundation

let units = ["meter", "smoot", "agate", "ångström"]

units.sorted { (lhs, rhs) in
    lhs.compare(rhs, locale: .current) == .orderedAscending
}
// => ["agate", "ångström", "meter", "smoot"]
```

You can also construct a `Locale` that corresponds to a particular locale identifier. A locale identifier typically comprises an ISO 639-1 language code (such as `en` for English) and an ISO 3166-2 region code (such as `US` for the United States).

```
let 🇸🇪 = Locale(identifier: "sv_SE")
units.sorted { (lhs, rhs) in
    lhs.compare(rhs, locale: 🇸🇪) == .orderedAscending
}
// => ["agate", "meter", "smoot", "ångström"]
```

Locale identifiers may also specify an explicit character encoding or other preferences like currency, calendar system, or number format with the following syntax:

```
language[_region][.character-encoding][@modifier=value[, ...]]
```

For example, the locale identifier `de_DE.UTF8@collation=phonebook,currency=DEM` specifies a German language locale in Germany that uses UTF-8 text encoding, [phonebook collation](http://developer.mimer.com/charts/german_phonebook.htm), and the pre-Euro [Deutsche Mark](https://en.wikipedia.org/wiki/Deutsche_Mark) currency.

Users can change their locale settings in the “Language & Text” system preference on macOS and in “General \> International” in the iOS Settings app.

![Locale Preferences](https://nshipster.com/assets/locale-preferences-f6a3164c035c4c460b2d297c2487d7ca132d180b601aec26308d0c25f0660a402c528ede9ae7240de8b8dfddfc897a1cfaf4cc7d175a13fdd563845818f7fdb6.png)

## _Terra Cognita_

`Locale` often takes a passive role, being passed into a property here and a method there. But if you give it a chance, it can tell you more about a place than you ever knew there was to know:

Language and Script  `languageCode`, `scriptCode`, `exemplarCharacterSet`  Region `regionCode` Collation  `collationIdentifier`, `collatorIdentifier`  Calendar `calendar` Currency  `currencyCode`, `currencySymbol`  Numbers and Units  `decimalSeparator`, `usesMetricSystem`  Quotation Delimiters  `quotationBeginDelimiter` / `quotationEndDelimiter`, `alternateQuotationBeginDelimiter` / `alternateQuotationEndDelimiter`

While this all may seem like fairly esoteric stuff, you’d be surprised by how many opportunities this kind of information unlocks for making a world-class app.

It’s the small things, like knowing that quotation marks vary between locales:

| **English** | “I can eat glass, it doesn’t harm me.” |
|---|---|
| **German** | „Ich kann Glas essen, das tut mir nicht weh.“ |
| **Japanese** | 「私はガラスを食べられます。それは私を傷つけません。」 |

So if you were building a component that added quotations around arbitrary text, you should use these properties rather than hard-coding English quotation marks.

## _Si Fueris Romae…_

As if it weren’t enough to know, among other things, the preferred currency for every region on the planet, `Locale` can also tell you how you’d refer to it in a particular locale. For example, here in the USA, we call our country the United States. But that’s just an [endonym](https://en.wikipedia.org/wiki/Exonym_and_endonym); elsewhere, American has other names — exonyms. Like in France, it’s…

```
import Foundation

let 🇺🇸 = Locale(identifier: "en_US")
let 🇫🇷 = Locale(identifier: "fr_FR")

🇺🇸.localizedString(forIdentifier: 🇺🇸.identifier)
// => "English (United States)"

🇫🇷.localizedString(forIdentifier: 🇺🇸.identifier)
// => "anglais (États-Unis)"
```

Use this technique whenever you’re displaying locale, like in this screen from the Settings app, which shows language endonyms alongside exonyms:

![Locale Languages Menu on iOS](https://nshipster.com/assets/locale-languages-84744d29273b95ff4d88b234fff8f3fe3fb6a9c6a97f48473a3dd272e81f37ae5016cb744ee3ca1f58f4ac813b1536ae68e1ab6864e7957555e14ed728103362.png)

## _Vox Populi_

The last stop in our tour of `Locale` is the `preferredLanguages` property. Contrary to what you might expect for a type (rather than an instance) property, the returned value depends on the current language preferences of the user. Each of the array elements is [IETF BCP 47 language identifier](http://tools.ietf.org/html/bcp47) and is returned in order of user preference.

If your app communicates with a web app over HTTP, you might use this property to set the [`Accept-Language` header field](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.4) to give the server an opportunity to return localized resources:

```
import Foundation

let url = URL(string: "https://nshipster.com")!
var request = URLRequest(url: url)

let acceptLanguage = Locale.preferredLanguages.joined(separator: ", ")
request.setValue(acceptLanguage, forHTTPHeaderField: "Accept-Language")
```

Even if your server doesn’t yet localize its resources, putting this in place now allows you to flip the switch when the time comes — without having to push an update to the client. _Neat!_

---

Travel is like internationalization: it’s something that isn’t exactly fun at the time, but we do it because it makes us better people. Both activities expand our cultural horizons and allow us to better know people we’ll never actually meet.

With `Locale` you can travel the world without going AFK.
