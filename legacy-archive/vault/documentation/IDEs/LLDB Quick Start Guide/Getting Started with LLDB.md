---
title: LLDB Quick Start Guide
apple_id: TP40012917
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2013-09-18'
source_url: https://developer.apple.com/library/archive/documentation/IDEs/Conceptual/gdb_to_lldb_transition_guide/document/lldb-basics.html
archived_at: '2026-07-15T07:42:25.283322Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [LLDB Quick Start Guide](About%20LLDB%20and%20Xcode.md)


[Next](GDB%20and%20LLDB%20Command%20Examples.md)[Previous](About%20LLDB%20and%20Xcode.md)

# Getting Started with LLDB

LLDB is a command-line debugging environment with functionality similar to GDB. LLDB provides the underlying debugging environment for Xcode, which includes a console pane in the debugging area for direct access to LLDB commands within the Xcode IDE environment.

This chapter briefly explains the LLDB syntax and command features, informs you on the use of the command aliasing capabilities, and introduces you to the LLDB help system.

All users starting out with LLDB should be aware of the LLDB command structure and syntax in order to tap the potential of LLDB and understand how to get the most from it. In many cases, commands provided by LLDB—for instance, `list` and `b`—work just like GDB commands and make learning LLDB easier for experienced GDB users.

The LLDB command syntax is structured and regular throughout. LLDB commands are all of the form:

```
<command> [<subcommand> [<subcommand>...]] <action> [-options [option-value]] [argument [argument...]]
```

_Command_ and _subcommand_ are names of LLDB debugger objects. Commands and subcommands are arranged in a hierarchy: a particular command object creates the context for a subcommand object which follows it, which again provides context for the next subcommand, and so on. The _action_ is the operation you want to perform in the context of the combined debugger objects (the string of _command subcommand.._ entities preceding it). Options are _action modifiers_, which often take a value. Arguments represent a variety of different things according to the context of the command being used—for example, using the `process launch` command to start a process, the arguments in that context are what you enter on the command line as if you were invoking the process outside of a debugging session.

The LLDB command-line parsing is completed before command execution. Commands, subcommands, options, option values, and arguments are all white space separated, and double quotes are used to protect white spaces in option values and arguments. If you need to put a backslash or double quote character into an argument, you precede that character with a backslash in the argument. LLDB uses both single and double quotes equivalently, allowing doubly quoted portions of a command line to be written easily. For example:

```
(lldb) command [subcommand] -option "some \"quoted\" string"
```

can also be written:

```
(lldb) command [subcommand] -option 'some "quoted" string'
```

This command parsing design helps make LLDB command syntax regular and uniform across all commands. (For the GDB users, it also means you may have to quote some arguments in LLDB that you wouldn’t have to quote in GDB.)

As example of a simple LLDB command, to set a breakpoint in file `test.c` at line 12 you enter:

```
(lldb) breakpoint set --file test.c --line 12
```

Commands which appear to diverge from this model—for example, `print` or `b`—are typically customized command forms created by the `command alias` mechanism, which is discussed in [Command Aliases and Help](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmjxfvbuqmrnknltcma).

Command options in LLDB have a canonical (also referred to as “discoverable”) form and an abbreviated form. For example, here is a partial listing of the command options for the `breakpoint set` command, listing the canonical form in parentheses:

```
breakpoint set
       -M <method> ( --method <method> )
       -S <selector> ( --selector <selector> )
       -b <function-name> ( --basename <function-name> )
       -f <filename> ( --file <filename> )
       -l <linenum> ( --line <linenum> )
       -n <function-name> ( --name <function-name> )
…
```

Options can be placed in any order on the command line following the command. If arguments begin with a hyphen (`-`), you indicate to LLDB that you’re done with options for the current command by adding the option termination signal, a double hyphen (`--`). For instance, if you want to launch a process and give the `process launch` command the `--stop-at-entry` option, and want that same process to be launched with the arguments `-program_arg_1 value` and `-program_arg_2 value`, you enter:

```
(lldb) process launch --stop-at-entry -- -program_arg_1 value -program_arg_2 value
```


The LLDB command parser supports “raw” commands, in which, after command options are removed, the rest of the command string is passed uninterpreted to the command. This is convenient for commands whose arguments might be some complex expression that would be clumsy to protect with backslashes. For instance, the `expression` command is a raw command.

