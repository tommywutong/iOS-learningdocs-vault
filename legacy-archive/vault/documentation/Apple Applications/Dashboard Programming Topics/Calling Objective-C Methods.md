---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/ObjCFromJavaScript.html
archived_at: '2026-07-15T05:17:34.807037Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Delivering%20Widgets.md)[Previous](Creating%20a%20Widget%20Plug-in.md)

# Calling Objective-C Methods

The web scripting capabilities of WebKit permit you to access Objective-C properties and call Objective-C methods from the JavaScript scripting environment.

An important but not necessarily obvious fact about this bridge is that it does _not_ allow _any_ JavaScript script to access Objective-C. You cannot access Objective-C properties and methods from a web browser unless a custom plug-in has been installed. The bridge is intended for people using custom plug-ins and JavaScript environments enclosed within WebKit objects (for example, a WebView).

The WebScripting informal protocol, defined in `WebScriptObject.h`, defines methods that you can implement in your Objective-C classes to expose their interfaces to a scripting environment such as JavaScript. Methods and properties can both be exposed. To make a method valid for export, you must assure that its return type and all its arguments are Objective-C objects or basic data types like `int` and `float`. Structures and non object pointers will not be passed to JavaScript.

Method argument and return types are converted to appropriate types for the scripting environment. For example:

- JavaScript numbers are converted to NSNumber objects or basic data types like `int` and `float`.
- JavaScript strings are converted to NSString objects.
- Other JavaScript objects are wrapped as WebScriptObject instances.

Instances of all other classes are wrapped before being passed to the script, and unwrapped as they return to Objective-C.

As an exception, JavaScript arrays cannot be cleanly mapped to `NSArray` objects because they are a hybrid between a numerically-indexed array and an associative array. To avoid loss of data during the mapping, you must instead use the [webScriptValueAtIndex:](https://developer.apple.com/documentation/webkit/webscriptobject/1528530-webscriptvalue) and [setWebScriptValueAtIndex:value:](https://developer.apple.com/documentation/webkit/webscriptobject/1528561-setwebscriptvalueatindex) methods.

Let’s look at a sample class. In this case, we will create an Objective-C address book class and expose it to JavaScript. Let’s start with the class definition:

```objc
@interface BasicAddressBook: NSObject {
}
+ (BasicAddressBook *)addressBook;
- (NSString *)nameAtIndex:(int)index;
@end
```

Now we’ll write the code to publish a `BasicAddressBook` instance to JavaScript:

```
BasicAddressBook *littleBlackBook = [BasicAddressBook addressBook];

id win = [webView windowScriptObject];
[win setValue:littleBlackBook forKey:@"AddressBook"];
```

Once you expose these methods to JavaScript (described at the end of this section), you should be able to access your basic address book from the JavaScript environment and perform actions on it using standard JavaScript functions.

Now, let’s make an example showing how you can use the `BasicAddressBook` class instance in JavaScript. In this case, we’ll print the name of a person at a certain index in our address book:

```
function printNameAtIndex(index) {
    var myaddressbook = window.AddressBook;
    var name = myaddressbook.nameAtIndex_(index);
    document.write(name);
}
```

You may have noticed one oddity in the previous code example. There is an underscore after the JavaScript call to the Objective-C `nameAtIndex` method. In JavaScript, it is called `nameAtIndex_`. This is an example of the default method renaming scheme in action.

Unless you implement `webScriptNameForSelector` to return a custom name, the default construction scheme is used. It is your responsibility to ensure that the returned name is unique to the script invoking this method. If your implementation of `webScriptNameForSelector` returns `nil` or you do not implement it, the default name for the selector will be constructed as follows:

- Any colon (`:`) in the Objective-C selector is replaced by an underscore (`_`).
- Any underscore in the Objective-C selector is prefixed with a dollar sign (`$`).
- Any dollar sign in the Objective-C selector is prefixed with another dollar sign.

The following table shows example results of the default method name constructor:

| Objective-C selector | Default script name for selector |
| --- | --- |
| `setFlag:` | `setFlag_` |
| `setFlag:forKey:withAttributes:` | `setFlag_forKey_withAttributes_` |
| `propertiesForExample_Object:` | `propertiesForExample$_Object_` |
| `set_$:forKey:withDictionary:` | `set$_$$_forKey_withDictionary_` |

Since the default construction for a method name can be confusing depending on its Objective-C name, you would benefit yourself and the users of your class if you implement `webScriptNameForSelector` and return more human-readable names for your methods.

Getting back to the BasicAddressBook, now we’ll implement `webScriptNameForSelector` and `isSelectorExcludedFromWebScript` for our `nameAtIndex` method. In our BasicAddressBook class implementation, we’ll add this:

```objc
+ (NSString *) webScriptNameForSelector:(SEL)sel
{
    ...

    if (sel == @selector(nameAtIndex:))
            name = @"nameAtIndex";

    return name;
}

+ (BOOL)isSelectorExcludedFromWebScript:(SEL)aSelector
{
    if (sel == @selector(nameAtIndex:)) return NO;
    return YES;
}
```

Now we can change our JavaScript code to reflect our more logical method name:

```
function printNameAtIndex(index) {
    var myaddressbook = window.AddressBook;
    var name = myaddressbook.nameAtIndex(index);
    document.write(name);
}
```


For more information about using Objective-C from JavaScript and vice versa, see the following documents:

- _[CallJS](../../../samplecode/CallJS/CallJS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimruge)_ sample code shows how to call JavaScript from Objective-C and vice versa.
- _[Birthdays](../../../samplecode/Birthdays/Birthdays.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojygi)_ sample code shows how to use a WebKit plug-in from JavaScript.
- _[WebKit Objective-C Framework Reference](https://developer.apple.com/documentation/webkit)_ provides more information on excluding methods and properties from the JavaScript environment.
- _[WebKit Plug-In Programming Topics](../../Internet%20Web/WebKit%20Plug-In%20Programming%20Topics/Introduction%20to%20WebKit%20Plug-in%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmrr)_ provides general information about writing WebKit plug-ins.

[Next](Delivering%20Widgets.md)[Previous](Creating%20a%20Widget%20Plug-in.md)

