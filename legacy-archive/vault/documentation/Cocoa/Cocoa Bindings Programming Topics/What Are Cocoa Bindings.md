---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/WhatAreBindings.html
archived_at: '2026-07-15T07:12:09.006538Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Programming Topics](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)


[Next](How%20Do%20Bindings%20Work.md)[Previous](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)

# What Are Cocoa Bindings?

In the simplest functional sense, the Cocoa bindings technology provides a means of keeping model and view values synchronized without you having to write a lot of “glue code.” It allows you to establish a mediated connection between a view and a piece of data, “binding” them such that a change in one is reflected in the other.

This article describes what the technology offers and how it makes writing applications easier. It also introduces the idea that rather than completely reimplementing an existing application to make use of bindings, you can incorporate bindings in stages.

This article also describes on a conceptual level how Cocoa bindings work, and the design patterns you should adopt. It gives a brief overview of the Model-View-Controller design pattern, and why it is beneficial. It then gives a conceptual overview of how the main technologies that underpin Cocoa bindings—key-value coding, key-value observing, and key-value binding—work, and how they inter-relate. The article finally explains the role of the controller classes that Cocoa bindings provide and why you should use them.

[How Do Bindings Work?](How%20Do%20Bindings%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3tglkdjjbeksscjbea) describes the supporting technologies in greater detail.

The Cocoa bindings technology offers a way to increase the functionality and consistency of your application while at the same time decreasing the amount of code you have to write and maintain. It takes care of most aspects of user interface management for you by allowing you to off load the work of custom glue code onto reusable pre-built controllers. It helps you build polished, easy-to-use applications that leverage object relationships, provide sortable tables, and include intelligent selection management.

Typically you do not need to completely rewrite your application in order to adopt Cocoa bindings. For example, it is likely that you can factor out User Preferences to be managed by Cocoa bindings without affecting the rest of an application. You will find it easier to make use of Cocoa bindings if your application adopts the recommended design patterns.

Cocoa applications generally adopt the Model-View-Controller (MVC) design pattern. When you develop a Cocoa application, you typically use model, view, and controller objects, each of which performs a different function. Model objects represent data and are typically saved to a file or some other permanent data store. View objects display model attributes. Controller objects act as go-betweens, to make sure that what a view displays is consistent with the corresponding model value and that any updates a user makes to a value in a view are propagated to the model. An understanding of the MVC design pattern is essential to fully understand and leverage Cocoa bindings. If you need to know more, read “The Model-View-Controller Design Pattern.”

If you adopt the MVC design pattern, much of your application code is easier to reuse and extend—you can reuse model and view classes in different applications. Much of the implementation of a controller object consists of what is commonly referred to as “glue code.” Glue code is the code that keeps the model values and views synchronized, and is unique to each application. It is typically tedious and cumbersome to write, contributes little to the fundamental function of the application, but you must do it well to provide a good user experience.

__Figure 1__  Controllers provide glue code

!

Cocoa bindings replace much of the glue code with reusable controllers and provide an infrastructure that allows you to connect the user interface with an application’s data.

Cocoa uses a number of terms that are commonly used in computer science. To avoid misunderstanding, they are defined in the “Terminology” section of _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_ with their particular meaning in the context of Cocoa bindings.

A binding is an attribute of one object that may be bound to a property in another such that a change in either one is reflected in the other. For example, the “value” binding of a text field might be bound to the temperature attribute of a particular model object. More typically, one binding might specify that a controller object “presents” a model object and another binding might specify that the value of a text field be tied to the temperature property of the object presented by the controller.

Although the following examples concentrate on simple cases, bindings are not restricted to the display of textual or numeric values. Among other things, a binding might specify the color in which text should be displayed, whether a view is hidden or not, or what message and arguments should be sent when a button is pressed.

Take as an example a very simple application in which the values in a text field and a slider are kept synchronized. Consider first an implementation that does _not_ use bindings. The text field and slider are connected directly to each other using target-action, where each is the other’s target and the action is `takeFloatValueFrom:` as shown in Figure 2. (If you do not understand this, you should read Getting Started With Cocoa.)

__Figure 2__  A simple Cocoa application

!

This example illustrates the dynamism of the Cocoa environment—the values of two user interface objects are kept synchronized without writing any code, even without compiling. It also serves to illustrate the target-action design pattern (for more details, read The Target-Action Paradigm).

The major flaw from which this example suffers is that, as it is, it has almost no real-world application. In order to find out the value to which either the slider or the text field has been set, and update a model attribute accordingly, you need connections to the text field and slider, and have to write some code. You typically use a controller that is connected to both (using outlets) and to which both are connected (using target-action), as illustrated in [Figure 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3teljrg4zdiobwfvbecssdiveecra).

__Figure 3__  Slider example using target-action

!

When a user moves the slider, it sends an action message to its target (the controller). The controller in turn updates the value in the model, and synchronizes the user interface (the text field and the slider). Although this example is not particularly difficult, the situation becomes more complex if you use more complicated models and displays, especially if you use, for example, table views that allow multiple selections, or if a value may be displayed in a different window. And you have to write all the code to support this functionality.

