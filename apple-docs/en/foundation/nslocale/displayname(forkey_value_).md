---
title: 'displayName(forKey:value:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nslocale/displayname(forkey:value:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslocale/displayname(forkey:value:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslocale/displayname%28forkey%3Avalue%3A%29.json'
content_hash: 'sha256:e94d673709c5194d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLocale](../nslocale.md)

# displayName(forKey:value:)

<sub>Instance Method</sub>

Returns the display name for the given locale component value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func displayName(forKey key: NSLocale.Key, value: Any) -> String?
```

## Parameters

- `key` — The locale property key of `value`. For possible values, see [Key](key.md).

- `value` — A value for `key`.

## Return Value

The display name for `value`.

## Discussion

Not all locale property keys have values with display name values.

You can use the [NSLocaleIdentifier](key/identifier.md) key to get the name of a locale in the language of another locale, as illustrated in the following examples.

**Swift**

```swift
let frLocale = NSLocale(localeIdentifier: "fr_FR")
print(frLocale.displayNameForKey(NSLocaleIdentifier, value: "fr_FR")!)
// "français (France)"
print(frLocale.displayNameForKey(NSLocaleIdentifier, value: "en_US")!)
// "anglais (États-Unis)"
```

**Objective-C**

```objc
NSLocale *frLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"fr_FR"];
NSLog(@"%@", [frLocale displayNameForKey:NSLocaleIdentifier value:@"fr_FR"]);
// "français (France)"
NSLog(@"%@", [frLocale displayNameForKey:NSLocaleIdentifier value:@"en_US"]);
// "anglais (États-Unis)"
```

The following example uses the `en_GB` locale.

**Swift**

```swift
let gbLocale = NSLocale(localeIdentifier: "en_GB")
print(gbLocale.displayNameForKey(NSLocaleIdentifier, value: "fr_FR")!)
// "French (France)"
print(gbLocale.displayNameForKey(NSLocaleIdentifier, value: "en_US")!)
// "English (United States)"
```

**Objective-C**

```objc
NSLocale *gbLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_GB"];
NSLog(@"%@", [gbLocale displayNameForKey:NSLocaleIdentifier value:@"fr_FR"]);
// "French (France)"
NSLog(@"%@", [gbLocale displayNameForKey:NSLocaleIdentifier value:@"en_US"]);
// "English (United States)"
```

## See Also

### Accessing Locale Information by Key

- [- objectForKey:](<object(forkey_).md>) — Returns the value of the component corresponding to the specified key.
- [Key](key.md) — The keys used to access components of a locale.
