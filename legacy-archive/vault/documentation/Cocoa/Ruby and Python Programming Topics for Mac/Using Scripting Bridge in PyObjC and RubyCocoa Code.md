---
title: Ruby and Python Programming Topics for Mac
apple_id: TP40004936
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: ScriptingBridge
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/RubyPythonCocoa/Articles/UsingScriptingBridge.html
archived_at: '2026-07-15T07:18:40.829013Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Ruby and Python Programming Topics for Mac](Introduction%20to%20Ruby%20and%20Python%20Programming%20Topics%20for%20OS%20X.md)


[Next](Generating%20Framework%20Metadata.md)[Previous](Using%20RubyOSA.md)

# Using Scripting Bridge in PyObjC and RubyCocoa Code

Scripting Bridge is a technology that you can use in PyObjC and RubyCocoa scripts to communicate with scriptable applications—that is, applications with scripting interfaces compliant with the Open Scripting Architecture (OSA). With Scripting Bridge, RubyCocoa and PyObjC scripts can do what AppleScript scripts can do: control scriptable applications and exchange data with them. The Scripting Bridge framework implements a bridge between OSA and the Objective-C runtime. It reads the scripting definition of applications and dynamically populates the Objective-C namespace with objects and methods representing the various items it finds (scripting objects, elements, commands, properties, and so on). RubyCocoa and PyObjC are also bridges to the Objective-C runtime and thus have access to everything in a program’s namespace, including Scripting Bridge–created objects.

The section on Scripting Bridge in [Ruby and Python on OS X](Ruby%20and%20Python%20on%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrtfvjvomi) surveys the technology, describing its capabilities and architecture. The following sections describe how your RubyCocoa and PyObjC scripts and programs can take advantage of Scripting Bridge.

The essential idea behind using Scripting Bridge is to get an object representing a scriptable application and then send messages to that object. Messages can result in objects being returned from the application object, and you can send messages to those objects—and so on down the object graph. The messages that you can send are described in the application’s scripting interface, or dictionary. Let’s start by looking at a simple example using RubyCocoa (Listing 1).

__Listing 1__  The `iTunes_inspect.rb` script

```
require 'osx/cocoa'
include OSX
OSX.require_framework 'ScriptingBridge'

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
iTunes.sources.each do |source|
  puts source.name
  source.playlists.each do |playlist|
    puts " -> #{playlist.name}"
    playlist.tracks.each do |track|
      puts "      -> #{track.name}" if track.enabled?
    end
  end
end
```

When you run this script from the command line, it prints information similar to the following lines:

```swift
Library
-> Classical CD
     -> Toccata & Fugue in D Minor
     -> Air on the G String (2nd movement from Orchestral Suite No. 3 in D)
     -> No.13 Waltz of the Flowers
     -> Montagues And Capulets
     -> Egmont Overture, Op 84
     -> Die Zauberflöte
     -> Horn concerto 3EFlat, 1. Allegro
     -> Horn concerto 3EFlat 2. Romance. Larguetto
     -> Horn concerto 3EFlat, 3. Allegro
     ........
```

The first thing to notice about the script in [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrufvjvomy) are the first three lines, which set up the necessary environment. The first statement loads the osx/cocoa library, and the next two statements append the features of the OSX module and import the Scripting Bridge framework from it.. All three statements in the given order are required for RubyCocoa programs that use the Scripting Bridge.

The next line is particularly interesting:

```
iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
```

This statement is a message expression that returns an proxy Ruby object representing a scriptable application, in this case iTunes. The message invokes the class method [applicationWithBundleIdentifier:](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1588086-applicationwithbundleidentifier) of the `SBApplication` class of the Scripting Bridge framework. This method requires that you identify the scriptable application by its bundle identifier. (See [The Scripting Bridge Classes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrufvjvomjq) for more about `SBApplication` and its methods for creating application objects.)

From this point on, the script sends messages across the bridge to the scriptable-application object and the objects it contains, gets the values of certain properties, and performs Ruby operations on the results. In Scripting Bridge’s internal representation of a scriptable application, a hierarchy of objects descends from the application object; sending a message to the application object may return elements, which are collections of other objects; each object in the element array may have elements containing objects, and so on. You can send appropriate messages to each of these objects. Take these lines as an example:

