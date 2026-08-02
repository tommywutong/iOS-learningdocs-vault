---
title: Shell Scripting Primer
apple_id: TP40004268
resource_type: Guide
platform: macOS
topic: Languages & Utilities
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/OpenSource/Conceptual/ShellScripting/SpecialShellVariables/SpecialShellVariables.html
archived_at: '2026-07-18T01:39:30.400829Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Shell Scripting Primer](Introduction.md)


[Next](Other%20Tools%20and%20Information.md)[Previous](Command%20Line%20Primer.md)

# Special Shell Variables

The Bourne shell has a number of special “automatic” variables that it maintains for informational purposes. These variables provide information such as the process ID of the shell, the exit status of the last command, and so on. This section provides a list of these special variables. For additional variables supported by specific Bourne shell variants such as BASH and ZSH, see the `bash` and `zshparam` manual pages, respectively.

__Table B-1__  Special shell variables

| Variable | Description |
| __Process information__ | __Process information__ |
| `$$` | Process ID of shell |
| `$PPID` | Process ID of shell’s parent process.  __Quirk Warning:__For subshells, the value of PPID is inherited from the parent shell. Thus, PPID is only the parent of the outermost shell process. |
| `$?` | Exit status of last command. |
| `$_` | Name of last command. |
| `$!` | Process ID of last process run in the background using ampersand (&) operator. This is commonly used in conjunction with the `wait` builtin. |
| `$PATH` | A colon-delimited list of locations where trusted executables are installed. Any executable in one of these locations can be executed without specifying a complete path. |
| __Field and record parsing__ | __Field and record parsing__ |
| `$IFS` | Input Field Separators (uses are explained in [Variable Expansion and Field Separators](Flow%20Control%2C%20Expansion%2C%20and%20Parsing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnbnknltemq)) |
| __User information__ | __User information__ |
| `$HOME` | The user’s home directory. |
| `$UID` | The user’s ID.  __Security Warning:__This value can be modified by the calling script, so it should not be used for authentication purposes. |
| `$USER` | The user’s (short) login name.  __Security Warning:__This value can be modified by the calling script, so it should not be used for authentication purposes. |
| __Miscellaneous Variables__ | __Miscellaneous Variables__ |
| `$#` | Number of arguments passed to the shell. This variable is described further in [Handling Flags and Arguments](Result%20Codes%2C%20Chaining%2C%20and%20Flags.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnjnknltmmy). |
| `$@` | Complete list of arguments passed to the shell, separated by spaces.. This variable is described further in [Handling Flags and Arguments](Result%20Codes%2C%20Chaining%2C%20and%20Flags.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnjnknltmmy). |
| `$*` | Complete list of arguments passed to the shell, separated by the first character of the `IFS` (input field separators) variable. This variable is described further in [Handling Flags and Arguments](Result%20Codes%2C%20Chaining%2C%20and%20Flags.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denryfvbuqnjnknltmmy). |
| `$-` | A list of all shell flags currently enabled. |
| `$PWD` | The current working directory. Equivalent to executing the `pwd` command. |

[Next](Other%20Tools%20and%20Information.md)[Previous](Command%20Line%20Primer.md)

