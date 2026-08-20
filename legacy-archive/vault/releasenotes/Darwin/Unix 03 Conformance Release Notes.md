---
title: Unix 03 Conformance Release Notes
apple_id: TP40004772
resource_type: Release Note
platform: macOS
topic: Cross Platform
technology: null
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/releasenotes/Darwin/RN-Unix03Conformance/index.html
archived_at: '2026-07-18T02:50:23.388011Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# UNIX 03 Conformance Release Notes

#### Contents:

- [Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzsfvcg63tujruw422fnrsw2zlooreuixzr)
- [Conformance and Legacy Behavior](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzsfvcg63tujruw422fnrsw2zlooreuixzs)
- [Types of Compatibility Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzsfvcg63tujruw422fnrsw2zlooreuixzt)
- [Compile/Link Issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzsfvcg63tujruw422fnrsw2zlooreuixzu)
- [Command usage issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzsfvcg63tujruw422fnrsw2zlooreuixzv)
- [Execution issues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donzsfvcg63tujruw422fnrsw2zlooreuixzw)

### Introduction

In an effort to increase compatibility with other UNIX operating systems, Apple has made a significant effort in OS X v.10.5 to support the Single UNIX Specification Version 3 (SUSv3). Although Apple has attempted to minimize the impact of the changes involved, some of them will affect developers who work with UNIX APIs and commands.

The OS X kernel, libraries, and utilities are drawn from a number of Open Source projects, including FreeBSD, GNU, NetBSD, and OpenBSD. Although these projects make an effort to follow industry standards, none of them have the resources to engage in a formal certification process.

By performing this work for OS X, Apple benefits both its developers (who can now rely on well-defined interfaces and behavior) and the contributing Open Source projects (whose code and documentation can be updated to include Apple's changes).

Although Apple has attempted to make the process as seamless as possible, some conformance changes are simply incompatible with commands and APIs found on earlier versions of OS X. This document provides an overview of these incompatibilities, along with information on specific changes that are likely to be problematic.

### Conformance and Legacy Behavior

In most cases, the conformance tests can be passed by adding functionality, such as functions and command-line options, to the operating system. As this does not change existing behavior or interfaces, it will not affect current applications (and will not be addressed in this document). For portability, however, new or changed code should use conformant interfaces.

In some cases, the standard defines behavior that was left unspecified by existing documentation, such as manual pages). The tests look for this behavior. In most cases, the changes needed to pass the tests will not affect current applications. In cases where specific problems have been observed, this document discusses them.

In a relatively small number of cases, conformant interfaces or behavior actually conflict with that found in previous (legacy) versions of OS X. As discussed in the `compat(5)` manual page, OS X v.10.5 provides ways to approximate legacy behavior. Although this does not guarantee that current programs will "Just Work", it should minimize the number of coding changes.

### Types of Compatibility Issues

Existing compiled applications should not encounter problems in moving to OS X v.10.5. If a system call or library function is known to have new behavior, the new version will only be used with programs that have been compiled for use on OS X v.10.5. An existing executable will not "see" these versions and thus will not be affected by the changes.

If an application is recompiled for use on OS X v.10.5, it will get the new versions of libraries and system calls, unless a legacy target is specified (See Execution issues, below) .Some scripts, such as bash and perl scripts, may also encounter problems with commands whose options and/or behavior has changed. It is possible to request legacy behavior by setting the environment variable `COMMAND_MODE` to the value "`legacy`".

### Compile/Link Issues

The include files and/or prototypes for a number of library functions and system calls have changed. If a change seems likely to cause problems, the previous version or versions have been documented in the `LEGACY SYNOPSIS` section of the relevant manual page.

Although you should use conformant include files and prototypes where possible, the following macro:

```
#define _NONSTD_SOURCE
```

will frequently allow the legacy versions to be used. Again, see the `compat(5)` manual page for details.

The following manual pages currently have `LEGACY SYNOPSIS` sections:

