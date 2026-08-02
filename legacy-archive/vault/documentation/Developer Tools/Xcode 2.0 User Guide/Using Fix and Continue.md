---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/db_fix_and_continue/db_fix_and_continue.html
archived_at: '2026-07-15T07:29:22.240433Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Remote%20Debugging%20in%20Xcode.md)[Previous](Shared%20Libraries%20Window.md)

# Using Fix and Continue

A very powerful feature of Xcode is the ability
to modify your executable while it is running and see the results
of your modification. This feature is implemented through the Fix
command in the Xcode interface.

The Fix command is not intended as a replacement for building
your project regularly. Instead, it is a convenience feature for
viewing the effect of small changes without restarting your debugging
session. This feature is useful in situations where it takes a significant
amount of time to reach the place in your application’s execution
cycle that you want to debug. You can use the feature to learn more
about potential bug fixes or to see the immediate results of code
changes.

The Fix command in Xcode is a way to modify an application
at debug time and see the results of your modification without restarting
your debugging session. This feature can be particularly useful
if it takes a lot of time to reach your application’s current
state of execution in the debugger. Rather than recompile your project
and restart your debugging session, you can make minor changes to
your code, patch your executable, and see the immediate results
of your changes.

The process of fixing source files while debugging is tricky.
GDB must manipulate your executable while it is running, inserting
new code while not disturbing the state of your program execution.
The actual process involves compiling your code with special flags and
rewriting portions of your binary to call the new code when appropriate.
At all times, the Fix command modifies the in-memory image of your
executable. It does not permanently modify the files of your original
application binary.

When it receives a patched binary, GDB compares that binary
against the code in the application’s original binary. GDB checks
for several modifications that cannot be patched into a running
application. If it detects any of these modifications, it reports
back to Xcode that it could not incorporate the patch. If this occurs,
you can stop debugging and rebuild your application or continue
debugging without the patch.

If GDB does not report any problems with your patch, it integrates
the patched code into your application’s memory image. It does
this by making the following modifications:

- GDB modifies
  functions in your original binary to jump to any patched versions.
- GDB modifies any static or global variables in the patched
  file to point back to the versions in the original binary.

After patching your application, you should be able to continue
debugging your code as before. The next time you encounter a patched
function, you should see the changes you made appear in the debugger
window. However, there are some caveats to be aware of when working
with patched code.

If you patch a function that is on the stack, you may not
see the results of that patch immediately. GDB is capable of patching
the function that is currently at the top of the stack. However,
if you patch a function that is further down the calling chain,
the patch does not take effect until the next time you call it.
Thus, the function must return and be called again before it receives
the patch. Until that time, the function on the stack continues to
execute the original code.

While your program is paused in the debugger, you can move
the program counter around and resume execution from any point in
the current function. This feature lets you rerun a patched function
from the beginning, or from any point, to account for the changes
you made.

If you quit your debugging session for any reason, you must
rebuild your program to acquire any changes made by patching. The
effects of the Fix command are only applicable to your executable
while it is active in the debugger. The reason is that the command
does not modify your program’s compiled object files. Instead,
it creates temporary object files and loads them into the memory
space of your process dynamically. When you quit the debugger, GDB
discards the temporary object files containing the patches. Recompiling your
project recreates your application’s original object files from
the patched code.

If you are running your executable in the debugger and you
make changes to your source code, you can patch your executable
by doing either of the following:

- Click the
  Fix button.
- Choose Debug > Fix.

If you change more than one source file, you must fix each
file separately. Xcode compiles the changes, patches the executable
to use the new code, and resumes execution from the location at
which the program was halted. If the changes to your code appear
before the line at which execution is set to resume, you will not
see the effect of your change until that code is called again. However,
you can get around this by manually altering the location at which
execution resumes. When your program is paused, you can drag the
PC indicator—the red arrow pointing to the line of code where
execution is paused—to the location at which you want to resume
execution, as shown here.

__Figure 36-1__  Changing
the position of the program counter

!