When you look up a command with `help`, the output for a command tells you whether the command is raw or not so that you know what to expect.

Raw commands can still have options, if your command string has dashes in it, you indicate that these are not option markers by putting an option termination (`--`) after the command name but before the command string.

LLDB supports command completion for source file names, symbol names, file names, and so forth. Completion in the Terminal window is initiated by inputting a tab character on the command line. Completions in the Xcode console work in the same way as the completions in the source code editor: The completions pop up automatically after the third character is typed, and the completions pop-up can be manually summoned via the Esc (Escape) key. In addition, completions in the Xcode console follow the Xcode Text Editing preferences specified in the Editing panel.

Individual options in a command can have different completers. For example, the `--file <path>` option in `breakpoint` completes to source files, the `--shlib <path>` option completes to currently loaded shared libraries, and so forth. The behavior can be quite specific—for example: if you specify `--shlib <path>`, and are completing on `--file <path>`, LLDB lists only source files in the shared library specified by `--shlib <path>`.

The command-line parsing and uniformity of the LLDB command parser differ when using LLDB compared with GDB. The LLDB command syntax sometimes forces you to be more explicit about stating your intentions, but it is more regular in use.

For example, setting a breakpoint is a common operation. In GDB, to set a breakpoint you might enter the following to break at line 12 of `foo.c`:

```
(gdb) break foo.c:12
```

And you might enter the following to break at the function `foo`:

```
(gdb) break foo
```

More complex `break` expressions are possible in GDB. One example is `(gdb) break foo.c::foo` , which means “set the breakpoint in the function `foo` in the file `foo.c`.” But at some point the GDB syntax becomes convoluted and limits GDB functionality, especially in C++, where there may be no reliable way to specify the function you want to break on. These deficiencies happen because GDB command-line syntax is supported by a complex of special expression parsers that can be at odds with each other.

The LLDB breakpoint command, by comparison, requires only a simple, straightforward approach in its expression and provides the advantages of intelligent auto completion and the ability to set breakpoints in more complex situations. To set the same file and line breakpoint in LLDB, enter:

```
(lldb) breakpoint set --file foo.c --line 12
```

To set a breakpoint on a function named `foo` in LLDB, enter:

```
(lldb) breakpoint set --name foo
```

Setting breakpoints by name is even more powerful in LLDB than in GDB because you can specify that you want to set a breakpoint at a function by method name. To set a breakpoint on all C++ methods named `foo`, enter:

```
(lldb) breakpoint set --method foo
```

To set a breakpoint on Objective-C selectors named `alignLeftEdges:`, enter:

```
(lldb) breakpoint set --selector alignLeftEdges:
```

You can limit any breakpoints to a specific executable image by using the `--shlib <path>` expression.

```
(lldb) breakpoint set --shlib foo.dylib --name foo
```

The LLDB commands presented in this section, using the discoverable command name and canonical form of the option, may seem somewhat lengthy. However, just as in GDB, the LLDB command interpreter does a shortest-unique-string match on command names, creating an abbreviated command form. For example, the following two command-line expressions demonstrate the same command:

```
(lldb) breakpoint set --name "-[SKTGraphicView alignLeftEdges:]"
(lldb) br s --name "-[SKTGraphicView alignLeftEdges:]"
```

Similarly, you can combine both shortest-unique-string matching with the abbreviated option format to reduce keystrokes. Using the two together can reduce command line expressions further. For example:

```
(lldb) breakpoint set --shlib foo.dylib --name foo
```

becomes:

```
(lldb) br s -s foo.dylib -n foo
```

Using these features of LLDB offers much the same ‘shorthand’ feel and brevity as when using GDB. Look at [Breakpoint Commands](GDB%20and%20LLDB%20Command%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmjxfvbuqmznknlte) and other sections in [GDB and LLDB Command Examples](GDB%20and%20LLDB%20Command%20Examples.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmjxfvbuqmznknltc) for more examples of how the shortest-unique-string matching and using abbreviated form options can save keystrokes.

