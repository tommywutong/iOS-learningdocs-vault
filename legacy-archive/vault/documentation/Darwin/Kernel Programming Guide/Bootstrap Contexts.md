---
title: Kernel Programming Guide
apple_id: TP30000905
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2013-08-08'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KernelProgramming/contexts/contexts.html
archived_at: '2026-07-15T07:23:13.750281Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Kernel Programming Guide](About%20This%20Document.md)


[Next](I-O%20Kit%20Overview.md)[Previous](Mach%20Scheduling%20and%20Thread%20Interfaces.md)

# Bootstrap Contexts

In OS X kernel programming, the term context
has several meanings that appear similar on the surface, but differ
subtly.

First, the term context can refer to a BSD process or Mach
task. Switching from one process to another is often referred to
as a context switch.

Second, context can refer to the part of the operating system
in which your code resides. Examples of this include thread contexts,
the interrupt context, the kernel context, an application’s context,
a Carbon File Manager context, and so on. Even for this use of the term,
the exact meaning depends, ironically, on the context in which the
term is used.

Finally, context can refer to a _bootstrap context_.
In Mach, the bootstrap task is
assigned responsibility for looking up requests for Mach ports.
As part of this effort, each Mach task is registered in one of two
groups—either in the startup context or a user’s login
context. (In
theory, Mach can support any number of independent contexts, however
the use of additional contexts is beyond the scope of this document.)

For the purposes of this chapter, the term context refers
to a bootstrap context.

When OS X first boots, there is only the top-level context,
which is generally referred to as the startup context. All other
contexts are subsets of this context. Basic system services that
rely on Mach ports must be started in this context in order to work
properly.

When a user logs in, the bootstrap task creates a new context
called the login context. Programs run by the user are started in
the login context. This allows the user to run a program that provides
an alternate port lookup mechanism if desired, causing that user’s tasks
to get a different port when the tasks look up a basic service.
This has the effect of replacing that service with a user-defined
version in a way that changes what the user’s tasks see, but does
not affect any of the rest of the system.

To avoid wasting memory, currently the login context is destroyed
when the user logs out (or shortly thereafter). This behavior may
change in the future, however. In the current implementation, programs
started by the user will no longer be able to look up Mach ports after
logout. If a program does not need to do any port lookup, it will
not be affected. Other programs will terminate, hang, or behave
erratically.

For example, in Mac OS 10.1 and earlier, `sshd` continues
to function when started from a user context. However, since it
is unable to communicate with `lookupd` or `netinfo`,
it stops accepting passwords. This is not a particularly useful
behavior.

Other programs such as `esound`, however,
continue to work correctly after logout when started from a user
context. Other programs behave correctly in their default configuration but
fail in other configurations—for example, when authentication
support is enabled.

There are no hard and fast rules for which programs will continue
to operate after their bootstrap context is destroyed. Only thorough
testing can tell you whether any given program will misbehave if
started from a user context, since even programs that do not appear
to directly use Mach communication may still do so indirectly.

In OS X v10.2, a great deal of effort has gone into making
sure that programs that use only standard BSD services and functions
do not use Mach lookups in a way that would fail if started from
a user context. If you find an application that breaks when started
from a Terminal.app window, please file a bug report.

From the perspective of a user, contexts are generally unimportant
as long as they do not want a program to survive past the end of
their login session.

Contexts do become a problem for the administrator, however.
For example, if the administrator upgrades `sshd` by
killing the old version, starting the new one, and logging out,
strange things could happen since the context in which `sshd` was
running no longer exists.

Contexts also pose an issue for users running background jobs
with `nohup` or users detaching terminal sessions
using `screen`. There are times when it is perfectly
reasonable for a program to survive past logout, but by default,
this does not occur.

There are three basic ways that a user can get around this.
In the case of daemons, they can modify the startup scripts to start
the application. On restart, the application will be started in
the startup context. This is not very practical if the computer
in question is in heavy use, however. Fortunately, there are other
ways to start services in a startup context.

The second way to run a service in the startup context is
to use `ssh` to connect to the computer. Since `sshd` is
running in the startup context, programs started from an `ssh` session
also register themselves in the startup context. (Note that a user
can safely kill the main `sshd` process without
being logged out. The user just needs to be careful to kill the right
one.)

The third way is to log in as the console user (`>console`),
which causes `LoginWindow` to exit and causes `init` to
spawn a `getty` process on the console. Since `init` spawns `getty`,
which spawns `login`, which spawns the user’s
shell, any programs started from the text console will be in the
startup context.

More generally, any process that is the child of a process
in the startup context (other than those inherited by `init` because
their parent process exited) is automatically in the startup context.
Any process that is the child of a process in the login context
is, itself, in the login context. This means that daemons can safely
fork children at any time and those children will be in the startup
context, as will programs started from the console (not the Console application).
This also means that any program started by a user in a terminal
window, from Finder, from the Dock, and so on, will be in the currently
logged in user’s login context, even if that user runs the application
using `su` or `sudo`.

If you are writing _only_ kernel code,
contexts are largely irrelevant (unless you are creating a new context,
of course). However, kernel developers frequently need to write
a program that registers itself in the startup context in order
to provide some level of driver communication. For example, you
could write a user-space daemon that brokers configuration information
for a sound driver based on which user is logged in at the time.

In the most general case, the problem of starting an application
in the startup context can be solved by creating a startup script
for your daemon, which causes it to be run in the startup context
after the next reboot. However, users generally do not appreciate
having to reboot their computers to install a new driver. Asking
the user to connect to his or her own computer with `ssh` to
execute a script is probably not reasonable, either.

The biggest problem with forcing a reboot, of course, is that
users often install several programs at once. Rebooting between
each install inconveniences the end user, and has no other benefit.
For that reason, you should not force the user to restart. Instead,
you should offer the user the option, noting that the software may
not work correctly until the user restarts. While this does not
solve the fundamental problem, it does at least minimize the most
common source of complaints.

There are a number of ways to force a program to start in
the startup context without rebooting or using `ssh`.
However, these are not robust solutions, and are not recommended.
A standard API for starting daemons is under consideration. When
an official API becomes available, this chapter will be updated
to discuss it.

[Next](I-O%20Kit%20Overview.md)[Previous](Mach%20Scheduling%20and%20Thread%20Interfaces.md)

