---
title: Code Size Performance Guidelines
apple_id: 10000149i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeFootprint/Articles/ReducingExports.html
archived_at: '2026-07-18T01:46:39.281566Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Size Performance Guidelines](Introduction%20to%20Code%20Size%20Performance%20Guidelines.md)


[Next](Document%20Revision%20History.md)[Previous](Reducing%20Shared%20Memory%20Pages.md)

# Minimizing Your Exported Symbols

If your application or framework has a public interface, you should limit your exported symbols to those required for your interface. Exported symbols take up space in your executable file and should be minimized when possible. Not only does this reduce the size of your executable, it also reduces the amount of work done by the dynamic linker.

By default, Xcode exports all symbols from your project. You can use the information that follows to identify and eliminate those symbols you do not want to export.

To view the symbols exported by your application, use the `nm` tool. This tool reads an executable’s symbol table and displays the symbol information you request. You can view all symbols or just the symbols from a specific segment of your executable code. For example, to display only the externally available global symbols, you would specify the `-g` option on the command line.

To view detailed symbol information, run `nm` with the `-m` option. The output from this option tells you the type of the symbol and whether it is external or local (non-external). For example, to view detailed symbol information for the TextEdit application, you would use `nm` as follows:

```
%cd /Applications/TextEdit.app/Contents/MacOS
% nm -m TextEdit
```

A portion of the resulting output might look like the following:

```
9005cea4 (prebound undefined [lazy bound]) external _abort (from libSystem)
9000a5c0 (prebound undefined [lazy bound]) external _atexit (from libSystem)
90009380 (prebound undefined [lazy bound]) external _calloc (from libSystem)
00018d14 (__DATA,__common) [referenced dynamically] external _catch_exception_raise
00018d18 (__DATA,__common) [referenced dynamically] external _catch_exception_raise_state
00018d1c (__DATA,__common) [referenced dynamically] external _catch_exception_raise_state_identity
```

In this mode, `nm` displays various information depending on the symbol. For functions and other code residing in the `__TEXT` segment, `nm` displays prebinding information and the originating library. For information in the `__DATA` segment, `nm` displays the specific section of the symbol and its linkage. For all symbols, `nm` displays whether the symbol is external or local.

If you know the symbols you want to export from your project, you should create an exports file and add that file to your project’s Linker settings. An exports file is a plain text file containing the names of the symbols you wish to make available to external callers. Each symbol must be listed on a separate line. Leading and trailing whitespace is not considered part of the symbol name. Lines starting with a `#` sign are ignored.

To include your exports file in your Xcode project, modify the target or build-style settings for your project. Set the value of the “Exported symbols file” setting to the name of your exports file. Xcode passes the appropriate options to the static linker.

To export a list of symbols from the command line, add the `-exported_symbols_list` option to your linker command. Rather than export a specific list of symbols, you can also export all symbols and then restrict a specific list. To restrict a specific list of symbols, use the `-unexported_symbols_list` option in your linker command.

Note that symbols exported by the runtime libraries must be included explicitly in your exports file for your application to launch properly. To gather a list of these symbols, link your code without an export file and then execute the `nm -m` command from Terminal. From the resulting output, gather any symbols that are marked `external` and are not part of your code and add them to your exports file.

GCC 4.0 supports custom visibility attributes for individual symbols. In addition, the compiler provides compile-time flags that let you set the default visibility for all symbols for the compiled files.

For information on using the new symbol visibility features of GCC 4.0, see “[Controlling Symbol Visibility](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/CppRuntimeEnv/Articles/SymbolVisibility.html#//apple_ref/doc/uid/TP40001670)“ in _[C++ Runtime Environment Programming Guide](../../Developer%20Tools/C%2B%2B%20Runtime%20Environment%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytmnrw)_.

[Next](Document%20Revision%20History.md)[Previous](Reducing%20Shared%20Memory%20Pages.md)

