---
title: Xcode Debugging Guide
apple_id: TP40007057
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeDebugging/230-Modifying_Running_Code/modifying_running_code.html
archived_at: '2026-07-15T07:28:00.969619Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Debugging Guide](Introduction.md)


[Next](Debugging%20Programs%20Remotely.md)[Previous](Viewing%20Variables%20and%20Memory.md)

# Modifying Running Code

A very powerful feature of Xcode is the ability to modify your executable while it is running and see the results of your modification. This feature, which is implemented through the Fix command, is useful when it takes a significant amount of time to reach the place in your application’s execution cycle that you want to debug. You can use the feature to learn more about potential bug fixes or to see the immediate results of code changes.

You use the Fix command in Xcode to modify an application at debug time and see the results of your modification without restarting your debugging session. This feature can be particularly useful if it takes a lot of time to reach your application’s current state of execution in the debugger. Rather than recompile your project and restart your debugging session, you can make minor changes to your code, patch your executable, and see the immediate results of your changes.

The Fix command is not intended as a replacement for building your product regularly. Instead, it is a convenience feature for viewing the effect of small changes without restarting your debugging session.

Although there are many restrictions to what you can fix, there are also some features that are explicitly supported by the Fix command, including the following:

- Storing pointers to a patched function. GDB inserts code to jump from the old function to the newly patched function. Thus, despite your code having a pointer to the original function, using that pointer executes the patched version.
- You can add local static variables to a file, but remember that GDB does not execute any initialization code associated with them. Thus, if you declare a new class instance as a global static, GDB does not execute any constructors or static initializers for the instance. there are also limitations on how those variables behave after multiple patches.
- You can add new C++ classes as part of a patch.

To learn about restrictions on the Fix command, see [Fix Command Restrictions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqmjqfvjvomzq).

The process of fixing source files while debugging is tricky. GDB must manipulate your executable while it is running, and insert new code without disturbing the state of your program execution. The actual process involves compiling your code with special flags and rewriting portions of your binary to call the new code when appropriate. At all times, the Fix command modifies the in-memory image of your executable. It does not permanently modify the files of your original application binary.

When it receives a patched binary, GDB compares that binary against the code in the application’s original binary. GDB checks for several modifications that cannot be patched into a running application. If it detects any of these modifications, it reports back to Xcode that it could not incorporate the patch. If this occurs, you can stop debugging and rebuild your application, or continue debugging without the patch.

If GDB does not report any problems with your patch, it integrates the patched code into your application’s memory image. It does this by making the following modifications:

- Modifies functions in your original binary to jump to any patched versions
- Modifies any static or global variables in the patched file to point back to the versions in the original binary

After patching your application, you should be able to continue debugging your code as before. The next time you encounter a patched function, you should see the changes you made appear in the debugger. However, there are some caveats to be aware of when working with patched code.

If you patch a function that is on the stack, you may not see the results of that patch immediately. GDB is capable of patching the function that is currently at the top of the stack. However, if you patch a function that is further down the calling chain, the patch does not take effect until the next time you call it. Thus, the function must return and be called again before it receives the patch. Until that time, the function on the stack continues to execute the original code.

While your program is paused in the debugger, you can move the program counter around and resume execution from any point in the current function. This feature lets you rerun a patched function from the beginning, or from any point, to account for the changes you made.

If you quit your debugging session for any reason, you must rebuild your program to acquire any changes made by patching. The effects of the Fix command are only applicable to your executable while it is active in the debugger. The reason is that the command does not modify your program’s compiled object files. Instead, it creates temporary object files and loads them into the memory space of your process dynamically. When you quit the debugger, GDB discards the temporary object files containing the patches. Recompiling your project recreates your application’s original object files from the patched code.

If you are running your executable in the debugger and you make changes to your source code, you can patch your executable by choosing Run > Fix.

