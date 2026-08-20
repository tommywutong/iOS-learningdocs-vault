---
title: JNI Development on Mac OS X
apple_id: DTS10003827
resource_type: Technical Note
platform: Java
topic: Cross Platform
technology: null
published: '2011-07-14'
source_url: https://developer.apple.com/library/archive/technotes/tn2147/_index.html
archived_at: '2026-07-26T19:54:08.739129Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



# Retired Document

__Important:__
This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

Technical Note TN2147

# JNI Development on Mac OS X

__Important:__ This document may not represent best practices for current development. Links to downloads and other resources may no longer be valid.

The Java Native Interface (JNI) is the standard mechanism for integrating Java code with code written in any C-derived language (C, C++, Objective-C). It can be used to access data, incorporate native elements into a Java user interface, even create a Java Virtual Machine (JVM) from within a native application.

This technote discusses techniques and concerns specific to JNI programming on Mac OS X with explicit examples of what to do (and what not to do).

You should read this technote if you are already working with the JNI on Mac OS X, or if you are writing an application in Java 1.4 or later which needs to interface with one of the many non-Java frameworks on Mac OS X. You should also read this technote if you are a Core Foundation or Cocoa developer who needs to leverage Java libraries or APIs from your application.

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfveu4vcsj4)[Building and Deploying JNI Libraries on Mac OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvbfkskmireu4ry)[Data Transfer Between Java and Native Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvcecvcb)[Working With Strings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvjviusjjzdvg)[Working With Object References](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvhuessfinkf6usfizjq)[Java-Native Graphical Interaction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvdvksk7jfhfirkhkjaviskpjy)[AWT Native Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvfecv2u)[CocoaComponent](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvbu6q2pifbu6tkqj5hektsu)[Thread-Safe JNI Programming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvkequsfifcf6u2bizcviwi)[Calling AppKit From AWT/Swing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvavaucljfkf6rssj5gv6qkxkq)[Calling AWT/Swing From AppKit](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvavovc7izje6tk7ififas2jkq)[Calling AppKit or AWT From Non-Event Threads](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvbeox2ujbjekqkekm)[Invoking the Java Virtual Machine From Native Code](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfveu4vspinaviskpjy)[Creating a JVM From Core Foundation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvbumx2jjzle6q2bkreu6tq)[Creating a JVM From Cocoa](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvhfgx2jjzle6q2bkreu6tq)[Staying off the Main Thread](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvkequsfifcekrc7jfhfmt2difkest2o)[Requesting a Specific J2SE Version](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvlekustjfhu4x2jjzde6)[Debugging JNI Applications on Mac OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvcekqsvi4)[Decoding UnsatisfiedLinkError](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvku4u2bkrevgrsjivceyskojncveuspki)[Further Reading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvjukrk7ifgfgty)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

The JNI is a low-level mechanism for communication between Java and C-based code. The most common use of the technology is accessing system functionality that does not easily match up with cross-platform Java features or APIs. In the case of Mac OS X, this could mean accessing data from the Mac OS X Address Book, or even displaying Quartz Composer compositions.

The JNI can also be used to facilitate incremental migration of a C codebase to Java, or vice-versa. Instead of migrating the entire project at once, conversion can occur across multiple releases, using the JNI to maintain integration between, for example, the new Java code and remaining C code.

Finally, the JNI provides an invocation interface for creating and communicating with a JVM from a native application.

This technote discusses the specific details of working with the JNI on Mac OS X. It begins with simple translation of data and object references, and moves on to the more advanced topic of integrating native Cocoa GUI objects within a Java GUI. Threading concerns and techniques for addressing and avoiding problems are also discussed. Finally, it explains how to correctly create a JVM from within a Core Foundation or Cocoa application.