- __System Calls:__

  - [killpg(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/killpg.2.html#//apple_ref/doc/man/2/killpg)
  - [pthread_kill(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/pthread_kill.2.html#//apple_ref/doc/man/2/pthread_kill)
  - [pthread_sigmask(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/pthread_sigmask.2.html#//apple_ref/doc/man/2/pthread_sigmask)
- __Library functions:__

  - [basename(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/basename.3.html#//apple_ref/doc/man/3/basename)
  - [bstring(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/bstring.3.html#//apple_ref/doc/man/3/bstring)
  - [crypt(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/crypt.3.html#//apple_ref/doc/man/3/crypt)
  - [dbm(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/dbm.3.html#//apple_ref/doc/man/3/dbm)
  - [directory(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/directory.3.html#//apple_ref/doc/man/3/directory)
  - [endgrent(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/endgrent.3.html#//apple_ref/doc/man/3/endgrent)
  - [fseek(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/fseek.3.html#//apple_ref/doc/man/3/fseek)
  - [ftime(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/ftime.3.html#//apple_ref/doc/man/3/ftime)
  - [ftok(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/ftok.3.html#//apple_ref/doc/man/3/ftok)
  - [ftw(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/ftw.3.html#//apple_ref/doc/man/3/ftw)
  - [gai_strerror(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/gai_strerror.3.html#//apple_ref/doc/man/3/gai_strerror)
  - [getaddrinfo(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getaddrinfo.3.html#//apple_ref/doc/man/3/getaddrinfo)
  - [getenv(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getenv.3.html#//apple_ref/doc/man/3/getenv)
  - [gethostbyname(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/gethostbyname.3.html#//apple_ref/doc/man/3/gethostbyname)
  - [getnameinfo(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getnameinfo.3.html#//apple_ref/doc/man/3/getnameinfo)
  - [getpwent(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/getpwent.3.html#//apple_ref/doc/man/3/getpwent)
  - [grantpt(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/grantpt.3.html#//apple_ref/doc/man/3/grantpt)
  - [inet(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/inet.3.html#//apple_ref/doc/man/3/inet)
  - [memory(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/memory.3.html#//apple_ref/doc/man/3/memory)
  - [mktemp(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/mktemp.3.html#//apple_ref/doc/man/3/mktemp)
  - [network(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/network.3.html#//apple_ref/doc/man/3/network)
  - [random(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/random.3.html#//apple_ref/doc/man/3/random)
  - [realpath(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/realpath.3.html#//apple_ref/doc/man/3/realpath)
  - [strtol(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/strtol.3.html#//apple_ref/doc/man/3/strtol)
  - [strtoul(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/strtoul.3.html#//apple_ref/doc/man/3/strtoul)
  - [swab(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/swab.3.html#//apple_ref/doc/man/3/swab)
  - [syslog(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/syslog.3.html#//apple_ref/doc/man/3/syslog)
  - [tcgetpgrp(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tcgetpgrp.3.html#//apple_ref/doc/man/3/tcgetpgrp)
  - [tcsetpgrp(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/tcsetpgrp.3.html#//apple_ref/doc/man/3/tcsetpgrp)
  - [wcstol(3)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/wcstol.3.html#//apple_ref/doc/man/3/wcstol)

### Command usage issues

If the options and/or behavior of a command have changed significantly, one or more `LEGACY` sections should document this fact. However, these sections are still very much "in progress" at this time.

The following commands respond to the COMMAND_MODE environment variable, as discussed in `compat(5)`:

- __awk__

  The `awk(1)` command honors several forms of extended regular expressions (i.e., `{n,m}`, `[[==]]`, and `[[..]]`). Legacy operation disables this behavior.
- __bash, sh__

  "`echo -n`" works in `bash(1)`, but not in `sh(1)`. In legacy operation, the `echo(1)` builtin also supports the option in `sh`. However, this requires that `sh` itself be run in legacy mode.

```
bash-3.1$ echo ===
===
bash-3.1$ echo -n ===
===bash-3.1$ COMMAND_MODE=legacy sh
sh-3.1$ echo -n ===
===sh-3.1$ exit
exit
bash-3.1$ sh
sh-3.1$ echo -n ===
-n ===
sh-3.1$ COMMAND_MODE=legacy sh -c 'echo -n ==='
===sh-3.1$
```

  Similar issues apply to the way `echo` treats "`\r`". The `printf(1)` command is the recommended way to handle newline and escape sequences.

  Existing scripts can be run in legacy mode, as:

```
COMMAND_MODE=legacy old_script arg ...
```

  However, this will cause the entire script (and any commands it runs) to operate in legacy mode (generally, like OS X v.10.4 would).
- __chown__

  If the `chown(8)` command when invoked as "chown -RP ..." encounters a symbolic link, the user ID of the symlink itself is modified. Legacy operation disables this behavior.
- __cp__

  The `-i` option to `cp(1)` disables `-f`. In legacy operation, the `-f` and `-i` options cannot be used together.

  The `-f` option specifies new access rights for any target file. Legacy operation disables this behavior, retaining the original access rights of any preexisting target file.

  With the `-R` option, a copying error for an individual file will cause the entire copy to terminate. In legacy operation, copying will continue despite errors..
- __crontab__

  If given no arguments, this command reads from stdin. In legacy operation, this command format is not allowed.
- __date__

  In legacy operation, the following exit values are returned:

  - `0`—The date was written successfully
  - `1`—Unable to set the date
  - `2`—Able to set the local date, but unable to set it globally
- __df__

  The `-t` option is normally a no-op (the total allocated-space figures are printed, by default). However, if used with an argument (e.g., "`-t hfs`", it acts like `-T`, but this usage is deprecated and should not be relied upon. In legacy operation, `-t` acts like `-T`.

  The "capacity" percentage is rounded up to the next higher integer. In legacy operation, it is rounded down to the next lower integer.

  The default block size is 512 bytes. This may be overridden by the `BLOCKSIZE` environment variable. The `-b`, `-g`, `-k`, `-m`, and `-P` options will override both the default and any `BLOCKSIZE` specification. In legacy operation, the default block size is 1024 bytes. So (unless `BLOCKSIZE` is specified), the `-k` option is a no-op and the `-b` and `-P` options actually force the use of 512-byte blocks.
- __du__

  Any combination of `-[LHP]` options can be specified. The last one encountered determines the command's behavior. In legacy operation, only one of these options may be specified.

  The command will detect and report a `SYMLOOP` error (loop involving symbolic links). In legacy operation, this is not the case.
- __ex, vi, view, vim__

  The -w option sets the default window size value for scrolling. In legacy operation, it defines a "scriptout" file.

  A number of the internal commands change (mostly in minor ways) when the commands are used in legacy operation.
- __file__

  The `-i` option means "if the file is a regular file, do not classify its contents. In legacy operation, `-i` and `--mime` cause the file command to output mime type strings, rather than the more traditional human readable ones.

  The `-r` and `--raw` options are no-ops. In legacy operation, these prevent the file command from translating unprintable characters to their octal representations.
- __grep__

  The caret (beginning of line) meta-character can never be matched in any location other than the beginning of the line. In `-E` mode, grep will print an error message and abort on certain cases of this usage (e.g., "`^^*`", "`^^+`", "`^^?`"). In legacy operation, the nonsense usage is allowed to fail (i.e., match nothing) silently.
- __join__

  The `-e` option causes a specified string to be substituted into empty fields, even if they are in the middle of a line. In legacy operation, the substitution only takes place at the end of a line.

  Only documented options are allowed. In legacy operation, some obsolete options are re-written into current options.
- __less, more__

  In the `more(1)` command, the `-n` option specifies the number of lines per screenful. In legacy operation, or when the command is invoked as `less(1)`, `-n` is used to suppress line numbering.

  In the `more` command, the `-p` option is used to specify commands (e.g., `:p`) for each new screenful of text. In legacy operation, or when invoked as `less`, the `-p` flag specifies a search pattern.
- __ls__

  When `-H` is specified (and not overridden by `-L` or `-P`) and a file argument is a symlink that resolves to a non-directory file, the output will reflect the nature of the link, rather than that of the file. In legacy operation, the output will describe the file.

  The `-f` option turns on the `-a` option (show files whose names have a period (`.`) as the first character). In legacy operation, it does not.

  The `-o` option causes the listing to be in long format, but to omit the group id. In legacy operation, the `-o` option modifies the `-l` option, causing file flags to be listed.

  The `-g`, `-n`, and `-o` options turn on the `-l` option (causing the listing to be in long format). In legacy operation, they do not.
- __mkfifo__

  The `-m` option sets the created FIFO to the specified mode. In legacy operation, the specified mode is masked with `0666`.
- __mv__

  The command "`mv dir/afile dir`" will abort with an error message. In legacy operation, it will fail silently with an exit code of `0`.
- __pr__

  The last space before the tab stop is replaced with a tab character. In legacy operation, it is not.
- __ps__

  The biggest change is in the interpretation of the `-u` option, which now displays processes belonging to the specified username(s). Thus, "`ps -aux`" will fail (unless you want to know about user "`x`"). As a convenience, however, "`ps aux`" still works as it did in OS X v.10.4.

  In legacy operation, ps has the following differences:

  - `-e` Display the environment as well. Same as `-E`.
  - `-g` Ignored for compatibility. Takes no argument.
  - `-l` Display information associated with the following keywords: `uid`, `pid`, `ppid`, `cpu`, `pri`, `nice`, `vsz`, `rss`, `wchan`, `state`, `tt`, `time`, and `command`.
  - `-u` Display information associated with the following keywords: `user`, `pid`, `%cpu`, `%mem`, `vsz`, `rss`, `tt`, `state`, `start`, `time`, and `command`.

    The `-u` option implies the `-r` option.
- __sed__

  Warnings are not generated for unused labels. In legacy operation, they are.

  When the `y` function is specified (for example, `sed y/string1/string2/`), doubled backslashes are not converted to single ones. In legacy operation, they are. To avoid this issue, use the `s` function instead.
- __sort__

  The form `sort +POS1 -POS2 ...` is no longer supported. For example:

```
bash-3.1$ cat data
b  a
a  b

bash-3.1$ sort data
a  b
b  a

bash-3.1$ sort +1 -2 data
sort: invalid option -- 2
Try `sort --help' for more information.
```

  The form `sort -k POS1,POS2` can be used to achieve the same effect, but note that the field and character positions are numbered starting with 1 (rather than 0). For example:

```
bash-3.1$ sort -k 2,3 data
b  a
a  b
```

  The options are not supported even in legacy operation, but they can be used by means of the following workaround:

```
bash-3.1$ _POSIX2_VERSION=200111 sort +1 -2 data
b  a
a  b
```
- __stty__

  The `bs[01]`, `cr[0-3]`, `ff[01]`, `nl[01]`, `tab[0-3]`, and `vt[01]` control modes are accepted, as well as `ocrnl`, `ofdel`, `ofill`, `onlret`, and `onocr` (along with their inverses, such as `-ocrnl`). In legacy operation, these modes are not accepted.
- __uudecode, uuencode__

  In legacy operation, `uudecode(1)` masks file modes with `0666`, preventing the creation of executable files.

  `uudecode` cannot change the mode of a created file which is not owned by the current user (unless that user is `root`). In legacy operation, [fchmod(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/fchmod.2.html#//apple_ref/doc/man/2/fchmod) allows the mode to be changed.
- __who__

  The `-u` option causes the `who(1)` command to display the process id (pid). In legacy operation, it does not.
- __xargs__

  In legacy operation, the `-L` option treats all newlines as end-of-line, regardless of whether the line is empty or ends with a space. In addition, the `-L` and `-n` options are not mutually-exclusive.

### Execution issues

SUSv3 requires a number of error checks that the OS X kernel has not made in the past. As a result, unexpected errno values may be encountered. Because specific reason(s) for most of these values have not yet been documented in the relevant manual pages, your best resource is the [intro(2)](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/intro.2.html#//apple_ref/doc/man/2/intro) manual page, which supplies general explanations for errno values.

Although some C-language calls now check for error conditions that they didn't under OS X v.10.4, commands and applications compiled for earlier releases of OS X (e.g., OS X v.10.4, OS X v.10.3) will not be affected. The changes take effect only if the programs are recompiled on OS X v10.5 (or greater) with a deployment target of OS X v10.5 (or greater).

The deployment target can be set in at least two ways. One way is to set an environment variable. For example, in `bash(1)`, this would look like this:

```
export MACOSX_DEPLOYMENT_TARGET=10.5   # Build for use on OS X v.10.5
export MACOSX_DEPLOYMENT_TARGET=10.4   # Build for use on OS X v.10.4
export MACOSX_DEPLOYMENT_TARGET=10.3   # Build for use on OS X v.10.3
```

Alternatively, the target can be passed to the compiler as a command-line option, as shown here:

```
gcc -mmacosx-version-min=10.5 ...      # Build for use on OS X v.10.5
gcc -mmacosx-version-min=10.4 ...      # Build for use on OS X v.10.4
gcc -mmacosx-version-min=10.3 ...      # Build for use on OS X v.10.3
```
