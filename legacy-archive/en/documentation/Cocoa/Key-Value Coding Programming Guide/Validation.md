---
title: Key-Value Coding Programming Guide
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/Validation.html
archived_at: '2026-07-15T07:16:17.103945Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Key-Value Coding Programming Guide](index.md)



## Adding Validation

The key-value coding protocol defines methods for validating properties by key or key path. The default implementation of these methods in turn rely on you to define methods following naming patterns similar to those used for accessor methods. Specifically, you provide a `validate<Key>:error:` method for any property with the name `key` that you want to validate. The default implementation searches for this in response to a key-coded [validateValue:forKey:error:](https://developer.apple.com/documentation/objectivec/nsobject/1416754-validatevalue) message.

If you don’t supply a validation method for a property, the default implementation of the protocol assumes validation succeeds for that property, regardless of the value. This means that you opt in to validation on a property-by-property basis.

> [!NOTE]
> 

### Implementing a Validation Method

When you do provide a validation method for a property, that method receives two parameters by reference: the value object to validate and the `NSError` used to return error information. As a result, your validation method can take one of three actions:

- When the value object is valid, return `YES``true` without altering the value object or the error.
- When the value object isn’t valid, and you either can’t or don’t want to provide a valid alternative, set the error parameter to an `NSError` object that indicates the reason for failure and return `NO``false`.

  > [!IMPORTANT]
  > 
- When the value object isn’t valid, but you know of a valid alternative, create the valid object, assign the value reference to the new object, and return `YES``true` without modifying the error reference. If you provide another value, always return a new object rather than modifying the one being validated, even if the original object is mutable.

Listing 11-1 demonstrates a validation method for a `name` string property that ensures that the value object is not `nil` and that the name is a minimum length. This method does not substitute another value if validation fails.

__Listing 11-1__Validation method for the name property

1. `- (BOOL)validateName:(id *)ioValue error:(NSError * __autoreleasing *)outError{`
2. `if ((*ioValue == nil) || ([(NSString *)*ioValue length] < 2)) {`
3. `if (outError != NULL) {`
4. `*outError = [NSError errorWithDomain:PersonErrorDomain`
5. `code:PersonInvalidNameCode`
6. `userInfo:@{ NSLocalizedDescriptionKey`
7. `: @"Name too short" }];`
8. `}`
9. `return NO;`
10. `}`
11. `return YES;`
12. `}`

### Validation of Scalar Values

Validation methods expect the value parameter to be an object, and as a result, values for non-object properties are wrapped in an `NSValue` or `NSNumber` object, as discussed in [Representing Non-Object Values](DataTypes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tclkciffekqkjivcq). The example in Listing 11-2 demonstrates a validation method for the scalar property `age`. In this case, one potential invalid condition, namely a `nil` `age` value, is handled by creating a valid value set to zero, and returning `YES``true`. You might also handle this particular condition in your `setNilValueForKey:` override, because a user of your class might not invoke the validation method.

__Listing 11-2__Validation method for a scalar property

1. `- (BOOL)validateAge:(id *)ioValue error:(NSError * __autoreleasing *)outError {`
2. `if (*ioValue == nil) {`
3. `// Value is nil: Might also handle in setNilValueForKey`
4. `*ioValue = @(0);`
5. `} else if ([*ioValue floatValue] < 0.0) {`
6. `if (outError != NULL) {`
7. `*outError = [NSError errorWithDomain:PersonErrorDomain`
8. `code:PersonInvalidAgeCode`
9. `userInfo:@{ NSLocalizedDescriptionKey`
10. `: @"Age cannot be negative" }];`
11. `}`
12. `return NO;`
13. `}`
14. `return YES;`
15. `}`

[Handling Non-Object Values](HandlingNon-ObjectValues.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydo2jninedklktk4yq)

[Describing Property Relationships](Relationships.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tmlkcijbuirchinbq)
