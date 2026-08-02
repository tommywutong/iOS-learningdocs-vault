---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.5.html
archived_at: '2026-07-15T08:14:54.618151Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.4.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.6.md)

#   Detecting Freed Object Exceptions

##  Synopsis

Describes how to detect a freed object exception.

##  Description

For applications written in Objective-C or applications that use the Java-wrapped Application Program Interfaces (APIs), you can use the
NSZombieEnabled
variable defined in NSDebug.h to detect why an object has been freed.

Note that the API provided in
NSDebug.h
is for debugging purposes only and may not be available in future releases.

Setting the
NSZombieEnabled
variable to
YES
when running your application from the command line changes the behavior of the memory manager. Objects are not deallocated but are converted to objects in the zombie class. When zombie objects receive a deallocation message, they print a warning that includes the name of the message.

The message name helps differentiate whether it is your code or something deep inside the WebObjects hierarchy that is attempting to deallocate the freed object. Another benefit of enabling zombie objects is that a freed object exception does not crash your application, allowing you to debug the application with all of its state intact.

The following code shows how to use the zombie API. Create a test application using Project Builder, and paste this code in the
_main.m
file. Compile and run it inside Project Builder to see the debug output.

```objc

// NSZombieTest.m
// Demonstrates how object zombies work.

#import <Foundation/Foundation.h>
#import <Foundation/NSDebug.h>
int main (int argc, const char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    id foo = [[NSDate alloc] init]; // some random class
    // Turn on zombie objects, so we can tell
    // what class a freed object was.
    // Note: NSZombieEnabled is declared in NSDebug.h
    NSZombieEnabled = YES;
    // throw foo into the pool
    [foo autorelease];
    // this will free foo
    [foo release];
    // this will try to free foo again, raising an exception
    [pool release];
    exit(0);       // insure the process exit status is 0
    return 0;      // ...and make main fit the ANSI spec.
}
```


This code produces the following sample output:

```

warning: Jul 21 01:38:09 ZombieTest[209] *** *** Selector 'release' sent to dealloced instance 0xa0edb0 of class NSConcreteDate.

Break at '-[_NSZombie release]' to debug. Stack=0x32046288 0x32046378 0x3203fc30 0x32040346 0x40108d 0x401561 0x401227 0x77f1b304

warning: Jul 21 01:38:10 ZombieTest[209] *** -[NSAutoreleasePool dealloc]: Exception ignored while releasing an object in an autorelease pool: NSGenericException *** Selector 'release' sent to dealloced instance 0xa0edb0 of class NSConcreteDate.

Break at '-[_NSZombie release]' to debug. Stack=0x32046288 0x32046378 0x3203fc30 0x32040346 0x40108d 0x401561 0x401227 0x77f1b304
```


Note that the class of the freed object is printed in the debugging output (
NSConcreteDate
or
NSDate
). You can set a breakpoint at [
_NSZombie release
] to debug further.

Note that running an application with
NSZombieEnabled
set to
YES
degrades performance.

##  See Also

- 

  [Detecting Memory Leaks](Detecting%20Memory%20Leaks.md#apple-giytemzt)
- 

  NSDebug.h
  header file in the Foundation Framework

##  Questions

- 

  How do I detect which object has been freed when encountering the freed object exception?

##  Keywords

- 

  Memory
- 

  Free
- 

  Exception

##  Revision History

20 July, 1998. Mai Nguyen. First Draft.

26 October, 1998. Clif Liu. Second Draft.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.4.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.6.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
