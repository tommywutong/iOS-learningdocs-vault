---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/VisitorExample.html
archived_at: '2026-07-15T07:48:07.424285Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](RoleOfScripts.md)

# Visitors Example

To explain how a WebScript operates within the larger context of a WebObjects application, this section uses the Visitors application as an example. The Visitors application takes the name of the current visitor, and displays the most recent visitor, the total number of visitors to the page, and the time remaining in the session:

!

 ____Figure 1.__  The Visitors Example__

The Visitors application includes the following directories and files:

```
/Visitors.woa
  Application.wos
  Session.wos
  /Main.wo
    Main.html
    Main.wod
      Main.wos
```

To view the contents of __Main.wod__ and __Main.html__, see the on-line Visitors example. The contents of __Application.wos__, __Session.wos__, and __Main.wos__ are listed in the following sections.

## Application.wos

__Application.wos__ is the application script for the Visitors application. It declares two application variables: __visitorNum__ and __lastVisitor__. Application variables can be accessed throughout the application, and they live for the duration of the application. For more information on application variables, see the section "[Variables and Scope](VariablesAndScope.md#apple-kjcumojwgazdo)".

```
id lastVisitor;
  // the most recent visitor
id visitorNum;
  // the total number of visitors the page

- init
{
    [super init];
    lastVisitor = @"";
    [self setTimeOut:7200];
    return self;
}
```

### Implementing the init Method

The __Application.wos__ script includes a method called __init__. The __init__ method is where you can initialize the variables associated with the object. Thus, in an application script, it's common to implement an __init__ method to initialize application variables. In a component script, on the other hand, you use __init__ to prepare the associated page and its variables for use during the processing of the page.

As illustrated in the above example, an implementation of __init__ should always begin by invoking the __init__ method of __super__ (the superclass object). It should always end by returning __self__.

## Session.wos

In __Session.wos__ of the Visitors application, an __init__ method also initializes declared variables. These variables have session-wide visibility and persistence. But this __init__ does much more than initialze variables.

- It sets a time-out period for the session.
- It creates a timer scheduled to fire every second.
- It implements a method that is invoked when the timer is fired. This method increments a "seconds-counter" variable, which is bound to a WOString on the page.

```
    id timeSinceSessionBegan;
    id timer;
    - init
    {
        [super init];

           timeSinceSessionBegan = 0;
             timer = [NSTimer scheduledTimerWithTimeInterval:1.0 target:self
                selector:"timeOfSession" userInfo:nil repeats:YES];
          [self setTimeOut:120];
            return self;
    }

    - timeOfSession
    {
        timeSinceSessionBegan++;
    }
```

As this example shows, you can do many things in the __init__ method to set up the associated object besides initializing variables. This code example also illustrates a couple specific aspects of WebScript. The "hidden" variable __self__ in this script refers to a WOSession object, and so the method invoked (__setTimeOut:__) must be declared by the WOSession class. Second, you can invoke any method of the Foundation framework, such as NSTimer's __scheduledTimerWithTimeInterval:target:selector:userInfo:repeats:__.

__Note:__  The example above illustrates a syntax difference between WebScript and Objective-C: the way you refer to selectors and similar entities. In Objective, you use the __@selector()__ directive; in WebScript, because "@" has special significance, you simply quote the selector.

## Main.wos

The script associated with the first (and in this example, only) page of the Visitors application is __Main.wos__. This script increments the number of visitors to the page (__visitorNum__), and assigns the name (__aName__) entered in the application's text field to the last visitor (__lastVisitor__). It then clears the text field by assigning an empty string to __aName__.

```
id number, aName;
- awake {
   if (!number) {
    number = [[self application] visitorNum];
    number++;
    [[self application] setVisitorNum:number];
  }
}

- recordMe
{
  if ([aName length]) {
    [[self application] setLastVisitor:aName];

    [self setAName:@""]; // clear the text field
  }
  return self; // use request page as response page
}
```

### Implementing the awake Method

For a given page, the __awake__ method is invoked exactly once per transaction, at the beginning of that transaction. The __init__ method is invoked only once, at the start of an object's lifetime (see "[The Duration of a Component](DurationOfComponent.md#apple-kjcummzzgy3ds) " for the reasons why). Because of this, it is more appropriate in the Visitor application to implement __awake__ rather than __init__. We want to track each "visit" to this page. Because __awake__ is invoked once per transaction, if the same page handles the request as well as generates the response (for example, the first page of an application), the __awake__ method is only invoked during the request phase.

The __awake__ method is the best place to initialize variables whose values are known or can be resolved at the start of the request-response cycle, such as a list of hyperlinks. The advantage of using __awake__ to perform this type of initialization is that the variables are guaranteed to be initialized every time the page is displayed.

The __awake__ method has a complementary method, __sleep__, in which you can explictly deallocate objects assigned to variables by assigning __nil__ to the variables. As a technique for improving application scalability, you can turn off page caching, initialize variables in __awake__ (rather than in __init__), and deallocate them in __sleep__.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](DurationOfComponent.md)
