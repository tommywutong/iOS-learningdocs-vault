---
title: Value Transformer Programming Guide
apple_id: 10000175i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2007-04-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ValueTransformers/Concepts/Registration.html
archived_at: '2026-07-15T07:21:04.329753Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Value Transformer Programming Guide](Introduction%20to%20Value%20Transformers.md)


[Next](Writing%20a%20Custom%20Value%20Transformer.md)[Previous](Available%20Value%20Transformers.md)

# Registering a Value Transformer

When creating bindings in Interface Builder, you can specify the name of a value transformer that is used as a “middleman”. In order for your custom value transformer objects to be used in this manner, they must first be registered by name.

The `NSValueTransformer` class maintains a mapping of value transformer names, and the corresponding value transformer object. Rather than registering a subclass, individual instances of the `NSValueTransformer` subclasses are registered. This allows a value transformer that provides a generalized functionality to be registered multiple times, with different parameters, for different names. For example, you could write a MultiplicationTransformer and specify the number that is used as the multiplier when an instance is initialized. Separate instances could be registered as “MultiplyByTwoTransformer”, “MultiplyByTenTransformer”, and so on.

The example in Listing 1 registers an instances of the Fahrenheit to Celsius value transformer created in [Writing a Custom Value Transformer](Writing%20a%20Custom%20Value%20Transformer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3dolkciffekqkjivcq) using the name “FahrenheitToCelsiusTransformer”.

__Listing 1__  Registering the Fahrenheit to Celsius value transformer

```
FahrenheitToCelsiusTransformer *fToCTransformer;

// create an autoreleased instance of our value transformer
fToCTransformer = [[[FahrenheitToCelsiusTransformer alloc] init]
                                                      autorelease];

// register it with the name that we refer to it with
[NSValueTransformer setValueTransformer:fToCTransformer
                                forName:@"FahrenheitToCelsiusTransformer"];
```

Value transformers are typically registered by an application’s delegate class, in response to receiving a `initialize:` class message. This allows registration to occur early in the application startup process, providing access to the value transformers as nib files load.

Your `NSValueTransformer` subclasses are not automatically listed in the Interface Builder bindings inspector. When inspecting a binding you can enter the name that the value transformer is registered with, but the functionality will not be present in Interface Builder’s test mode. When your application is compiled and run the transformer will be used.

[Next](Writing%20a%20Custom%20Value%20Transformer.md)[Previous](Available%20Value%20Transformers.md)

