---
title: Accessibility Programming Guidelines for Mac
apple_id: 10000118i
resource_type: Guide
platform: macOS
topic: User Experience
technology: null
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Accessibility/cocoaAXAccessEnabling/cocoaAXAccessEnabling.html
archived_at: '2026-07-15T05:25:25.752766Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Accessibility Programming Guidelines for Mac](Introduction%20to%20Accessibility%20Programming%20Guidelines%20for%20Cocoa.md)


[Next](Supporting%20Attributes.md)[Previous](Accessibility%20Notifications.md)

# Access Enabling a Cocoa Application

This article describes the tasks you may have to perform to access enable a Cocoa application. Because many Cocoa classes support accessibility by adopting the NSAccessibility protocol, standard objects are already accessible to a great degree. For the most part, you have to add code for only the application-specific information that Cocoa cannot automatically supply.

This article is divided into sections that describe the tasks associated with specific scenarios in your application. Read this article to find out which of the tasks described in each section are necessary in your application. For example, the tasks in the first section, Provide Descriptive Information for All Elements, are required for all applications. The tasks in [Make Custom Classes and Subclasses Accessible](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2tsljyhe2dsnq), on the other hand, are required for only those applications that define custom classes or subclasses.

An assistive application needs to be able to describe all accessible user interface elements to the user. Often, an assistive application can present the title of the element to the user, but sometimes an element’s title is either unavailable or not sufficiently descriptive. Therefore, you must examine your application and ensure that all accessibility objects supply descriptive information about themselves in either the title or description attributes.

First, determine if a given accessibility object already includes the title attribute. An object that displays a text title as part of its visual interface, such as an OK button, already includes the title attribute with the value of the displayed text. Such an object does not need a description attribute because its title is sufficient to convey its purpose to the user.

A button that displays an icon instead of a text title, however, does not have a title attribute. An example of such an object is a “back” button that displays a left-pointing arrow instead of the word “Back”. An assistive application cannot describe such a button’s purpose to a user unless the accessibility object representing the button includes the description attribute. If you have such an object in your application, you must supply an appropriate description in the description attribute.

Some user interface elements do not display a title, but are accompanied by a piece of static text that serves as a title. An example of this is a set of editable text fields accompanied by the string “Address:”. To a sighted user, the proximity of the string to the text fields implies that “Address:” serves as the title for the entire set of text fields. An assistive application, however, cannot make this determination. If you use static text objects to title user interface elements (or sets of user interface elements), you must make the relationship between them clear to assistive applications.

To do this, you create an accessibility object to represent the static text object. Then, in each accessibility object representing one of the titled user interface elements (each of the address fields, in this example), you add the `NSAccessibilityTitleUIElementAttribute` attribute. The value of this attribute is the accessibility object representing the static text title. Finally, in the static text title accessibility object, add the `NSAccessibilityServesAsTitleForUIElementsAttribute` attribute. The value of this attribute is an array of the accessibility objects for which this static text object serves as title (in this example, the array comprises the set of editable text fields).

The title and description attributes provide information about the layout of your application’s user interface and so their values are static and not settable by an assistive application. This means you can choose to use a convenience method to provide these values instead of having to subclass the accessibility object and override the appropriate methods. See [Supporting Attributes](Supporting%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3delkcineueskeivda) for details on the two techniques you can use to support these descriptive attributes.

In OS X version 10.4, the NSAccessibility protocol introduced two new attributes that allow you to describe conceptual links between accessibility objects. Conceptual links are those that are visually implied onscreen, but that are difficult for an assistive application to determine. An example of such a link is in the Mail application where the main window’s upper view contains a list of message headers and the lower view displays the content of a selected message. It is obvious to a sighted user that the text in the lower view is the contents of the selected message header in the upper view, but an assistive application cannot make this determination. Another example is the relationship between a search field and the view containing the search results. An assistive application has no way to know where you display search results unless you make clear the relationship between the search field and the results view.

If your application includes elements that are linked conceptually, you should ensure that the accessibility objects representing those elements include the `NSAccessibilityLinkedUIElementsAttribute` attribute. The value of this attribute is an array of accessibility objects to which the element is linked. An assistive application can use the accessibility objects in the array to provide to the user a shortcut between the linked objects. Without this attribute, a user has to know which views are conceptually linked and must step through every intervening object to move between them.