Cocoa bindings uses prebuilt controller objects (subclasses of NSController) and supporting technologies to keep values synchronized automatically. The application design for an implementation of the slider example that uses bindings is shown in Figure 4.

__Figure 4__  Slider demonstration using bindings

!

Note that this implementation does not use the target-action pattern. The slider does not send an action message to the controller. Instead, as the slider moves, it informs the controller directly that the value of its content’s number has changed and what the value is. The controller updates the model and in turn informs the text field and slider that the value they are displaying has changed. (In examples as simple as this controllers are not really necessary, however in most cases they are.) The mechanisms used to relay information are explained later in this article and in greater detail in [How Do Bindings Work?](How%20Do%20Bindings%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3tglkdjjbeksscjbea), but it is important to appreciate that in most cases you will not have to write any glue code.

Many bindings allow you to specify options to customize their behavior. There are three types of option: value transformers, placeholders, and other parameters.

A value transformer, as its name implies, applies a transformation to a value. A value transformer may also allow reverse transformations. The Foundation framework provides the abstract NSValueTransformer class and several convenient transformers, including one that negates a value—that is, it turns a Boolean `YES` into `NO` (and vice versa). You can also implement your own transformers.

To see how transformers might be useful, suppose that in the previous example the number in the model represents temperature in degrees Fahrenheit, but that you want to display the value in Celsius. You could implement a reversible value transformer that converts values from one scale to the other. If you then specify it as the transformer option for the text field and slider, as shown in [Figure 5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3teljrg44tqnzzfvbecssiizducsi), the user interface displays the temperature in Celsius, and any new values entered using the slider or text field converted to Fahrenheit.

__Figure 5__  Displaying temperature using transformers

!

To learn more about transformers read _[Value Transformer Programming Guide](../Value%20Transformer%20Programming%20Guide/Introduction%20to%20Value%20Transformers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tk2i)_ (the article also shows an implementation of the Fahrenheit to Celsius transformer).

Placeholder options allow you to specify what a view should display: if the value of the property to which it is bound is null (nil); if there is no selection; if there is a multiple selection; or if for some other reason the value is not applicable.

In addition to value transformers and placeholders, some bindings offer a variety of other options, such as whether the value of the binding is updated as edits are made to the user interface item, or whether the editable state of a user interface item is automatically configured based on the controller’s selection. For a complete list of all the binding options available, see _[Cocoa Bindings Reference](../Cocoa%20Bindings%20Reference/Introduction%20to%20Cocoa%20Bindings%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ds2i)_.

The Cocoa bindings architecture extends the traditional Cocoa MVC configuration, where there is a single custom-built controller that manages the user interface. It provides a set of reusable controller classes that inherit from an abstract superclass, NSController. In a bindings-based application there may be several controllers—your own (such as an NSWindowController subclass, managing a document’s user interface) and others that are subclasses of NSController and manage different parts of the user interface. You might also create your own subclasses of the standard Application Kit controller classes—in particular you might subclass NSArrayController to customize sorting and filtering behavior.

Other figures in this document present a convenient shorthand. Although the NSController instance is conceptually bound directly to its model object, in most situations the binding will be “indirect,” to a variable in your document object, as shown in Figure 6.

__Figure 6__  Typical bindings configuration using existing controller

!

Cocoa bindings rely primarily on two other technologies, key-value coding (KVC) and key-value observing (KVO). Bindings themselves are established using key-value binding (KVB) as illustrated in Figure 7. In practice you typically need to understand these technologies only if you want to create your own custom view with bindings. If you want to use bindings, the only requirement that is imposed on you is that your model classes must be compliant with key-value coding conventions for any properties to which you want to bind.

A binding is established with a `bind:toObject:withKeyPath:options:` message which tells the receiver to keep its specified attribute synchronized—modulo the options—with the value of the property identified by the key path of the specified object. The receiver must watch for relevant changes in the object to which it is bound and react to those changes. The receiver must also inform the object of changes to the bound attribute. After a binding is established there are therefore two aspects to keeping the model and views synchronized: responding to user interaction with views, and responding to changes in model values.

__Figure 7__  Bindings established using key-value binding

!

In a view-initiated update a value changed in the user interface is passed to the controller, which in turn pushes the new value onto the model. To preserve the abstraction required to allow this to work with any controller or model object, the system uses a common access protocol—key-value coding.

In a model-initiated update models notify controllers, and controllers notify views, of changes to values in which interest has been registered using a common protocol—key-value observing. Note that a model-initiated update can be triggered by direct manipulation of the model—for example by a Scripted Apple event—or as the result of a view-initiated update—a change to the temperature made by editing the Celsius field must be propagated back to the slider.

Key-value coding is a mechanism whereby you can access a property in an object using the property’s name as a string—the “key.” You can also use key paths to follow relationships between objects. For example, given an Employee class with an attribute `firstName`, you could retrieve an employee’s first name using key-value coding with the key `firstName`. If Employee has a relationship called “manager” to another Employee, you could retrieve an employee’s manager’s first name using key-value coding with the key path `manager.firstName`. For more details, see _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_.

