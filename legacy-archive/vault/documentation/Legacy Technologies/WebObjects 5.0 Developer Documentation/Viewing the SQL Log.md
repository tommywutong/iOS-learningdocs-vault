---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Topics/ProgrammingTopics.7.html
archived_at: '2026-07-15T08:14:54.688899Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.6.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.8.md)

#   Viewing the SQL Log

##  Synopsis

Describes how you log the SQL statements that EOF sends to the database.

##  Description

SQL logging is a useful debugging tool that allows you to view the SQL commands EOF sends to the database server. It can be enabled from the command line or turned on and off programmatically. The log is printed to standard error using
NSLog()
(see the
NSLog
function specification in the Foundation Framework Reference).

###  Enabling SQL Logging From the Command Line

To enable SQL logging for an application, set the default
EOAdaptorDebugEnabled
to
YES
. This can be done from a UNIX shell (a Bourne Shell under Windows NT) using the
defaults
command.

```

defaults write
MyApp
 EOAdaptorDebugEnabled YES
```


When you launch your application, the SQL prints to standard error.n the launch window. You can also enable SQL logging for all applications using the
defaults
command.

```

defaults write NSGlobalDomain EOAdaptorDebugEnabled YES
```


For more information abouts the defaults system, see the NSUserDefaults class specification in the Foundation Framework Reference and the
defaults
man page.

###  Enabling SQL Logging From Project Builder

You can also use the launcher to enable SQL logging by clicking the launcher preferences button (looks like a check mark), clicking the Arguments tab and entering

```

-EOAdaptorDebugEnabled YES
```


This sets the
EOAdaptorDebugEnabled
command line argument to
YES
every time Project Builder's launcher starts your application.

Some developers find it convenient to enable SQL logging globally and selectively disable it for individual applications with the launcher (
-EOAdaptorDebugEnabled NO
).

###  Enabling SQL Logging Programmatically

The EOAdaptorContext class actually uses the
EOAdaptorDebugEnabled
flag. In order to turn on SQL logging for all EOAdaptorContexts that get created, you use the EOAdaptorContext static method (class method in Objective-C)
setDebugEnabledDefault
.

```

EOAdaptorContext.setDebugEnabledDefault(true);
```


The best place to put this code is in the application's constructor so that all EOAdaptorContexts that get created will log their SQL. Be sure to import
com.apple.yellow.eoaccess.\*
.

You can also enable debugging for individual adaptor contexts by sending them a
setDebugEnabled
message. This is also useful when you need to turn the logging on and off while the application is running. To find out how to access your application's adaptor contexts, see the programming topic [Accessing Adaptor Sublayer Objects](Accessing%20Adaptor%20Sublayer%20Objects.md#apple-gi3tanbu)
.

##  See Also

- 

  [Accessing Adaptor Sublayer Objects](Accessing%20Adaptor%20Sublayer%20Objects.md#apple-gi3tanbu)
- 

  NSUserDefaults class specification in the _Foundation Framework Reference_
- 

  defaults
  man pages

##  Questions

- 

  How do I view the SQL that EOF sends to the database server?
- 

  How can I enable and disable SQL logging?

##  Keywords

- 

  SQL Logging
- 

  Debugging
- 

  EOAdaptorContext

##  Revision History

10 March 1999. Clif Liu. First Draft.

---

© 1999 Apple Computer, Inc.

[![Up](attachments/Topics/up.gif)](TopicsTOC.md) [![Previous](attachments/Topics/previous.gif)](ProgrammingTopics.6.md) [![Next](attachments/Topics/next.gif)](ProgrammingTopics.8.md)[an error occurred while processing this directive]

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
