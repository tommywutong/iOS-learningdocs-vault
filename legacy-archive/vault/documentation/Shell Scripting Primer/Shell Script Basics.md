---
title: Shell Scripting Primer
apple_id: TP40004268
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/shell_scripts/shell_scripts.html
archived_at: '2026-07-18T01:39:31.263899Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Shell Scripting Primer](Introduction.md)


[Next](Shell%20Input%20and%20Output.md)[Previous](Before%20You%20Begin.md)

# Shell Script Basics

Writing a shell script is like riding a bike. You fall off and scrape your knees a lot at first. With a bit more experience, you become comfortable riding them around town, but also quickly discover why most people drive cars for longer trips.

Shell scripting is generally considered to be a glue language, ideal for creating small pieces of code that connect other tools together. While shell scripts can be used for more complex tasks, they are usually not the best choice.

If you have ever successfully trued a bicycle wheel (or paid someone else to do so), that’s similar to learning the basics of shell scripting. If you don’t true your scripts, they wobble. Put another way, it is often easy to write a script, but it can be more challenging to write a script that consistently works well.

This chapter and the next two chapters introduce the basic concepts of shell scripting. The remaining chapters in this document provide additional breadth and depth. This document is not intended to be a complete reference on writing shell scripts, nor could it be. It does, however, provide a good starting point for beginners first learning this black art.

There are many different dialects of shell scripts, each with their own quirks, and some with their own syntax entirely. Because of these differences, the road to good shell scripting can be fraught with peril, leading to script failures, misbehavior, and even outright data loss.

To that end, the first lesson you must learn before writing a shell script is that there are two fundamentally different sets of shell script syntax: the Bourne shell syntax and the C shell syntax. The C shell syntax is more comfortable to many C programmers because the syntax is somewhat similar. However, the Bourne shell syntax is significantly more flexible and thus more widely used. For this reason, this document only covers the Bourne shell syntax.

The second hard lesson you will invariably learn is that each dialect of Bourne shell syntax differs slightly. This document includes only pure Bourne shell syntax and a few BASH-specific extensions. Where BASH-specific syntax is used, it is clearly noted.

The terminology and subtle syntactic differences can be confusing—even a bit overwhelming at times; had Dorothy in _The Wizard of Oz_ been a programmer, you might have heard her exclaim, "BASH and ZSH and CSH, Oh My!" Fortunately, once you get the basics, things generally fall into place as long as you avoid using shell-specific features. Stay on the narrow road and your code will be portable.

Some common shells are listed below, grouped by script syntax:

__Bourne-compatible shells__

- `sh`
- `bash`
- `zsh`
- `ksh`

__C-shell-compatible shells__

- `csh`
- `tcsh`
- `bcsh` (C shell to Bourne shell translator/emulator)

Many of these shells have more than one variation. Most of these variations are denoted by prefixing the name of an existing shell with additional letters that are short for whatever differentiates them from the original shell. For example:

- The shell `pdksh` is a variant of `ksh`. Being a public domain rewrite of AT&T's `ksh`, it stands for "Public Domain Korn SHell." (This is a bit of a misnomer, as a few bits are under a BSD-like open source license. However, the name remains.)
- The shell `tcsh` is an extension of `csh`. It stands for the TENEX C SHell, as some of its enhancements were inspired by the TENEX operating system.
- The shell `bash` is an extension of `sh`. It stands for the Bourne Again SHell. (Oddly enough, it is not a variation of `ash`, the Almquist SHell, though both are Bourne shell variants. This should not be confused with the `dash` shell—an `ash`-derived shell used in some Linux distributions—whose name stands for the Debian Almquist SHell.)

And so on. In general, with the exception of `csh` and `tcsh`, it is usually safe to assume that any modern login shell is compatible with Bourne shell syntax.