```
iTunes.sources.each do |source|
    puts source.name
    source.playlists.each do |playlist|
        puts " -> #{playlist.name}"
```

The `sources` message to the iTunes proxy object returns an object that implements the Ruby Array interface; on the other side of the bridge, this is an [SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbelementarray) object. The script then loops through the array and in a block sends a `name` message to each fetched object (`source`, representing a music source) and prints the returned Ruby string. It next sends `playlists` to `source` and iterates through the array returned from that call, which represents the playlists associated with that music source. It prints the name of each playlist. And so on until it gets and prints the name of each track.

Using Scripting Bridge in a PyObjC script is as simple and straightforward as it is for RubyCocoa. Here is a short script that prints (to standard output) the name of the track currently playing on iTunes:

```
from Foundation import *
from ScriptingBridge import *

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
print iTunes.currentTrack().name()
```

In this case, setting up the environment for using Scripting Bridge involves just two import statements, one for the Foundation framework and the other for the Scripting Bridge framework.

The Scripting Bridge also allows you to add objects to a scriptable application. For this it declares the following `SBApplication` method, which returns the class object for the scripting class specified in the receiver’s scripting definition:

```objc
+ (Class)classForScriptingClass:(NSString *)className;
```

Once you have the `Class` object, you can instantiate a scripting object of the indicated type and add it to the application. If, for example, you wanted to add a playlist to iTunes, in PyObjC code you could similar to the example in [Listing 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrufvjvona):

__Listing 2__  Adding an object to a scriptable application in PyObjC code

```
from Foundation import *
from ScriptingBridge import *

iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
p = {'name':'Testing'}
playlist = iTunes.classForScriptingClass_("playlist").alloc().initWithProperties_(p)
iTunes.sources()[0].playlists().insertObject_atIndex_(playlist, 0)
```

Scripting Bridge does not actually create an object in the target application until you add the allocated and initialized object to an appropriate element array ([SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbelementarray)), such as `playlists` in the above example.

The Scripting Bridge framework has three public Objective-C classes:

