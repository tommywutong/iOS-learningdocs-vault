---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/More/EOValidation_m.html
archived_at: '2026-07-18T01:28:33.771890Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOValidation.md)

---

# EOValidation

---

### Validating Individual Properties

The most general method for validating individual properties, [__validateValueForKey__](EOValidation.md), validates a property indirectly by name (or key). This method is responsible for two things: coercing the value into an appropriate type for the object, and validating it according to the object's rules. The default implementation provided by EOCustomObject consults the object's EOClassDescription (using the EOEnterpriseObject interface method [__classDescription__](EOEnterpriseObject.md)) to coerce the value and to check for basic errors, such as a __null__ value when that isn't allowed. If no basic errors exist, this default implementation then validates the value according to the object itself. It searches for a method of the form __validate__ _Key_ and invokes it if it exists. These are the methods that your custom classes can implement to validate individual properties, such as __validateAge__ to check that the value the user entered is within acceptable limits.

Coercion is performed automatically for you (by the EOClassDescription), so all you need handle is validation itself. Since you can implement custom validation logic in the __validate__ _Key_ methods, you rarely need to override the EOValidation method [__validateValueForKey__](EOValidation.md). Rather, the default implementation provided by EOCustomObject is generally sufficient.

As an example of how validating a single property works, suppose that Member objects have an __age__ attribute stored as an integer. This attribute has a lower limit of 16, defined by the Member class. Now, suppose a user types "12" into a text field for the age of a member. The value comes into the Framework as a string. When [__validateValueForKey__](EOValidation.md)is invoked to validate the new value, the method uses its EOClassDescription to convert the string "12" into an NSNumber, then invokes __validateAge__ with that NSNumber. The __validateAge__ method compares the age to its limit of 16 and throws an exception to indicate that the new value is not acceptable.

> ```
> public void validateAge(java.lang.Object age) throws EOvalidation.Exception {
>     if ((((Number)age).intValue) < 16)
>         throw new EOValidation.Exception("Age of " + age + " is below minimum.");
> }
> ```

---

#### When Properties are Validated

The Framework validates all of an object's properties before the object is saved to an external source-either inserted or updated. Additionally, you can design your application so that changes to a property's value are validated immediately, as soon as a user attempts to leave an editable field in the user interface (in Java Client and Application Kit applications only). Whenever an EODisplayGroup sets a value in an object, it sends the object a [__validateValueForKey__](EOValidation.md)message, allowing the object to coerce the value's type, perform any additional validation, and throw an exception if the value isn't valid. By default, the display group leaves validation errors to be handled when the object is saved, using [__validateValueForKey__](EOValidation.md)only for type coersion. However, you can use the EODisplayGroup method __setValidatesChangesImmediately:__ with an argument of __true__ to tell the display group to immediately present an attention panel whenever a validation error is encountered.

---

### Validating Before an Operation

The remaining EOValidation methods-[__validateForInsert__](EOValidation.md), [__validateForUpdate__](EOValidation.md), [__validateForSave__](EOValidation.md), and [__validateForDelete__](EOValidation.md)-validate an entire object to see if it's valid for a particular operation. These methods are invoked automatically by the Framework when the associated operation is initiated. EOCustomObject provides default implementations, so you only have to implement them yourself when special validation logic is required. For example, you can override these methods in your custom enterprise object classes to allow or refuse the operation based on property values. For example, a Fee object might refuse to be deleted if it hasn't been paid yet. Or you can override these methods to perform delayed validation of properties or to compare multiple properties against one another; for example, you might verify that a pair of dates is in the proper temporal order.

If you override any of these operation-specific validation methods, be sure to invoke __super__ 's implementation. This is important, as the default implementations of the __validateFor...__ methods pass the check on to the object's EOClassDescription, which performs basic checking among properties, including invoking [__validateValueForKey__](EOValidation.md)for each property. The access layer's EOEntityClassDescription class verifies constraints based on an EOModel, such as delete rules. For example, the delete rule for a Department object might state that it can't be deleted if it still contains Employee objects.

The method [__validateForSave__](EOValidation.md)is the generic validation method for when an object is written to the external store. If an object performs validation that isn't specific to insertion or to updating, it should go in [__validateForSave__](EOValidation.md).

---

[!](EOValidation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
