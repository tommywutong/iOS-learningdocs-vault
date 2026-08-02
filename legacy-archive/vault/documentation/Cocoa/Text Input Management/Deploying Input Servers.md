---
title: Text Input Management
apple_id: 10000065i
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-06-02'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/InputManager/Tasks/InputServerDeployment.html
archived_at: '2026-07-15T07:16:09.035361Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Text Input Management](Introduction%20to%20Text%20Input%20Management.md)


[Next](Creating%20Custom%20Views.md)[Previous](Creating%20Input%20Servers.md)

# Deploying Input Servers

This section explains how to deploy an input server
for use with the Cocoa text input management system.

An input server is implemented as an
NSInputServer object
wrapped in a server application, which communicates via interprocess
communication (IPC) with
the current input manager. The input
server must be initialized with its delegate (if a delegate is used) and
an IPC connection
name at runtime. The IPC connection name must match the one in the
input server’s `Info` file
(see [Installing Input Servers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgaztsljzg42tqmi).

The easiest way to do this is to perform the initialization
in the application’s `main()` function—for
example in the following code:

```
int main(int argc, const char *argv[])
{
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    [[NSInputServer alloc] initWithDelegate:[HexInputServer sharedInstance]
                           name:@"HexInputServer2ConnectionName"];
    [[NSApplication sharedApplication] run];
    [pool release];
    return 0;
}
```

Note that the HexInputServer class uses a `sharedInstance` method
to create a HexInputServer object because only one such object will
ever be created.

An input server is installed as a directory
hierarchy, which must be installed in
`~/Library/InputManagers` or `/Library/InputManagers` to
be useful to users. At the top level of the hierarchy there is a
text file called `Info`,
an application bundle, and optionally a key-bindings dictionary file. The `Info` file
contains a dictionary property list. When an application starts
up, NSInputManager scans
the `InputManagers` directories
for input servers and uses the data from each folder’s `Info` file
to create an input manager for its input server. If there are any
custom input servers installed, an Input submenu appears in the
Edit menu which lets the user switch between the different installed
input servers. When the user chooses an input server, the input
manager launches the input server if it’s not already running
and connects to it via interprocess communication.

The `Info` file tells
NSInputManager how to find the application executable, tells what
the IPC connection name to use is, provides an optional key-bindings
dictionary, and contains localized text strings to represent the
input server in the Edit > Input submenu. The file can be an
XML property list or an old-style
ASCII property list, such as this example:

```
{
    // relative path to the executable to be launched
    ExecutableName = "HexInputServer.app/Contents/MacOS/HexInputServer";

    // The name registered with the IPC mechanism, the same as the one
    // used to initialize the NSInputServer object
    ConnectionName = "HexInputServer2ConnectionName";
    DisplayName = "Hexadecimal Input";
    DefaultKeyBindings = "HexInputServer.dict";

    // The name that will appear in the Edit > Input submenu
    LocalizedNames = { Deutsch = "Hexadezimaler Input"; }

    // Default name used for languages not found in LocalizedNames
    DisplayName = "Hexadecimal Input"

    // Optional. Returned by the current input manager’s language: method.
    LanguageName = "English";

    // Optional file to map keyboard characters to selector names
    DefaultKeyBindings = "HexInputServer.dict"
}
```

The `DefaultKeyBindings` file
overrides the system’s default key-bindings file. (See [About Key Bindings](About%20Key%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dsmbsfvbecssdirdemsi) for more
information.)

If you want to override the key-bindings mechanism entirely,
make your input server’s `wantsToInterpretAllKeystrokes` method
return `YES`.

[Next](Creating%20Custom%20Views.md)[Previous](Creating%20Input%20Servers.md)

