---
title: doesRelativeDateFormatting
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/dateformatter/doesrelativedateformatting
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/doesrelativedateformatting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/doesrelativedateformatting.json'
content_hash: 'sha256:d252aa83e631f0e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# doesRelativeDateFormatting

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver uses phrases such as “today” and “tomorrow” for the date component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var doesRelativeDateFormatting: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the receiver uses relative date formatting, otherwise [false](../../swift/false.md).

If a date formatter uses relative date formatting, where possible it replaces the date component of its output with a phrase—such as “today” or “tomorrow”—that indicates a relative date. The available phrases depend on the locale for the date formatter; whereas, for dates in the future, English may only allow “tomorrow,” French may allow “the day after the day after tomorrow,” as illustrated in the following example.

**Swift**

```swift
let dateFormatter = DateFormatter()
dateFormatter.timeStyle = .none
dateFormatter.dateStyle = .medium
dateFormatter.locale = Locale(identifier: "fr_FR")
 
dateFormatter.doesRelativeDateFormatting = true
 
let date = Date(timeIntervalSinceNow: 60 * 60 * 24 * 2)
let dateString = dateFormatter.string(from: date)
print(dateString)  // après-demain
```

**Objective-C**

```objc
NSDateFormatter *dateFormatter = [[NSDateFormatter alloc] init];
dateFormatter.timeStyle = NSDateFormatterNoStyle;
dateFormatter.dateStyle = NSDateFormatterMediumStyle;
NSLocale *frLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"fr_FR"];
dateFormatter.locale = frLocale;
 
dateFormatter.doesRelativeDateFormatting = YES;
 
NSDate *date = [NSDate dateWithTimeIntervalSinceNow:60*60*24*2];
NSString *dateString = [dateFormatter stringFromDate:date];
 
NSLog(@"dateString: %@", dateString);
// Output
// dateString: après-demain
```

## See Also

### Managing Natural Language Support

- [lenient](islenient.md) — A Boolean value that indicates whether the receiver uses heuristics when parsing a string.
