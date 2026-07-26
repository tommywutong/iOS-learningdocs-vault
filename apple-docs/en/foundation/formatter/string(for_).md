---
title: 'string(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatter/string(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatter/string(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter/string%28for%3A%29.json'
content_hash: 'sha256:fefa238fe03b51d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Formatter](../formatter.md)

# string(for:)

<sub>Instance Method</sub>

The default implementation of this method raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(for obj: Any?) -> String?
```

## Parameters

- `obj` — The object for which a textual representation is returned.

## Return Value

An `NSString` object that textually represents `object` for display. Returns `nil` if `object` is not of the correct class.

## Discussion

When implementing a subclass, return the `NSString` object that textually represents the cell’s object for display and—if [- editingStringForObjectValue:](<editingstring(for_).md>) is unimplemented—for editing. First test the passed-in object to see if it’s of the correct class. If it isn’t, return `nil`; but if it is of the right class, return a properly formatted and, if necessary, localized string. (See the specification of the [NSString](../nsstring.md) class for formatting and localizing details.)

The following implementation (which is paired with the [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) example above) prefixes a two-digit float representation with a dollar sign:

```objc
- (NSString *)stringForObjectValue:(id)anObject {
 
    if (![anObject isKindOfClass:[NSNumber class]]) {
        return nil;
    }
    return [NSString stringWithFormat:@"$%.2f", [anObject  floatValue]];
}
```

## See Also

### Related Documentation

- [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — The default implementation of this method raises an exception.

### Getting Textual Representations of Object Values

- [- attributedStringForObjectValue:withDefaultAttributes:](<attributedstring(for_withdefaultattributes_).md>) — The default implementation returns `nil` to indicate that the formatter object does not provide an attributed string.
- [- editingStringForObjectValue:](<editingstring(for_).md>) — The default implementation of this method invokes [- stringForObjectValue:](<string(for_).md>).