The information and techniques described in this technote are specific to Java 1.4 and later on Mac OS X. Basic knowledge of the JNI is assumed. Developers unfamiliar with the JNI should first read [The Java Native Interface: Programmer's Guide and Specification](http://java.sun.com/docs/books/jni/).

[Back to Top](#)

## Building and Deploying JNI Libraries on Mac OS X

The Xcode IDE can be a very powerful tool for building JNI applications, as both Java and native code can be built and bundled from a single project. However, this technote focuses mainly on JNI programming. The numerous samples cited below all include Xcode projects as starting points. For information on building a JNI project in Xcode from scratch, see [Building a JNI Universal Project With Xcode](https://developer.apple.com/java/jniuniversal.html).

There are a few things to keep in mind when building JNI libraries on Mac OS X, regardless of the tools you're using. JNI libraries must be:

- Built as Dynamic Libraries in Xcode (`MACH_O_TYPE mh_dylib`). Libraries of any other type (e.g. Static) do not load.
- Built as universal binaries. PowerPC libraries do not load on Intel-based Macs, nor vice-versa. See [Technical Q&A QA1295, 'Java on Intel-based Macs'](https://developer.apple.com/qa/qa2005/qa1295.html).
- Named `libFoo.jnilib`, where `Foo` is the name passed to `System.loadLibrary`
- Placed in a loadable library path. Possible paths include:
- - The Java Resources subdirectory of your application bundle (e.g. `YourApp.app/Contents/Resources/Java`)
  - The working directory at launch time (i.e. `user.dir`)
  - A Java extension directory listed in [Technical Q&A QA1170, 'Important Java Directories on Mac OS X'](https://developer.apple.com/qa/qa2001/qa1170.html)
  - The Mac OS X dynamic library search path explained in [Dynamic Library Usage Guidelines](https://developer.apple.com/documentation/DeveloperTools/Conceptual/DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html)
- You can also set the `java.library.path` system property at application launch time to specify an alternate installation path.

[Back to Top](#)

## Data Transfer Between Java and Native Code

### Working With Strings

Accessing or creating Java `String` objects with the JNI is no different than on any other platform. As in Java, Core Foundation and Cocoa string objects represent an array of UTF-16 Unicode characters; Unicode is therefore the preferred character type when translating between Java strings and other native string types on Mac OS X. This is worth mentioning because many of the older JNI tutorials use UTF-8 characters when dealing with Java strings.

#### Creating Java Strings From Native Strings

On Mac OS X, the `jchar` and `UniChar` types are interchangeable and can be safely casted back and forth, making conversion between Java and native string objects much easier. Converting a Cocoa string (`NSString`) to a Java string (`jstring`) is illustrated in Listing 1.

__Listing 1__  Creating a Java String from an `NSString`

```
NSString *myNSString = @"This is an NSString";
// Note that length returns the number of UTF-16 characters,
// which is not necessarily the number of printed/composed characters
jsize buflength = [myNSString length];
unichar buffer[buflength];
[myNSString getCharacters:buffer];
jstring javaStr = (*env)->NewString(env, (jchar *)buffer, buflength);
```

Listing 2 demonstrates creating a `jstring` from a Core Foundation `CFString` when programming in C or C++.

__Listing 2__  Creating a Java String from a `CFString`

```
CFStringRef myCFString = CFSTR("This is a CFString");
CFRange range;
range.location = 0;
// Note that CFStringGetLength returns the number of UTF-16 characters,
// which is not necessarily the number of printed/composed characters
range.length = CFStringGetLength(myCFString);
UniChar charBuf[range.length];
CFStringGetCharacters(myCFString, range, charBuf);
jstring javaStr = (*env)->NewString(env, (jchar *)charBuf, (jsize)range.length);
```

#### Creating Native Strings From Java Strings

Creating native strings (`NSString`/`CFString`) from Java strings is equally simple and both techniques are demonstrated in Listings 3 and 4.

__Listing 3__  Creating an `NSString` from a Java String

```
const jchar *chars = (*env)->GetStringChars(env, my_jstring, NULL);
NSString *myNSString = [NSString stringWithCharacters:(UniChar *)chars
                        length:(*env)->GetStringLength(env, my_jstring)];
(*env)->ReleaseStringChars(env, my_jstring, chars);
```

__Listing 4__  Creating a `CFString` from a Java String

```
const jchar *chars = (*env)->GetStringChars(env, my_jstring, NULL);
CFStringRef myCFString = CFStringCreateWithCharacters (kCFAllocatorDefault,
            chars, (*env)->GetStringLength(env, my_jstring));
(*env)->ReleaseStringChars(env, my_jstring, chars);
```

__Important:__ Both of these examples finish with a necessary call to `ReleaseStringChars`, which notifies the JVM that you no longer require access to the Java string. [Section 10.11 of The Java Native Interface: Programmer's Guide and Specification](http://java.sun.com/docs/books/jni/html/pitfalls.html#29163) states: "Forgetting to call the `ReleaseStringChars` function may cause either the `jstring` object to be pinned indefinitely, leading to memory fragmentation, or the C copy to be retained indefinitely, a memory leak." You can alternately pass Java `char` or `byte` arrays through the JNI, eliminating the need to call `GetStringChars` or `ReleaseStringChars`.

#### Handling Unicode Supplementary Characters

The previous examples demonstrate conversion of full strings between environments. Accessing single characters or substrings has repercussions when dealing with Unicode supplemental characters (from `0x10000` to `0x10FFFF`). Mac OS X and Java both treat supplemental characters as surrogate pairs of UTF-16 characters. Accessing UTF-16 characters from an arbitrary index, then, risks extracting only half of a surrogate pair. To ensure you obtain all the data you need, use the following APIs:

- Core Foundation (`CFString`): [CFStringGetRangeOfComposedCharactersAtIndex](https://developer.apple.com/documentation/CoreFoundation/Reference/CFStringRef/Reference/reference.html#//apple_ref/c/func/CFStringGetRangeOfComposedCharactersAtIndex)
- Cocoa (`NSString`): [rangeOfComposedCharacterSequenceAtIndex:](https://developer.apple.com/documentation/Cocoa/Reference/Foundation/ObjC_classic/Classes/NSString.html#//apple_ref/occ/instm/NSString/rangeOfComposedCharacterSequenceAtIndex:)
- Java (`String`): [codePointAt](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html#codePointAt(int)), [codePointBefore](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html#codePointBefore(int)), [codePointCount](http://java.sun.com/j2se/1.5.0/docs/api/java/lang/String.html#codePointCount(int,%20int))

  __Note:__ Supplemental character support is new to J2SE 5.0 (JDK 1.5); previous versions of Java did not contain these APIs.

### Working With Object References

The rules for using Java object references in native code, as well as C pointers in Java code, are no different on Mac OS X from other platforms. However, the key points in sharing object references across the JNI are worth a brief discussion.

References to nearly every type of Java object are represented in the JNI by the generic `jobject` type. The other explicit types are `jstring` (discussed in the previous section) and `jclass` (which represents a `java.lang.Class` reference). `jobject` references are typically stored in C structures or C++/Objective-C objects using JNI __global references__. The techniques and rules for using global references are described in [Chapter 5 of The Java Native Interface: Programmer's Guide and Specification](http://java.sun.com/docs/books/jni/html/refs.html).

#### Passing Native Pointers Across the JNI

JNI functions which return pointers to Java code should have a return type of `jlong`. This stores the pointer in a 64-bit Java `long` variable that can later be passed back down to JNI functions, cast to the appropriate pointer type, and used in any necessary operations. Casting a `jlong` on 32-bit systems correctly preserves the lower 32 bits where the address is stored.

[Back to Top](#)

## Java-Native Graphical Interaction

Aside from simply sharing data, the JNI can also be used to access the user interface resources of the underlying platform. There are a number of mechanisms for integrating Java and Cocoa user interface components using the JNI. This section discusses those mechanisms, and the important guidelines for using them successfully. The content and examples below will assume some understanding of Quartz and Cocoa; for familiarity with these technologies see [Getting Started With Cocoa](https://developer.apple.com/referencelibrary/GettingStarted/GS_Cocoa/index.html) and [Quartz 2D Programming Guide](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/index.html).

### AWT Native Interface

The AWT Native Interface (JAWT) is the oldest and most universal method for drawing into a Java component with native code. A JAWT-enabled AWT component can use a native library to access Quartz (Core Graphics), Core Image, or any other graphical framework available on Mac OS X.

For an introduction to the JAWT and how to use it, see [The AWT Native Interface](http://java.sun.com/j2se/1.5.0/docs/guide/awt/1.3/AWT_Native_Interface.html). [Sample Code Project 'JAWTExample'](https://developer.apple.com/samplecode/JAWTExample/) demonstrates steps and structures specific to Mac OS X.

In addition to native rendering, the JAWT also allows access to platform-specific resources such as (in the case of Mac OS X) a Java component's `NSView`-based native peer and parent `NSWindow`, allowing for some less-conventional but still legitimate uses. [Sample Code Project 'JSheets'](https://developer.apple.com/samplecode/JSheets/) uses the JAWT to display a document modal sheet from a `JFrame`.

### CocoaComponent

`CocoaComponent` is an extendable class which allows you to embed a native Cocoa view inside a Java container. Once added to a container and shown, a `CocoaComponent` object allows the underlying Cocoa view to do all of the drawing and event processing. This technology can be used, for example, to place a `WebView` from the Web Kit framework inside a Java frame and instantly turn your Java application into a web browser.

A `CocoaComponent` implementation has two parts: a Java class to be instantiated and added to your AWT hierarchy; and an Objective-C `NSView` subclass which dictates the `CocoaComponent` object's runtime behavior. To create your own `CocoaComponent`, you must:

- Extend the `com.apple.eawt.CocoaComponent` class.
- Implement the `createNSView` and `createNSViewLong` methods. Depending on the system architecture, one of these methods is called around the time your `CocoaComponent` is added to the component hierarchy and returns a Java `int` (or `long`) representing a pointer to your underlying `NSView`. It is recommended that you implement `createNSViewLong`, which returns the pointer in a 64-bit Java `long`, and implement `createNSView` to simply return the result of `createNSViewLong` cast down to a Java `int` (for 32-bit support).

  __Listing 5__  `createNSView` and `createNSViewLong` methods

  ```
  // Instantiate the NSView on the native side and return it as a long
  public native long createNSViewLong();

  // Deprecated; just cast the correct createNSViewLong implementation
  public int createNSView() {
      return (int)createNSViewLong();
  }
  ```
- Implement your `NSView` subclass in Objective-C. This is where you decide exactly what your `CocoaComponent` will be and do: it could be a `WebView`, an `ABPeoplePickerView` from the Address Book framework, or any other `NSView`-based object.
- Provide a native implementation of `createNSViewLong`. This is where you instantiate your `NSView` and return its pointer to Java as a `jlong`. There is no need to retain the view — it is retained by the AWT implementation when the `CocoaComponent` object is added to the container hierarchy.

  __Listing 6__  Native implementation of `createNSViewLong`

  ```
  JNIEXPORT jlong JNICALL Java_com_mycompany_MyCocoaComponent_createNSViewLong (JNIEnv *env, jobject caller) {
      MyCCView *newView = [[[MyCCView alloc] init] autorelease];
      return (jlong)newView;
  }
  ```

This is all that is required to create a trivial `CocoaComponent` and have it show up in a Java container. However, you may also need to communicate back and forth between your Cocoa view and its Java peer.

#### Messaging CocoaComponent

`CocoaComponent` provides a `sendMessage` convenience method for Java-to-Cocoa communication. This allows you to pass in an opcode (defined by you) and a single parameter object for your underlying cocoa view to use and interpret in its own `awtMessage:message:env` method. [Sample Code Project QCCocoaComponent](https://developer.apple.com/samplecode/QCCocoaComponent/) uses `sendMessage` to load and play Quartz Composer compositions inside a Java frame. Listing 7 shows a controller class making calls on methods defined by the sample project's `JavaQCView` class.

__Listing 7__  Example use of `CocoaComponent`.`sendMessage`

```
public void actionPerformed(ActionEvent e) {
    if (e.getSource() == loadButton) {
        view.loadComposition ("Particle System.qtz");
    } else {
        view.startRendering();
    }
}
```

The above `loadComposition` and `startRendering` methods use the `sendMessage` API to communicate with the underlying Quartz Composer view.

__Listing 8__  Abstracting `sendMessage` for specific use

```
final static int LOAD_MESSAGE = 0;
final static int START_MESSAGE = 1;

public void loadComposition(String fullPath) {
    sendMessage(LOAD_MESSAGE, fullPath);
}

public void startRendering() {
    sendMessage(START_MESSAGE, null);
}
```

Finally, the `QCView` subclass implements `awtMessage:message:env` to respond to calls from the `CocoaComponent` object.

__Listing 9__  Implementation of `awtMessage:message:env`: responds to Java `sendMessage` calls

```objc
- (void) awtMessage:(jint)messageID message:(jobject)message env:(JNIEnv *)env {
  jchar *chars;
  switch (messageID) {
    case apple_dts_samplecode_qccocoacomponent_JavaQCView_LOAD_MESSAGE:
      // CocoaComponent.sendMessage takes an Object; we need a String here
      if ((*env)->IsInstanceOf(env, message, (*env)->FindClass(env, "java/lang/String"))) {
        chars = (*env)->GetStringChars(env, (jstring)message, NULL);
        NSString *cocoaPath = [NSString stringWithCharacters:(unichar *)chars
                    length:(*env)->GetStringLength(env, message)];
        [self loadCompositionFromFile:cocoaPath];
        (*env)->ReleaseStringChars(env, message, chars);
      } else {
        jclass argExcClass = (*env)->FindClass(env, "java/lang/IllegalArgumentException");
        (*env)->ThrowNew(env, argExcClass,
                    "JavaQCView: sendMessage with an ID of LOAD_MESSAGE must be accompanied by a String");
      }
      break;
    case apple_dts_samplecode_qccocoacomponent_JavaQCView_START_MESSAGE:
      [self startRendering];
      break;
    default:
      break;
  }
}
```

#### Receiving Messages From CocoaComponent

Calling back into Java is a little more complicated, although it still involves completely standard JNI practices. Simply displaying a Java dialog to alert the user, for example, does not require a specific point of entry. However, it may be necessary for your Cocoa view to talk directly to its Java peer (the `CocoaComponent` object). This can be facilitated by using JNI global references as you would on other platforms. By creating and holding a global reference to the Java object, you can make calls on it whenever necessary. An opportune time to create your global reference is inside the native implementation of `createNSViewLong`, as that function receives a reference to the `jobject` representing your `CocoaComponent`. Listing 10 shows how [Sample Code Project 'CWCocoaComponent'](https://developer.apple.com/samplecode/CWCocoaComponent/) does this.

__Listing 10__  Saving a global reference to a `CocoaComponent`

```objc
JNIEXPORT jlong JNICALL Java_apple_dts_samplecode_cwcocoacomponent_JavaColorWell_createNSViewLong
        (JNIEnv *env, jobject caller) {
    return (jlong)[JavaColorWell colorWellWithCaller:caller env:env];
}

@implementation JavaColorWell

+ (id) colorWellWithCaller:(jobject) caller env:(JNIEnv *)env {
    return [[[JavaColorWell alloc] initWithCaller:caller env:env] autorelease];
}

// Obtain a JNI global reference to the enclosing Java object
// This will be used later to fire AWT events after a color change
- (id) initWithCaller:(jobject)caller env:(JNIEnv *)env {
    self = [super init];
    // "javaPeer" is declared in JavaColorWell.h;
    javaPeer = (*env)->NewGlobalRef(env, caller);
    return self;
}
```

The Cocoa `JavaColorWell` class then makes calls on the global reference using standard JNI method lookups. See [Section 4.2 of The Java Native Interface: Programmer's Guide and Specification](http://java.sun.com/docs/books/jni/html/fldmeth.html#26010) for the basics of calling Java methods from C.

Those familiar with the JNI will realize that the above technique presents a problem: since global reference affect garbage collection, the `CocoaComponent` object will not be collected as long as the global reference exists. The `CocoaComponent`'s removal from its container, signalled by the inherited `java.awt.Component.removeNotify` method, is an opportune time to delete the global reference, and `sendMessage` makes the task simple. We again turn to [Sample Code Project 'CWCocoaComponent'](https://developer.apple.com/samplecode/CWCocoaComponent/) for a demonstration, illustrated in Listings 11 and 12.

__Listing 11__  Relaying `removeNotify` to the underlying Cocoa view

```
final static int REMOVE_NOTIFY = 0;

// Tell the peer we've been removed from the hierarchy
public void removeNotify() {
    sendMessage(REMOVE_NOTIFY, null);
    super.removeNotify();
}
```

__Listing 12__  Deleting a JNI global reference in response to `removeNotify`

```objc
- (void) awtMessage:(jint)messageID message:(jobject)message env:(JNIEnv *)env {
    switch (messageID) {
    // Delete the globalRef to the Java peer when the component is removed from its container
        case apple_dts_samplecode_cwcocoacomponent_JavaColorWell_REMOVE_NOTIFY:
            if (javaPeer != NULL) {
                (*env)->DeleteGlobalRef(env, javaPeer);
            }
            break;
        // more cases...
    }
}
```

#### CocoaComponent Compatibility Mode

In Mac OS X Tiger, changes were made to the AWT implementation which could cause `CocoaComponent` code written in the Mac OS X Panther timeframe to deadlock. A compatibility layer was added to alleviate this problem by adding timeouts to certain operations, which can adversely affect performance on otherwise safe code. If you are using `CocoaComponent`, it is strongly recommended that you follow the guidelines in [Thread-Safe JNI Programming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvkequsfifcf6u2bizcviwi) and disable this compatibility layer by setting the `com.apple.eawt.CocoaComponent.CompatibilityMode` system property to `false` when launching your Java application.

[Back to Top](#)

## Thread-Safe JNI Programming

The examples presented in the previous section are fairly simple in principle: clear entry points are defined, and the Java and Cocoa environments do their respective jobs with no evident change in normal application behavior. Care must be taken, however, when integrating code that makes use of both the Cocoa and AWT event models.

While it is true that the AWT in Java 1.4 and later is implemented in Cocoa, the AWT Event Queue runs on a separate thread from the underlying Cocoa application's main event loop (which executes on the main thread, sometimes called "Thread-0"). Using JNI techniques such as JAWT and `CocoaComponent`, then, does carry synchronization concerns, which are discussed below.

__Note:__ Although this section uses the term "AWT" almost exclusively, it also applies to Swing applications. The term "AppKit" refers to the Cocoa Application Kit framework and supporting APIs.

The [javadoc for CocoaComponent](https://developer.apple.com/documentation/Java/Reference/1.5.0/appledoc/api/com/apple/eawt/CocoaComponent.html) states:

- Do not block the AWT event dispatch thread against the AppKit thread. Doing so likely results in a deadlock.
- Do not block the AppKit thread against the AWT event thread. Doing so likely results in a deadlock. Note that grabbing a Java-accessible lock (such as the AWT TreeLock) from the AppKit thread is considered unsafe for this reason. Avoid calling AWT or Swing methods from the AppKit thread.
- Once the `NSView` you are using has been added to the Cocoa view hierarchy on the AppKit thread, all calls on the implementation's `NSView` must be made on the AppKit thread.

When working with `CocoaComponent` you should assume that your Cocoa view is added to the hierarchy immediately after `createNSView` (or `createNSViewLong`) returns, and that the call takes place on the thread that adds your Java component. __Do not__ assume the call occurs on the AWT event thread, for example, if you add your component from `main`.

The first two items above, apply to __any__ integration of AppKit and AWT (`CocoaComponent` or otherwise). The inability to block either thread against the other forces us to adopt an asynchronous model when communicating between AppKit code and AWT code. Both environments have utility methods for accomplishing this.

### Calling AppKit From AWT/Swing

When you make calls to AppKit that may result in a view refresh or some other event-based action, you must make those calls on the main AppKit thread. Isolate your call into a method that can be passed into one of the `performSelectorOnMainThread:` methods defined in `NSObject`. An excerpt from [Sample Code Project 'JSheets'](https://developer.apple.com/samplecode/JSheets/), shown below, demonstrates this technique.

__Listing 13__  Using performSelectorOnMainThread for AppKit operations

```objc
JNIEXPORT void JNICALL Java_apple_dts_samplecode_jsheets_JSheetDelegate_nativeShowSheet
        (JNIEnv *env, jclass caller, jint type, jobject parent, jobject listener) {
    // Never assume an AutoreleasePool is in place, unless you are on the main AppKit thread
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];

    JSheetDelegate *jdel;

    NSWindow *parentWindow = GetWindowFromComponent(parent, env);
    switch (type) {
        case apple_dts_samplecode_jsheets_JSheetDelegate_OPEN_PANEL:
            jdel = [JSheetDelegate delegateWithListener:listener env:env];
            // We retain the delegate for use later; released after use in openPanelDidEnd:
            [jdel retain];
            [jdel performSelectorOnMainThread:@selector(showOpenPanelForWindow:)
                        withObject:parentWindow waitUntilDone:NO];
            break;
    }

    [pool release];
}

- (void) showOpenPanelForWindow:(NSWindow *)parentWindow {
    NSOpenPanel *op = [NSOpenPanel openPanel];
    [op setAllowsMultipleSelection:YES];
    [op beginSheetForDirectory:NSHomeDirectory() file:nil types:nil
            modalForWindow:parentWindow modalDelegate:self
            didEndSelector:@selector(openPanelDidEnd:returnCode:contextInfo:) contextInfo:nil];
}
```

There are two important things to note here: the call to `performSelectorOnMainThread:` and the `waitUntilDone:NO` parameter. It is not enough to simply execute on the main thread; __you must do so asynchronously__. Passing `waitUntilDone:YES` can cause as much trouble as being on the wrong thread. The [Sample Code Project 'JSheets'](https://developer.apple.com/samplecode/JSheets/) includes a (disabled) alternate implementation of the `nativeShowSheet` function which does not call `performSelectorOnMainThread:` Be sure to see what happens in the alternate case.

This technique is necessary even in pure Cocoa applications, for example when a peripheral thread needs to refresh the user interface after receiving information from a socket.

At this point you may be asking why none of the previous `CocoaComponent` examples make explicit use of this technique. This is because the `sendMessage` method is implemented to asynchronously message your underlying Cocoa view on the main thread (this explains why `sendMessage` has a return type of `void`). `sendMessage`, then, is a double convenience: it eliminates the need for numerous JNI functions, and it provides automatic asynchronous messaging to the main AppKit thread.

### Calling AWT/Swing From AppKit

The same principle applies in the opposite direction — making AWT calls from AppKit. Say your native code receives a Cocoa notification you are subscribed to. Notifications occur on the main AppKit thread, so making a direct AWT call from your notification handler can easily deadlock your application. The solution is to use the standard `invokeLater` method in the `java.awt.EventQueue` and `javax.swing.SwingUtilities` classes (`SwingUtilities` is just a wrapper class for `EventQueue`). Again we reference [Sample Code Project 'JSheets'](https://developer.apple.com/samplecode/JSheets/):

__Listing 14__  Reporting NSSavePanel results to Java

```objc
- (void)savePanelDidEnd:(NSSavePanel *)sheet returnCode:(int)returnCode contextInfo:(void *)contextInfo {
    JNIEnv *env;
    bool shouldDetach = false;

    if (GetJNIEnv(&env, &shouldDetach) != JNI_OK) {
        NSLog(@"savePanelDidEnd: could not attach to JVM");
        return;
    }

    // Call back to Java if the user clicked Save
    if (returnCode == NSOKButton) {
        if (saveFinish_mID != NULL) {
            jsize buflength = [[sheet filename] length];
            jchar buffer[buflength];
            [[sheet filename] getCharacters:(unichar *)buffer];
            jstring str = (*env)->NewString(env, buffer, buflength);

            (*env)->CallStaticVoidMethod(env, jDelegateClass, saveFinish_mID, sheetListener, str);
            (*env)->DeleteLocalRef(env, str);
        } else NSLog(@"savePanelDidEnd: null Java methodID");
    } else if (cancel_mID != NULL) {
        (*env)->CallStaticVoidMethod(env, jDelegateClass, cancel_mID, sheetListener);
    }

    (*env)->DeleteGlobalRef(env, sheetListener);

    if (shouldDetach) {
        (*jvm)->DetachCurrentThread(jvm);
    }
    [self autorelease];
}
```

__Listing 15__  Using `invokeLater` for AWT operations

```
private static void fireSaveSheetFinished(final SaveSheetListener ssl, final String filename) {
    EventQueue.invokeLater(new Runnable() {
        public void run() {
            ssl.saveSheetFinished(new SheetEvent(filename));
        }
    });
}
```

__Note:__ The `saveFinish_mID` and `cancel_mID` variables in Listing 14 are references to Java methods (of type `jmethodID`) defined and cached elsewhere in the source file. See the full JSheets project for more.

### Calling AppKit or AWT From Non-Event Threads

The guidelines listed above change very little when dealing with peripheral "worker" threads: AppKit must still be messaged using one of the `performSelectorOnMainThread:` variants, and AWT must still be called using the appropriate `EventQueue` or `SwingUtilities` methods. SwingWorker threads, for example, must still observe Cocoa threading rules when making AppKit calls. One difference is that it may be possible to make these calls in a blocking fashion (using `waitUntilDone:YES` in Cocoa or `invokeAndWait` in Java). However, it is still possible to create a scenario that blocks AWT and AppKit against each other, even if you are working from a non-event thread. As with any multithreaded design, be mindful of these decisions.

For more on thread safety in both Java and Cocoa, see [Multithreaded Programming Topics: Cocoa Thread Safety](https://developer.apple.com/documentation/Cocoa/Conceptual/Multithreading/articles/CocoaSafety.html#//apple_ref/doc/uid/20000736-123351-BBCFIIEB) and [Threads and Swing](http://java.sun.com/products/jfc/tsc/articles/threads/threads1.html).

[Back to Top](#)

## Invoking the Java Virtual Machine From Native Code

The VM Invocation Interface is described in detail in [Chapter 7 of The Java Native Interface: Programmer's Guide and Specification](http://java.sun.com/docs/books/jni/html/invoke.html). Embedding a JVM into a native Mac OS X application has one major difference from other platforms: __If using AWT, the JVM must not be started on the application's main thread__. Many tutorials and documents start the JVM on the main thread, so it is important to recognize this unique requirement of Mac OS X.

The following sections explain how to correctly create a JVM from both Core Foundation and Cocoa environments, as well as how to request an explicit version of Java.

### Creating a JVM From Core Foundation

Core Foundation developers wishing to create a JVM must create a new thread (using the `pthreads` API) and pass it a function which performs the VM invocation. This ensures that the JVM is created on a thread other than the application's main thread. The below excerpt from [Sample Code Project 'simpleJavaLauncher'](https://developer.apple.com/samplecode/simpleJavaLauncher/) demonstrates this process.

__Listing 16__  Creating a new pthread to invoke a JVM

```swift
/* Start the thread that runs the VM. */
pthread_t vmthread;

/* create a new pthread copying the stack size of the primordial pthread */
struct rlimit limit;
size_t stack_size = 0;
int rc = getrlimit(RLIMIT_STACK, &limit);
if (rc == 0) {
    if (limit.rlim_cur != 0LL) {
        stack_size = (size_t)limit.rlim_cur;
    }
}

pthread_attr_t thread_attr;
pthread_attr_init(&thread_attr);
pthread_attr_setscope(&thread_attr, PTHREAD_SCOPE_SYSTEM);
pthread_attr_setdetachstate(&thread_attr, PTHREAD_CREATE_DETACHED);
if (stack_size > 0) {
    pthread_attr_setstacksize(&thread_attr, stack_size);
}

/* Start the thread that we will start the JVM on. */
/* startupJava is a separate function that creates the JVM */
pthread_create(&vmthread, &thread_attr, startupJava, launchOptions);
pthread_attr_destroy(&thread_attr);
```

### Creating a JVM From Cocoa

The principles behind invoking a JVM from Cocoa are the same as from Core Foundation. Cocoa developers can use the `NSThread` APIs to move JVM invocation off the application's main thread. Listing 16 demonstrates a very simple example of such an approach.

__Listing 17__  Detaching a new `NSThread` to invoke a JVM

```objc
- (IBAction)applicationWillFinishLaunching:(id)sender {
    // Detach a new thread, and in that thread invoke the VM.
    [NSThread detachNewThreadSelector:@selector(startupJava:) toTarget:self withObject:nil];
}

- (void)startupJava:(id)userData {
    // All new native threads (Cocoa and Java) need an autorelease pool.
    NSAutoreleasePool *pool = [[NSAutoreleasePool allocWithZone:NULL] init];

    // Startup the JVM (startupJava is a C function defined elsewhere)
    startupJava();

    [pool release];

    // Once the JVM has exited we will want to exit this application.
    [[NSApplication sharedApplication] terminate:self];
}
```

### Staying off the Main Thread

It is important to understand that the JVM cannot be started from the native application's main thread if your Java code uses an AWT/Swing-based GUI; in such applications the main thread must be kept free for use by Cocoa's event loop. Both of the above examples abide by this rule: Listing 16 starts a `CFRunLoop` in `main`, which is used by the `NSApplication` instance that the AWT creates. Listing 17 responds to `NSApplication`'s `applicationWillFinishLaunching:` delegate method, indicating that an `NSApplication` is already in place on the main thread. Starting an AWT application from the native launcher's main thread significantly affects performance and may produce unrecoverable errors. Listing 18 shows a paraphrased example of the most common error thrown.

__Listing 18__  Error initializing AWT after starting Java on the main thread

```
Exception in thread "main" java.lang.InternalError: Can't start the AWT [...]
        at java.lang.ClassLoader$NativeLibrary.load(Native Method)
        at java.lang.ClassLoader.loadLibrary0(ClassLoader.java:1751)
        at java.lang.ClassLoader.loadLibrary(ClassLoader.java:1668)
        at java.lang.Runtime.loadLibrary0(Runtime.java:822)
        at java.lang.System.loadLibrary(System.java:992)
        at sun.security.action.LoadLibraryAction.run(LoadLibraryAction.java:50)
        at java.security.AccessController.doPrivileged(Native Method)
        at sun.awt.NativeLibLoader.loadLibraries(NativeLibLoader.java:38)
        at sun.awt.DebugHelper.<clinit>(DebugHelper.java:29)
        at java.awt.Component.<clinit>(Component.java:545)
```

Native launchers running "headless" Java code — code that does not use AWT — do not have this requirement and can safely start the JVM on the main thread. However, if there is __any__ chance that your invoked Java code will use the AWT event queue, keep the main thread free. Regardless of your situation, it is highly recommended to minimize risk by starting the JVM from a non-main thread.

### Requesting a Specific J2SE Version

The presence of multiple Java versions on Mac OS X presents a dilemma for native launchers: selecting the Java version you actually want. This problem is solved by defining a `JAVA_JVM_VERSION` environment variable prior to calling `JNI_CreateJavaVM`, typically using the `setenv` function. Set the `version` member of your `JavaVMInitArgs` struct to `JNI_VERSION_1_4`.

A few things to remember when using the invocation API on Mac OS X:

- Before setting `JAVA_JVM_VERSION`, check for the existence of the desired Java version by inspecting the JavaVM framework. The behavior of `JNI_CreateJavaVM` when `JAVA_JVM_VERSION` is set to an unsupported or non-existent version is undefined.
- If you require a specific major version (1.4, 1.5, etc.) of Java, be sure to request it even if the version you want appears to launch without guidance. Never assume that a specific version of Java is the "default" on a given system.
- Invocation of a 1.3 JVM is not supported. Note that passing `JNI_VERSION_1_2` explicitly requests Java 1.3; use `JNI_VERSION_1_4`.

[Sample Code Project 'simpleJavaLauncher'](https://developer.apple.com/samplecode/simpleJavaLauncher/) declares a `startupJava` function that could be used by the two previous examples, including logic to detect and explicitly request J2SE 5.0.

__Listing 19__  Detecting and requesting J2SE 5.0 from Core Foundation

```swift
CFStringRef targetJVM = CFSTR("1.5");
CFBundleRef JavaVMBundle;
CFURLRef    JavaVMBundleURL;
CFURLRef    JavaVMBundlerVersionsDirURL;
CFURLRef    TargetJavaVM;
UInt8 pathToTargetJVM [PATH_MAX] = "\0";
struct stat sbuf;

// Look for the JavaVM bundle using its identifier
JavaVMBundle = CFBundleGetBundleWithIdentifier(CFSTR("com.apple.JavaVM") );

if(JavaVMBundle != NULL) {
    // Get a path for the JavaVM bundle
    JavaVMBundleURL = CFBundleCopyBundleURL(JavaVMBundle);
    CFRelease(JavaVMBundle);

    if(JavaVMBundleURL != NULL) {
        // Append to the path the Versions component
        JavaVMBundlerVersionsDirURL = CFURLCreateCopyAppendingPathComponent
            (kCFAllocatorDefault,JavaVMBundleURL,CFSTR("Versions"),true);
        CFRelease(JavaVMBundleURL);

        if(JavaVMBundlerVersionsDirURL != NULL) {
            // Append to the path the target JVM's version
            TargetJavaVM = CFURLCreateCopyAppendingPathComponent
                (kCFAllocatorDefault,JavaVMBundlerVersionsDirURL,targetJVM,true);
            CFRelease(JavaVMBundlerVersionsDirURL);

            // Verify the desired major version exists in the framework
            if(TargetJavaVM != NULL) {
                if(CFURLGetFileSystemRepresentation
                  (TargetJavaVM,true,pathToTargetJVM,PATH_MAX )) {
                    if(stat((char*)pathToTargetJVM,&sbuf) == 0) {
                        if(CFStringGetCString(targetJVM, (char*)pathToTargetJVM,
                          PATH_MAX, kCFStringEncodingUTF8)) {
                            setenv("JAVA_JVM_VERSION", (char*)pathToTargetJVM,1);
                        }
                    }
                    CFRelease(TargetJavaVM);
                }
            }
        }
    }
}
```

[Back to Top](#)

## Debugging JNI Applications on Mac OS X

As stated earlier, using Xcode for JNI development is covered in [Building a JNI Universal Project With Xcode](https://developer.apple.com/java/jniuniversal.html). Xcode provides the ability to build C/C++/Objective-C and Java-based sources in a single project, making it a great tool for JNI development. Step-based debugging, sadly, is slightly more complicated, as Xcode only allows you to use a single debugging environment at once (Java Debugger or gcc).

We can work around this problem by using one environment outside of Xcode. can be worked around with a the knowledge that the Xcode debugger for C-based applications is simply a front-end around gcc, which can be easily used from the command line. The Java Debugger in Xcode, however, is not accessible from the command line.

### Decoding UnsatisfiedLinkError

The `UnsatisfiedLinkError` is the earliest and most common exception thrown when working with JNI libraries. This error is thrown when the VM failed to interface with native code on the system. There are two basic scenarios where this can happen: loading a library that could not be found; and calling a native method that could not be found. Both are discussed below along with common troubleshooting steps.

__Note:__ It is possible for pure Java applications to throw `UnsatisfiedLinkError`. Such cases usually involve problems with the Java implementation or the client system itself. Please log a bug at [http://bugreport.apple.com](http://bugreport.apple.com) whenever you are unsure of a problem's origin.

#### Failure to Load a Library

Listing 20 shows one variation of `UnsatisfiedLinkError` thrown when a JNI library failed to load, taken from a modified version of [Sample Code Project 'MyFirstJNIProject'](https://developer.apple.com/samplecode/MyFirstJNIProject/).

__Listing 20__  `UnsatisfiedLinkError` loading a JNI library

```
Exception in thread "main" java.lang.UnsatisfiedLinkError: no MyFirstJNILib in java.library.path
    at java.lang.ClassLoader.loadLibrary(ClassLoader.java:1682)
    at java.lang.Runtime.loadLibrary0(Runtime.java:822)
    at java.lang.System.loadLibrary(System.java:992)
    at MyFirstJNIProject.<clinit>(MyFirstJNIProject.java:219)
    at java.lang.Class.forName0(Native Method)
    at java.lang.Class.forName(Class.java:242)
    at apple.launcher.LaunchRunner.loadMainMethod(LaunchRunner.java:55)
    at apple.launcher.LaunchRunner.run(LaunchRunner.java:84)
    at apple.launcher.LaunchRunner.callMain(LaunchRunner.java:50)
    at apple.launcher.JavaApplicationLauncher.launch(JavaApplicationLauncher.java:52)
```

There are two telling things in this stack trace: the "no MyFirstJNILib" message and the call to `System.loadLibrary` in the stack. Both of these things tell us the failure occurred when the JVM attempted to load the JNI library. There are a number of reasons this can happen. If you see this error in your own project, make sure your library conforms to all of the guidelines listed in [Building and Deploying JNI Libraries on Mac OS X](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgobsg4wugsbrfvbfkskmireu4ry). Any of those details can prevent your library from loading if missed.

#### Failure to Call a Native Method

Another common case where `UnsatisfiedLinkError` can be thrown is when Java code calls a method with the `native` keyword, but the native implementation could not be found. Listing 21 shows a typical stack trace seen when this occurs.

__Listing 21__  `UnsatisfiedLinkError` calling a native method.

```
Exception in thread "AWT-EventQueue-0" java.lang.UnsatisfiedLinkError: getMyFullNameBorken
    at MyFirstJNIProject.getMyFullNameBorken(Native Method)
    at MyFirstJNIProject.paint(MyFirstJNIProject.java:213)
    at sun.awt.RepaintArea.paintComponent(RepaintArea.java:276)
    at sun.awt.RepaintArea.paint(RepaintArea.java:241)
    at apple.awt.ComponentModel.handleEvent(ComponentModel.java:251)
    at apple.awt.CWindow.handleEvent(CWindow.java:159)
    at java.awt.Component.dispatchEventImpl(Component.java:4097)
    at java.awt.Container.dispatchEventImpl(Container.java:2068)
    at java.awt.Window.dispatchEventImpl(Window.java:1774)
    at java.awt.Component.dispatchEvent(Component.java:3869)
    at java.awt.EventQueue.dispatchEvent(EventQueue.java:463)
    at java.awt.EventDispatchThread.pumpOneEventForHierarchy(EventDispatchThread.java:269)
    at java.awt.EventDispatchThread.pumpEventsForHierarchy(EventDispatchThread.java:190)
    at java.awt.EventDispatchThread.pumpEvents(EventDispatchThread.java:184)
    at java.awt.EventDispatchThread.pumpEvents(EventDispatchThread.java:176)
    at java.awt.EventDispatchThread.run(EventDispatchThread.java:110)
```

Note that in this case, the exception message is the name of the Java method that was called, rather than the name of a JNI library. As in the previous case, there are a few ways this can happen:

- The JNI library containing the implementation is not loaded. Always load your JNI libraries in a static initializer to ensure they are loaded before other code tries to use them, and make sure any calls to `System.loadLibrary` are successful.
- The Java method signature does not match the native signature. This typically happens when you change the Java method's signature but forget to change the underlying C code to match it. The `javah` tool will regenerate a new signature for you, which you can cut and paste into your native source. See [Chapter 2 of The Java Native Interface: Programmer's Guide and Specification](http://java.sun.com/docs/books/jni/html/start.html#769) for a basic example of writing a native method.
[Back to Top](#)

## Further Reading

- [The Java Native Interface: Programmer's Guide and Specification](http://java.sun.com/docs/books/jni/)
- [JNI Documentation](http://java.sun.com/j2se/1.4.2/docs/guide/jni/index.html)
- [The AWT Native Interface](http://java.sun.com/j2se/1.5.0/docs/guide/awt/1.3/AWT_Native_Interface.html)
- [Threads and Swing (Sun Developer Network)](http://java.sun.com/products/jfc/tsc/articles/threads/threads1.html)
- [Multithreaded Programming Topics: Cocoa Thread Safety](https://developer.apple.com/documentation/Cocoa/Conceptual/Multithreading/articles/CocoaSafety.html#//apple_ref/doc/uid/20000736-123351-BBCFIIEB)
- [Getting Started With Cocoa](https://developer.apple.com/referencelibrary/GettingStarted/GS_Cocoa/index.html)
- [Quartz 2D Programming Guide](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/index.html)
- [Dynamic Library Programming Topics](https://developer.apple.com/documentation/DeveloperTools/Conceptual/DynamicLibraries/)
- [Technical Q&A QA1170, 'Important Java Directories on Mac OS X'](https://developer.apple.com/qa/qa2001/qa1170.html)
- [Technical Q&A QA1295, 'Java on Intel-based Macs'](https://developer.apple.com/qa/qa2005/qa1295.html)
- [Building a JNI Universal Project With Xcode](https://developer.apple.com/java/jniuniversal.html)
- [Java Native Interface Code Samples (Sun Developer Network)](http://java.sun.com/developer/codesamples/jni.html)
- [Sample Code Project 'MyFirstJNIProject'](https://developer.apple.com/samplecode/MyFirstJNIProject/)
- [Sample Code Project 'HelpHook'](https://developer.apple.com/samplecode/HelpHook/)
- [Sample Code Project 'QCCocoaComponent'](https://developer.apple.com/samplecode/QCCocoaComponent/)
- [Sample Code Project 'CWCocoaComponent'](https://developer.apple.com/samplecode/CWCocoaComponent/)
- [Sample Code Project 'JAWTExample'](https://developer.apple.com/samplecode/JAWTExample/)
- [Sample Code Project 'JSheets'](https://developer.apple.com/samplecode/JSheets/)
- [Sample Code Project 'simpleJavaLauncher'](https://developer.apple.com/samplecode/simpleJavaLauncher/)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-07-14 | Added Building, Debugging, CocoaComponent Compatibility sections. |
| 2006-04-17 | New document that discusses use of native APIs and UI elements from Java applications |

