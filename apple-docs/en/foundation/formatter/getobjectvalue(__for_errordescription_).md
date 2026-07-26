---
title: 'getObjectValue(_:for:errorDescription:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatter/getobjectvalue(_:for:errordescription:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatter/getobjectvalue(_:for:errordescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter/getobjectvalue%28_%3Afor%3Aerrordescription%3A%29.json'
content_hash: 'sha256:6ee0a343962bb2f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Formatter](../formatter.md)

# getObjectValue(_:for:errorDescription:)

<sub>Instance Method</sub>

The default implementation of this method raises an exception.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>?, for string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

## Parameters

- `obj` — If conversion is successful, upon return contains the object created from `string`.

- `string` — The string to parse.

- `error` — If non-`nil`, if there is a error during the conversion, upon return contains an `NSString` object that describes the problem.

## Return Value

[true](../../swift/true.md) if the conversion from string to cell content object was successful, otherwise [false](../../swift/false.md).

## Discussion

When implementing this method in a subclass, return by reference the object `anObject` created from `string`. If `string` is equal to the value of the converted object, such as for formatters whose converted value type is `NSString`, it can be returned by reference without creating a new object.

Return [true](../../swift/true.md) if the conversion is successful. If you return [false](../../swift/false.md), also return by indirection (in `error`) a localized user-presentable `NSString` object that explains the reason why the conversion failed; the delegate (if any) of the `NSControl` object managing the cell can then respond to the failure in control:didFailToFormatString:errorDescription:. However, if `error` is `nil`, the sender is not interested in the error description, and you should not attempt to assign one.

The following example (which is paired with the example given in [- stringForObjectValue:](<string(for_).md>)) converts a string representation of a dollar amount that includes the dollar sign; it uses an `NSScanner` instance to convert this amount to a float after stripping out the initial dollar sign.

```objc
- (BOOL)getObjectValue:(id *)obj forString:(NSString *)string errorDescription:(NSString  **)error {
    float floatResult;
    NSScanner *scanner;
    BOOL returnValue = NO;
 
    scanner = [NSScanner scannerWithString: string];
    [scanner scanString: @"$" intoString: NULL]; // ignore  return value
    if ([scanner scanFloat:&floatResult] && ([scanner isAtEnd])) {
        returnValue = YES;
        if (obj) {
            *obj = [NSNumber numberWithFloat:floatResult];
        }
    } else {
        if (error) {
            *error = NSLocalizedString(@"Couldn’t convert  to float", @"Error converting");
        }
    }
    return returnValue;
}
```

### Special Considerations

Prior to OS X v10.6, the implementation of this method in both [NumberFormatter](../numberformatter.md) and [DateFormatter](../dateformatter.md) would return [true](../../swift/true.md) and an object value even if only part of the string could be parsed. This is problematic because you cannot be sure what portion of the string was parsed. For applications linked on or after OS X v10.6, this method instead returns an error if part of the string cannot be parsed. You can use `getObjectValue:forString:range:error:` to get the old behavior—it returns the range of the substring that was successfully parsed.

## See Also

### Related Documentation

- [- stringForObjectValue:](<string(for_).md>) — The default implementation of this method raises an exception.
