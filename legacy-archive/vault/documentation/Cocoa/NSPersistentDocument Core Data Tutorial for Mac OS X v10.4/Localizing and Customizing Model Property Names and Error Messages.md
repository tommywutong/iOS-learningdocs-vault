---
title: NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.
apple_id: TP40008168
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NSPersistentDocumentTutorial104/06_CustomisingErrors/errors.html
archived_at: '2026-07-15T07:16:51.584092Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [NSPersistentDocument Core Data Tutorial for Mac OS X v10.4.](Introduction%20to%20NSPersistentDocument%20Core%20Data%20Tutorial%20for%20Mac%20OS%20X%20v10.4.md)


[Next](Document%20Metadata.md)[Previous](Copy%20and%20Paste.md)

This document will not be modified in the future.

# Localizing and Customizing Model Property Names and Error Messages

By default, if an error occurs the user is presented an alert indicating what the problem was. Although useful, the text in the alert may not be very user friendly. If there was a validation error, the name of the property that failed validation is given as defined in the model (for example, “firstName”) rather than something more natural (such as “First name”)—this may be especially unhelpful for users whose native language is not that of the developer. Moreover, if more than one error occurs, the alert simply states that many errors have occurred. In order to give the user more information and help them to fix the problems, you can customize the display of property names and multiple errors.

You can customize and localize entity and property names by adding a model strings file to your project resources (see _[Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)_ > Using a Managed Object Model). You set the name of the strings file to `<ModelName>Model.strings`. For properties where there is only one entity with the given property name, the keys in the file take the form `Property/<NonLocalizedPropertyName>`—if there is a chance of a conflict, you can use `Property/<NonLocalizedPropertyName>/Entity/<NonLocalizedEntityName>`.

