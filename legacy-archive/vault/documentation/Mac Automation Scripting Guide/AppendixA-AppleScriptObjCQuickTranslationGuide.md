---
title: Mac Automation Scripting Guide
apple_id: TP40016239
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/AppendixA-AppleScriptObjCQuickTranslationGuide.html
archived_at: '2026-07-15T07:45:13.919728Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Mac Automation Scripting Guide](index.md)



## Objective-C to AppleScript Quick Translation Guide

This appendix provides AppleScript equivalents for typical Objective-C features of a class. Below the table is a list of notes that correspond to the numbers in column 1.

| Note | Objective-C | AppleScript |
| --- | --- | --- |
| image: ../Art/1_2x.png | `@interface MyClass : NSObject {` | `script MyClass`  `property parent: class "NSObject"` |
| image: ../Art/2_2x.png | `int myProperty;`  `IBOutlet NSTextField *myField;`  `}`  `IBOutlet @property (retain) NSButton *myButton;` | `property myProperty: 0`  `property myField: missing value`  `property myButton: missing value` |
| image: ../Art/3_2x.png | `@end`    `@implementation MyClass` |  |
| image: ../Art/4_2x.png | `- (IBAction) myAction:(id) object {` | `-- Handler with interleaved parameters`  `on myAction:object`    `-- or`    `-- Handler with positional parameters`  `on myAction_(object)` |
| image: ../Art/5_2x.png | `// No Arguments`  `[object method];`    `// One Argument`  `[object method:parameterName];`    `// Multiple Argument`  `[object methodWithArgument1:parameter1 Argument2:parameter2];` | `-- No Arguments`  `object's methodName()`  `-- or`  `methodName() of object`  `-- or`  `tell object to methodName()`    `-- One Argument`  `object's methodName:parameterName`  `-- or`  `methodName_(parameterName) of object`  `-- or`  `tell object to methodName:parameterName`    `-- Multiple Arguments`  `object's methodWithArgument1:parameter1 Argument2:parameter2`  `-- or`  `methodWithArgument1_Argument2_(parameter1, parameter2) of object`  `-- or`  `tell object to methodWithArgument1:parameter1 Argument2:parameter2` |
| image: ../Art/6_2x.png | `[object propertyName];`  `object.propertyName;` | `object's propertyName()`  `-- or`  `propertyName() of object`    `object's propertyName`  `-- or`  `propertyName of object` |
| image: ../Art/7_2x.png | `}`  `@end` | `end myAction_`  `end script` |

1. An Objective-C class corresponds to an AppleScript `script` object. In AppleScript, inheritance is denoted using the `parent` property.
2. An instance variable or `@property` in Objective-C corresponds to a `property` in AppleScript.

   AppleScript doesn’t require explicit tagging of Interface Builder outlet properties (`IBOutlet`). Interface Builder sees any property with a value of `missing value` as a potential outlet.
3. Objective-C divides class definitions into an `@interface` section containing properties and an `@implementation` section containing method definitions. AppleScript has no such division. Properties and methods are all contained within the same `script` object.
4. An Objective-C method definition corresponds to an AppleScript handler that uses either an interleaved- or positional-style for parameter placement.

   Interleaved parameters are preceded by colons and separated by spaces, similar to Objective-C syntax. See [Handlers with Interleaved Parameters](../Apple%20Script/AppleScript%20Language%20Guide/About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzs) in _[AppleScript Language Guide](../Apple%20Script/AppleScript%20Language%20Guide/Introduction%20to%20AppleScript%20Language%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobt)_.

   A positional parameter hander name is the Objective-C selector name, with colons changed to underscores. This handler name is followed by parentheses enclosing comma-separated parameters. See [Handlers with Positional Parameters](../Apple%20Script/AppleScript%20Language%20Guide/About%20Handlers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobtfvbuqmrqgywvgvzrgm) in _[AppleScript Language Guide](../Apple%20Script/AppleScript%20Language%20Guide/Introduction%20to%20AppleScript%20Language%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsobt)_.

   AppleScript doesn’t require explicit tagging of Interface Builder action methods (`IBAction`). Interface Builder sees any method with a single parameter as a potential action method.
5. A method call in Objective-C corresponds to an AppleScript handler call that uses either interleaved- or positional-style parameters. Regardless of style, parameters must always be provided in the order the method definition specifies.

   AppleScript has three equivalent syntaxes for addressing object handlers and properties: `object's method`, `method of object`, and `tell object to method`.
