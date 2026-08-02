---
title: Code Size Performance Guidelines
apple_id: 10000149i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/CompilerOptions.html
archived_at: '2026-07-18T01:46:33.594211Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Size Performance Guidelines](Introduction%20to%20Code%20Size%20Performance%20Guidelines.md)


[Next](Improving%20Locality%20of%20Reference.md)[Previous](Overview%20of%20the%20Mach-O%20Executable%20Format.md)

# Managing Code Size

The GCC compiler supports a variety of options for optimizing your code. Most of these techniques result in the generation of less code or faster code, depending on your needs. As you prepare your software for release, you should experiment with these techniques to see which ones benefit your code the most.

As your project code stabilizes, you should begin experimenting with the basic GCC options for optimizing code. The GCC compiler supports optimization options that let you choose whether you prefer a smaller binary size, faster code, or faster build times.

For new projects, Xcode automatically disables optimizations for the development build style and selects the “fastest, smallest” option for the deployment build style. Code optimizations of any kind result in slower build times because of the extra work involved in the optimization process. If your code is changing, as it does during the development cycle, you do not want optimizations enabled. As you near the end of your development cycle, though, the deployment build style can give you an indication of the size of your finished product.

Table 1 lists the optimization levels available in Xcode. When you select one of these options, Xcode passes the appropriate flags to the GCC compiler for the given group or files. These options are available at the target-level or as part of a build style. See the Xcode Help for information on working with build settings for your project.

__Table 1__  GCC compiler optimization options

| Xcode Setting | Description |
| None | The compiler does not attempt to optimize code. Use this option during development when you are focused on solving logic errors and need a fast compile time. Do not use this option for shipping your executable. |
| Fast | The compiler performs simple optimizations to boost code performance while minimizing the impact to compile time. This option also uses more memory during compilation. |
| Faster | Performs nearly all supported optimizations that do not require a space-time trade-off. The compiler does not perform loop unrolling or function inlining with this option. This option increases both compilation time and the performance of generated code. |
| Fastest | Performs all optimizations in an attempt to improve the speed of the generated code. This option can increase the size of generated code as the compiler performs aggressive inlining of functions.  This option is generally not recommended. See [Avoid Excessive Function Inlining](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dcljrgmytonzq) for more information. |
| Fastest, smallest | Performs all optimizations that do not typically increase code size. This is the preferred option for shipping code as it gives your executable a smaller memory footprint. |

As with any performance enhancement, do not make assumptions about which option will give you the best results. You should always measure the results of each optimization you try. For example, the “Fastest” option might generate extremely fast code for a particular module, but it usually does so at the expense of executable size. Any speed advantages you gain from the code generation are easily lost if the code needs to be paged in from disk at runtime. 

Besides code-level optimizations, there are some additional techniques you can use to organize your code at the module level. The following sections describes these techniques.

For statically-linked executables, dead-code stripping is the process of removing unreferenced code from the executable file. The idea behind dead-stripping is that if the code is unreferenced, it must not be used and therefore is not needed in the executable file. Removing dead code reduces the size of your executable and can help reduce paging.

Starting with Xcode Tools version 1.5, the static linker (`ld`) supports dead stripping of executables. You can enable this feature directly from Xcode or by passing the appropriate command-line options to the static linker.

To enable dead-code stripping in Xcode, do the following:

1. Select your target.
2. Open the Inspector or Get Info window and select the Build tab.
3. In the Linking settings, enable the Dead Code Stripping option.
4. In the Code Generation settings, set the Level of Debug Symbols option to All Symbols.

To enable dead-code stripping from the command line, pass the `-dead_strip` option to `ld`. You should also pass the `-gfull` option to GCC to generate a complete set of debugging symbols for your code. The linker uses this extra debugging information to dead strip the executable.

If you do not want to remove any unused functions, you should at least isolate them in a separate section of your `__TEXT` segment. Moving unused functions to a common section improves the locality of reference of your code and reduces the likelihood of their being loaded into memory. For more information on how to group functions in a common section, see [Improving Locality of Reference](Improving%20Locality%20of%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3delkdjjbeursjirca).

Debugging symbols and dynamic-binding information can take up a lot of space and comprise a large percentage of your executable’s size. Before shipping your code, you should strip out all unneeded symbols.

