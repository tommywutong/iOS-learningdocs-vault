---
title: Scripting Bridge Programming Guide
apple_id: TP40006104
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptingBridgeConcepts/UsingScriptingBridge/UsingScriptingBridge.html
archived_at: '2026-07-15T07:18:54.596789Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Scripting Bridge Programming Guide](Introduction%20to%20Scripting%20Bridge%20Programming%20Guide%20for%20Cocoa.md)


[Next](Improving%20the%20Performance%20of%20Scripting%20Bridge%20Code.md)[Previous](About%20Scripting%20Bridge.md)

# Using Scripting Bridge

Scripting Bridge code is very much like any other Objective-C code. However, there are some differences, mostly deriving from the OSA architecture on which the dispatch and handling of Apple events is based. This chapter describes how to use Scripting Bridge in Objective-C projects, pointing out those differences along the way. [Improving the Performance of Scripting Bridge Code](Improving%20the%20Performance%20of%20Scripting%20Bridge%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnrnknltc) also discusses the correct or optimal use of Scripting Bridge, but from a performance angle.

Before you begin writing any Scripting Bridge code for your project, there are a few steps you should complete:

1. Generate header files for all scriptable applications that your code is sending messages to.
2. Add these files to your project.
3. In your header or implementation files, add `#import` statements for the generated header files.
4. Add the Scripting Bridge framework to your project.

You can use `id` to type Scripting Bridge objects dynamically, but such code is vulnerable to programming errors and results in lots of warning messages when you build your project. It is recommended that you generate a header file for each scriptable application, add these files to your project, and in your code give Scripting Bridge specific types based on what you find in the header files. Doing so allows the compiler to check the types of objects (eliminating spurious warning messages) and gives you more assurance that you are sending messages to the correct recipients.

A header file that you generate for a scriptable application serves as reference documentation for the scripting classes of that application. It includes information about the inheritance relationships between classes and the containment relationships between their objects. It also shows how commands, properties, and elements are declared. Taking the iTunes application as an example, the header file shows the definition of the application class (`iTunesApplication`), the application’s scripting classes (such as `iTunesTrack` and `iTunesSource`), commands (such as the `eject` method), and properties (such as the `artist` declared property). A header file also includes comments extracted from the scripting definition, such as the comment added to this declaration for the `FinderApplication` class:

```objc
- (void)empty;   // Empty the trash
```

To create a header file, you need to run two command-line tools—`sdef` and `sdp`—together, with the output from one piped to the other. This is the recommended syntax:

`sdef` _/path/to/application_`.app | sdp -fh --basename` _applicationName_

The `sdef` utility gets the scripting definition from the designated application; if that application does not contain an `sdef` file, but does instead contain scripting information in an older format (such as the scripting suite and terminology property lists), it translates that information into the sdef format first. The `sdp` tool run with the above options generates an Objective-C header file for the designated scriptable application. Thus, for iTunes, you would run the following command to produce a header file named `iTunes.h`:

```
sdef /Applications/iTunes.app | sdp -fh --basename iTunes
```

Add the generated file to your Xcode project by choosing Add to Project from the Project menu and specifying the file in the ensuing dialog. In any source or header file in your project that references Scripting Bridge objects, insert the appropriate #import statements, such as the following:

```objc
#import "iTunes.h"
```

Finally, make sure that you have added the Scripting Bridge framework (`/System/Library/Frameworks/ScriptingBridge.framework`) to your project using the Project > Add to Project menu command. It is not necessary to have `#import` statements for the framework because the header files for the scriptable applications do that already.

Before you can send messages to a scriptable application, you need an object that represents the application. As explained in [Classes of the Scripting Bridge Framework](About%20Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqmznknltc), the Scripting Bridge framework declares three class factory methods for creating instances of scriptable applications; each takes a different value for locating the application.

- [applicationWithBundleIdentifier:](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1588086-applicationwithbundleidentifier) locates an application by its bundle identifier.
- [applicationWithURL:](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1588084-applicationwithurl) locates a (local or remote) application by URL.
- [applicationWithProcessIdentifier:](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1588085-applicationwithprocessidentifier) locates an application by its BSD process identifier (pid).

