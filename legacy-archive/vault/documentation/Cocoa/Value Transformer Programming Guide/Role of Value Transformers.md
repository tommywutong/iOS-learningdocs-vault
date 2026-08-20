---
title: Value Transformer Programming Guide
apple_id: 10000175i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2007-04-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ValueTransformers/Concepts/TransformersRole.html
archived_at: '2026-07-15T07:21:05.327123Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Value Transformer Programming Guide](Introduction%20to%20Value%20Transformers.md)


[Next](Available%20Value%20Transformers.md)[Previous](Introduction%20to%20Value%20Transformers.md)

# Role of Value Transformers

Value transformer classes are used to transform the value of an object in some manner. This is particularly useful when using Cocoa bindings and creating a binding between a model property of a controller and a user interface element, or another controller object. By using the built-in value transformers, or creating custom value transformers, you can further reduce the amount of glue code required by your application.

For example, it’s often necessary to disable a user interface element if a model property is a `nil` value. Instead of writing a method that returns `YES` if the property is `nil`, you specify that the binding use a “is not nil” transformer. The transformer acts as the “middleman”, providing a `YES` value to the user interface element if the property is `nil`.

Value transformation is done immediately before a value is passed to a user interface element’s `setObjectValue:` method. Likewise, the reverse transformation is applied before the value in the user interface is set in the model. See [Bindings Message Flow](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/MessageFlow.html#//apple_ref/doc/uid/TP40002149) in _[Cocoa Bindings Programming Topics](../Cocoa%20Bindings%20Programming%20Topics/Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3do2i)_ for a detailed description of when value transformers are applied in the context of Cocoa bindings.

All value transformers are subclasses of `NSValueTransformer`. In addition to providing the abstract methods for subclasses, the `NSValueTransformer` class maintains a mapping of value transformer names and the corresponding value transformer objects. This name is used in Interface Builder to specify the value transformer that is used for a binding. You register instances of your custom value transformers in order to expose them, allowing them to be used by Cocoa bindings in Interface Builder.

A value transformer can be reversible, able to convert a value to a new value, and back again. A reversible transformer can be thought of as “read-write”, it transforms the original property value, but will also return any changes made to the transformed value. A non-reversible transformer is “read-only”, only able to reflect changes in the original property.

[Next](Available%20Value%20Transformers.md)[Previous](Introduction%20to%20Value%20Transformers.md)