For advanced users, LLDB has a built-in Python interpreter accessible by using the `script` command. All the features of the debugger are available as classes in the Python interpreter. As a result, the more complex commands that in GDB are introduced with the `define` command can be achieved by writing Python functions using the LLDB-Python library and then loading the scripts into your running session, accessing them with the `script` command. For more information about the LLDB-Python library, visit the [LLDB Python Reference](http://lldb.llvm.org/python-reference.html) and [LLDB Python Scripting Example](http://lldb.llvm.org/scripting.html) sections of [The LLDB Debugger website](http://lldb.llvm.org/).

Now that you understand the LLDB syntax and command-line dynamics, turn your attention to two very useful features of LLDB—command aliases and the help system.

Use the command alias mechanism in LLDB to construct aliases for commonly used commands. For instance, if you repeatedly type:

```
(lldb) breakpoint set --file foo.c --line 12
```

you can construct an alias with:

```
(lldb) command alias bfl breakpoint set -f %1 -l %2
```

which lets you enter this command as:

```
(lldb) bfl foo.c 12
```

Because command aliases are useful in a wide variety of situations, you should become familiar with their construction. For a complete explanation of command alias construction, limitations, and syntax, use the LLDB help system. Type:

```
(lldb) help command alias
```


Explore the LLDB help system to gain a broader understanding of what LLDB has to offer and to view details of LLDB command constructions. Becoming familiar with the `help` command gives you access to the extensive command documentation in the help system.

A simple invocation of the `help` command returns a list of all top-level LLDB commands. For example, here is a partial listing:

```
(lldb) help
The following is a list of built-in, permanent debugger commands:

_regexp-attach    -- Attach to a process id if in decimal, otherwise treat the
                     argument as a process name to attach to.
_regexp-break     -- Set a breakpoint using a regular expression to specify the
                     location, where <linenum> is in decimal and <address> is
                     in hex.
_regexp-bt        -- Show a backtrace.  An optional argument is accepted; if
                     that argument is a number, it specifies the number of
                     frames to display.  If that argument is 'all', full
                     backtraces of all threads are displayed.
 … and so forth …
```

Invoking `help` followed by any of the commands lists the help entry for that command and any subcommands, options, and arguments. By invoking `help <command> <subcommand> [<subcommand>…]` iteratively over all the commands, you traverse the entire LLDB command hierarchy.

The `help` command display includes all current command aliases when invoked with the option `--show-aliases` (`-a` in short form).

```
(lldb) help -a
```

A more directed way to explore what’s available in LLDB is to use the `apropos` command: It searches the LLDB help documentation for a word and dumps a summary help string for each matching command. For example:

```
(lldb) apropos file
The following commands may relate to 'file':
…
log enable                     -- Enable logging for a single log channel.
memory read                    -- Read from the memory of the process being
                                  debugged.
memory write                   -- Write to the memory of the process being
                                  debugged.
platform process launch        -- Launch a new process on a remote platform.
platform select                -- Create a platform if needed and select it as
                                  the current platform.
plugin load                    -- Import a dylib that implements an LLDB
                                  plugin.
process launch                 -- Launch the executable in the debugger.
process load                   -- Load a shared library into the current
                                  process.
source                         -- A set of commands for accessing source file
                                  information
… and so forth …
```

Use the `help` command with command aliases to understand their construction. For instance, type the following command to see an explanation of the supplied GDB `b` emulation and its implementation:

```
(lldb) help b
…
'b' is an abbreviation for '_regexp-break'
```

Another feature of the `help` command is shown by investigating the command `break command add` (used in [Setting Breakpoints](Using%20LLDB%20as%20a%20Standalone%20Debugger.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdsmjxfvbuqnbnknltg)). To demonstrate it, you should execute the command and examine the help system results:

```
(lldb) help break command add
Add a set of commands to a breakpoint, to be executed whenever the breakpoint is hit.

Syntax: breakpoint command add <cmd-options> <breakpt-id>
etc...
```

Arguments to a command that are specified in the help output in angle brackets (such as `<breakpt-id>`), indicate that the argument is a common argument type for which further help is available by querying the command system. In this case, to learn more about `<breakpt-id>`, enter:

```
(lldb) help <breakpt-id>

<breakpt-id> -- Breakpoint IDs consist major and minor numbers; the major
etc...
```

Using `help` often and exploring the LLDB help documentation is a great way to familiarize yourself with the scope of LLDB capabilities.

[Next](GDB%20and%20LLDB%20Command%20Examples.md)[Previous](About%20LLDB%20and%20Xcode.md)