The recommended method for creating an instance of a scriptable application is `applicationWithBundleIdentifier:`. The method can locate an application on a system even if the user has renamed the application, and it doesn’t require you to know where an application is installed in the file system (which could be anywhere). The following line of code creates an instance of the iTunes application:

```
iTunesApplication *iTunes = [SBApplication applicationWithBundleIdentifier:@"com.apple.iTunes"];
```

If you don’t know an application’s bundle identifier, you can find it by looking for the value of `CFBundleIdentifier` property in the `Info.plist` file stored in the application bundle.

There might be occasions when using one of the other class factory methods makes sense. For example, if you are writing an application that uses Scripting Bridge for your own personal use, you could refer to applications by URL. The following example creates an instance of the Pages application, locating it by URL in an installation location other than `/Applications`.

```
NSURL *pagesURL = [NSURL fileURLWithPath:[NSString stringWithFormat:@"%@/Applications/iWork/Pages.app", NSHomeDirectory()]];
PagesApplication *pagesApp = [SBApplication applicationWithURL:pagesURL];
```


To control a scriptable application, simply send to the instance of the application or one of its objects a message based on a method declared by the object’s class. These methods correspond to commands in the application’s scripting definition. The action method listed in Listing 2-1 plays the currently selected iTunes track and then modulates the volume of the sound, eventually restoring it to the original level.

__Listing 2-1__  Controlling the volume of iTunes

```objc
- (IBAction)play:(id)sender {
    iTunesApplication *iTunes = [SBApplication applicationWithBundleIdentifier:@"com.apple.iTunes"];
    if ( [iTunes isRunning] ) {
        int rampVolume, originalVolume;
        originalVolume = [iTunes soundVolume];

        [iTunes setSoundVolume:0];
        [iTunes playOnce:NO];

        for (rampVolume = 0; rampVolume < originalVolume; rampVolume += originalVolume / 16) {
            [iTunes setSoundVolume: rampVolume];
            /* pause 1/10th of a second (100,000 microseconds) between adjustments. */
            usleep(100000);
        }
        [iTunes setSoundVolume:originalVolume];
    }
}
```

Note that this method tests whether the application is running before it attempts to control it. (The [isRunning](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423981-isrunning) method is declared by the `SBApplication` class.) This programming practice is discussed in more detail in [Improving the Performance of Scripting Bridge Code](Improving%20the%20Performance%20of%20Scripting%20Bridge%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnrnknltc).

In the object graph that Scripting Bridge dynamically generates for a scriptable application, most objects are containers of other objects, or of objects that refer to another scripting object. In a data-modeling sense, they express to-many or to-one relationships and enable your code to “drill down” the object graph. It is only when you get to the leaf nodes of the graph, which are typically the properties of an object, that you are able to access concrete data, such as a name, a color, or a numerical value. As you may recall, Scripting Bridge implements properties of scripting objects as declared properties in Objective-C.

Getting the value of a property requires you to navigate the object hierarchy of the application until you come to the target object—that is, the object that declares those properties—and then send a message to that object that is the same as the property name. Sometimes you don’t have to navigate that far. For example, the fragment of code in Listing 2-2 sends two messages to the `ITunesApplication` object.

__Listing 2-2__  Getting the name of the current track

```
iTunesApplication *iTunes = [SBApplication applicationWithBundleIdentifier:@"com.apple.iTunes"];
NSLog(@"Current song is %@", [[iTunes currentTrack] name]);
```

The first message to the application gets the value of its `currentTrack` property; this message yields an object of class `iTunesTrack` representing the track currently playing. This object does itself not represent any concrete data, but the message then sent to it (`name`) returns the value of its `name` property as an [NSString](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/cl/NSString) object.

You can also set the values of properties unless they are (in their declaration) marked as `readonly`. The code in Listing 2-3 implements a command-line tool that clears the `locked` property in items in the Trash.