Recall that a binding specifies the key path to a property to which a given attribute is bound. If the value in the slider or the text field is changed, it uses key-value coding—using the key path specified by the binding as the key—to communicate that change directly to the controller, as illustrated in Figure 8. Note that the arrows in this figure represent the direction in which messages are sent and in which information flows. The new value is passed from the user interface widget to the controller, and from the controller to the model.

__Figure 8__  Using key-value-coding to update values

!

Key-value observing is a mechanism whereby an object can register with another to be notified of changes to the value of a property. When one object is bound to another object, it registers itself as an observer of the relevant property of that object. In the current example, the text field and slider register as observers of the temperature property of the controller’s content, as illustrated in Figure 9.

__Figure 9__  Key-value observing—registering observers

!

Note that the arrows shown in Figure 9 indicate direction of observation, not of data flow. Observation is a “passive” process (akin to registering to receive notifications from an NSNotificationCenter). When a value changes, the observed object sends a message to interested observers to notify them, as illustrated in Figure 10. The arrows in Figure 10 show the direction in which messages are sent.

__Figure 10__  Key-value observing—notification of observers

!

Bindings can, in principle, be made between almost any two objects, provided that they are KVC-compliant and KVO-compliant. A view could bind directly to a model object. Bindings-based applications, however, use controller objects to manage individual model objects and collections of model objects and to interface to the user preferences system.

It is possible to make bindings directly to your model objects or to controllers that do not inherit from NSController—however you lose (or must reimplement) functionality provided by the Application Kit’s controller objects.

- NSController instances manage their current selection and placeholder values. This allows a view to display an appropriate value if the controller’s selection is null, or if there is a multiple selection.
- NSController (and Application Kit user interface elements that support binding) implements the NSEditor and NSEditorRegistration protocols. The NSEditorRegistration protocol provides a means for an editor (a view) to inform a controller when it has uncommitted changes. The NSEditor protocol provides a means for requesting that the receiver commit or discard any pending edits.

  For example, if a user is typing in a text field and then clicks a button, the controller ensures that the model object is updated with the complete contents of the text field before the button action takes place.

  Although the methods are typically invoked on user interface elements by a controller they can also be sent to a controller, for example in response to a user’s attempt to save a document or quit an application.

NSController is an abstract class. Its concrete subclasses are NSObjectController, NSUserDefaultsController, NSArrayController, and NSTreeController. NSObjectController manages a single object and provides the functionality discussed so far. NSUserDefaultsController provides a convenient interface to the preferences system.

NSArrayController and NSTreeController manage collections of model objects and track the current selection. The collection controllers also allow you to add objects to, and remove objects from, the content collection. The objects that the collection controllers manage don’t even have to be in an array—your container can implement suitable methods (“indexed accessor” methods, defined in the NSKeyValueCoding protocol) to present the values to the controller as if they were in an array.

You can make bindings for most of the Application Kit view classes, such as NSButton and NSTableView. Using an array controller, for example, you can bind the contents of a pop-up menu to objects in an array. The remainder of this article presents an example that is moderately complex. Although the details are intentionally left vague it nevertheless serves to illustrate a number of points, and provides examples of more complex bindings.

Consider a game application in which the user manages a number of combatants, from which they can select one as an attacker. A combatant can carry three weapons, one of which is selected at any time. In the application, the list of combatants is shown in a table view, the window’s title shows the attacker’s name, and a pop-up menu shows the currently selected weapon, as shown in [Figure 11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3teljrhaytcnjtfvbecssji5eumri).

__Figure 11__  User interface for Combatants application

!

Combatants are represented by instances of the Combatant class. In the Combatant class, each weapon is referenced as a separate instance variable, as shown in Figure 12. By implementing suitable “indexed” accessor methods (defined by the key-value coding protocol), however, the Combatant class can allow an array controller to access the weapons as if they were in an array.

__Figure 12__  Combatant class

!

When the user chooses an attacker from the table view, the window title is updated to reflect the attacker’s name, and the title of the pop-up menu is updated to reflect the attacker’s selected weapon. When the user activates the pop-up its contents are created dynamically from the set of weapons carried by the combatant. When the user selects a menu item, the combatant’s selected weapon is set to that corresponding to that menu item. If a different attacker is selected, the pop-up, selection and window title update accordingly.

[Figure 13](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3teljrhaytembsfvbecssijfauesq) illustrates how the user interface of the Combatants application can be implemented using bindings. The table view is bound to an array controller that manages an array of combatants. The window title is bound to the name of the selected combatant. The pop-up menu retrieves its list of items from an array controller bound to the attacker’s weapons “array,” and its selection is bound to the attacker’s selected weapon.

__Figure 13__  Combatants application managed by bindings

!!

This example illustrates a number of points:

- In an application you can use more than one controller object.
- Different aspects of a user interface element may be bound to different controllers.
- You can use your own custom model classes.

Finally, it should be emphasized that the example requires no actual code to set up the user interface—the controllers and bindings can all be created in Interface Builder. This represents a considerable reduction in programming effort compared with the traditional target-action based approach.

[Next](How%20Do%20Bindings%20Work.md)[Previous](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)

