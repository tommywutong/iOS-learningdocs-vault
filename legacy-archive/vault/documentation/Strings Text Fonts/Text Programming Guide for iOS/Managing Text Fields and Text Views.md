---
title: Text Programming Guide for iOS
apple_id: TP40009542
resource_type: Guide
platform: tvOS|iOS
topic: Data Management
technology: UIKit
published: '2018-01-16'
source_url: https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/ManageTextFieldTextViews/ManageTextFieldTextViews.html
archived_at: '2026-07-18T02:06:59.746268Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Programming Guide for iOS](About%20Text%20Handling%20in%20iOS.md)


[Next](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/KeyboardManagement/KeyboardManagement.html)[Previous](Typographical%20Concepts.md)

# Managing Text Fields and Text Views

Text fields and text views have two main functions: to display text and to enable the entry and editing of text. Several programming tasks are associated with these simple purposes, including configuring the text object, accessing the current text, validating what the user enters, and displaying overlay views such as bookmark buttons in text fields.

The [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) of a [UITextField](https://developer.apple.com/documentation/uikit/uitextfield) or [UITextView](https://developer.apple.com/documentation/uikit/uitextview) object is responsible for most of these tasks. The delegate must adopt the [UITextFieldDelegate](https://developer.apple.com/documentation/uikit/uitextfielddelegate) or [UITextViewDelegate](https://developer.apple.com/documentation/uikit/uitextviewdelegate) [protocols](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) and implement one or more of the protocol methods. Implementation of all protocol methods is optional. To have these methods called, you must set the `delegate` properties of text fields and text views either programmatically or in Interface Builder.

In most cases, instances of the `UITextField` or `UITextView` classes send a sequence of similarly named messages to their [delegates](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) when there is a change (or impending change) in [first-responder](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Responder.html#//apple_ref/doc/uid/TP40009071-CH1) status for a given text object. When the user taps a text object, it automatically becomes first responder; as a result, the system displays the keyboard and an editing session begins for that text object. When the user taps another text object or taps a button to end editing, the current text object resigns first-responder status. If no other text object is selected, the system hides the keyboard; if, on the other hand, the user selects another text object, it becomes first responder and the keyboard for that object is displayed.

There are a couple of exceptions to this common behavior. On the iPad, if a view controller modally presents its view using the "form sheet" style, the keyboard, once shown, is not hidden until the user taps the dismiss key or the modal view controller is programmatically dismissed. The purpose of this behavior is to avoid excessive animations as a user moves between views that are largely, but not entirely, text fields. Another exception involves custom input views. An input view is a substitute for system keyboards that is assigned to the [inputView](https://developer.apple.com/documentation/uikit/uiresponder/1621092-inputview) property of a text view or a custom view. When there are input views, UIKit might swap out the keyboard even when a text object is first responder, and it might show a keyboard-like input view on the developer's behalf for non-text objects.

The sequence of messages that both text views and text fields send to their delegates is as follows:

1. __Just before a text object becomes first responder__—[textFieldShouldBeginEditing:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619601-textfieldshouldbeginediting) (text field) and [textViewShouldBeginEditing:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618608-textviewshouldbeginediting) (text view).

   The delegate can verify whether the text object should become first responder by returning `YES` (the default) or `NO`.
2. __Just after a text object becomes first responder__—[textFieldDidBeginEditing:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619590-textfielddidbeginediting) (text field) and [textViewDidBeginEditing:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618610-textviewdidbeginediting) (text view).

   The delegate can respond to this message by updating state information or, for example, by showing an overlay view during the editing session.
3. __During the editing session__—various.

   While the user enters and edits text, the text object invokes certain delegation methods (if implemented). For example, the delegate of a text view can receive a [textViewDidChange:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618599-textviewdidchange) message when any text changes. The delegate of a text field can receive a [textFieldShouldClear:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619594-textfieldshouldclear) message when the user taps the clear button of a text field; the delegate returns a Boolean value indicating whether the text should be cleared.
4. __Just before a text object resigns first responder__—[textFieldShouldEndEditing:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619592-textfieldshouldendediting) (text field) and [textViewShouldEndEditing:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618603-textviewshouldendediting) (text view).

   The primary reason for a delegate to implement these methods is to validate entered text. For example, if text should conform to a given format, the delegate validates the entered string here and returns `NO` if the string does not conform. The default return value is `YES`.

   A related method for text fields is [textFieldShouldReturn:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619603-textfieldshouldreturn). When the user taps the return key, the text field class sends a `textFieldShouldReturn:` message to the delegate to ask whether it should resign first responder.
5. __Just after text a object resigns first responder__—[textFieldDidEndEditing:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619591-textfielddidendediting) (text field) and [textViewDidEndEditing:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618628-textviewdidendediting) (text view).

   A delegate can implement these methods to get the text that the user has just entered or edited.

Objects other than the delegate can be informed of changes in the first-responder status of text views and text fields by observing [notifications](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35). (They can’t, however, approve or deny the transition to a new status.) The notifications have names such as [UITextFieldTextDidBeginEditingNotification](https://developer.apple.com/documentation/uikit/uitextfield/1619616-textdidbegineditingnotification), [UITextViewTextDidEndEditingNotification](https://developer.apple.com/documentation/uikit/uitextviewtextdidendeditingnotification), and [UITextViewTextDidChangeNotification](https://developer.apple.com/documentation/uikit/uitextview/1618609-textdidchangenotification). As with [textFieldDidEndEditing:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619591-textfielddidendediting) and [textViewDidEndEditing:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618628-textviewdidendediting), the primary reason for observing and handling the [UITextFieldTextDidEndEditingNotification](https://developer.apple.com/documentation/uikit/uitextfield/1619633-textdidendeditingnotification) and `UITextViewTextDidEndEditingNotification` notifications is to access the text in the associated text field or text view. See _[UITextField Class Reference](https://developer.apple.com/documentation/uikit/uitextfield)_ and _[UITextView Class Reference](https://developer.apple.com/documentation/uikit/uitextview)_ to learn more about the notifications posted by these classes.

As with any [view object](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/ViewObject.html#//apple_ref/doc/uid/TP40009071-CH5) provided by the UIKit framework, you usually need to configure text fields and text views before they’re displayed. You can configure them either programmatically or using the attribute inspector of Interface Builder. In either case, you are setting a [property](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) of the text object.

Some properties are common to text views and text fields, and others are specific to each type of object, including the following:

- __Text characteristics—__Text color, alignment, font family, font typeface, and font size.
- __Keyboard—__Keyboard type, return key name, secure text entry, and auto-enabled return key, all of which are declared by the [UITextInputTraits](https://developer.apple.com/documentation/uikit/uitextinputtraits) protocol. (Note that an auto-enabled return key associated with a text view acts as a carriage-return key when tapped.) For more information, see [Configuring the Keyboard for Text Objects](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/KeyboardManagement/KeyboardManagement.html#//apple_ref/doc/uid/TP40009542-CH5-SW5).
- __Text-field specific—__Border, background image, disabled image, clear button, and placeholder text. As a [UIControl](https://developer.apple.com/documentation/uikit/uicontrol) object, text fields also have highlighted, selected, enabled, and other properties.
- __Text-view specific—__Editable status, data detectors (for phone numbers and URL links). Because a text view inherits from [UIScrollView](https://developer.apple.com/documentation/uikit/uiscrollview), you can also manage scroll-view behavior by setting the appropriate properties.

All methods of the [UITextFieldDelegate](https://developer.apple.com/documentation/uikit/uitextfielddelegate) or [UITextViewDelegate](https://developer.apple.com/documentation/uikit/uitextviewdelegate) [protocols](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Protocol.html#//apple_ref/doc/uid/TP40008195-CH45) have a parameter that identifies the text field or text view with the change in [first-responder](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Responder.html#//apple_ref/doc/uid/TP40009071-CH1) status, the change in value, or any other change that is the reason for the [delegation](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) message. If there is only one text object in the currently displayed view, the identity of the text object referenced by the parameter is obvious. However, if the currently displayed view has multiple text fields or text views, the delegate must find a way to identify the text object that is the subject of a delegation message.

You can make this determination using one of two approaches: outlets or tags. For the outlet approach, declare an [outlet](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Outlet.html#//apple_ref/doc/uid/TP40009071-CH4) instance variable (using the `IBOutlet` keyword) and then [make an outlet connection.](https://developer.apple.com/library/archive/recipes/XcodeRecipes/Connecting_an_Outlet/OutletConnection.html#//apple_ref/doc/uid/TP40009043-CH8) In your delegation method, test whether the passed-in text object is the same object referenced by the outlet, using pointer comparison. For example, say you declare and connect an outlet named `SSN`. Your code might look something like Listing 3-1.

__Listing 3-1__  Identifying the passed-in text object using an outlet

```objc
- (BOOL)textFieldShouldEndEditing:(UITextField *)textField {
    if (textField == SSN) {
            // .....
            return NO;
        }
    return YES;
}
```

Defining outlet connections for the text objects in a view is especially useful, even essential, when you need to write string values to these objects, not just obtain them.

For the tag approach, declare a set of `enum` constants, one constant for each tag.

```
enum {
    NameFieldTag = 0,
    EmailFieldTag,
    DOBFieldTag,
    SSNFieldTag
};
```

Then assign the integer value to the [tag](https://developer.apple.com/documentation/uikit/uiview/1622493-tag) property of the text object, either programmatically or in the attribute inspector of Interface Builder. (The `tag` property is declared by [UIView](https://developer.apple.com/documentation/uikit/uiview).) In a delegation method, you can use a switch statement to evaluate the tag value of the passed-in text object and proceed accordingly (as shown in Listing 3-2).

__Listing 3-2__  Identifying the passed-in text object using tags

```objc
- (void)textFieldDidEndEditing:(UITextField *)textField {

    switch (textField.tag) {
        case NameFieldTag:
            // do something with this text field
            break;
        case EmailFieldTag:
             // do something with this text field
            break;
        // remainder of switch statement....
    }
}
```


After a user enters or edits text in a text field or text view and the editing session ends, the [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) should get the text and store it in the app’s [data model](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ModelObject.html#//apple_ref/doc/uid/TP40008195-CH31). The best delegation methods for accessing entered text are [textFieldDidEndEditing:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619591-textfielddidendediting) (text fields) and [textViewDidEndEditing:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618628-textviewdidendediting) (text views).

Listing 3-3 illustrates how you might get text the user has entered in a text field (differentiating among multiple text fields in a view using tags). The [text](https://developer.apple.com/documentation/uikit/uitextfield/1619635-text) [property](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) of `UITextField` or `UITextView` holds the string currently displayed by the text object. The delegate gets the string from this property and stores it in a [dictionary object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10) using a key defined for each field. If the text field has no string value—that is, the field holds an empty string—the delegate simply returns.

__Listing 3-3__  Getting the text entered into a text field

```objc
- (void)textFieldDidEndEditing:(UITextField *)textField {
    if ([textField.text isEqualToString:@""])
        return;

    switch (textField.tag) {
        case NameFieldTag:
            [thePerson setObject:textField.text forKey:MyAppPersonNameKey];
            break;
        case EmailFieldTag:
            [thePerson setObject:textField.text forKey:MyAppPersonEmailKey];
            break;
        case SSNFieldTag:
            [thePerson setObject:textField.text forKey:MyAppPersonSSNKey];
            break;
        default:
            break;
    }
}
```

Listing 3-4 shows an implementation of the [textViewDidEndEditing:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618628-textviewdidendediting) method that gets the displayed string from the text view and stores it in a dictionary. Here the method doesn’t ask the text view to resign [first responder](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Responder.html#//apple_ref/doc/uid/TP40009071-CH1). (The [resignFirstResponder](https://developer.apple.com/documentation/uikit/uiresponder/1621097-resignfirstresponder) method was called earlier in an [action method](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/TargetAction.html#//apple_ref/doc/uid/TP40009071-CH3) invoked when the user tapped a Done button in the view’s user interface.)

__Listing 3-4__  Getting the text entered into a text view

```objc
- (void)textViewDidEndEditing:(UITextView *)textView {
    NSString *theText = textView.text;
    if (![theText isEqualToString:@""]) {
        [thePerson setObject:theText forKey:MyAppPersonNotesKey];
    }
    doneButton.enabled = NO;
}
```

If you need to _write_ string values to text objects—usually after retrieving them from the app’s data model—simply assign the strings to the `text` property of the text object. For example:

```
NSString *storedValue = [thePerson objectForKey:MyAppPersonEmailKey];
emailField.text = storedValue;
```

To do this, it’s useful to define [outlets](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Outlet.html#//apple_ref/doc/uid/TP40009071-CH4) for each text field or text view that you want to write string values to (`emailField`, in this example).

[Formatter objects](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Formatter.html#//apple_ref/doc/uid/TP40009071-CH14) automatically parse strings in a specific format and convert the string to an object representing a number, date, or other value; they also work in reverse, converting [NSDate](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateClassCluster/Description.html#//apple_ref/occ/cl/NSDate), [NSNumber](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumber/Description.html#//apple_ref/occ/cl/NSNumber), and similar objects to a formatted string that represents those object values. The Foundation [framework](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Framework.html#//apple_ref/doc/uid/TP40008195-CH56) provides the abstract base class [NSFormatter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/cl/NSFormatter) and two concrete subclasses of that class, [NSDateFormatter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSDateFormatter/Description.html#//apple_ref/occ/cl/NSDateFormatter) and [NSNumberFormatter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/cl/NSNumberFormatter). Using these classes, users can enter values such as the following into a text field:

```
11/15/2010
-1,348.09
```

And your app can use formatter objects to convert the strings into an `NSDate` object and an `NSNumber` object, respectively.

The following code listings use a date-formatter object to illustrate the use of formatters. (Of course, you could use a [UIDatePicker](https://developer.apple.com/documentation/uikit/uidatepicker) object for date input rather than a text field, but a text field with an attached date formatter is another option.) The code in Listing 3-5 creates an `NSDateFormatter` object and assigns it to an instance variable. It configures the date formatter to use the “short style” for dates, but in a way that is responsive to changes in calendar, locale, and time zone. It also assigns today’s date in the given format as a placeholder string so that users have a model to follow when they enter dates.

__Listing 3-5__  Configuring a date formatter

```objc
- (void)viewDidLoad {
    [super viewDidLoad];
    dateFormatter = [[NSDateFormatter alloc] init];
    [dateFormatter setGeneratesCalendarDates:YES];
    [dateFormatter setLocale:[NSLocale currentLocale]];
    [dateFormatter setCalendar:[NSCalendar autoupdatingCurrentCalendar]];
    [dateFormatter setTimeZone:[NSTimeZone defaultTimeZone]];
    [dateFormatter setDateStyle:NSDateFormatterShortStyle]; // example: 4/13/10
    DOB.placeholder = [NSString stringWithFormat:@"Example: %@", [dateFormatter stringFromDate:[NSDate date]]];

    // code continues....
}
```

After you have configured the date formatter, the [delegate](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) can call the [dateFromString:](https://developer.apple.com/documentation/foundation/dateformatter/1409994-date) method on the formatter to convert the entered date string into an `NSDate` object, as shown in Listing 3-6.

__Listing 3-6__  Using an `NSDateFormatter` object to convert a date string to a date object

```objc
- (void)textFieldDidEndEditing:(UITextField *)textField {
    [textField resignFirstResponder];
    if ([textField.text isEqualToString:@""])
        return;
    switch (textField.tag) {
        case DOBField:
            NSDate *theDate = [dateFormatter dateFromString:textField.text];;
            if (theDate)
                [inputData setObject:theDate forKey:MyAppPersonDOBKey];
            break;
        // more switch case code here...
        default:
            break;
    }
}
```

The use of formatters does not guarantee that the entered string contains valid values—for example, a user could enter `13` for a month number in the Gregorian calendar. To ensure that the user has entered a correct value, the delegate must validate the string as explained in [Validating Entered Text](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tknbsfvbuqmjqfvjvooa). And because validation often requires a known format and range of valid values, if you configure the date formatter as in Listing 3-5 so that it is sensitive to different calendars and locales, the format cannot be known with certainty. To specify a known date format, configure the date formatter by calling [setDateFormat:](https://developer.apple.com/documentation/foundation/dateformatter/1413514-dateformat), passing in a format pattern defined by the Unicode standard.

You can also reverse the procedure shown above: Convert a date object to a string in a given format by calling the `NSDateFormatter` method [stringFromDate:](https://developer.apple.com/documentation/foundation/nsdateformatter/1415810-stringfromdate) and then assign that string to the `text` property of a text field, text view, or label.

For more information on `NSDateFormatter` and [NSNumberFormatter](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/cl/NSNumberFormatter), see _[Data Formatting Guide](../../Cocoa/Data%20Formatting%20Guide/Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgazds2i)_.

An app sometimes cannot accept the strings entered in text fields and text views without validating the value first. Perhaps the string must be in a certain format, or the value (after it is converted to a numeric value) must fall within a certain range. The best [delegation](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Delegation.html#//apple_ref/doc/uid/TP40008195-CH14) methods for validating entered strings are [textFieldShouldEndEditing:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619592-textfieldshouldendediting) for text fields and [textViewShouldEndEditing:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618603-textviewshouldendediting) for text views. These methods are called just before the text field or text view resigns [first responder](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/Responder.html#//apple_ref/doc/uid/TP40009071-CH1) status. Returning `NO` prevents that from happening, and consequently the text object remains the focus of editing. If an entered string is invalid, you should also display an alert to inform the user of the error.

Listing 3-7 uses a regular expression to verify that the string entered in a “Social Security Number” field conforms to the format for such numbers.

__Listing 3-7__  Validating the format of a text field’s string using a regular expression

```objc
- (BOOL)textFieldShouldEndEditing:(UITextField *)textField {
    if (textField == SSN) { // SSN is an outlet
        NSString *regEx = @"[0-9]{3}-[0-9]{2}-[0-9]{4}";
        NSRange r = [textField.text rangeOfString:regEx options:NSRegularExpressionSearch];
        if (r.location == NSNotFound) {
            UIAlertView *av = [[[UIAlertView alloc] initWithTitle:@"Entry Error"
                message:@"Enter social security number in 'NNN-NN-NNNN' format"
                delegate:self cancelButtonTitle:@"OK" otherButtonTitles:nil] autorelease];
            [av show];
            return NO;
        }
    }
        return YES;
}
```

The implementation of [textViewShouldEndEditing:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618603-textviewshouldendediting) in Listing 3-8 enforces a character limit for the text entered in a text view.

__Listing 3-8__  Validating a text view’s string for allowable length

```objc
- (BOOL)textViewShouldEndEditing:(UITextView *)textView {
      if (textView.text.length > 50) {
        UIAlertView *av = [[[UIAlertView alloc] initWithTitle:@"Entry Error"
            message:@"You must enter less than 50 characters." delegate:self cancelButtonTitle:@"OK"
            otherButtonTitles:@"Clear", nil] autorelease];
        [av show];
        return NO;
    }
    return YES;
}
```

The delegate can also validate each character as it is entered into a text field by implementing the [textField:shouldChangeCharactersInRange:replacementString:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619599-textfield) method. The code in Listing 3-9 verifies that each entered character (`string`) represents a digit. (You could accomplish the same goal by specifying a [UIKeyboardTypeNumberPad](https://developer.apple.com/documentation/uikit/uikeyboardtype/uikeyboardtypenumberpad) keyboard for the text field.)

__Listing 3-9__  Validating each character as it’s entered

```objc
- (BOOL)textField:(UITextField *)textField shouldChangeCharactersInRange:(NSRange)range
replacementString:(NSString *)string {
    if ([string isEqualToString:@""]) return YES;
    if (textField.tag == SalaryFieldTag) {
        unichar c = [string characterAtIndex:0];
        if ([[NSCharacterSet decimalDigitCharacterSet] characterIsMember:c]) {
            return YES;
        } else {
            return NO;
        }
    }

    return YES;
}
```

You can also implement the [textField:shouldChangeCharactersInRange:replacementString:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619599-textfield) method to offer possible word completions or corrections to the user as they enter text.

Overlay views are small views inserted into the left and right corners of a text field. They act as controls when users tap them (frequently they are buttons) and act on the current contents of the text field. Searching and bookmarking are two common tasks for overlay views, but others are possible. This overlay view loads a web browser using the (partial) URL in the text field:

![../Art/overlay_view_2x.png](attachments/Art/overlay_view_2x.png)

To implement an overlay view, create a view of a size that fits within the height of the text field and give the view an appropriately sized image. If the view is a button or other control, specify a [target object, an action selector, and the triggering control events](https://developer.apple.com/library/archive/documentation/General/Conceptual/Devpedia-CocoaApp/TargetAction.html#//apple_ref/doc/uid/TP40009071-CH3). Usually you want an overlay view to appear when its text field is the focus of editing, so assign it to the text field’s [leftView](https://developer.apple.com/documentation/uikit/uitextfield/1619597-leftview) or [rightView](https://developer.apple.com/documentation/uikit/uitextfield/1619596-rightview) [property](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/DeclaredProperty.html#//apple_ref/doc/uid/TP40008195-CH13) in the delegate’s [textFieldDidBeginEditing:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619590-textfielddidbeginediting) method. You can control when an overlay view appears during the editing session—for example, before the user begins entering text or only after the user begins entering text—by assigning a [UITextFieldViewMode](https://developer.apple.com/documentation/uikit/uitextfield/viewmode) constant to the [leftViewMode](https://developer.apple.com/documentation/uikit/uitextfield/1619588-leftviewmode) or [rightViewMode](https://developer.apple.com/documentation/uikit/uitextfield/1619607-rightviewmode) property. Listing 3-10 illustrates how you might implement an overlay view.

__Listing 3-10__  Displaying an overlay view in a text field

```objc
- (void)textFieldDidBeginEditing:(UITextField *)textField {
     if (textField.tag == NameField && self.overlayButton) {
        textField.leftView = self.overlayButton;
        textField.leftViewMode = UITextFieldViewModeAlways;
    }
}

@dynamic overlayButton;

- (UIButton *)overlayButton {
    if (!overlayButton) {
        overlayButton = [[UIButton buttonWithType:UIButtonTypeCustom] retain];
        UIImage *overlayImage = [UIImage imageNamed:@"bookmark.png"];
        if (overlayImage) {
            [overlayButton setImage:overlayImage forState:UIControlStateNormal];
            [overlayButton addTarget:self action:@selector(bookmarkTapped:)
                forControlEvents:UIControlEventTouchUpInside];
        }
    }
    return overlayButton;
}
```

If you use a control for an overlay view, be sure to implement the action method.

To remove an overlay view, simply set the [leftView](https://developer.apple.com/documentation/uikit/uitextfield/1619597-leftview) or [rightView](https://developer.apple.com/documentation/uikit/uitextfield/1619596-rightview) property to `nil` in the [textFieldDidEndEditing:](https://developer.apple.com/documentation/uikit/uitextfielddelegate/1619591-textfielddidendediting) delegation method, as in Listing 3-11.

__Listing 3-11__  Removing the overlay view

```objc
- (void)textFieldDidEndEditing:(UITextField *)textField {

    if (textField.tag == NameFieldTag) {
        textField.leftView = nil;
    }
    // remainder of implementation....
}
```


The [textViewDidChangeSelection:](https://developer.apple.com/documentation/uikit/uitextviewdelegate/1618620-textviewdidchangeselection) method of `UITextViewDelegate` lets you track changes to the selections that a user makes in a text view. You can implement the method to obtain the selected substring and do something with it. Listing 3-12 is a whimsical example that makes all characters in the selected substring uppercase.

__Listing 3-12__  Getting the selected substring and changing it

```objc
- (void)textViewDidChangeSelection:(UITextView *)textView {
    NSRange r = textView.selectedRange;
    if (r.length == 0) {
        return;
    }
    NSString *selText = [textView.text substringWithRange:r];
    NSString *upString = [selText uppercaseString];
    NSString *newString = [textView.text stringByReplacingCharactersInRange:r withString:upString];
    textView.text = newString;
}
```

[Next](https://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/KeyboardManagement/KeyboardManagement.html)[Previous](Typographical%20Concepts.md)