__Listing 2-3__  Setting the `locked` property of Finder items

```
int main (int argc, const char * argv[]) {
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
    FinderApplication *theFinder = [SBApplication applicationWithBundleIdentifier: @"com.apple.finder"];
    SBElementArray *trashItems = [[theFinder trash] items];
    if ([trashItems count] > 0) {
        for (FinderItem *item in trashItems) {
            if ([item locked]==YES)
                [item setLocked:NO];
        }
    }
    [pool drain];
    return 0;
}
```

As the listing shows, you can set the value with a message of the form `set`_Property_`:`, where _Property_ is the name of the property with the initial letter capitalized. You can also use dot notation when setting property values—these are, after all, Objective-C declared properties. For example, you could set the value of the `locked` property with this statement:

```
item.locked = NO;
```

However, you could rewrite the Scripting Bridge code in [Listing 2-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnbnknltg) to be more efficient by using the [setValue:forKey:](https://developer.apple.com/documentation/foundation/nsarray/1408301-setvalue) method of `NSArray`. The example in Listing 2-4 sends just one Apple event instead of one event per item in the Trash.

__Listing 2-4__  More efficiently setting the `locked` property

```
int main (int argc, const char * argv[]) {
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
    FinderApplication *theFinder = [SBApplication applicationWithBundleIdentifier: @"com.apple.finder"];
    SBElementArray *trashItems = [[theFinder trash] items];
    [trashItems setValue:[NSNumber numberWithBool:NO] forKey:@"locked"];
    [pool drain];
    return 0;
}
```

Instead of messages you can use dot notation to traverse the object graph of a scriptable application. The following line is equivalent to the second line in [Listing 2-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnbnknlti):

```
NSLog(@"Current song is %@", iTunes.currentTrack.name);
```

Sometimes asking a scripting object for the value of a property might not return the expected concrete data. This happens if the returned value itself is an instance of an application-specific subclass of `SBObject`, and thus an object specifier referring to what may be the concrete data. Consider the example in Listing 2-5. This code copies the textual content of each selected Mail message to a TextEdit document.

__Listing 2-5__  Forcing evaluation of a scripting object to get a property value

```objc
- (IBAction)copyMailMessage:(id)sender {
    MailApplication *mailApp = [SBApplication applicationWithBundleIdentifier:@"com.apple.mail"];
    TextEditApplication *textEdit = [SBApplication applicationWithBundleIdentifier:@"com.apple.TextEdit"];
    SBElementArray *viewers = [mailApp messageViewers];
    for (MailMessageViewer *viewer in viewers) {
        NSArray *selected = [viewer selectedMessages];
        for (MailMessage *message in selected) {
            TextEditDocument *doc = [[[textEdit classForScriptingClass:@"document"] alloc] init];
            [[textEdit documents] addObject:doc];
            doc.text = [[message content] get];
        }
    }
}
```

The last line of code in the example includes the message `[message content]`, but this message does not yield the textual content of the message as one might expect. Instead, a [get](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423965-get) message is required to force evaluation and thereby obtain the text for assignment. What `[message content]` returns in an instance of `MailText`, which a subclass of `SBObject`. This instance is an object specifier that refers to the actual text. For more on forced evaluation of object specifiers through the `get` method, see [Improving the Performance of Scripting Bridge Code](Improving%20the%20Performance%20of%20Scripting%20Bridge%20Code.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnrnknltc).

Element arrays, or [SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbelementarray) objects, are collections of scripting objects of the same type. Scripting Bridge implements the elements it finds in an application’s scripting definition as methods that return [SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbelementarray) instances. Because `SBElementArray` is a subclass of [NSMutableArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSMutableArray), you can send methods to element arrays that are declared by `NSMutableArray` and its superclass, [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray). For example, as shown in Listing 2-6, you could use an [NSEnumerator](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSEnumerator/Description.html#//apple_ref/occ/cl/NSEnumerator) object to enumerate through the array.

__Listing 2-6__  Using an enumerator to iterate through an element array

```
FinderApplication *theFinder = [[[SBApplication applicationWithBundleIdentifier: @"com.apple.finder"] alloc] init];
SBElementArray *trashItems = [[theFinder trash] items];
if ([trashItems count] > 0) {
    NSEnumerator *tren = [trashItems objectEnumerator];
    FinderItem *item;
    while (item = [tren nextObject]) {
        if ([item locked]==YES)
            [item setLocked:NO];
    }
}
```

Or you could even use the fast enumeration feature of Objective-C 2.0 to more efficiently iterate through the array, as shown in Listing 2-7.

__Listing 2-7__  Using fast enumeration on an element array

```
FinderApplication *theFinder = [[[SBApplication applicationWithBundleIdentifier: @"com.apple.finder"] alloc] init];
    SBElementArray *trashItems = [[theFinder trash] items];
    if ([trashItems count] > 0) {
        for (FinderItem *item in trashItems) {
            item.locked = NO;
        }
    }
```

Although it is possible to enumerate through `SBElementArray` objects, as a general rule don’t enumerate if you can avoid it. You can get much better performance by using one of the “bulk operation” array methods that Cocoa and Scripting Bridge provide:

- Use [makeObjectsPerformSelector:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/makeObjectsPerformSelector:withObject:) (`NSArray`) to make contained objects perform an operation.
- Use `[valueForKey:](../../../../LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/NSArrayAdditions.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxu4u2bojzgc6jpozqwy5lfizxxes3fpe5a)` and [setValue:forKey:](https://developer.apple.com/documentation/foundation/nsarray/1408301-setvalue) (NSArray) for bulk fetching and setting, respectively, of the properties of objects in an element array.
- Use [filteredArrayUsingPredicate:](https://developer.apple.com/documentation/foundation/nsarray/1411033-filtered) (`NSArray`) to obtain a subset of the objects in the array.
- Use [arrayByApplyingSelector:withObject:](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1424007-array) (`SBElementArray`) to get a particular value from each object in the array.

The code in Listing 2-8 uses the last of these methods to create a pop-up list with the calendar names obtained from the iCal application.

__Listing 2-8__  Using the `arrayByApplyingSelector:` method to populate a pop-up button

```objc
- (void)awakeFromNib {

    [time setDateValue: [NSDate date]];
    [NSApp setDelegate: self];
    iCalApplication *iCal = [SBApplication applicationWithBundleIdentifier:@"com.apple.iCal"];
    SBElementArray *calendars = [iCal calendars];
    [cal_popup removeAllItems]; // cal_pop is an outlet to a pop-up button
    [cal_popup addItemsWithTitles:[calendars arrayByApplyingSelector: @selector(name)]];
}
```

The code fragment in Listing 2-9 (which is extracted from the method shown in [Listing 2-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnbnknltm)) uses the `filteredArrayUsingPredicate:` method to create an array containing a subset of calendar events that each have a particular name.

__Listing 2-9__  Filtering an element array using a predicate

```
iCalEvent *theEvent;
NSArray *matchingEvents = [[theCalendar events] filteredArrayUsingPredicate:
            [NSPredicate predicateWithFormat:@"summary == %@", eventName]];
if ( [matchingEvents count] >= 1 ) {
        // handle any events that match..
}
```

`SBElementArray` also declares methods for extracting individual objects from element arrays using various forms of reference: name ([objectWithName:](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423971-objectwithname)), unique identifier ([objectWithName:](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423971-objectwithname)), and location within the array ([objectAtLocation:](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423963-objectatlocation)). The code fragment in Listing 2-10 shows the use of the `objectWithName:` method. (Again, this fragment is taken from the example in [Listing 2-11](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnbnknltm).)

__Listing 2-10__  Getting an object from an element array by specifying its name

```
iCalApplication *iCal = [[[SBApplication applicationWithBundleIdentifier:@"com.apple.iCal"] alloc] init];
iCalCalendar *theCalendar;

[iCal activate];

NSString *calendarName = [calendar titleOfSelectedItem];

if ( [[[iCal calendars] objectWithName:calendarName] exists] ) {
    theCalendar = [[iCal calendars] objectWithName:calendarName];
}
// etc....
```

For adding scripting objects to element arrays, you may use `NSMutableArray` methods such as [insertObject:atIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/insertObject:atIndex:) and [addObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/addObject:). To remove objects from element arrays, call [removeObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSMutableArray/removeObject:) (or a related method of `NSMutableArray`) on the element array.

In addition to allowing you to control an application and get and set the properties of scripting objects, Scripting Bridge lets you add scripting objects to an application. For example, you could use Scripting Bridge to dynamically add a playlist to iTunes. There are two important guidelines to remember when adding a scripting object to an application:

- Call [classForScriptingClass:](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423987-class) on the application instance to get the `Class` object to use for allocating the object.

  This method takes the name of the class as specified in the scripting definition—for example, `document`. Do not use a class name in the `sdp`-generated header file as the receiver of the `alloc` method.
- Immediately after creating the object, insert it in the appropriate element array.

  The object is not “viable” in the application until it has been added to its container. Consequently, you cannot set or access its properties until it’s been added.

You can use the [init](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423993-init) and [initWithProperties:](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423973-init) methods of `SBObject` to initialize the scripting object. Here are a few lines of code (taken from [Listing 2-5](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnbnknltk)) that use `init`:

```
TextEditDocument *doc = [[[textEdit classForScriptingClass:@"document"] alloc] init];
[[textEdit documents] addObject:doc];
doc.text = [[message content] get];
```

Note that the code does not set the `text` property until the scripting object has been added to TextEdit’s element array of documents. The following code fragment, on the other hand, creates a dictionary with the text property and then initializes the scripting object with it using `initWithProperties:` :

```
NSDictionary *props = [NSDictionary dictionaryWithObject:[[message content] get] forKey:@"text"];
TextEditDocument *doc = [[[textEdit classForScriptingClass:@"document"] alloc] initWithProperties:props];
[[textEdit documents] addObject:doc];
```

Listing 2-11 provides an extended example of conditionally creating and inserting iCal `calendar` and `event` objects, showing both approaches.

__Listing 2-11__  Creating and adding new scripting objects to the object graph

```objc

- (IBAction)addUpdateEvent:(id)sender {

    iCalApplication *iCal = [SBApplication applicationWithBundleIdentifier:@"com.apple.iCal"];
    iCalCalendar *theCalendar;

    [iCal activate];

    NSString *calendarName = [calendar titleOfSelectedItem];

    if ( [[[iCal calendars] objectWithName:calendarName] exists] ) {
        theCalendar = [[iCal calendars] objectWithName:calendarName];
    } else {

        NSDictionary *props = [NSDictionary dictionaryWithObject:calendarName forKey:@"name"];
        theCalendar = [[[[iCal classForScriptingClass:@"calendar"] alloc] initWithProperties: props] autorelease];
        [[iCal calendars] addObject: theCalendar];
    }

    NSString *eventName = [event stringValue];
    NSDate* startDate = [time dateValue];
    NSDate* endDate = [[[NSDate alloc] initWithTimeInterval:3600 sinceDate:startDate] autorelease];

    iCalEvent *theEvent;
    NSArray *matchingEvents =
        [[theCalendar events] filteredArrayUsingPredicate:
            [NSPredicate predicateWithFormat:@"summary == %@", eventName]];

    if ( [matchingEvents count] >= 1 ) {
        theEvent = (iCalEvent *) [matchingEvents objectAtIndex:0];
        [theEvent setStartDate:startDate];
        [theEvent setEndDate:endDate];
    } else {
        theEvent = [[[[iCal classForScriptingClass:@"event"] alloc] init] autorelease];
        [[theCalendar events] addObject: theEvent];
        [theEvent setSummary:eventName];
        [theEvent setStartDate:startDate];
        [theEvent setEndDate:endDate];
    }
    [iCal release];
}
```

[Next](Improving%20the%20Performance%20of%20Scripting%20Bridge%20Code.md)[Previous](About%20Scripting%20Bridge.md)

