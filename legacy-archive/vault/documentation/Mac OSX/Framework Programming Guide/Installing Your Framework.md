---
title: Framework Programming Guide
apple_id: 10000183i
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2013-09-17'
source_url: https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPFrameworks/Tasks/InstallingFrameworks.html
archived_at: '2026-07-15T08:15:45.437610Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Framework Programming Guide](Introduction%20to%20Framework%20Programming%20Guide.md)


[Next](Including%20Frameworks.md)[Previous](Exporting%20Your%20Framework%20Interface.md)

# Installing Your Framework

Once your framework is ready to go, you need to decide where to install it. Where you install a framework also helps determine how to install the framework.

Third-party frameworks can go in a number of different file-system locations, depending on certain factors.

- Most public frameworks should be installed at the local level in `/Library/Frameworks`.
- If your framework should only be used by a single user, you can install it in the `~/Library/Frameworks` subdirectory of the current user; however, this option should be avoided if possible.
- If they are to be used across a local area network, they can be installed in `/Network/Library/Frameworks`; however, this option should be avoided if possible.

For nearly all cases, installing your frameworks in `/Library/Frameworks` is the best choice. Frameworks in this location are discovered automatically by the compiler at compile time and the dynamic linker at runtime. Applications that link to frameworks in other directories, such as `~/Library/Frameworks` or `/Network/Library/Frameworks`, must specify the exact path to the framework at build time so that the dynamic linker can find it. If the path changes (as it might for a user home directory), the dynamic linker may be unable to find the framework.

Another reason to avoid installing frameworks in `~/Library/Frameworks` or `/Network/Library/Frameworks` is the potential performance penalties. Frameworks installed in network directories or in network-based user home directories can cause significant delays in compilation times. Loading the framework across the network can also slow down the launch of the target application.

Third-party frameworks should never be installed in the `/System/Library/Frameworks` directory. Access to this directory is restricted and is reserved for Apple-provided frameworks only.

When you build an application or other executable, the compiler looks for frameworks in`/System/Library/Frameworks` as well as any other location specified to the compiler. The compiler writes path information for any required frameworks in the executable file itself, along with version information for each framework. When the application is run, the dynamic link editor tries to find a suitable version of each framework using the paths in the executable file. If it cannot find a suitable framework in the specified location (perhaps because it was moved or deleted), it looks for frameworks in the following locations, in this order:

1. The explicit path to the framework that was specified at link time.
2. The `/Library/Frameworks` directory.
3. The `/System/Library/Frameworks` directory.

If the dynamic link editor cannot locate a required framework, it generates a link edit error, which terminates the application.

Custom frameworks intended for internal use should be installed inside the application that uses them. Frameworks embedded in an application are stored in the `Frameworks` directory of the application bundle. The advantage of embedding frameworks in this manner is that it guarantees the application always has the correct version of the framework to run against. See [Embedding a Private Framework in Your Application Bundle](Creating%20a%20Framework.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2tqljrga3dqobq) for information on how to embed a custom framework in your application.

The limitation of embedding frameworks is that you cannot share the framework among a suite of applications. If your company develops a suite of applications that rely on the same framework, you might want to install one copy of that framework that all of the applications can share. In such a situation, you should install the frameworks in the `/Library/Frameworks` directory and make sure the frameworks bundle does not contain any public header information.

How you install frameworks depends on your framework. If your framework is bundled inside of a particular application, there is nothing special you need to do. The user can drag the application bundle to a local system and use the application without any need for additional installation steps.

If your framework is external to an application, you should use an installation package to make sure it is put in the proper location. You should also use an installation package in situations where an older version of your framework might be in place. In that case, you might want to write some scripts to update an existing framework bundle rather than replace it entirely. For example, you may want to install a new major version of your framework without disturbing any other versions. Similarly, if you have multiple applications that rely on the same framework, your installation package should check for the existence of the framework and install it only as needed.

For more information on creating installation packages, see Distributing Apps Outside the Mac App Store.

[Next](Including%20Frameworks.md)[Previous](Exporting%20Your%20Framework%20Interface.md)