1. Select the Resources folder of your project. Create a new empty file by choosing File > New File then selecting Empty File in Project. Press Next, then name the file `MyDocumentModel.strings`.
2. Make the file localizable (in the Inspector (File Info window), click Make File Localizable). You should also ensure that the file is saved in UTF-16 encoding (see [Inspecting File Attributes](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/ed_file_attr/ed_file_attr.html#//apple_ref/doc/uid/TP40001440-CH255) > "Choosing File Encodings").
3. Add key-value pairs for localized representations of the Employee entity’s properties of the form `"Property/NonLocalizedPropertyName" = "Pretty Property Name";` as illustrated in the following examples. Note that it is important to include the semicolon at the end of each line.

```
"Property/firstName" = "First Name";
"Property/lastName" = "Last Name";
"Property/salary" = "Salary";
```
4. Add a second localized version of the file (in the Xcode inspector, click Add Localization). Choose a localization for a language into which you can translate the property names, or use “fr” (for French) and follow this example:

```
"Property/firstName" = "Prénom";
"Property/lastName" = "Nom de famille";
"Property/salary" = "Salaire";
```


Build and run the application. Add a single new employee to a document, and delete the first name. Save the document. You should see an alert that includes the text, “First Name is a required value”.

Inspect the executable and add the argument `-AppleLanguages "(fr)"` (or instead of “fr” use whatever locale identifier you chose earlier). Run the application again, and add a single new employee to a document. Delete the value for the first name, and try to save. This time you should see an alert that displays the localized version of the first name key. Other parts of the interface may also be localized, depending on what locales you installed on your system, and what locale you chose for this test.

Cocoa provides a sophisticated error-handling architecture. Exactly how you deal with an error, and which object receives a message in the event of an error, is described in detail in _[Error Handling Programming Guide](../Error%20Handling%20Programming%20Guide/Introduction%20to%20Error%20Handling%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytqmbw)_. In some cases, for example, if a document fails to open, it may be the responsibility of the `NSDocumentController` object or of the application object to deal with the error. This section focuses on specific errors that may be dealt with by the document itself.

There may be many reasons why an error occurs, and many errors may occur simultaneously—for example, if a user enters several data values that fail validation then tries to save a document. In the event that an error occurs, Core Data provides a rich set of information that describes the problem in an `NSError` object, but if many things go wrong at the same time the actual description provided to the user may be impoverished. `NSDocument` provides a method—`willPresentError:`—that you can override to customize an error message. The method’s argument is the original error. You first, therefore, need to determine whether an error is one that you want to handle in a custom manner. In the case of the `willPresentError:` method, if it’s not an error you want to handle in a custom manner you then simply return it, otherwise analyze the error to determine what to do.

1. In the My Document class, create a stub entry for the method `willPresentError:`.

```objc
- (NSError *)willPresentError:(NSError *)inError {
    // implementation continues...
}
```
2. To customize error messages for Core Data, you first check the error domain. If it is not a Core Data error, (in this example) simply return the original error.

```
if (!([[inError domain] isEqualToString:NSCocoaErrorDomain])) {
    return inError;
}
```
3. Core Data provides errors for a range of different situations. In this example, the only errors of interest are validation errors. The error codes for Core Data validation errors lie within a range delimited by `NSValidationErrorMinimum` and `NSValidationErrorMaximum` (declared in `NSError.h`—error codes and `userInfo` dictionary keys specific to Core Data are declared in `CoreData/CoreDataErrors.h`). If the error code is not within this range, again return the original error. (This step is not strictly necessary—the only test required is the next one—but is a useful example.)

```
int errorCode = [inError code];
if ((errorCode < NSValidationErrorMinimum) ||
            (errorCode > NSValidationErrorMaximum)) {
    return inError;
}
```
4. If there are multiple validation errors, the error is an `NSValidationMultipleErrorsError`. If the error is not an `NSValidationMultipleErrorsError`, then there is only one error message to report, so again return the original error.

```
if (errorCode != NSValidationMultipleErrorsError) {
    return inError;
}
```
5. If the error is an `NSValidationMultipleErrorsError`, its `userInfo` dictionary contains an array of the original error under the key, `NSDetailedErrorsKey`.

   For this example, present error messages for no more than three validation errors at a time. You can do so simply by concatenating the localized description for each error. You could instead construct a more customized, user-friendly error by examining the error code of each individual error.

```
NSArray *detailedErrors = [[inError userInfo] objectForKey:NSDetailedErrorsKey];

unsigned numErrors = [detailedErrors count];
NSMutableString *errorString = [NSMutableString stringWithFormat:@"%u validation errors have occurred", numErrors];

if (numErrors > 3) {
    [errorString appendFormat:@".\nThe first 3 are:\n"];
} else {
    [errorString appendFormat:@":\n"];
}
unsigned i, displayErrors = numErrors > 3 ? 3 : numErrors;
for (i = 0; i < displayErrors; i++) {
    [errorString appendFormat:@"%@\n",
            [[detailedErrors objectAtIndex:i] localizedDescription]];
}
```
6. Finally, create a new error based on the original error and the new description and return it.

```
NSMutableDictionary *newUserInfo = [NSMutableDictionary
            dictionaryWithDictionary:[inError userInfo]];
[newUserInfo setObject:errorString forKey:NSLocalizedDescriptionKey];

NSError *newError = [NSError errorWithDomain:[inError domain]
                                        code:[inError code]
                                    userInfo:newUserInfo];
return newError;
```


The complete `willPresentError:` method is shown in Listing 6-1.

__Listing 6-1__  Complete listing of the `willPresentError:` method

```objc
- (NSError *)willPresentError:(NSError *)inError {

    // The error is a Core Data validation error if its domain is
    // NSCocoaErrorDomain and it is between the minimum and maximum
    // for Core Data validation error codes.

    if (!([[inError domain] isEqualToString:NSCocoaErrorDomain])) {
        return inError;
    }

    int errorCode = [inError code];
    if ((errorCode < NSValidationErrorMinimum) ||
                (errorCode > NSValidationErrorMaximum)) {
        return inError;
    }

    // If there are multiple validation errors, inError is an
    // NSValidationMultipleErrorsError. If it's not, return it

    if (errorCode != NSValidationMultipleErrorsError) {
        return inError;
    }

    // For an NSValidationMultipleErrorsError, the original errors
    // are in an array in the userInfo dictionary for key NSDetailedErrorsKey
    NSArray *detailedErrors = [[inError userInfo] objectForKey:NSDetailedErrorsKey];

    // For this example, only present error messages for up to 3 validation errors at a time.

    unsigned numErrors = [detailedErrors count];
    NSMutableString *errorString = [NSMutableString stringWithFormat:@"%u validation errors have occurred", numErrors];

    if (numErrors > 3) {
        [errorString appendFormat:@".\nThe first 3 are:\n"];
    } else {
        [errorString appendFormat:@":\n"];
    }
    unsigned i, displayErrors = numErrors > 3 ? 3 : numErrors;
    for (i = 0; i < displayErrors; i++) {
        [errorString appendFormat:@"%@\n",
            [[detailedErrors objectAtIndex:i] localizedDescription]];
    }

    // Create a new error with the new userInfo
    NSMutableDictionary *newUserInfo = [NSMutableDictionary
                dictionaryWithDictionary:[inError userInfo]];
    [newUserInfo setObject:errorString forKey:NSLocalizedDescriptionKey];

    NSError *newError = [NSError errorWithDomain:[inError domain] code:[inError code] userInfo:newUserInfo];

    return newError;
}
```


Build and run the application again. Add two employees to a document, and set some invalid values—for example, set their salaries to negative numbers. When you try to save the document, you should find that an alert is presented that lists the validation failures. Add two more employees and try the same test again to ensure that the alert displays just the first three errors.

Comment out the `willPresentError:` method and build and run the application again. Contrast the alert presented without the custom method with that presented using your custom method.

Create a new directory and remove write permissions for yourself—now try to save the document into that directory. What error is presented? What error code is generated?

You have made the application more user friendly. Core Data provides rich information when something goes wrong. You can typically help the user by making it as clear as possible what the problem is, so that the user may have a chance to fix it.

You investigated Core Data’s error handling, in particular you discovered that errors are given a rich description. It’s possible to find out whether a given error is a Core Data error, if so whether it’s a validation error, and finally, if it’s a multiple validation error, what were the original errors.

[Next](Document%20Metadata.md)[Previous](Copy%20and%20Paste.md)

