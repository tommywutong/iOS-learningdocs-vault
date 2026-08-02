---
title: Control and Cell Programming Topics
apple_id: 10000015i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2008-10-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ControlCell/Tasks/ValidatingControlEntries.html
archived_at: '2026-07-15T07:13:51.432439Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Control and Cell Programming Topics](Introduction%20to%20Control%20and%20Cell%20Programming%20Topics%20for%20Cocoa.md)


[Next](Displaying%20Cell%20Values.md)[Previous](Manipulating%20Cells%20and%20Controls.md)

# Validating Control Entries

NSControl provides the delegation method `control:isValidObject:` for validating the contents of cells embedded in controls (instances of NSTextField and NSMatrix in particular). In validating you check for values that are permissible as objects, but that are undesirable in a given context, such as a date field in which dates should never be in the future, or zip codes that are valid for a certain state.

The method `control:isValidObject:` is invoked when the insertion point leaves a cell (that is, the associated control relinquishes first-responder status) but before the string value of the cell's object is displayed. Return `YES` to allow display of the string and `NO` to reject display and return the cursor to the cell. The following Objective-C example evaluates an object (an NSDate) and rejects it if the date is in the future:

```objc
- (BOOL)control:(NSControl *)control isValidObject:(id)obj
{
    if (control == contactsForm) {
        if (![obj isKindOfClass:[NSDate class]]) return NO;
        if ([[obj laterDate:[NSDate date]] isEqual:obj]) {
            NSRunAlertPanel(@"Date not valid",
                @"Reason: date in future", NULL, NULL, NULL);
            return NO;
        }
    }
    return YES;
}
```

NSControl provides several delegate methods for its subclasses that allow text editing, such as NSTextField and NSMatrix. Some are invoked when formatters for a control’s cells cannot format a string (`control:didFailToFormatString:errorDescription:`) or reject a partial string entry (`control:didFailToValidatePartialString:errorDescription:`). NSControl also provides `control:textView:doCommandBySelector:`, which allows delegates the opportunity to detect and respond to key bindings, such as `complete:` (name completion). Note that although NSControl defines delegate methods, it does not itself have a delegate. Any subclass that uses the delegate methods must contain a delegate and the methods to get and set it.

[Next](Displaying%20Cell%20Values.md)[Previous](Manipulating%20Cells%20and%20Controls.md)

