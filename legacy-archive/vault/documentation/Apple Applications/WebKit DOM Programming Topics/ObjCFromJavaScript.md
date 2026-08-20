---
title: WebKit DOM Programming Topics
apple_id: TP40001483
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: null
technology: WebKit
published: '2017-09-19'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/SafariJSProgTopics/ObjCFromJavaScript.html
archived_at: '2026-07-15T05:18:10.829848Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit DOM Programming Topics](index.md)



## Calling Objective-C Methods

The web scripting capabilities of WebKit permit you to access Objective-C properties and call Objective-C methods from the JavaScript scripting environment.

An important but not necessarily obvious fact about this bridge is that it does _not_ allow _any_ JavaScript script to access Objective-C. You cannot access Objective-C properties and methods from a web browser unless a custom plug-in has been installed. The bridge is intended for people using custom plug-ins and JavaScript environments enclosed within WebKit objects (for example, a WebView).

### How to Use Objective-C in JavaScript

The WebScripting informal protocol, defined in `WebScriptObject.h`, defines methods that you can implement in your Objective-C classes to expose their interfaces to a scripting environment such as JavaScript. Methods and properties can both be exposed. To make a method valid for export, you must assure that its return type and all its arguments are Objective-C objects or basic data types like `int` and `float`. Structures and non object pointers will not be passed to JavaScript.

Method argument and return types are converted to appropriate types for the scripting environment. For example:

- JavaScript numbers are converted to NSNumber objects or basic data types like `int` and `float`.
- JavaScript strings are converted to NSString objects.
- Other JavaScript objects are wrapped as WebScriptObject instances.

Instances of all other classes are wrapped before being passed to the script, and unwrapped as they return to Objective-C.

As an exception, JavaScript arrays cannot be cleanly mapped to `NSArray` objects because they are a hybrid between a numerically-indexed array and an associative array. To avoid loss of data during the mapping, you must instead use the [webScriptValueAtIndex:](https://developer.apple.com/documentation/webkit/webscriptobject/1528530-webscriptvalue) and [setWebScriptValueAtIndex:value:](https://developer.apple.com/documentation/webkit/webscriptobject/1528561-setwebscriptvalueatindex) methods.

### A Sample Objective-C Class

Let’s look at a sample class. In this case, we will create an Objective-C address book class and expose it to JavaScript. Let’s start with the class definition:

1. `@interface BasicAddressBook: NSObject {`
2. `}`
3. `+ (BasicAddressBook *)addressBook;`
4. `- (NSString *)nameAtIndex:(int)index;`
5. `@end`

Now we’ll write the code to publish a `BasicAddressBook` instance to JavaScript:

1. `BasicAddressBook *littleBlackBook = [BasicAddressBook addressBook];`
3. `id win = [webView windowScriptObject];`
4. `[win setValue:littleBlackBook forKey:@"AddressBook"];`

Once you expose these methods to JavaScript (described at the end of this section), you should be able to access your basic address book from the JavaScript environment and perform actions on it using standard JavaScript functions.

Now, let’s make an example showing how you can use the `BasicAddressBook` class instance in JavaScript. In this case, we’ll print the name of a person at a certain index in our address book:

1. `function printNameAtIndex(index) {`
2. `var myaddressbook = window.AddressBook;`
3. `var name = myaddressbook.nameAtIndex_(index);`
4. `document.write(name);`
5. `}`

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

1. `+ (NSString *) webScriptNameForSelector:(SEL)sel`
2. `{`
3. `...`
5. `if (sel == @selector(nameAtIndex:))`
6. `name = @"nameAtIndex";`
8. `return name;`
9. `}`
11. `+ (BOOL)isSelectorExcludedFromWebScript:(SEL)aSelector`
12. `{`
13. `if (sel == @selector(nameAtIndex:)) return NO;`
14. `return YES;`
15. `}`

Now we can change our JavaScript code to reflect our more logical method name:

1. `function printNameAtIndex(index) {`
2. `var myaddressbook = window.AddressBook;`
3. `var name = myaddressbook.nameAtIndex(index);`
4. `document.write(name);`
5. `}`

> [!IMPORTANT]
> 

### Other Resources

For more information about using Objective-C from JavaScript and vice versa, see the following documents:

- _[CallJS](../../../samplecode/CallJS/CallJS.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimruge)_ sample code shows how to call JavaScript from Objective-C and vice versa.
- _[Birthdays](../../../samplecode/Birthdays/Birthdays.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgojygi)_ sample code shows how to use a WebKit plug-in from JavaScript.
- _[WebKit Objective-C Framework Reference](https://developer.apple.com/documentation/webkit)_ provides more information on excluding methods and properties from the JavaScript environment.
- _[WebKit Plug-In Programming Topics](../../Internet%20Web/WebKit%20Plug-In%20Programming%20Topics/Introduction%20to%20WebKit%20Plug-in%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmrr)_ provides general information about writing WebKit plug-ins.

[Cross-Document Messaging](Cross-documentmessaging.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dcnzvfvjvomi)
