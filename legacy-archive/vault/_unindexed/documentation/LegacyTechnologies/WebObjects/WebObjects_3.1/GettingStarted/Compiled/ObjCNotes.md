---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/ObjCNotes.html
archived_at: '2026-07-15T07:48:24.463442Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](compiled.book.md) [!Previous Section](Deploy.md)

# Notes for Objective-C Developers

As explained at the beginning of the tutorial, you can write your application's logic using Java, Objective-C, WebScript, or a combination of WebScript and Objective-C. If you choose Java, you must write the entire application in Java. If you choose Objective-C, you can write part of the application in WebScript. Often, you would choose to write custom business logic in Objective-C and write component logic in WebScript.
The following sections describe the differences between developing applications in Objective-C and developing applications in Java.

## Creating an Objective-C project

To create an Objective-C application, simply create a new project in Project Builder of type WebObjectsApplication. Project Builder creates the directory with the __.woa__ extension and adds __Application.wos__, __Session.wos__, and __Main.wo__ to it as well as the makefiles and other supporting files. After you create the Project Builder project, you can open the __.woa__ directory in WebObjects Builder-it's not necessary to create the project in both WebObjects Builder and Project Builder.

## Objective-C main function

If you create an Objective-C project in Project Builder, __main__ is provided as a C function in the file __main.m__:

```objc
void main (int argc, const char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    WOApplication *application = [[[WOApplication alloc] init]
        autorelease];

    [application run];

    [pool release];
    exit(0);
}
#ifdef WIN32
#import <EOAccess/EOAccess.h>

void _referenceEOFrameworks()
{
    static id a;
    a = [EOEntity new];          // EOAccess
}
#endif
```


The __main()__ function begins by creating an autorelease pool that's used for the automatic deallocation of objects that receive the __autorelease__ message. Next, it creates the WebObjects application object and starts the request-response loop. The last statement releases the autorelease pool, which sends a __release__ message to any object that has been added to the pool since the application began.
If you're setting up a project by hand and you intend to run the application on the Windows NT platform, you must include the ___referenceEOFrameworks()__ function as well. This function makes sure the Enterprise Objects DLLs are loaded at the appropriate time.
__Note:__  If you're setting up a project by hand, you'll need to add the link line to the makefile youself. For example:

```
/bin/cc -o executableName  -LobjectFiles -framework WebObjects
-framework Foundation
```


Be sure to link to the WebObjects framework before the Foundation framework.
On the Solaris platform, you also need to link to the framework __NextLibrary/PrivateFrameworks/MultiScript.framework__. If you use the provided makefiles, this is set up for you.

## Subclassing WebObjects classes

If you subclass WOApplication or WOSession, name the subclass Application or Session, respectively. If you follow this naming convention, you are able to add further functionality to your object in __Application.wos__ or __Session.wos__. If you name your subclass something else, you shouldn't implement __Application.wos__ or __Session.wos__.

## Accessing compiled code from a script

Accessing compiled code from a script is simply a matter of getting an object of the compiled class and sending it a message. For example, if you implemented Registration's Main component in WebScript, you'd write the following line to instantiate a Person object:

```
/* Return a Person object by invoking Person's
      personWithDictionary: method */
aPerson = [Person personWithDictionary:newPerson];
```


## Accessing script methods from compiled code

To access a scripted object's methods from compiled code, you simply get the object that implements the method and send it a message. If you're accessing a method in the application or session script, you can use WOApplication methods to access the object:

```
[[WOApplication application] applicationScriptMethod];
[[[WOApplication application] session] sessionScriptMethod];
```


To access a component's methods, you must store the component in the session and then access it through the session.
For example, suppose you wanted to rewrite the Registration application so that Person's __validate__ method directly sets the value of the __message__ variable in the Main component. You'd add the following statement to the __init__ method __Main.wos__:

```
/* Store the component in the session. */
[self.session setObject:self forKey:@"Main"];
```


and then you can access it in Person's __validate__ method this way:

```
/* Get the component from the session: */
WOComponent *mainPage = [[[WOApplication application] session]
        objectForKey:@"Main"];

/* Send it a message */
[mainPage setMessage:@"You must supply a name and address"];
```


(__Main.wos__ implicitly implements the __setMessage:__ method because it declares a variable named __message__.)
To avoid compiler warnings, you should declare the scripted method you want to invoke in your code. This is because scripted objects don't declare methods-their methods are parsed from the script at run time. If you don't declare their methods in your code, the compiler issues a warning that the methods aren't part of the receiver's interface.
__Note:__  This step isn't strictly required-your code will still build, you'll just get warnings.
For the example above, you'd add the following declaration to the __Person.m__ file:

```objc
@interface WOComponent (RegistrationMainComponent)
- (void)setMessage:(NSString *)aMessage;
@end
```


While it's certainly straightforward to access a scripted object's methods from compiled code, you may not want to have that degree of interdependence between your scripts and your compiled code. You may want to minimize the interdependence to facilitate reusability.

## Using C and C++ in WebObjects applications

In addition to using compiled Objective-C in WebObjects applications, you can also use compiled C or C++. The interface you provide to WebObjects must be in Objective-C because WebObjects can't invoke C or C++ functions. However, you can directly invoke C and C++ functions from Objective-C.
Some of the options for integrating C or C++ code into your application are as follows:

- Putting the C or C++ functions into the same file as your Objective-C code
- Putting the C or C++ functions in separate files and importing their headers into your Objective-C code
- Adding a third-party library to your project and importing its headers into your Objective-C code