- [SBApplication](https://developer.apple.com/documentation/scriptingbridge/sbapplication)—A class whose objects represent scriptable applications
- [SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbelementarray)—A class whose objects represent collections of elements in the scripting definition
- [SBObject](https://developer.apple.com/documentation/scriptingbridge/sbobject)—The base class of scripting objects in a scriptable application

The class factory methods of `SBApplication` enable you to obtain an object representing an OSA-compliant application. The following methods return an `SBApplication` object representing an application (autoreleased in memory-managed environments):

- `+ (id) applicationWithBundleIdentifier:(NSString *)bundleID;`

  Finds the application using its bundle identifier, for example `@“com.apple.iTunes”`. This is the recommended approach for most situations, especially when the application is local, because it dynamically locates the application.
- `+ (id) applicationWithURL:(NSURL *)url;`

  Finds the application using an object representing a URL with a `file:` or `eppc:` file scheme; the latter scheme is used for locating remote applications.
- `+ (id) applicationWithProcessIdentifier:(pid_t)pid;`

  Finds the application using its BSD process identifier (`pid`).

When you create an `SBApplication` object, Scripting Bridge reads the application’s scripting definition and constructs a graph of objects that represents what it finds. It creates an instance representing an application from a dynamically defined and implemented subclass of `SBApplication` that is specific to the application. This instance is the top-level object of the graph. It populates the subordinate objects of the graph with `SBElementArray` and `SBObject` objects. It creates instances of the scripting classes it finds in the application’s `sdef` file from dynamically defined and implemented subclasses of `SBObject`. Elements, however, are always represented in Objective-C code by instances of `SBElementArray`, which is a subclass of [NSMutableArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSMutableArray). This means that you can invoke on `SBElementArray` object all the methods of `NSMutableArray` and its superclass, [NSArray](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/cl/NSArray),

In addition to creating objects, Scripting Bridge implements various methods in the `SBApplication` and `SBObject` subclasses to represent the types of certain items it finds in the application’s `sdef` file. It implements scriptable properties as Objective-C declared properties (that is, with the `@property` directive); the declared properties, in turn, synthesize accessor methods to get and (in some cases) set the value of the property. It implements elements as methods that return `SBElementArray` objects. And it implements commands as parameter-less methods returning no value; where these methods are implemented depends on whether they are of a specific or generic object class:

- If it is of a specific object class (such as “document”) it is implemented as a method on that class.
- If it is a generic object (such as “specifier”) it is implemented as a method of the `SBApplication` subclass.

Each `SBObject` and `SBApplication` object is built around an object specifier, a reference that tells Scripting Bridge how to locate the actual object in the target application. To obtain the more specific, canonical form of the reference, you must evaluate the object in an appropriate message expression or send it a [get](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423965-get) message. See [Improving the Performance of Scripting Bridge Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrufvjvomjr) for more information on this subject.

You can find out which messages you can send to a scriptable application by examining a header file containing Objective-C declarations of the application class and the application’s scripting classes. The header file serves as reference documentation for that application. It includes information about the inheritance relationships between classes and the containment relationships between their objects. It declares commands and elements as methods, and declares properties as Objective-C declared properties. Taking the iTunes application as an example, the header file shows the definition of the application class (`iTunesApplication`), the application’s scripting classes, such as `iTunesTrack` and `iTunesSource`, commands (such as the `eject` method), and properties (such as the `artist` declared property). A header files also includes comments extracted from the scripting definition, such as the comment added to this declaration for the `FinderApplication` class:

```objc
- (void)empty;   // Empty the trash
```

You need to translate Objective-C method declarations into the Ruby or Python equivalent—or example, replacing the colon of each keyword with an underscore.

To create a header file you need to run two command-line tools—`sdef` and `sdp`—together, with the output from one piped to the other. This is the recommended syntax:

`sdef` _/path/to/application_`.app | sdp -fh --basename` _applicationName_ `--bundleid` _bundleIdentifier_

The `sdef` utility gets the scripting definition from the designated application; if that application does not contain an sdef file, but does instead contain scripting information in an older format (such as the scripting suite and terminology property lists), it translates that information into the sdef format first. The `sdp` tool run with the above options generates an Objective-C header file for the designated scriptable application. Thus, for iTunes, you would run the following command to produce a header file named `iTunes.h`:

```
sdef /Applications/iTunes.app | sdp -fh --basename iTunes --bundleid com.apple.iTunes
```


Because fetching data from a scriptable application via Apple events is expensive, the Scripting Bridge is designed to defer the sending of Apple events until it needs to. It does this by using references to objects. When you ask the Scripting Bridge for an object in a scriptable application, it returns a reference to that object, not the object itself. It defers evaluation of the reference into its original canonical form until you actually request data from that object. This technique is called lazy evaluation. For example, if you request an iTunes track, it returns a reference to the track object; but when you request the name of the track, it evaluates the reference and sends an Apple event to fetch the string data (that is, the name). This design of the Scripting Bridge leads to a few recommended programming practices:

- Be careful about the order of the statements in your code; do not assume you’ve received the data that was present in an object when you first obtained a reference to it.
- To force the evaluation of an object reference, invoke the [get](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423965-get) method (declared by `SBObject`) on an object. This call returns the more specific, canonical form of reference to the object.

  Using `get` to force evaluation is valuable when you want to retain a reference to the current object when the non-canonical form of reference—`app.documents[0]` (for frontmost document)—could refer to different objects over time. However, because calling `get` involves the sending of an Apple event, you should use it only when necessary.
- Do not force repeated evaluations of an object reference in a loop, such as when comparing the name of an object against a series of string constants. Each such call results in the sending of an Apple event. Instead force evaluation once and store the returned value in a local variable; then use that variable in the loop.
- As a corollary to the above guideline, avoid enumerating [SBElementArray](https://developer.apple.com/documentation/scriptingbridge/sbelementarray) objects if there are alternatives, which Scripting Bridge and Cocoa provide:

  - Use the [arrayByApplyingSelector:](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423951-arraybyapplyingselector) or [arrayByApplyingSelector:withObject:](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1424007-array) method to get a value from each object in the array.
  - Use the [makeObjectsPerformSelector:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/makeObjectsPerformSelector:) or [makeObjectsPerformSelector:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/makeObjectsPerformSelector:withObject:) method if you want to make each object in the array do something.
  - Use the [filteredArrayUsingPredicate:](https://developer.apple.com/documentation/foundation/nsarray/1411033-filtered) method if you want a specific subset of the original array.

Another technique for improving the performance of your code is checking whether an application is launched before trying to communicate with it. When you create an instance of a scriptable application, the Scripting Bridge automatically launches it if it hasn’t already been launched. This is an expensive operation. Sometimes this might be what you want, but in other situations you might be interested in communicating with an application only if it’s currently being used. In such cases, invoke the [isRunning](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423981-isrunning) method of `SBApplication` and check the returned Boolean value before proceeding.

_[Scripting Bridge Release Note](https://developer.apple.com/library/archive/releasenotes/ScriptingAutomation/RN-ScriptingBridge/index.html#//apple_ref/doc/uid/TP40004741)_ presents detailed information on lazy evaluation, checking for launched applications, and related APIs and programming guidelines.

To better appreciate the varieties of ways in which you might use Scripting Bridge in RubyCocoa or PyObjC code, let’s examine a few examples. The script in Listing 3 creates a proxy instance of the Finder application and from it requests the current contents of the Desktop. Using Ruby regular expressions and string-manipulation methods, it formats and prints these items.

__Listing 3__  The `Finder_show_desktop.rb` script

```
# Lists the content of the Finder desktop.

require 'osx/cocoa'
include OSX
OSX.require_framework 'ScriptingBridge'

app = SBApplication.applicationWithBundleIdentifier_("com.apple.finder")
ary = app.desktop.entireContents.get
ary.each do |x|
    next unless x.is_a?(OSX::FinderItem)
    puts "#{x.class.name.sub(/^.+::/, '').sub(/_/, ' ').ljust(25)} #{x.name}"
end
```

The script in Listing 4 exchanges data between proxy instances of two applications, TextEdit and Mail. It gets the selected messages in all current Mail viewers and copies each the content of each message to a TextEdit window. There are a couple things of special note in this script. It shows how to create a scripting class for the current application using [classForScriptingClass:](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423987-class) to obtain the `Class` object to use for allocation; it then adds the created document to an `SBElementArray` object (`textedit.documents`) _before_ setting its text to that of the email message.

__Listing 4__  The `get_selected_mail.rb` script

```

# Copy contents of selected Mail messages to a TextEdit window

require 'osx/cocoa'
include OSX
OSX.require_framework 'ScriptingBridge'

textedit = SBApplication.applicationWithBundleIdentifier_("com.apple.TextEdit")
mailApp = SBApplication.applicationWithBundleIdentifier_("com.apple.mail")
viewers = mailApp.messageViewers
viewers.each do |viewer|
  viewer.selectedMessages.each do |message|
    doc = textedit.classForScriptingClass_("document").alloc.init
    textedit.documents.addObject_(doc)
    doc.setText_(message.content.get)
 end
end
```

Finally. the Listing 5 script updates in the iChat status area the time the system has been running since it was last booted. It is similar to [Listing 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2timrufvjvomy) it that it makes a system call, but instead of calling the `system` method, it invokes the `uptime` command simply by enclosing it in single quotes. It then formats the output of the command and assigns this formatted string to the iChat `status_message` property. All this occurs in a closed loop, which is re-executed after a five-second pause, which causes a periodic update of the system-uptime message.

__Listing 5__  The `iChat_uptime.rb` script

```

# Periodically set your iChat status to the output of uptime(1).

require 'osx/cocoa'
include OSX
OSX.require_framework 'ScriptingBridge'

app = SBApplication.applicationWithBundleIdentifier_("com.apple.iChat")
previous_status_message = app.statusMessage
trap('INT') { app.statusMessage = previous_status_message; exit 0 }
while true
    u = `uptime`
    hours = u.scan(/^\s*(\d+:\d+)\s/).to_s + ' hours'
    days = u.scan(/\d+\sdays/).to_s
    app.statusMessage = "OSX up #{days} #{hours}"
    sleep 5
end
```

This script traps interruption of the script (such as happens when the user presses Control-C) and restores the previous value of the iChat status message before exiting.

[Next](Generating%20Framework%20Metadata.md)[Previous](Using%20RubyOSA.md)