6. An Objective-C method with no parameters, such as a property or constant, can be called using an explicit accessor method call or more concise dot syntax. Similarly in AppleScript, a method with no parameters can be called using a handler call with empty parentheses, or as a property without the parentheses.
7. In AppleScript, handlers and `script` objects are closed using the `end` syntax.

### Resolving Terminology Conflicts in AppleScriptObjC

AppleScript distinguishes between _reserved words_, _application identifiers_, and _user identifiers_. Reserved words are terms defined by AppleScript itself. Application identifiers, also known as _application keywords_, are terms defined by an app’s scripting dictionary. User identifiers are variable or subroutine names defined by the script writer.

Identifiers passed to AppleScriptObjC, in particular, Cocoa method names, must be user identifiers. If an identifier conflicts with a reserved word or an application identifier, you can force it to be considered a user identifier by escaping it—enclosing it in vertical bars. For example, the `NSColor` class has a `set` method for setting the current drawing color. However, `set` is a reserved AppleScript term for assigning variables. Calling the `set` method without escaping it would produce a syntax error. Listing 43-1 shows the correct usage.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=myColor%27s%20%7Cset%7C%28%29%0A--%20OR%0A%7Cset%7C%28%29%20of%20myColor%0A--%20OR%0Atell%20myColor%20to%20%7Cset%7C%28%29)

__Listing 43-1__AppleScriptObjC: Escaping a method name that conflicts with a reserved word

1. `myColor's |set|()`
2. `-- OR`
3. `|set|() of myColor`
4. `-- OR`
5. `tell myColor to |set|()`

Similarly, `NSWindow` has a `bounds` property, but `bounds` is an application-defined term. Therefore, any references to this property must also be escaped. See Listing 43-2.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=get%20myWindow%27s%20%7Cbounds%7C%0A--%20OR%0Aget%20%7Cbounds%7C%20of%20myWindow%0A--%20OR%0Atell%20myColor%20to%20get%20%7Cbounds%7C)

__Listing 43-2__AppleScriptObjC: Escaping a property name that conflicts with an application identifier

1. `get myWindow's |bounds|`
2. `-- OR`
3. `get |bounds| of myWindow`
4. `-- OR`
5. `tell myColor to get |bounds|`

When in doubt, add the vertical bars. If they’re unnecessary, they are merely redundant and harmless.

### Importing Frameworks

To import a framework in AppleScript, use the `use` command, followed by the framework name. See Listing 43-3.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=use%20framework%20%22Foundation%22%0A%0Aset%20theString%20to%20%22Hello%20World%22%0Aset%20theString%20to%20stringWithString_%28theString%29%20of%20NSString%20of%20current%20application%0Aset%20theString%20to%20%28uppercaseString%28%29%20of%20theString%29%20as%20string)

__Listing 43-3__AppleScriptObjC: Importing Foundation framework

1. `use framework "Foundation"`
3. `set theString to "Hello World"`
4. `set theString to stringWithString_(theString) of NSString of current application`
5. `set theString to (uppercaseString() of theString) as string`
6. `--> Result: "HELLO WORLD"`

### Accessing Scripting Additions

A normal AppleScript automatically loads and has access to terminology from scripting additions that are installed on the system. In AppleScriptObjC scripts, you must explicitly state that you want to use scripting addition terminology. Listing 43-4 shows how to do this.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=use%20scripting%20additions%0Adisplay%20dialog%20%22Hello%20World%22%20as%20string)

__Listing 43-4__AppleScriptObjC: Using scripting additions

1. `use scripting additions`
2. `display dialog "Hello World" as string`

### Classes and Constants

In AppleScriptObjC, Objective-C classes and constants are referred to in the context of the `current application` constant—a reference to the app that’s running the script.

In this context, classes are referenced using the `class` specifier, followed by the class name, as shown in Listing 43-5.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=use%20framework%20%22Foundation%22%0Aclass%20%22NSView%22%20of%20current%20application)

__Listing 43-5__AppleScriptObjC: Referencing a class

1. `use framework "Foundation"`
2. `class "NSView" of current application`

Constants are referenced without a preceding identifier. See Listing 43-6.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=use%20framework%20%22Foundation%22%0A%0Acurrent%20application%27s%20NSCalibratedRGBColorSpace%0A--%20OR%0ANSCalibratedRGBColorSpace%20of%20current%20application)

__Listing 43-6__AppleScriptObjC: Referencing a constant

1. `use framework "Foundation"`
3. `current application's NSCalibratedRGBColorSpace`
4. `-- OR`
5. `NSCalibratedRGBColorSpace of current application`

