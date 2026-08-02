---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/NSUserDefaultsController.html
archived_at: '2026-07-15T07:12:07.994570Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Programming Topics](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)


[Next](Creating%20a%20Master-Detail%20Interface.md)[Previous](Bindings%20Message%20Flow.md)

# User Defaults and Bindings

Many applications provide a preferences window that allows the user to customize an application’s settings. NSUserDefaultsController provides a layer on top of NSUserDefaults and allows you to bind attributes of user interface items to the corresponding key in an application’s user defaults.

NSUserDefaultsController is a concrete subclass of NSController that implements a bindings-compatible interface to NSUserDefaults. Properties of an instance of NSUserDefaultsController are bound to user interface items to access and modify values stored using NSUserDefaults.

NSUserDefaultsController is typically used when implementing your application’s preference window interface, or when you can bind a user interface item directly to a default value. NSUserDefaults remains the primary programmatic interface to your application’s default values for the rest of your application.

By default NSUserDefaultsController immediately applies any changes made to its properties. It can be configured so that changes are not applied until it receives an `applyChanges:` message, allowing the preferences dialog to support an Apply button. NSUserDefaultsController also supports reverting to the last applied set of values, using the `revert:` method.

NSUserDefaultsController also allows you to provide a dictionary of factory defaults that can be used to reset the user configurable values for your application, usually done in response to a user clicking a Revert to Factory Defaults button.

NSUserDefaultsController provides a shared instance of itself via the class method `sharedUserDefaultsController`. This shared instance uses the NSUserDefaults instance returned by the method `standardUserDefaults` as its model, has no initial values, and immediately applies changes made through its bindings.

Care must be taken that changes to the settings of the shared user defaults controller are made before any nib files containing bindings to the shared controller are loaded. To ensure that these changes are made before any nib files are loaded, they are often implemented in the `initialize` class method of the application delegate, or in your preferences window controller.

The shared NSUserDefaultsController is always available as a bindable controller in the Bindings Info window in Interface Builder. When establishing a binding to a user default, set the Controller Key to `values`, and the Model Key Path to the key of the default.

Creating bindings programmatically requires that you retrieve the shared user defaults controller using the NSUserDefaultsController class method `sharedUserDefaultsController`. You then provide that object as the _observableController_ to the `bind:toObject:withKeyPath:options:` method.

The example in Listing 1 establishes a binding between an NSTextField (`theTextField`) and the `userName` default using the shared user defaults controller.

__Listing 1__  Binding the userName defaults key to an NSTextField programmatically

```
 [theTextField bind:@"value"
             toObject:[NSUserDefaultsController sharedUserDefaultsController]
          withKeyPath:@"values.userName"
              options:[NSDictionary dictionaryWithObject:[NSNumber numberWithBool:YES]
                                                  forKey:@"NSContinuouslyUpdatesValue"]];
```


The initial values dictionary allows you to provide a means to reset the user configurable default values to the factory defaults. Typically these values represent a subset of the defaults that your application registers using the NSUserDefaults method `registerDefaults:`.

Calling the NSUserDefaultsController method `setInitialValues:` should not be considered a replacement for registering your application's preference defaults using NSUserDefault's `registerDefaults:` method.

The example in Listing 2 loads the default values from a file in the application wrapper, registers those values with NSUserDefaults, and then registers a subset of the values as the initial values of the shared user defaults controller. The `setupDefaults` method would be called from your application delegate’s `initialize` class method.

__Listing 2__  Changing the initial values of the sharedUserDefaultsController instance

```objc
+ (void)setupDefaults
{
    NSString *userDefaultsValuesPath;
    NSDictionary *userDefaultsValuesDict;
    NSDictionary *initialValuesDict;
    NSArray *resettableUserDefaultsKeys;

    // load the default values for the user defaults
    userDefaultsValuesPath=[[NSBundle mainBundle] pathForResource:@"UserDefaults"
                               ofType:@"plist"];
    userDefaultsValuesDict=[NSDictionary dictionaryWithContentsOfFile:userDefaultsValuesPath];

    // set them in the standard user defaults
    [[NSUserDefaults standardUserDefaults] registerDefaults:userDefaultsValuesDict];

    // if your application supports resetting a subset of the defaults to
    // factory values, you should set those values
    // in the shared user defaults controller
    resettableUserDefaultsKeys=[NSArray arrayWithObjects:@"Value1",@"Value2",@"Value3",nil];
    initialValuesDict=[userDefaultsValuesDict dictionaryWithValuesForKeys:resettableUserDefaultsKeys];

    // Set the initial values in the shared user defaults controller
    [[NSUserDefaultsController sharedUserDefaultsController] setInitialValues:initialValuesDict];
}
```


When a method that is key-value coding compliant attempts to get a value for a key from an NSUserDefaultsController the following search pattern is used:

1. The value of a corresponding key in `values`
2. The value of a corresponding key in the NSUserDefaults instance returned by the NSUserDefaultsController method `defaults`.
3. The value of a corresponding key in the initial values dictionary

If no corresponding value is found, `nil` is returned.

The search path is somewhat different when you retrieve the result directly from the NSUserDefaults instance associated with the NSUserDefaultsController. In that case, any unapplied values in the NSUserDefaultsController, as well as the values in the initial values dictionary are ignored.

Although NSUserDefaults should remain your primary programmatic interface to the user defaults, some circumstances require that you get and set the default values contained in an NSUserDefaultsController instance directly. For example, when implementing portions of your preferences window that don’t directly interact with an existing binding, such as setting a font or choosing a directory path.

The NSUserDefaultsController method `values` returns a KVC-compliant object that is used to access these default values. To get the value of a default, use the `valueForKey:` method.

```
[[theDefaultsController values] valueForKey:@"userName"];
```

Similarly, to set a value for a default, use `setValue:forKey:`.

```
[[theDefaultsController values] setValue:newUserName
                                 forKey:@"userName"];
```

The NSUserDefaultsController automatically provides notification of the value change to any established bindings for that key path.

[Next](Creating%20a%20Master-Detail%20Interface.md)[Previous](Bindings%20Message%20Flow.md)

