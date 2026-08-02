---
title: Xcode Project Management Guide
apple_id: TP40006917
resource_type: Guide
platform: iOS|Xcode Developer Tools|macOS
topic: Xcode
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeProjectManagement/240-Running_Programs/running_programs.html
archived_at: '2026-07-15T07:28:32.066482Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Project Management Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Defining%20Executable%20Environments.md)

# Running Programs

After you build a product, you can test it from Xcode. To run a product, perform these steps:

1. __Choose the appropriate build configuration.__ Depending on how you want to test the product, you run a release or debug configuration of it. See [Build Configurations](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeBuildSystem/400-Build_Configurations/build_configs.html#//apple_ref/doc/uid/TP40002692) for details.
2. __Build the product.__ In the build process you may find problems that prevent Xcode from creating a binary to run. Xcode must successfully build the product before you can run it. See [Building with Xcode](Building%20Products.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojtfvjvomrq) for more information.
3. __Run the product.__ To run the product, do one of the following:

   - Choose Run > Run – Breakpoints Off.
   - Choose Run > Debug – Breakpoints On.
   - Choose Run > Run with Performance Tool.

   If none of these commands are available, try associating an executable with the selected target. See [Defining Executable Environments](Defining%20Executable%20Environments.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmojyfvbecqscifduisa).

In addition, after halting a program, you can restart it using the last run configuration by choosing Run > Go.

Many programs print messages to `stdout`, as well as logging debugging messages to the console or `stderr`. When you run your program in Xcode, you can see this output in the console window. In addition, if you are creating a command-line program that takes input from `stdin`, you can use the console to interact with your program. To open console, choose Run > Console.

In some unique cases, you may want to unconditionally stop your program’s execution with a trap. Such an operation in programs launched from Xcode would cause the debugger to appear, pointing to the code line that caused the trap. In programs launched directly, the CrashReporter application would log a crash with stack traces for the program’s threads.

Listing 11-1 shows the assembly-language instructions that stop a program.

__Listing 11-1__  Halting a program with a trap instruction

```
asm {trap}            ; Stops a program running on PPC32 or PPC64.
__asm {int 3}         ; Stops a program running on IA-32.
```

[Next](Document%20Revision%20History.md)[Previous](Defining%20Executable%20Environments.md)