The C shell is popular among some users as a shell for interacting with the computer because it allows simple scripts to be written more easily. However, the C shell scripting language is limited in a number of ways, many of which are hard to work around. For this reason, use of the C shell scripting language for writing complex scripts is not recommended. For more information, read “CSH Programming Considered Harmful” at [http://www.faqs.org/faqs/unix-faq/shell/csh-whynot/](http://www.faqs.org/faqs/unix-faq/shell/csh-whynot/). Although many of the language flaws it describes are fixed by some modern C shells, if you are writing a script that must work on multiple computers across different operating systems, you cannot always guarantee that the installed C shell will support those extensions.

However, the C shell scripting language has its uses, particularly for writing scripts that set up environment variables for interactive shell environments, execute a handful of commands in order, or perform other relatively lightweight chores. To support such uses, the C shell syntax is presented alongside the Bourne shell syntax within this "basics” chapter where possible.

Outside of this chapter, this document does not generally cover the C shell syntax. If after reading this, you still want to write a more complex script using the C shell programming language, you can find more information in on the C shell in the manual page for `csh`.

What follows is a very basic shell script that prints “Hello, world!” to the screen:

```
#!/bin/sh

echo "Hello, world!"
```

The first thing you should notice is that the script starts with ‘`#!`’. This is known as an interpreter line. If you don’t specify an interpreter line, the default is usually the Bourne shell (`/bin/sh`). However, it is best to specify this line anyway for consistency.

The second thing you should notice is the `echo` command. The `echo` command is nearly universal in shell scripting as a means for printing something to the user’s screen. (Technically speaking, `echo` is generally a shell builtin, but it also exists as as standalone command, `/bin/echo`. You can read more about the difference between the builtin version and the standalone version in [echo](Designing%20Scripts%20for%20Cross-Platform%20Deployment.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrg4wvgvzrgi) and [Use Shell Builtins Wherever Possible](Performance%20Tuning.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjsgawvgvzrgq).)

If you’d like, you can try this script by saving those lines in a text file (say “hello_world.sh”) in your home directory. Then, in Terminal, type:

```
chmod u+x hello_world.sh
./hello_world.sh
```

Of course, this script isn’t particularly useful. It just prints the words “Hello, world!“ to your screen. To make this more interesting, the next script throws in a few variables.

```
#!/bin/sh

FIRST_ARGUMENT="$1"
echo "Hello, world $FIRST_ARGUMENT!"
```

Type or paste this script into the text editor of your choice (see [Creating Text Files in Your Home Directory](Before%20You%20Begin.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmjnknltcmq) for help creating a text file) and save the file in your home directory in a file called `test.sh`.

Once you have saved the file in your home directory, type ‘`chmod a+x test.sh`’ in Terminal to make it executable. Finally, run it with ‘`./test.sh leaders`’. You should see “Hello, world leaders!” printed to your screen.

This script provides an example of a variable assignment. The variable `$1` contains the first argument passed to the shell script. In this example, the script makes a copy and stores it into a variable called `FIRST_ARGUMENT`, then prints that variable.

You should immediately notice that variables may or may not begin with a dollar sign, depending on how you are using them. If you want to dereference a variable, you precede it with a dollar sign. The shell then inserts the contents of the variable at that point in the script. For all other uses, you do not precede it with a dollar sign.

You should also notice that the argument to echo is surrounded by double quotation marks. This is explained further in the next section, [Using Arguments And Variables That Contain Spaces](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrtg4wvgvzu).

Take a second look at the script from the previous section:

```
#!/bin/sh

FIRST_ARGUMENT="$1"
echo "Hello, world $FIRST_ARGUMENT!"
```

Notice that the echo statement is followed by a string surrounded by quotation marks. Normally, the shell uses spaces to separate arguments to commands. Outside of quotation marks, the shell would treat “Hello,” and “world” as separate arguments to `echo`.

By surrounding the string with double quote marks, the shell treats the entire string as a single argument to `echo` even though it contains spaces.

To see how this works, save the script above as `test.sh` (if you haven’t already), then type the following commands:

```
./test.sh leaders and citizens
./test.sh "leaders and citizens"
```

The first line above prints “Hello, world leaders!” because the space after “leaders” ends the first argument (`$1`). Inside the script, the variable `$1` contains “leaders”, `$2` contains “and”, and `$3` contains “citizens”.

The second line above prints “Hello, world leaders and citizens!” because the quotation marks on the command line cause everything within them to be grouped as a single argument.

Notice also that there are similar quotation marks on the right side of the assignment statement:

```
FIRST_ARGUMENT="$1"
```

With most modern shells, these double quotation marks are not required for this particular assignment statement (because there are no literal spaces on the right side), but they are a good idea for maximum compatibility. See [Historical String Parsing](Historical%20Footnotes%20and%20Arcana.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnrnknlte) in [Historical Footnotes and Arcana](Historical%20Footnotes%20and%20Arcana.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnrnknltc) to learn why.

When assigning literal strings (rather than variables containing strings) to a variable, however, you must surround any spaces with quotation marks. For example, the following statement does not do what you might initially suspect:

```
STRING2=This is a test
```

If you type this statement, the Bourne shell gives you an error like this:

```
sh: is: command not found
```

The reason for this seemingly odd error is that the assignment statement ends at the first space, so the next word after that statement is interpreted as a command to execute. See [Overriding Environment Variables for Child Processes (Bourne Shell)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrtg4wvgvzrgi) for more details.

Instead, write this statement as:

```
STRING2="This is a test"
```

Using quotation marks is particularly important when working with variables that contain filenames or paths. For example, type the following commands:

```
mkdir "/tmp/My Folder"
FILENAME="/tmp/My Folder"
ls "$FILENAME"
ls $FILENAME
```

The above example creates a directory in `/tmp` called “My Folder”. (Don’t worry about deleting it because `/tmp` gets wiped every time you reboot.) It then attempts to list the files in that directory. The first time, it uses quotation marks. The second time, it does not. Notice that the shell misinterprets the command the second time as being an attempt to list the files in `/tmp/My` and the files in `Folder`.

In modern Bourne shells, expansion of variables, occurs _after_ the statement itself is fully parsed by the shell. (See [Historical String Parsing](Historical%20Footnotes%20and%20Arcana.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnrnknlte) in [Historical Footnotes and Arcana](Historical%20Footnotes%20and%20Arcana.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnrnknltc) for more information.) Thus, as long as the variable is enclosed in double quote marks, you do not get any execution errors even if the variable’s value contains double-quote marks.

However, if you are using double quote marks within a literal string, you must quote that string properly. For example:

```
MYSTRING="The word of the day is \"sedentary\"."
```

This quoting technique also applies to literal strings within commands entered on the command line. For example, using the script from earlier in [Shell Variables and Printing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrtg4wvgvzy), the command:

```
./test.sh "\"leaders\""
```

prints the phrase “Hello, world “leaders”!”

The details of quotes as they apply to variable expansion are explained in [Parsing, Variable Expansion, and Quoting](Flow%20Control%2C%20Expansion%2C%20and%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnbnknltema). (Variable safety with shells that predate this behavior is generally impractical. Fortunately, the modern behavior has been the norm since the mid-1990s.)

Shell scripts also allow the use of single quote marks. Variables between single quotes are not replaced by their contents. Be sure to use double quotes unless you are intentionally trying to display the actual name of the variable. You can also use single quotes as a way to avoid the shell interpreting the contents of the string in any way. These differences are described further in [Parsing, Variable Expansion, and Quoting](Flow%20Control%2C%20Expansion%2C%20and%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnbnknltema).

One key feature of shell scripts is that variables are typically limited in their scope to the currently running script. The scoping of variables is described in more detail in [Subroutines, Scoping, and Sourcing](Subroutines%2C%20Scoping%2C%20and%20Sourcing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvkfanbqgaydgnjrgmwvgvzr). For now, though, it suffices to say that variables generally do not get passed on to scripts or tools that they execute.

Normally, this is what you want. Most variables in a shell script do not have any meaning to the tools that they execute, and thus represent clutter and the potential for variable namespace collisions if they are exported. Occasionally, however, you will find it necessary to make a variable's value available to an outside tool. To do this, you must export the variable. These exported variables are commonly known as environment variables because they affect the execution of every script or tool that runs but are not part of those scripts or tools themselves.

A classic example of an environment variable that is significant to scripts and tools is the `PATH` variable. This variable specifies a list of locations that the shell searches when executing programs by name (without specifying a complete path). For example, when you type `ls` on the command line, the shell searches in the locations specified in `PATH` (in the order specified) until it finds an executable called `ls` (or runs out of locations, whichever comes first).

The details of exporting shell variables differ considerably between the Bourne shell and the C shell. Thus, the following sections explain these details in a shell-specific fashion.

Generally speaking, the first time you assign a value to an environment variable such as the `PATH` variable, the Bourne shell creates a new, _local_ copy of this shell variable that is specific to your script. Any tool executed from your script is passed the original value of `PATH` inherited from whatever script, tool, or shell that launched it.

With the BASH shell, however, any variable inherited from the environment is automatically exported by the shell. Thus, in some versions of OS X, if you modify inherited environment variables (such as `PATH`) in a script, your local changes will be seen automatically by any tool or script that your script executes. Thus, in these versions of OS X, you do not have to explicitly use the `export` statement when modifying the `PATH` variable.

Because different Bourne shell variants handle these external environment variables differently (even among different versions of OS X), this creates two minor portability problems:

- A script written without the `export` statement may work on some versions of OS X, but will fail on others. You can solve this portability problem by using the `export` builtin, as described in this section.
- A shell script that changes variables such as `PATH` will alter the behavior of any script that it executes, which may or may not be desirable. You can solve this problem by overriding the `PATH` environment variable when you execute each individual tool, as described in [Overriding Environment Variables for Child Processes (Bourne Shell)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrtg4wvgvzrgi).

To guarantee that your modifications to a shell variable are passed to any script or tool that your shell script calls, you _must_ use the `export` builtin. You do not have to use this command every time you change the value; the variable remains exported until the shell script exits.

For example:

```
export PATH="/usr/local/bin:$PATH"
# or
PATH="/usr/local/bin:$PATH"
export PATH
```

Either of these statements has the same effect—specifically, they export the local notion of the `PATH` environment variable to any command that your script executes from now on. There is a small catch, however. You cannot later undo this export to restore the original global declaration. Thus, if you need to retain the original value, you must store it somewhere yourself.

In the following example, the script stores the original value of the `PATH` environment variable, exports an altered version, executes a command, and restores the old version.

```
ORIGPATH="$PATH"
PATH="/usr/local/bin:$PATH"
export PATH
# Execute some command here---perhaps a
# modified ls command....
ls
PATH="$ORIGPATH"
```

If you need to find out whether an environment variable (whether inherited by your script or explicitly set with the `export` directive) was set to empty or was never set in the first place, you can use the `printenv` command to obtain a complete list of defined variables and use `grep` to see if it is in the list. (You should note that although `printenv` is a csh builtin, it is also a standalone command in `/usr/bin`.)

For example:

```
DEFINED=`printenv | grep -c '^VARIABLE='`
```

The resulting variable will contain 1 if the variable is defined in the environment or 0 if it is not.

Because the BASH Bourne shell variant automatically exports all variables inherited from its environment, any changes you make to preexisting environment variables such as `PATH` are automatically inherited by any tool or script that your script executes. (This is not true for other Bourne shell variants; see [Using the export Builtin (Bourne Shell)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrtg4wvgvzrge) for further explanation.)

While automatic export is usually convenient, you may sometimes wish to change a preexisting environment variable without modifying the environment of any script or tool that your script executes. For example, if your script executes a number of tools in `/usr/local/bin`, it may be convenient to change the value of `PATH` to include `/usr/local/bin`. However, you may not want child processes to also look in `/usr/local/bin`.

This problem is easily solved by overriding the environment variable `PATH` on a per-execution basis. Consider the following script:

```
#!/bin/sh

echo $MYVAR
```

This script prints the value of the variable `MYVAR`. Normally, this variable is empty, so this script just prints a blank line. Save the script as `printmyvar.sh`, then type the following commands:

```
chmod a+x printmyvar.sh      # makes the script executable
MYVAR=7 ./printmyvar.sh      # runs the script
echo "MYVAR IS $MYVAR"       # prints the variable
```

Notice that the assignment statement `MYVAR=7` applies `only` to the command that follows it. The value of `MYVAR` is altered in the environment of the command `./printmyvar.sh`, so the script prints the number 7. However, the original (empty) value is restored after executing that command, so the echo statement afterwards prints an empty string for the value of `MYVAR`.

Thus, to modify the `PATH` variable locally but execute a command with the original `PATH` value, you can write a script like this:

```
#!/bin/sh
GLOBAL_PATH="$PATH"
PATH=/usr/local/bin

PATH="$GLOBAL_PATH" /bin/ls
```


In the C shell, variables are exported if you set them with `setenv`, but not if you set them with `set`. Thus, if you want your shell variable modifications to be seen by any tool or script that you call, you should use the `setenv` builtin. This builtin is the C shell equivalent to issuing an assignment statement with the `export` builtin in the Bourne shell.

```
setenv VALUE "Four"
echo "VALUE is '$VALUE'."
```

If you want your shell variables to only be available to your script, you should use the `set` builtin (described in [Shell Variables and Printing](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqmrtg4wvgvzy)). The `set` builtin is equivalent to a simple assignment statement in the Bourne shell.

```
set VALUE = "Four"
echo "VALUE is '$VALUE'."
```

Notice that the local variable version requires an equals sign (`=`), but the exported environment version does not (and produces an error if you put one in).

To remove variables in the C shell, you can use the `unsetenv` or `unset` builtin. For example:

```
setenv VALUE "Four"
unsetenv VALUE

set VALUE = "Four"
unset VALUE

echo "VALUE is '$VALUE'."
```

This will generate an error message. In the C shell, it is not possible to print the value of an undefined variable, so if you think you may need to print the value later, you should set it to an empty string rather than using `unset` or `unsetenv`.

If you need to test an environment variable (_not_ a shell-local variable) that may or may not be part of your environment (a variable set by whatever process called your script), you can use the `printenv` builtin. This prints the value of a variable if set, but prints nothing if the variable is not set, and thus behaves just like the variable behaves in the Bourne shell.

For example:

```
set X = `printenv VALUE`
echo "X is "\"$X\"
```

This prints `X is ""` if the variable is either empty or undefined. Otherwise, it prints the value of the variable between the quotation marks.

If you need to find out if a variable is simply empty or is actually not set, you can also use `printenv` to obtain a complete list of defined variables and use `grep` to see if it is in the list. For example:

```
set DEFINED = `printenv | grep -c '^VARIABLE='`
```

The resulting variable will contain 1 if the variable is defined in the environment or 0 if it is not.

Unlike the Bourne shell, the C shell does not provide a built-in syntax for overriding environment variables when executing external commands. However, it is possible to simulate this either by using the `env` command.

The best and simplest way to do this is with the `env` command. For example:

```
env PATH="/usr/local/bin" /bin/ls
```

As an alternative, you can use the `set` builtin to make a temporary copy of any variable you need to override, change the value, execute the command, and restore the value from the temporary copy.

You should notice, however, that whether you use the `env` command or manually make a copy, the `PATH` variable is altered _prior to_ searching for the command. Because the `PATH` variable controls where the shell looks for programs to execute, you must therefore explicitly provide a _complete_ path to the `ls` command or it will not be found (unless you have a copy in `/usr/local/bin`, of course). The `PATH` environment variable is explained in [Special Shell Variables](Special%20Shell%20Variables.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnznknltc).

As a workaround, you can determine the path of the executable using the `which` command prior to altering the `PATH` environment variable.

```
set GLOBAL_PATH = "$PATH"
set LS = `which ls`
setenv PATH "/usr/local/bin"
$LS
setenv PATH "$GLOBAL_PATH"
unset GLOBAL_PATH
```

Or, using `env`:

```
set LS = `which ls`
env PATH='/usr/local/bin' $LS
```

The use of the backtick (`) operator in this fashion is described in [Inline Execution](Flow%20Control%2C%20Expansion%2C%20and%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnbnknltgma).

For the most part, in Bourne shell scripts, when you need to get rid of a variable, setting it to an empty string is sufficient. However, in long-running scripts that might encounter memory pressure, it can be marginally useful to delete the variable entirely. To do this, use the `unset` builtin.

For example:

```
MYVAR="this is a test"
unset MYVAR
echo "MYVAR IS \"$MYVAR\""
```

The `unset` builtin can also be used to delete environment variables.

[Next](Shell%20Input%20and%20Output.md)[Previous](Before%20You%20Begin.md)

