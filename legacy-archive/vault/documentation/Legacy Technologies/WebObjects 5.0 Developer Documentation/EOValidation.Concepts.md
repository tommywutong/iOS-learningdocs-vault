---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/Concepts/EOValidationConcepts.html
archived_at: '2026-07-15T08:13:47.779497Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Protocols/Art/up.gif)](../../EOControlTOC.md)

# EOValidation.Concepts

## Validating Individual Properties

The most general method for validating individual properties, validateValueForKey, validates a property indirectly by name (or key). This method is responsible for two things: coercing the value into an appropriate type for the object, and validating it according to the object's rules. The default implementation provided by EOCustomObject consults the object's EOClassDescription (using the EOEnterpriseObject interface method classDescription) to coerce the value and to check for basic errors, such as a __null__ value when that isn't allowed. If no basic errors exist, this default implementation then validates the value according to the object itself. It searches for a method of the form __validate___Key_ and invokes it if it exists. These are the methods that your custom classes can implement to validate individual properties, such as `validateAge` to check that the value the user entered is within acceptable limits. The `validateAge` method should raise an EOValidation.Exception if it finds an unacceptable value.

Coercion is performed automatically for you (by the EOClassDescription), so all you need handle is validation itself. Since you can implement custom validation logic in the __validate___Key_ methods, you rarely need to override the EOValidation method validateValueForKey. Rather, the default implementation provided by EOCustomObject is generally sufficient.

As an example of how validating a single property works, suppose that Member objects have an __age__ attribute stored as an integer. This attribute has a lower limit of 16, defined by the Member class. Now, suppose a user types "12" into a text field for the age of a member. The value comes into the Framework as a string. When __validateValueForKey__ is invoked to validate the new value, the method uses its EOClassDescription to convert the string "12" into an NSNumber, then invokes __validateAge__ with that NSNumber. The __validateAge__ method compares the age to its limit of 16 and throws an exception to indicate that the new value is not acceptable.

```
public void validateAge(Object age) throws EOvalidation.Exception {
    if ((((Number)age).intValue) < 16)
        throw new EOValidation.Exception("Age of " + age + " is below minimum.");
}
```

### When Properties are Validated

The Framework validates all of an object's properties before the object is saved to an external source-either inserted or updated. Additionally, you can design your application so that changes to a property's value are validated immediately, as soon as a user attempts to leave an editable field in the user interface (in Java Client and Application Kit applications only). Whenever an EODisplayGroup sets a value in an object, it sends the object a __validateValueForKey__ message, allowing the object to coerce the value's type, perform any additional validation, and throw an exception if the value isn't valid. By default, the display group leaves validation errors to be handled when the object is saved, using __validateValueForKey__ only for type coercion. However, you can use the EODisplayGroup method __setValidatesChangesImmediately__ with an argument of true to tell the display group to immediately present an attention panel whenever a validation error is encountered.

## Validating Before an Operation

The remaining EOValidation methods-validateForInsert, validateForUpdate, validateForSave, and validateForDelete-validate an entire object to see if it's valid for a particular operation. These methods are invoked automatically by the Framework when the associated operation is initiated. EOCustomObject provides default implementations, so you only have to implement them yourself when special validation logic is required. For example, you can override these methods in your custom enterprise object classes to allow or refuse the operation based on property values. For example, a Fee object might refuse to be deleted if it hasn't been paid yet. Or you can override these methods to perform delayed validation of properties or to compare multiple properties against one another; for example, you might verify that a pair of dates is in the proper temporal order.

If you override any of these operation-specific validation methods, be sure to invoke __super__'s implementation. This is important, as the default implementations of the __validateFor...__ methods pass the check on to the object's EOClassDescription, which performs basic checking among properties, including invoking validateValueForKey for each property. The access layer's EOEntityClassDescription class verifies constraints based on an EOModel, such as delete rules. For example, the delete rule for a Department object might state that it can't be deleted if it still contains Employee objects.

The method __validateForSave__ is the generic validation method for when an object is written to the external store. The default implementations of __validateForInsert__, validateForUpdate both invoke it. If an object performs validation that isn't specific to insertion or to updating, it should go in __validateForSave__.

© 2001 Apple Computer, Inc. (Last Published April 23, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Protocols/Art/up.gif)](../../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
