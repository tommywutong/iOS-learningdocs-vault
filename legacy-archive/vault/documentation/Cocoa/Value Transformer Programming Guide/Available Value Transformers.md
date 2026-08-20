---
title: Value Transformer Programming Guide
apple_id: 10000175i
resource_type: Guide
platform: macOS
topic: Data Management
technology: Foundation
published: '2007-04-06'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ValueTransformers/Concepts/TransformersAvail.html
archived_at: '2026-07-15T07:21:04.835677Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Value Transformer Programming Guide](Introduction%20to%20Value%20Transformers.md)


[Next](Registering%20a%20Value%20Transformer.md)[Previous](Role%20of%20Value%20Transformers.md)

# Available Value Transformers

In addition to providing a mechanism for registering your own value transformers, there are several built-in transformers provided by `NSValueTransformer`.

The built-in transformers provide facilities for negating boolean values, testing for `nil` or non `nil` values, and archiving and unarchiving values into `NSData` instances.

The `NSNegateBooleanTransformerName` value transformer returns an instance of `NSNumber` containing a boolean value. The returned value is the boolean negation of the original value and is reversible.

This value transformer is useful in enabling or disabling user interface elements, as well as setting the values of checkboxes and radio buttons.

The `NSIsNilTransformerName` value transformer returns an instance of `NSNumber` containing a boolean value. The returned value is `YES` if the original value is `nil`, otherwise the returned value is `NO`. This value transformer is not reversible.

This value transformer is often used to enable or disable user interface elements.

The `NSIsNotNilTransformerName` value transformer returns an instance of `NSNumber` containing a boolean value. The returned value is `YES` if the original value is not `nil`, otherwise the returned value is `NO`. This value transformer is not reversible.

This value transformer is often used to enable or disable user interface elements.

The `NSUnarchiveFromDataTransformerName` transformer returns an object created by attempting to unarchive the data in the `NSData` object passed as the value. The reverse transformation returns an `NSData` instance created by archiving the value.

An object must implement the `NSCoding` protocol using sequential archiving in order to be unarchived and archived with this transformer.

This transformer is primarily used with instances of `NSUserDefaultsController`. This transformer allows your application to store objects in the user defaults that are not natively supported, for example, `NSColor` objects.

The `NSKeyedUnarchiveFromDataTransformerName` transformer returns an object created by attempting to unarchive the data in the `NSData` object passed as the value. The reverse transformation returns an `NSData` instance created by archiving the value.

This transformer differs from the `NSUnarchiveFromDataTransformerName` transformer in that the object must implement the `NSCoding` protocol using _keyed archiving_, rather than sequential archiving..

This transformer is primarily used with instances of `NSUserDefaultsController`. This transformer allows your application to store objects in the user defaults that are not natively supported, for example, `NSColor` objects.

[Next](Registering%20a%20Value%20Transformer.md)[Previous](Role%20of%20Value%20Transformers.md)

