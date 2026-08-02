---
title: Runtime Configuration Guidelines
apple_id: 10000170i
resource_type: Guide
platform: iOS|macOS
topic: Data Management
technology: null
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPRuntimeConfig/Articles/EnvironmentVars.html
archived_at: '2026-07-15T08:16:27.226103Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Runtime Configuration Guidelines](Introduction.md)


[Next](Additional%20Configuration%20Tips.md)[Previous](The%20Preferences%20System.md)

# Environment Variables

Environment variables are another way to configure your application dynamically. Many applications and systems use environment variables to store important information, such as the location of executable programs and header files. The variable consists of a key string with the name of the variable and a value string.

To get the value of an environment variable, your application must call the `getenv` function that is part of the standard system library (`stdlib.h`). You pass this function a string containing the name of the variable you want and it returns the value, or NULL if no variable of that name was found. Your application can then use the variable as it sees fit.

Environment variables are scoped to the process that created them and to any children of that process. The Terminal application treats each window as its own separate process for the sake of managing environment variables. Thus, if you create a Terminal window and define some environment variables, any programs you execute from that window inherit those variables. However, you cannot access the variables defined in the first window from a second Terminal window, and vice versa.

Sessions can be inherited. For example, when a user logs in, the system creates a user session and defines a standard set of environment variables. Any processes launched by the user during the session inherit the user environment variables. However, this inheritance is a read-only relationship. Any changes made to the variable by a process remain local to that process and are not inherited by other processes.

There are two ways to make environment variables available to an application. The first is to define the variables in a Terminal session and then launch the application from the same session. When launched from Terminal, the application inherits the session settings, including any environment variables defined there.

The second way to associate environment variables with an application is to include the `LSEnvironment` key in the application’s information property list file. The `LSEnvironment` key lets you specify an arbitrary number of key/value pairs representing environment variables and their values. Because it requires modifying the application’s information property list file, use of this key is best for options that do not change too frequently. For more information on using this key, see _[Information Property List Key Reference](../../General/Information%20Property%20List%20Key%20Reference/About%20Info.plist%20Keys%20and%20Values.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbx)_.

[Next](Additional%20Configuration%20Tips.md)[Previous](The%20Preferences%20System.md)