Xcode automatically locates the correct target to use when
creating the fix bundle. For example, if you are debugging an application
suite that relies on a framework you created, you can make a change
in the framework code. When you click the Fix button, Xcode automatically
uses the correct framework target, instead of the target associated
with the running executable, to create the fix. Xcode will also
follow cross-project references to targets in other projects.

The Fix command in Xcode is a powerful way to make small changes
to a source file without restarting your debugging session. Although
powerful, there are some things you need to do before you can take
advantage of the Fix command. The command itself is enabled only
when you are actively debugging an executable. In addition, you
must make sure you build your program using the following settings:

- Build using
  native targets
- Compile your code with GCC version 3.3 or later
- For C++ developers, link your code using ZeroLink
- Build your code without optimizations
- Build your code with debugging symbols enabled

In general, if you build using the Development build style
provided by Xcode, the correct settings are used. However, if you
try to patch your executable and get a file-not-found error, check
your target’s build settings and make sure that debugging symbols
are turned on, as described in [Generating Debugging Information](Running%20in%20Xcode%E2%80%99s%20Debugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrthewueqkcjfbumrsh).
You can also check the build log to make sure that the patch bundle
was created.

The Fix command works on only one file at a time. If you make
changes to multiple source files, you must fix each file separately
before continuing with your debugging session.

There are many types of code changes that cannot be patched.
The GDB debugger reports an error if it cannot integrate any of
your changes due to a known restriction. If GDB reports one of these
errors, you must rebuild your program and restart your debugging session
or continue debugging the program without the changes.

GDB recognizes the following changes to your code and reports
an error if you try to include them as part of a fix:

- Changes to
  the number or type of arguments in a function or method that is
  currently on the stack
- Changes to the return type or name of a function or method
  that is currently on the stack
- Changes to the number or type of local variables in a function
  or method that is currently on the stack
- Changes to the type of global or file-static variables
- Symbol type redefinitions, that is, changing a function to
  a variable or a variable to a function.

In addition to the restrictions reported by GDB, there are
additional restrictions that GDB currently does not check. If you
attempt to include any of these changes in a patch, your application
may crash or exhibit other undefined behavior when it encounters
the code. The solution is to avoid using the Fix command for the
change. Instead, rebuild your program and restart your debugging
session.

The following is a list of changes that cannot be included
as part of a fix:

- Changes to
  a nib file
- Changes to the definition of a structure or union
- The addition of a new Objective-C class
- The addition or removal of class instance variables
- The addition or removal of class methods
- The addition or removal of methods to an Objective-C category.
  These methods are not registered with the Objective-C runtime and
  thus cannot be called. (You can fix existing methods in a category.)
- Any reference to an unresolved external variable or function.
  Link errors of this nature cannot be resolved by the dynamic linker.
- The addition of a static variable across multiple patches
  in one session. GDB maintains a copy of the static in each patch;
  however, because there is no original to refer to, each variable
  remains separate from the others, which can lead to unpredictable
  results.
- The addition of a function to one file when it is called from
  a different patched file. New functions are private to the patch
  file in which they appear.
- The addition of a new `try` block
  or the addition of a `catch` handler
  to an existing block
- The addition of a C++ template class specialization
- Changes to functions that require two-level namespaces during
  linking to prevent known symbol conflicts across different libraries.
  GDB supports patching two-level namespace binaries but currently
  does so using flat namespace conventions.

Although there are many restrictions to what you can fix,
there are also some features that are explicitly supported by the
Fix command, including the following:

- Storing pointers
  to a patched function still works. GDB inserts code to jump from
  the old function to the newly-patched function. Thus, despite your
  code having a pointer to the original function, using that pointer
  executes the patched version.
- You can add new file-local static variables to a file. One
  caveat to adding such variables is that GDB does not execute any
  initialization code associated with them. Thus, if you declare a
  new class instance as a global static, GDB does not execute any
  constructors or static initializers for the instance. Also, there
  are limitations on how those variables behave after multiple patches.
  See [Additional Restrictions](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrugqwueqsdineueqkb) for more information.
- You can add new C++ classes as part of a patch.

[Next](Remote%20Debugging%20in%20Xcode.md)[Previous](Shared%20Libraries%20Window.md)

