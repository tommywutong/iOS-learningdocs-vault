---
title: App Sandbox Design Guide
apple_id: TP40011183
resource_type: Guide
platform: macOS
topic: Security
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AppSandboxImplementationChecklist/AppSandboxImplementationChecklist.html
archived_at: '2026-07-27T06:57:08.406163Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Sandbox Design Guide](About%20App%20Sandbox.md)


[Next](Document%20Revision%20History.md)[Previous](Migrating%20an%20App%20to%20a%20Sandbox.md)

# App Sandbox Checklist

If you have adopted App Sandbox according to the guidelines presented throughout this book, you should be ready to distribute your app either through the Mac App Store or directly to users. But before you do, every time you release a new update of your app, use this checklist to verify that your app is following best practices.

- Make sure that your app makes use of each entitlement in its entitlements file. If your app does not need an entitlement, remove it from the entitlements file.
- Make sure you have enabled sandboxing on all Mach-O executables included in your app's bundle. Every Mach-O executable must have an entitlements file, and request the `com.apple.security.app-sandbox` entitlement. This includes XPC services and custom helper tools that request the `com.apple.security.inherit` entitlement. They must also request the `com.apple.security.app-sandbox` entitlement.

  You can check if a binary is a Mach-O executable using the `file` command. If any slice of the binary identifies itself as `Mach-O executable` or `Mach-O 64-bit executable`, the binary must be sandboxed.

  __Listing 5-1__  Running the `file` command on a Mach-O binary that is executable.

  ```shell
  $ file /Applications/Safari.app/Contents/MacOS/Safari
  /Applications/Safari.app/Contents/MacOS/Safari: Mach-O universal binary with 2 architectures
  /Applications/Safari.app/Contents/MacOS/Safari (for architecture i386): Mach-O executable i386
  /Applications/Safari.app/Contents/MacOS/Safari (for architecture x86_64): Mach-O 64-bit executable x86_64
  ```

  __Listing 5-2__  Running the `file` command on a Mach-O binary that is NOT executable.

  ```shell
  $ file /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
  /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation: Mach-O universal binary with 2 architectures
  /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation (for architecture x86_64): Mach-O 64-bit dynamically linked shared library x86_64
  /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation (for architecture i386): Mach-O dynamically linked shared library i386
  ```

  You can use the following command to find all the Mach-O executables in your compiled app bundle.

  ```
  find -H YourAppBundle -print0 | xargs -0 file | grep "Mach-O .*executable"
  ```
- Make sure that every file system path specified in your entitlements begins with a '/'. This includes both absolute paths and paths relative to the current user's home directory. Additionally, make sure that the '~' character does not appear anywhere in a path that is relative to the user's home directory.
- Make sure your app is not requesting a file access exception for the purpose of allowing it to skip presenting an open or save dialog to read or write files on the user's behalf. For instance, access to the Desktop or Documents folders must always be initiated by the user. Do not request an exception for these locations.
- Make sure your app is not requesting a file access exception for the purpose of granting it access to another app's data or the system's data. Sandboxed apps must not rely on read or write access to files they did not create, or have not been given explicit access to, for their operation.
- Make sure your app is not requesting a file access exception for a location it already has access to. Every sandboxed app is implicitly granted access to various directories on the system outside their own container. These directories contain files common to the operation of all apps, for instance, /bin and /System/Library/Frameworks. Requesting exceptions to these locations is redundant. Before requesting an exception, you should be able to demonstrate a use case that will encounter a sandbox violation if the exception is not present.
- If your app requests the `com.apple.security.temporary-exception.apple-events` or `com.apple.security.temporary-exception.mach-lookup.global-name` entitlements, make sure you have provided an array of strings for the value of the entitlement as detailed in the [Entitlement Key Reference](https://developer.apple.com/library/etc/redirect/DTS/AppSandboxTempExcpEntitlements) for that entitlement. Be specific when specifying values for these entitlements. There is no value that will grant your app access to every app installed on the user's system.
- If you edit the entitlements file by hand as opposed to using the property list editor in Xcode, make sure you have not introduced any syntax errors. The entitlements file must contain a valid property list structure. You can use the `plutil` command to check your entitlements file for syntax errors. A common mistake is entering `YES`/`NO` instead of the syntactically-correct `true`/`false` when specifying the value of a Boolean.

  __Listing 5-3__  Running the `plutil` command on an entitlements file with a syntax error.

  ```shell
  $ plutil Invalid-Entitlements.plist
  Invalid-Entitlements.plist: Encountered unknown tag YES on line 6
  ```

  __Listing 5-4__  Running the `plutil` command on a syntacticly correct entitlements file.

  ```shell
  $ plutil Valid-Entitlements.plist
  Valid-Entitlements.plist: OK
  ```

[Next](Document%20Revision%20History.md)[Previous](Migrating%20an%20App%20to%20a%20Sandbox.md)