Like the description and title attributes, the value of the linked-elements attribute is part of the layout of your application’s user interface. An assistive application does not need to set the value of this attribute, so you have the option of using a convenience method to supply the value or of subclassing the accessibility objects and overriding the appropriate methods. For more details on both these techniques, see [Supporting Attributes](Supporting%20Attributes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga3delkcineueskeivda).

Sometimes, your application uses a view object that contains substructure you need to make accessible. However, some NSView objects are implemented as monolithic objects; objects that, as far as Cocoa is concerned, contain no substructure. NSScrollBar is an example of such an object. Even though a sighted user can manipulate separately the parts of a scroll bar (the scroller, the page-up and page-down regions in the scroll track, and the scroll arrows), Cocoa does not represent these parts as separate objects. Therefore, an assistive application cannot make any of these subviews directly accessible to a user. This also affects the determination of mouse location and keyboard focus. A scroll bar can tell an assistive application that it has keyboard focus, for example, but not the precise part of itself that has keyboard focus.

If you use an object, such as an NSScrollBar, in your application and you need to make its substructure accessible, you must create an accessibility object to represent each part. The accessibility object must, of course, implement the NSAccessibility protocol, but it can be very lightweight. This is because it can ask its parent (the NSScrollBar object, in this example) to supply most of the information for which it might be asked, such as its containing window or position. This accessibility object’s main responsibility is to allow an otherwise inaccessible part of the user interface to be represented in the application’s accessibility hierarchy.

The most efficient way to create these accessibility objects is to define a utility class that implements the NSAccessibility protocol. Then, you create an instance of this class as needed and allow it to provide only the information that is specific to the subview it represents. In particular, the utility class should implement the hit-test and focus-test methods. This way, the accessibility object representing a subview can return itself when it receives a hit-test or focus-test message.

In most cases, it works well to create these accessibility objects as they are asked for; it’s not necessary to create and store them in advance. This is because these accessibility objects will never be asked for (and therefore never created) if the user has not enabled access by assistive applications in the Universal Access System Preferences.

Your utility class should create an instance given the parent accessibility object of the subview and its role. This allows you easily to provide some of the required attributes for the new accessibility object. In the NSScrollBar example, the parent object is the accessibility object representing the NSScrollBar as a whole and the role is `NSAccessibilityScrollBarRole`.

If you implement custom classes or custom subclasses of Cocoa classes in your application, you may need to create accessibility objects to represent them. Any custom subclass of NSObject, for example, does not inherit any accessibility support and must implement the methods to supply supported attributes and actions and to return hit-test and focus-test information.

Although NSObject does not adopt the NSAccessibility protocol, the following common base classes do:

- NSApplication
- NSWindow
- NSView
- NSControl
- NSCell

Although all the classes listed above implement the NSAccessibility protocol, they each support a different set of attributes, actions, and methods and each has its own default ignored status. It’s important to be aware of the base set of functionality of these classes so you can determine what your subclass needs to override. Table 1 shows the default accessibility support of each class.

__Table 1__  AppKit classes and default accessibility support

| Class | Supported attributes | Implemented methods | Ignored by default |
| NSApplication | role, role description, menu bar, windows, active, main window, key window, focused accessibility object (UIElement) | hit-testing, focus testing | No |
| NSWindow | role, role description, title, focused, parent, position, size, main, key | hit-testing, focus testing | No |
| NSView | role, role description, help, focused, parent, children, window, position, size | hit-testing, focus testing, keystroke handling | Yes |
| NSControl | role, role description, help, focused, parent, children, window, position, size, enabled | position and size of child methods | Yes, unless control has multiple child cells |
| NSCell | role, role description, help, focused, parent, children, window, position, size, enabled, value | hit-testing, focus-testing | No |

When you need to make a custom class or subclass accessible, you create an accessibility object to represent it, as described in [Make Substructure Accessible](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2tsljyhe2dqny). Be sure to take into account the default ignored status of your chosen base class so you can override this value if appropriate for your subclass.

[Next](Supporting%20Attributes.md)[Previous](Accessibility%20Notifications.md)

