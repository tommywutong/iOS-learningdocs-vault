---
title: AppleScriptObjC Release Notes
apple_id: TP40008853
resource_type: Release Note
platform: macOS
topic: Languages & Utilities
technology: null
published: '2009-05-27'
source_url: https://developer.apple.com/library/archive/releasenotes/ScriptingAutomation/RN-AppleScriptObjC/index.html
archived_at: '2026-07-18T02:59:02.240949Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# AppleScriptObjC Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dqnjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Objective-C/AppleScript Quick Translation Guide](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dqnjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)
- [Identifiers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dqnjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6my)
- [Classes and Constants](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dqnjtfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6na)

### Introduction

AppleScriptObjC is a new framework in OS X v10.6 that allows Cocoa applications to be written in AppleScript. Using AppleScriptObjC, your AppleScript code can work with any Cocoa framework, and can function as a first-class citizen in the Cocoa world.

This note covers the syntactical details of using AppleScriptObjC and accessing Cocoa functionality from AppleScript. To write a complete application, you will need to learn Cocoa itself, and should start with the _[Cocoa Fundamentals Guide](../../documentation/Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu)_.

AppleScriptObjC obsoletes AppleScript Studio, which is deprecated as of OS X v10.6. Developers using AppleScript Studio should migrate to AppleScriptObjC, and should start new projects using AppleScriptObjC exclusively. AppleScript Studio development is still supported, but functions for creating new projects have been removed, and the AppleScript Studio palette in Interface Builder has been hidden. To re-enable it, use this command in Terminal, and then re-launch Interface Builder:

```
defaults write com.apple.InterfaceBuilder3 IBEnableAppleScriptStudioSupport -bool YES
```


### Objective-C/AppleScript Quick Translation Guide

AppleScriptObjC lets AppleScript objects serve as Objective-C objects in the Cocoa runtime, so development using AppleScriptObjC follows Objective-C and Cocoa patterns. This table is a quick reference to the AppleScript equivalents for various Objective-C features, shown as a definition of an ersatz class with the Objective-C version on the left and the AppleScript version on the right.

| Objective-C | AppleScript |
| --- | --- |
| `@interface MyClass : NSObject {` | `script MyClass`  `property parent: class "NSObject"` |
|
| `int myProperty;`  `IBOutlet NSTextField *myField;`  `}`  `IBOutlet @property (retain) NSButton *myButton;` | `property myProperty: 0`  `property myField: missing value`  `property myButton: missing value` |
|
| `@end`    `@implementation MyClass` |  |
|
| `- (IBAction) myAction:(id) object {` | `on myAction_(object)` |
|
| `[object method];`  `[object method:param];`  `[object methodWithArg1:p1 arg2:p2];` | `object's method()`  `object's method_(param)`  `object's methodWithArg1_arg2_(p1, p2)` |
|
| `[object property];`  `object.property;` | `object's property()`  `object's property` |
|
| `}`  `@end` | `end myAction_`  `end script` |

### Identifiers

AppleScript distinguishes between _application identifiers_, which are terms defined by AppleScript or an application’s scripting interface, and _user identifiers_, which are terms defined by the script writer. In the AppleScript Editor preferences, these are referred to as “application keywords” and “variables and subroutine names”, respectively. Identifiers passed to AppleScriptObjC, in particular Cocoa method names, must be user identifiers. If an identifier would conflict with an existing application identifier (or even an AppleScript reserved word), you can force it to be considered a user identifier by escaping it with vertical bars.

For example, `NSColor` has a `set` method for setting the current drawing color, but `set` is also an AppleScript reserved word for assigning variables. Using `set` as a handler name without escaping it would be a syntax error, so the correct usage looks something like this:

```
tell myColor to |set|()
```

Similarly, `NSWindow` has a `bounds` property, but `bounds` is also an application-defined term, so to use it as the `NSWindow`, it must be escaped:

```
get myWindow's |bounds|
```

When in doubt, add the vertical bars: if they are not necessary, then they are merely redundant and harmless.

### Classes and Constants

Classes are treated as by-name elements, and constants and enumerated values as properties, both of `current application`. Observe the use of `NSView`, `NSColor`, and `NSCalibratedRGBColorSpace` in this example:

```
script MyView
   property parent: class "NSView"

   on drawRect_(rect)
       set c to current application's class "NSColor"'s whiteColor()
       c's colorUsingColorSpaceName_(current application's NSCalibratedRGBColorSpace)
   end drawRect_
end script
```

In places where `current application` is the implicit container, such as in the parent property or at the top level of the script, it may be shortened to `my`, or in the case of class specifiers omitted entirely. (In the handler body, the implicit container is the script object’s parent, `class "NSView"`, so the `current application's` must be explicit.) This allows a convenience technique to save typing: define properties at the top level of the script, and then refer to the properties in the handler, like this:

```
property NSColor: class "NSColor"
property NSCalibratedRGBColorSpace: my NSCalibratedRGBColorSpace

script MyView
   property parent: class "NSView"
   on drawRect_(rect)
       set c to NSColor's whiteColor()
       c's colorUsingColorSpaceName_(NSCalibratedRGBColorSpace)
   end drawRect_
end script
```
