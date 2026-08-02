---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/DetectFreedObj.html
archived_at: '2026-07-15T08:01:06.238394Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Detecting Freed Object Exceptions

##  Synopsis

Describes how to detect a freed object exception.

##  Description

For applications written in Objective C or applications that use the Java-wrapped Application Program Interfaces (APIs), you can use the _NSZombieEnabled_
variable defined in NSDebug.h to detect why an object has been freed.

Note that the API provided in _NSDebug.h_
is for debugging purposes only, and may not be available in future releases.

Setting the _NSZombieEnabled_
variable to _YES_
when running your application from the command line changes the behavior of the memory manager. Objects are not deallocated, but converted to objects in the zombie class. When zombie objects receive a deallocation message, they print a warning that includes the name of the message.

The message name helps differentiate whether it is your code or something deep inside the WebObjects hierarchy that is attempting to deallocate the freed object. Another benefit of enabling zombie objects is that a freed object exception does not crash your application, allowing you to debug the application with all of its state intact.

The following code shows how to use the zombie API. Create a test application using ProjectBuilder, and paste this code in the __main.m_
file. Compile and run it inside Project Builder to see the debug output.

#####  Figure 1. Objective C Code

```
// NSZombieTest.m
```



```
// Demonstrates how object zombies work.
```



```

```



```
#import
```



```
#import
```



```
int main (int argc, const char *argv[])
```



```
{
```



```
       NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
```



```
       id foo = [[NSDate alloc] init]; // some random class
```



```
// Turn on zombie objects, so we can tell what class a freed object was.
```



```
    // Note: NSZombieEnabled is declared in NSDebug.h
```



```
       NSZombieEnabled = YES;
```



```
    // Throw foo into the pool
```



```
       [foo autorelease];
```



```
    // This will free foo
```



```
       [foo release];
```



```
    // This will try to free foo again, raising an exception
```



```
       [pool release];
```



```
       exit(0);       // insure the process exit status is 0
```



```
       return 0;      // ...and make main fit the ANSI spec.
```



```
}
```


This code produces the following sample output:

#####  Figure 2. Sample Output

```
warning: Jul 21 01:38:09 ZombieTest[209] *** *** Selector 'release' sent
to dealloced instance 0xa0edb0 of class NSConcreteDate.
```



```
Break at '-[_NSZombie release]' to debug. Stack=0x32046288 0x32046378 0x3
203fc30 0x32040346 0x40108d 0x401561 0x401227 0x77f1b304
```



```
warning: Jul 21 01:38:10 ZombieTest[209] *** -[NSAutoreleasePool dealloc]
: Exception ignored while releasing an object in an autorelease pool: NSG
enericException *** Selector 'release' sent to dealloced instance 0xa0edb
0 of class NSConcreteDate.
```



```
Break at '-[_NSZombie release]' to debug. Stack=0x32046288 0x32046378 0x3
203fc30 0x32040346 0x40108d 0x401561 0x401227 0x77f1b304
```


Note that the class of the freed object is printed in the debugging output (_NSConcreteDate_
or _NSDate_
). You can set a breakpoint at [__NSZombie release_
] to debug further.

Note that running an application with _NSZombieEnabled_
set to _YES_
degrades performance.

##  See Also

· Detecting Memory Leaks

· NSDebug.h

##  Questions

· How do I detect which object has been freed when encountering the freed object exception?

##  Keywords

· _NSZombieEnabled_

· Freed Object Exception

##  Revision History

20 July, 1998. Mai Nguyen. First Draft.

26 October, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
