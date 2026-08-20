---
title: Value Transformer Programming Guide
apple_id: 10000175i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2007-04-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ValueTransformers/Concepts/CustomTransformer.html
archived_at: '2026-07-15T07:21:03.843183Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Value Transformer Programming Guide](Introduction%20to%20Value%20Transformers.md)


[Next](Document%20Revision%20History.md)[Previous](Registering%20a%20Value%20Transformer.md)

# Writing a Custom Value Transformer

The Foundation framework provides several built-in value transformers. You create your own custom value transformers by subclassing `NSValueTransformer`.

An `NSValueTransformer` subclass must, at a minimum, implement the `transformedValueClass`, `allowsReverseTransformation` and `transformedValue:` methods. If your custom value transformer supports reverse transformations, you must also implement the `reverseTransformedValue:` method.

As an example, we’ll create an `NSValueTransformer` subclass, `FahrenheitToCelsiusTransformer`, that converts Fahrenheit temperatures to the Celsius scale. This value transformer is also reversible, able to convert Celsius temperatures back to the Fahrenheit scale.

A value transformer subclass must implement the `transformedValueClass` class method. This method returns the class of the object that the `transformedValue:` method returns.

The `FahrenheitToCelsiusTransformer` class returns an NSNumber, as shown in Listing 1.

__Listing 1__  Fahrenheit to Celsius `transformedValueClass` implementation

```objc
+ (Class)transformedValueClass
{
    return [NSNumber class];
}
```


`NSValueTransformer` subclasses must also implement the `allowsReverseTransformation` class method. The subclass implementation should return `YES` if the value transformer is reversible.

The Fahrenheit to Celsius value transformer is reversible, so the `allowsReverseTransformation` implementation returns `YES`, as shown in Listing 2.

__Listing 2__  Fahrenheit to Celsius `allowsReverseTransformation` implementation

```objc
+ (BOOL)allowsReverseTransformation
{
    return YES;
}
```


The `transformedValue:` method implements the actual value transformation. It’s passed the object to transform, and returns the result of the transformation. The result must be an instance of the class returned by `transformedValueClass`.

For maximum flexibility, an implementation of `transformedValue:` should be prepared to handle a variety of different classes as the value. The Fahrenheit to Celsius transformer can handle values of both [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) and [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber) classes, by using the `floatValue` method to convert the value to a scalar.

The result that is returned when the value is `nil` is dependent on what the value transformer is attempting to do. The Fahrenheit to Celsius implementation of `transformedValue:`, shown in Listing 3, returns `nil` in this case.

__Listing 3__  Fahrenheit to Celsius `transformedValue` implementation

```objc
- (id)transformedValue:(id)value
{
    float fahrenheitInputValue;
    float celsiusOutputValue;

    if (value == nil) return nil;

    // Attempt to get a reasonable value from the
    // value object.
    if ([value respondsToSelector: @selector(floatValue)]) {
    // handles NSString and NSNumber
        fahrenheitInputValue = [value floatValue];
    } else {
        [NSException raise: NSInternalInconsistencyException
                    format: @"Value (%@) does not respond to -floatValue.",
        [value class]];
    }

    // calculate Celsius value
    celsiusOutputValue = (5.0/9.0)*(fahrenheitInputValue - 32.0);

    return [NSNumber numberWithFloat: celsiusOutputValue];
}
```


If an `NSValueTransformer` subclass supports reverse transformations, it must implement the `reverseTransformedValue:` method.

Care should be taken when implementing reversible value transformers to ensure that the reversal does not result in a loss of accuracy. In many cases, passing the result of `transformedValue:` to `reverseTransformedValue:` should return an object with the same value as the original object.

The Fahrenheit to Celsius implementation of `reverseTransformedValue:` is shown in Listing 4. The only significant difference between this and the `transformedValue:` implementation is the temperature conversion formula.

__Listing 4__  Fahrenheit to Celsius `reverseTransformedValue` implementation

```objc
- (id)reverseTransformedValue:(id)value
{
    float celsiusInputValue;
    float fahrenheitOutputValue;

    if (value == nil) return nil;

    // Attempt to get a reasonable value from the
    // value object.
    if ([value respondsToSelector: @selector(floatValue)]) {
    // handles NSString and NSNumber
        celsiusInputValue = [value floatValue];
    } else {
        [NSException raise: NSInternalInconsistencyException
                    format: @"Value (%@) does not respond to -floatValue.",
        [value class]];
    }

    // calculate Fahrenheit value
    fahrenheitOutputValue = ((9.0/5.0) * celsiusInputValue) + 32.0;

    return [NSNumber numberWithDouble: fahrenheitOutputValue];
}
```

[Next](Document%20Revision%20History.md)[Previous](Registering%20a%20Value%20Transformer.md)