Listing 43-7 demonstrates how to reference both Objective-C classes and constants.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=script%20MyView%0A%20%20%20%20property%20parent%20%3A%20class%20%22NSView%22%0A%0A%20%20%20%20on%20drawRect%3Arect%0A%20%20%20%20%20%20%20%20set%20theWhiteColor%20to%20current%20application%27s%20class%20%22NSColor%22%27s%20whiteColor%28%29%0A%20%20%20%20%20%20%20%20--%20OR%0A%20%20%20%20%20%20%20%20set%20theWhiteColor%20to%20whiteColor%28%29%20of%20class%20%22NSColor%22%20of%20current%20application%0A%20%20%20%20%20%20%20%20--%20OR%0A%20%20%20%20%20%20%20%20tell%20class%20%22NSColor%22%20of%20current%20application%20to%20set%20theWhiteColor%20to%20whiteColor%28%29%0A%0A%20%20%20%20%20%20%20%20theWhiteColor%27s%20colorUsingColorSpaceName%3A%28current%20application%27s%20NSCalibratedRGBColorSpace%29%0A%20%20%20%20%20%20%20%20--%20OR%0A%20%20%20%20%20%20%20%20colorUsingColorSpaceName_%28NSCalibratedRGBColorSpace%20of%20current%20application%29%20of%20theWhiteColor%0A%20%20%20%20end%20drawRect%3A%0Aend%20script)

__Listing 43-7__AppleScriptObjC: Example of a script that references both classes and constants

1. `script MyView`
2. `property parent : class "NSView"`
4. `on drawRect:rect`
5. `set theWhiteColor to current application's class "NSColor"'s whiteColor()`
6. `-- OR`
7. `set theWhiteColor to whiteColor() of class "NSColor" of current application`
8. `-- OR`
9. `tell class "NSColor" of current application to set theWhiteColor to whiteColor()`
11. `theWhiteColor's colorUsingColorSpaceName:(current application's NSCalibratedRGBColorSpace)`
12. `-- OR`
13. `colorUsingColorSpaceName_(NSCalibratedRGBColorSpace of current application) of theWhiteColor`
14. `end drawRect:`
15. `end script`

In places where `current application` is the current context, such as the top level of a script, `current application` may be shortened to `my` or `me`. In the case of class specifiers, it may be omitted entirely. See Listing 43-8.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=use%20framework%20%22Foundation%22%0A%0Aclass%20%22NSView%22%0A%0Amy%20NSCalibratedRGBColorSpace%0A--%20OR%0ANSCalibratedRGBColorSpace%20of%20me)

__Listing 43-8__AppleScriptObjC: Referencing a classes and constants in the context of the current application

1. `use framework "Foundation"`
3. `class "NSView"`
5. `my NSCalibratedRGBColorSpace`
6. `-- OR`
7. `NSCalibratedRGBColorSpace of me`

As a convenience technique to save typing, it’s good practice to define properties for classes at the top of your script. This way, you can refer to them by property name throughout your script.

__APPLESCRIPT__

[Open in Script Editor](applescript://com.apple.scripteditor?action=new&script=script%20MyView%0A%20%20%20%20property%20parent%20%3A%20class%20%22NSView%22%0A%20%20%20%20property%20NSColor%20%3A%20class%20%22NSColor%22%0A%0A%20%20%20%20on%20drawRect%3Arect%0A%20%20%20%20%20%20%20%20set%20theWhiteColor%20to%20NSColor%27s%20whiteColor%28%29%0A%20%20%20%20%20%20%20%20theWhiteColor%27s%20colorUsingColorSpaceName%3ANSCalibratedRGBColorSpace%0A%20%20%20%20end%20drawRect%3A%0Aend%20script)

__Listing 43-9__AppleScriptObjC: Defining classes as properties

1. `script MyView`
2. `property parent : class "NSView"`
3. `property NSColor : class "NSColor"`
5. `on drawRect:rect`
6. `set theWhiteColor to NSColor's whiteColor()`
7. `theWhiteColor's colorUsingColorSpaceName:NSCalibratedRGBColorSpace`
8. `end drawRect:`
9. `end script`

### Resources

For additional information about AppleScriptObjC, see _[AppleScriptObjC Release Notes](https://developer.apple.com/library/archive/releasenotes/ScriptingAutomation/RN-AppleScriptObjC/index.html#//apple_ref/doc/uid/TP40008853)_ and the third-party book [EveryDay AppleScriptObjC](http://macosxautomation.com/applescript/apps/everyday_book.html).

[Using Dictation to Run Scripts](UseDictationtoRunScripts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3demzzfvbuqobxfvjvomi)
