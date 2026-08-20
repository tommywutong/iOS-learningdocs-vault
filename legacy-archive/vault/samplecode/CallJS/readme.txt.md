---
title: CallJS
apple_id: DTS10004241
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2011-07-05'
source_url: https://developer.apple.com/library/archive/samplecode/CallJS/Listings/readme_txt.html
archived_at: '2026-07-18T03:02:50.136810Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CallJS](CallJS.md)


[Next](main.m.md)[Previous](CallJS.md)

# readme.txt

```objc
CallJS
======

DESCRIPTION:

This sample illustrates how to add JavaScript methods that call through to your Objective-C code.  These methods can be used in Mac OS X 10.3.9 and later.


Here is how you would go about implementing your own console.log() method in your WebKit application.  For the purposes of this description we'll assume you already have a delegate object set up for your WebView.  This sample has used this same technique for implementing three Objective-C methods that can be called from JavaScript. 


First, implement a webView:webView windowScriptObjectAvailable: method on your WebFrameLoadDelegate delegate object.  This method will be called once the page is loaded and it is ready for JavaScripts to run.  To install a 'console' object on the window, you would call the setValue:forKey: method on the windowScriptObject received as a parameter.  Here, we have passed a reference to the myConsoleObject and associated it with the name 'console'.  

- (void)webView:(WebView *)webView
        windowScriptObjectAvailable:(WebScriptObject *)windowScriptObject {

    [windowScriptObject setValue:myConsoleObject forKey:@"console"];

}

myConsoleObject is an instance of an object sub-classed from NSObject that will implement all of the Objective-C functionality for the 'console' object being made available to JavaScript.  In this sample, we have used the same object we are using for our WebKit delegates and for our window controller.  

On that object we will need to implement the .log() method that will be called from JavaScript along with a few other minor house keeping methods.  

For example, our .log() method may be implemented something like this:

- (void)doOutputToLog:(NSString *)theMessage
{
    NSLog(@"LOG: %@", theMessage);
}

you'll notice right away that the name of the method is much different than the name we would like to use in JavaScript.  In fact, we cannot use the name "doOutputToLog:" in JavaScript because of the colon.  So, the following house keeping routines will allow us to (a) let WebKit know that JavaScript is allowed to call this method, and (b) provide a mapping between the Objective-C method name and the JavaScript method name.  

To let WebKit know that it is okay to call our method, we implement the following class method on our myConsoleObject's class as follows:

+ (BOOL)isSelectorExcludedFromWebScript:(SEL)selector {
    if (selector == @selector(doOutputToLog:)) {
        return NO;
    }
    return YES;
}

This tells webkit that the method defined for the selector doOutputToLog: should not be excluded from the methods JavaScript is allowed to call.

Next, to provide the name mapping, we would provide the following class method on our myConsoleObject's class:

+ (NSString *) webScriptNameForSelector:(SEL)sel {
    if (sel == @selector(doOutputToLog:)) {
        return @"log";
    } else {
        return nil;
    }
}

This will provide a mapping between the Objective-C name and the the name used in JavaScript.

===========================================================================
BUILD REQUIREMENTS

Xcode 3.2, Mac OS X 10.6 Snow Leopard or later.

===========================================================================
RUNTIME REQUIREMENTS

Mac OS X 10.6 Snow Leopard or later.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS

Version 1.1
- Updated classes to use properties.
- Project updated for Xcode 4.
Version 1.0
- Initial Version

===========================================================================
Copyright (C) 2007-2011 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](CallJS.md)