If you change more than one source file, you must fix each file separately. Xcode compiles the changes, patches the executable to use the new code, and resumes execution from the location at which the program was paused. If the changes to your code appear before the line at which execution is set to resume, you will not see the effect of your change until that code is called again. To see the effect of your change, you can manually alter the location at which execution resumes: When your program is paused, drag the PC indicator—the red arrow pointing to the line of code where execution is paused—to the location at which you want to resume execution.

Xcode automatically locates the correct target to use when creating the fix bundle. For example, if you are debugging an application suite that relies on a framework you created, you can make a change in the framework code. When you execute the Fix command, Xcode automatically uses the correct framework target instead of the target associated with the running executable, to create the fix. Xcode also follows references to targets in other projects.

This is the typical fix-and-continue workflow:

1. Start a debugging session for your program.
2. Use your program until it reaches a state at which you want to modify its code without restarting the debugging session.

   You can use breakpoints with ignore-counts to facilitate this task. See [Viewing Breakpoints](Managing%20Program%20Execution.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanjxfvbuqobnknltcnq) for details.
3. In Xcode, modify the implementation file containing the code you want to modify, and save your changes.
4. Choose Run > Fix to modify the program.
5. Switch to your program and continue the debugging session.

The Fix command in Xcode is a powerful way to make small changes to a source file without restarting your debugging session. Although powerful, there are some things you need to do before you can take advantage of the Fix command. The command itself is enabled only when you are debugging an executable. In addition, you must make sure you build your program as follows:

- Compile your code with GCC version 3.3 or later
- Build your code without optimizations
- Build your code with debugging symbols

In general, if you build using the Debug build configurations provided by Xcode, the correct settings are used. However, if you try to patch your executable and get a file-not-found error, check the build settings of your target and make sure that debugging symbols are turned on, as described in [Building for Debugging](../Xcode%20Project%20Management%20Guide/Building%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojtfvbecqsjindemry). You can also check the build log to make sure that the patch bundle was created.

The Fix command works on only one file at a time. If you make changes to multiple source files, you must patch each file separately before continuing with your debugging session.

There are many types of code changes that cannot be patched. The GDB debugger reports an error if it cannot integrate any of your changes because of a known restriction. If GDB reports one of these errors, you must rebuild your program and restart your debugging session, or continue debugging the program without the changes.

GDB recognizes the following changes to your code and reports an error if you try to include them as part of a fix:

- Changes to the number or type of arguments in a function or method that is currently on the stack
- Changes to the return type or name of a function or method that is currently on the stack
- Changes to the number or type of local variables in a function or method that is currently on the stack
- Changes to the type of global or local static variables
- Symbol type redefinitions, that is, changing a function to a variable or a variable to a function

In addition to the restrictions reported by GDB, there are some restrictions that GDB currently does not check. If you attempt to include any of these changes in a patch, your application may crash or exhibit other undefined behavior when it encounters the code. The solution is to avoid using the Fix command for the change. Instead, rebuild your program and restart your debugging session.

The following changes cannot be included as part of a fix:

- Changes to a nib file.
- Changes to the definition of a structure or union.
- The addition of an Objective-C class.
- The addition or removal of class instance variables.
- The addition or removal of class methods.
- The addition or removal of methods to an Objective-C category. These methods are not registered with the Objective-C runtime and thus cannot be called. (You can fix existing methods in a category.)
- Any reference to an unresolved external variable or function. Link errors of this nature cannot be resolved by the dynamic linker.
- The addition of a static variable across multiple patches in one session. GDB maintains a copy of the static in each patch; however, because there is no original variable to refer to, each variable remains separate from the others, which can lead to unpredictable results.
- The addition of a function to one file when it is called from a different patched file. New functions are private to the patch file in which they appear.
- The addition of a `try` block or the addition of a `catch` handler to an existing `try` block.
- The addition of a C++ template class specialization.
- Changes to functions that require two-level namespaces during linking to prevent known symbol conflicts across different libraries. GDB supports patching two-level namespace binaries but currently does so using flat namespace conventions.

[Next](Debugging%20Programs%20Remotely.md)[Previous](Viewing%20Variables%20and%20Memory.md)