To strip debugging symbols from your executable, change the Xcode build-style settings to “Deployment” and rebuild your executable. You can also generate debugging symbols on a target-by-target basis if you prefer. See the Xcode Help for more information on build styles and target settings.

To remove dynamic-binding symbols manually from your executable, use the `strip` tool. This tool removes symbol information that would normally be used by the dynamic linker to bind external symbols at runtime. Removing the symbols for functions that you do not want to be dynamically bound reduces your executable size and reduces the number of symbols the dynamic linker must bind. Typically, you would use this command without any options to remove non-external symbols, as shown in the following example:

```shell
% cd ~/MyApp/MyApp.app/Contents/MacOS
% strip MyApp
```

This command is equivalent to running `strip` with the `-u` and `-r` options. It removes any symbols marked as `non-external` but does not remove symbols that are marked `external`.

An alternative to stripping out dynamic-binding symbols manually is to use an exports file to limit the symbols exported at build time. An exports file identifies the specific symbols available at runtime from your executable. For more information on creating an exports file, see [Minimizing Your Exported Symbols](Minimizing%20Your%20Exported%20Symbols.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dilkdjjbeursjirca).

When an exception is thrown, the C++ runtime library must be able to unwind the stack back to the point of the first matching `catch` block. For this to work, the GCC compiler generates stack unwinding information for each function that may throw an exception. This unwinding information is stored in the executable file and describes the objects on the stack. This information makes it possible to call the destructors of those objects to clean them up when an exception is thrown.

Even if your code does not throw exceptions, the GCC compiler still generates stack unwinding information for C++ code by default. If you use exceptions extensively, this extra code can increase the size of your executable significantly.

You can disable exception handling in Xcode altogether by disabling the “Enable C++ Exceptions” build option for your target. From the command line, pass the `-fno-exceptions` option to the compiler. This option removes the stack unwinding information for your functions. However, you must still remove any `try`, `catch`, and `throw` statements from your code.

If your code uses exceptions in some places but not everywhere, you can explicitly identify methods that do not need unwinding information by adding an empty exception specification to the method declaration. For example, in the following code, the compiler must generate stack unwinding information for `my_function` on the grounds that `my_other_function` or a function called by it may throw an exception.

```
extern int my_other_function (int a, int b);
int my_function (int a, int b)
{
   return my_other_function (a, b);
}
```

However, if you know that `my_other_function` cannot throw exceptions, you can signal this to the compiler by including the empty exception specification (`throw ()`) in the function declarations. Thus, you would declare the preceding function as follows:

```
extern int foo (int a, int b) throw ();
int my_function (int a, int b) throw ()
{
   return foo (a, b);
}
```


When writing your code, consider your use of exceptions carefully. Exceptions should be used to indicate exceptional circumstances—that is, they should be used to report problems that you did not anticipate. If you read from a file and got an end-of-file error, you would not want to throw an exception because this is a known type of error and can be handled easily. If you try to read from a file you know to be open and are told the file ID is invalid, then you would probably want to throw an exception.

Although inline functions can improve speed in some situations, they can also degrade performance on OS X if used excessively. Inline functions eliminate the overhead of calling a function but do so by replacing each function call with a copy of the code. If an inline function is called frequently, this extra code can add up quickly, bloating your executable and causing paging problems.

Used properly, inline functions can save time and have a minimal impact on your code footprint. Remember that the code for inline functions should generally be very short and called infrequently. If the time it takes to execute the code in a function is less than the time it takes to call the function, the function is a good candidate for inlining. Generally, this means that an inline function probably should have no more than a few lines of code. You should also make sure that the function is called from as few places as possible in your code. Even a short function can cause excessive bloat if it is made inline in dozens or hundreds of places.

Also, you should be aware that the “Fastest” optimization level of the GCC should generally be avoided. At this optimization level, the compiler aggressively tries to create inline functions, even for functions that are not marked as inline. Unfortunately, doing so can significantly increase the size of your executable and cause far worse performance problems due to paging.

Most shared libraries don’t need the module features of the Mach-O runtime. In addition, cross-module calls incur the same overhead as cross-library calls. As a result, you should link all of your project’s intermediate object files together into a single module.

To combine your object files, you must pass the `-r` option to `ld` during the link phase. If you are using Xcode to build your code, this is done for you by default.

[Next](Improving%20Locality%20of%20Reference.md)[Previous](Overview%20of%20the%20Mach-O%20Executable%20Format.md)

