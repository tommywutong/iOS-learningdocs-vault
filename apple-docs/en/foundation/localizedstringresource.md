---
title: LocalizedStringResource
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/localizedstringresource
source_url: 'https://developer.apple.com/documentation/foundation/localizedstringresource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/localizedstringresource.json'
content_hash: 'sha256:d8f0b507c7f1328d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# LocalizedStringResource

<sub>Structure</sub>

A reference to a localizable string, accessible from another process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LocalizedStringResource
```

## Overview

Use [LocalizedStringResource](localizedstringresource.md) to provide localizable strings with lookups you defer to a later time.

When you create a localized string or a localized attributed string with an initializer that takes [String.LocalizationValue](../swift/string/localizationvalue.md), those initializers lookup the localized string immediately. If you want to perform the lookup at a later time, use this [LocalizedStringResource](localizedstringresource.md) type to refer to the localizable strings. Then, when you need to perform localization, create a [String](../swift/string.md) or [AttributedString](attributedstring.md) from an initializer that takes a [LocalizedStringResource](localizedstringresource.md) parameter, such as:

- [String](../swift/string.md): [init(localized:)](<../swift/string/init(localized_).md>) or [init(localized:options:)](<../swift/string/init(localized_options_).md>).
- [AttributedString](attributedstring.md): [init(localized:)](<attributedstring/init(localized_).md>), [init(localized:including:)](<attributedstring/init(localized_including_)-2xebo.md>), or [init(localized:including:)](<attributedstring/init(localized_including_)-15xc5.md>).

This approach allows you to provide localizable strings to an entirely separate process, which may use a different locale. For example, consider an app with a data model type called `UserAction` that uses [LocalizedStringResource](localizedstringresource.md) rather than strings for its `title` and `description` properties.

```swift
public protocol UserAction {
    static var title: LocalizedStringResource { get }
    static var description: LocalizedStringResource { get }
}
```

This app (or one of its embedded frameworks) then uses these [LocalizedStringResource](localizedstringresource.md) members to defer looking up localized strings. Typically, this happens when calling out to another process over XPC.

```swift
public func perform(action: UserAction) {
    ...
    // Send text to another process via XPC or similar.
    performActionOutOfProcess(title: action.title, description: action.description)
}
```

Then, when the other process receives the call, it can alter the [locale](localizedstringresource/locale.md) in the [LocalizedStringResource](localizedstringresource.md), prior to resolving the localized strings.

```swift
func performActionOutOfProcess(title: LocalizedStringResource,
                               description: LocalizedStringResource) {
    // Set resource locales to match the current locale
    // of the separate process.
    var fixedTitle = title
    fixedTitle.locale = .current
    var fixedDescription = description
    fixedDescription.locale = .current
    
    // Look up localized strings.
    let titleString = String(localized: fixedTitle)
    let descriptionString = String(localized: fixedDescription)
        
    // Use a correctly localized title/description.
}
```

The [App Intents](../appintents.md) framework uses [LocalizedStringResource](localizedstringresource.md) to perform a late resolution of localized strings. This allows the Siri UI to potentially use different localization preferences than the app providing the intent.

## Relationships

- **Conforms To**: [CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md), [Decodable](../swift/decodable.md), [Encodable](../swift/encodable.md), [Equatable](../swift/equatable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringInterpolation](../swift/expressiblebystringinterpolation.md), [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a localized string resource from literal values

- [init(stringLiteral:)](<localizedstringresource/init(stringliteral_).md>) — Creates a localized string resource from the specified string literal.
- [init(stringInterpolation:)](<localizedstringresource/init(stringinterpolation_).md>) — Creates a localized string resource from the given string interpolation.

### Accessing resource properties

- [key](localizedstringresource/key.md) — The key to use to look up a localized string.
- [defaultValue](localizedstringresource/defaultvalue.md) — The resource’s default value.
- [table](localizedstringresource/table.md) — The name of the table containing the key-value pairs.
- [bundle](localizedstringresource/bundle.md) — The bundle containing the table’s strings file.
- [BundleDescription](localizedstringresource/bundledescription.md) — The location of a bundle to use for looking up localized strings, such as the main bundle, or a bundle at a specific file URL.
- [locale](localizedstringresource/locale.md) — The locale to use to look up the localized string from the string resource.

### Describing a resource

- [localizedStringResource](localizedstringresource/localizedstringresource.md) — A resource that helps provide a description of the instance.

### Initializers

- [init(_:defaultValue:table:locale:bundle:comment:)](<localizedstringresource/init(__defaultvalue_table_locale_bundle_comment_)-1apqa.md>) — Creates a localized string resource from a static string and its bundle properties.
- [init(_:defaultValue:table:locale:bundle:comment:)](<localizedstringresource/init(__defaultvalue_table_locale_bundle_comment_)-8jyvr.md>)
- [init(_:table:locale:bundle:comment:)](<localizedstringresource/init(__table_locale_bundle_comment_)-69k32.md>) — Creates a localized string resource from a localization key and its bundle properties.
- [init(_:table:locale:bundle:comment:)](<localizedstringresource/init(__table_locale_bundle_comment_)-8o153.md>)

## See Also

### Localization

- [Locale](locale.md) — Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [NSOrthography](nsorthography.md) — A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [NSLocalizedString(_:tableName:bundle:value:comment:)](<nslocalizedstring(__tablename_bundle_value_comment_).md>) — Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md) — A type that provides an out-of-process localizable description.
- [URLResource](urlresource.md) — A resource located at a particular file URL within a bundle.
