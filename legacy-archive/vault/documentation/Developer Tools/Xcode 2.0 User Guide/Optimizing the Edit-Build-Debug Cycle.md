---
title: Xcode 2.0 User Guide
apple_id: TP40001440
resource_type: Guide
platform: Xcode Developer Tools
topic: null
technology: null
published: '2006-11-07'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/XcodeUserGuide20/Contents/Resources/en.lproj/bs_speed_up_build/bs_speed_up_build.html
archived_at: '2026-07-15T07:29:03.198150Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode 2.0 User Guide](Introduction%20to%20Xcode%202.0%20User%20Guide.md)


[Next](Using%20Cross-Development%20in%20Xcode.md)[Previous](Linking.md)

# Optimizing the Edit-Build-Debug Cycle

Xcode offers a number of features you can take
advantage of to decrease build time for your project. For example,
you can use distributed builds to shorten the time it takes to build
your whole project or multiple projects. ZeroLink and predictive
compilation, on the other hand, improve turnaround time for single
file changes, thereby speeding up the edit–build–debug cycle. All
of these features reduce the amount of time you spend idle while
waiting for your project to build.

This chapter describes the following features:

- Precompiled
  prefix headers let you decrease the amount of time spent building compiling
  each source file in a target by specifying a single header file
  that includes all of the headers commonly used by the target’s
  files and compiling this header a single time.
- Predictive compilation reduces the time required to compile
  single file changes by beginning to compile a file while you are
  still editing it.
- Distributed builds can dramatically reduce build time for
  large projects by distributing compiles to available machines on
  the network.

Other features that you can use to optimize the edit-build-debug
cycle include:

- Fix and Continue,
  described in [Using Fix and Continue](Using%20Fix%20and%20Continue.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrugqwugqkdjfduuskj), improves
  your debugging efficiency by allowing you to make changes to your
  application and see the results of your modification without stopping
  your debugging session.
- ZeroLink, described in [Using ZeroLink](Linking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinbqfvbuqmrtgmwugsceincuqrce), shortens build
  time by eliminating the linking step for development builds.

A precompiled header is a file in the intermediate form used
by the compiler to compile a source file. Using precompiled headers,
you can significantly reduce the amount of time spent building your
product. Often, many of the source code files in a target include
a subset of common system and project headers. For example, each
source file in a Cocoa application typically includes the `Cocoa.h` system
header, which in turn includes a number of other headers. When you
build a target, the compiler spends a great deal of time repeatedly
processing the same headers.

You can significantly reduce build time by providing a prefix
header that includes the set of common headers used by all or most
of the source code files in your target and having Xcode precompile
that prefix header.

If you have indicated that Xcode should do so, Xcode precompiles
the prefix header when you build the target. Xcode then includes
that precompiled header file for each of the target's source files.
The contents of the prefix header are compiled only once, resulting
in faster compilation of each source file. Furthermore, subsequent
builds of the target can use that same precompiled header, provided
that nothing in the prefix header or any of the files on which it
depends has changed. Each target can have only one prefix header.

When Xcode compiles your prefix header, it generates a variant
for each C language dialect used by your source files; it stores
these in a folder in your project’s build directory. It also generates—as
needed—a variant for each combination of source header and compiler
flags. For example, you may have per-file compiler flags set for
some of the files in your target. Xcode will create a variant of
the precompiled header by precompiling the prefix header with the
set of compiler flags derived from the target and the individual source
file. As Xcode invokes the compiler to process each source file
in your target, the compiler searches this directory for a precompiled
header variant matching the language and compiler flags for the
current compile. The first precompiled header variant that is valid
for the compilation is used.

Xcode automatically regenerates the precompiled header whenever
the prefix header, or any of the files it depends on are changed,
so you don't need to manually maintain the precompiled header.

To take advantage of precompiled headers in Xcode, you must
first create a prefix header. Create a header file containing any
common `#include` and `#define` statements
used by the files in your target.

Do not include anything that changes frequently in the prefix
header. Xcode recompiles your precompiled header file when the prefix
header, or any of the headers it includes, change. Each time the
precompiled header changes, all of the files in the target must
be recompiled. This can be an expensive operation for large projects.

Because the compiler includes the prefix header file before
compiling each source file in the target, the contents of the prefix
header must be compatible with each of the C language dialects used
in the target. For example, if your target uses Cocoa and contains
both Objective-C and C source files, the prefix header needs to
include the appropriate guard macros to make it compatible with
both language dialects, similar to the example shown here:

```objc
    #ifdef __OBJC__
    #import <Cocoa/Cocoa.h>
    #endif
    #define MY_CUSTOM_MACRO 1
    #include "MyCommonHeaderContainingPlainC.h"
```


Once you have created the prefix header, you need to set up
your target to precompile that header. To do this, you must provide
values for the two build settings described here. You can edit these
build settings in the Build pane of the target inspector or Info
window. The settings you need to change are:

- Prefix Header
  (GCC_PREFIX_HEADER). Change the value of this build setting to the project-relative
  path of the prefix header file. If you have a precompiled header
  file from an existing project, set the prefix header path to the
  path to that file.
- Precompile Prefix Header (GCC_PRECOMPILE_PREFIX_HEADER). Make
  sure that this option is turned on. A checkmark is present in the
  Value column if this option is enabled.

You must provide values for these settings in each target
that uses a precompiled prefix header, even if those targets use
the same prefix header.

By default, Xcode precompiles a version of the header for
each C-like language used by the target (C, C++, Objective-C, or
Objective-C++). The C Dialects to Precompile (GCC_PFE_FILE_C_DIALECTS)
build setting lets you explicitly specify the C dialects for which
Xcode should produce versions of the precompiled header.

It is possible to share a precompiled header binary across
multiple targets, provided that those targets use the same prefix
header and compiler options. In order to share a precompiled header
binary, each individual target must have the same prefix header specified.
To use the same prefix header for multiple targets, set the value
of the Prefix Header build setting for each target to the path to
the header.

The PRECOMP_DESTINATION_DIR build setting specifies the location
of the directory to which Xcode writes the precompiled header binary.
For each target, set this location to a common directory. When Xcode
invokes GCC to compile each source file in a target, GCC searches
this common directory for the appropriate header binary. For any
targets that use the same prefix header and compiler options, GCC
uses the same precompiled header binary when it builds those targets.

This build setting is not exposed in the Xcode user interface.
To change the value of this build setting, add a new entry in the
build settings table that appears in the Build pane of the target
inspector. Enter PRECOMP_DESTINATION_DIR as the name of the build setting
and enter the path to the directory you want to use for precompiled
binaries in the Value column for the build setting.

If you specify the same prefix header for multiple targets,
but do not specify a common location for the precompiled binary,
Xcode precompiles the prefix header once for each target as it is
built.

Xcode caches the precompiled header files that it generates.
To control the size of the cache devoted to storing those files,
use the `BuildSystemCacheSizeInMegabytes` user
default. In the Terminal application, type:

`defaults write com.apple.xcode BuildSystemCacheSizeInMegabytes` _defaultCacheSize_

Specifying 0 for the cache size gives you an unlimited cache.
200 MB is the default cache size set by Xcode. If the cache increases
beyond the default size, Xcode removes as many precompiled headers
as is necessary to reduce the cache to its default size when Xcode
is next launched. Xcode removes the oldest files first.

To take advantage of Xcode’s automatic support for precompiled
headers you must:

- Use GCC 3.3 or
  later. Xcode uses GCC 3.3’s PCH mechanism to create precompiled headers.
  PCH is not available with previous versions of GCC.
- Use a native target. Xcode’s automatic support for precompiled
  prefix headers using PCH is only available for targets that use
  Xcode’s own native build system. Xcode automatically handles many
  of the restrictions upon using precompiled headers with GCC. If
  you are using an external target to work with another build system—such
  as `make`—you can still
  use precompiled headers, but you must create and maintain them yourself.
  For more information on using precompiled headers with GCC, see _GNU C/C++/Objective-C Compiler_. Jam-based targets can also use precompiled prefix
  headers, but they are limited to the PFE (persistent front end)
  mechanism introduced with GCC 3.1. PFE is no longer recommended.
- Use one and only one prefix header per target.
- Set the Prefix Header and Precompile Prefix Header build settings
  for every target that uses precompiled headers.

Building a product involves many small operations. Many of
these operations—such as compiling source files—can be performed
in parallel, decreasing the total amount of time it takes to build
your product. If you have a dual-processor computer, Xcode automatically uses
both processors. However, the greater the number of processors available
to you, the greater the number of build tasks you can run in parallel. Distributed
builds give you the ability to distribute build tasks among multiple
computers on a network. When you use distributed builds, Xcode distributes
as many build operations as possible among the computers available
for that purpose.

Xcode uses `distcc` to
manage distributed builds. The `distcc` client
manages the setup and distribution of build tasks. The server process
(`distccd`) manages communication
with the remote computers hosting the build tasks. The server process
runs on both the local, or client, computer and on the remote computer.

When you initiate a build, Xcode invokes the `distcc` client
on your local computer. For each source module that needs to be
compiled, the client process connects to the server process running
on the local machine and gives it the information required to distribute that
task. Namely, the client process tells `distccd` the
operation to perform and gives it any necessary arguments, a list
of files to copy to the remote host (input files) and a list of
files to copy from the remote host (output files). The server process
broadcasts a work request for that operation. When an available
computer responds, `distccd` sends
the inputs to that computer. When the compile is complete and the
remote computer returns the results, `distccd` places
the output files in the appropriate locations in the file system
and returns the results to the client process.

On a remote computer accepting build operations, the server
process listens for requests for assistance. When it receives a
request, it creates a connection with the client computer, obtains
the inputs required for the compilation, and invokes `gcc`.
When the compile is complete, `distccd` sends
the results—the generated `.o` files, `stderr` and `stdout`—back
to the client computer.

If the attempt to distribute a build task fails—for example,
if communication with the remote host is lost, or the remote host
cannot execute the compile—the compilation is performed on your
local computer.

Xcode only distributes compilation of individual source modules.
Your local computer still performs all of the build setup, linking,
and product packaging. Preprocessing is also done on your local
computer; this is done to avoid the problem of ensuring that all machines
participating in a build have exactly the same version of all headers
used in the build. For each source file, the `distcc` client
invokes GCC to generate a `.i` file
containing the preprocessed source; this is the input file sent
to the remote host.

Computers that are shared respond to requests for assistance
as they are able. Xcode determines how best to use available machines
for a build, based on processing capacity. A computer’s processing
capacity is determined through a combination of availability and processing
power.

You can use precompiled headers with distributed builds. If
a precompiled header is present, the path to that header is listed
in the preprocessed file generated from each source file. Before
it sends a file to a remote computer, `distcc` checks
for this path and, if found, sends the precompiled header to the
remote computer.

Use of distributed builds is subject to the following constraints:

- You must
  use GCC 3.3 or later.
- Machines that tasks are distributed to must be running the
  same version of the compiler, operating system, and Xcode.
- Distributed builds work with native targets. Jam-based targets
  or targets using another external build system are not compatible
  with distributed builds.
- Distributed builds support C, C++, Objective-C and Objective-C++.
- Distributed builds are enabled on a per-user basis, for all
  projects and targets built by that user.

To enable distributed builds on your computer, choose Xcode >
Preferences and click Distributed Builds. To use other computers
on the network for your builds, select “Distribute builds to.”

Xcode uses Bonjour to automatically discover computers
that are set up to broadcast their availability. The Distributed
Builds preference pane lists the computers currently available for
sharing build tasks. Services discovered through Bonjour display
the Bonjour name of the computer on which `distccd` is
running.

By default, Xcode will use any computers that are available
when you begin a build. You can restrict which computers are used
by selecting “trusted computers only” from the “Distribute
builds to” menu. When you choose this option, Xcode distributes
builds only to computers that you explicitly designate as “trusted.”
A computer is trusted if the checkbox in the Trusted column next
to its entry is selected.

Each entry in the Distributed Builds preference pane represents
a single computer. However, shared computers with dual processors
run two instances of `distccd`,
each of which can accept build tasks. The Max Connections column
displays the number of processors of, and therefore the number of
possible connections with, each available computer.

Computers to which tasks are distributed to must be running
the same version of the compiler, operating system, and Xcode. The
Status column shows whether a shared computer is compatible or not.
If a computer goes to sleep, its services disappear from the preference
pane, and that computer is no longer available for performing compilations.

To allow other computers to use your computer for their builds, select
the “Share my computer for building with” option in the Distributed
Builds pane of the Xcode Preferences window and choose a priority
for sharing your computer from the menu.

Don’t share your computer if you are using it to host a
distributed build as well. Because precompilation and the distribution
of build tasks are done on your local machine, sharing it for others
to distribute build tasks to can significantly slow down your own
build.

To distribute builds across a firewall, the firewall must
allow traffic on ports `3632` and `7264`.
Some firewalls allow Bonjour traffic, making shared computers
behind the firewall visible in the Distributed Builds preference
pane. However, the distributed build will not work. When Xcode attempts
to distribute build tasks and receives no response from the computers
behind the firewall, it times out and builds the project on the
local machine.

To allow traffic on ports `3632` and `7264` on
computers with a firewall enabled, use the Firewall pane of Sharing
Preferences.

Using Xcode to distribute builds across multiple computers
can greatly decrease the time it takes to build your product. To
get the most benefit from using distributed builds, you should consider
the following:

- Networking
  speed. The distributed build system sends files to be built on other computers;
  those machines, in turn, send back the resulting object files. To
  see a significant reduction in build time, your network must be
  fast enough that the cost of transferring files between machines
  is minimal. This occurs around 100 Mbit/s (megabits per second).
  For this reason, using distributed builds over a wireless network does
  not show any build speed benefits.
- Number of available computers. As stated at the beginning
  of this article, the more processors you have available to you,
  the more build tasks can be performed in parallel and the more significant
  the reduction in build time that you see. If you have a limited number
  of computers available for sharing—especially if those computers
  do not have significant processing capacity, whether due to limited
  availability or slow processor speed—you may not see any noticeable
  improvements in build performance. The overhead of managing distribution
  of build tasks may overcome the benefit you get from building on
  additional machines. You may find that you get better build performance
  from utilizing other optimizations, such as precompiled headers
  or parallel builds, on your local computer.
- Differing processing capacity between the computers managing
  the build and those hosting the build tasks. If you have a number
  of different computers available to you, of varying speed, you will
  get better performance if you use the faster computers for building
  and the slower computer to manage the build and farm out build tasks.
  For example, if you have a G4 and a G5 available, on a fast network,
  host the project on the G4 and make the G5 available for shared
  builds.

Predictive compilation is a feature introduced to reduce the
time required to compile single file changes and speed up the edit-compile-debug
cycle of software development. If you have predictive compilation
enabled for your project, Xcode begins compiling the files required
to build the current target even before you tell Xcode to build.

Predictive compilation uses the information that Xcode maintains
about the build state of targets that use the native build system.
Xcode keeps the graph of all files involved in the build and their
dependencies, as well as a list of files that require updating.
At any point in time, Xcode knows which of the files used in building
a target’s product are out of date and what actions are required
to bring those files up to date. A file can be updated when all
of the other files on which it depends are up to date. As files
become available for processing, Xcode begins to update them in
the background, even as you edit your project.

Xcode will even begin compiling a source code file as you
are editing it. Xcode begins reading in and parsing headers, making
progress compiling the file even before you initiate a build. When
you do choose to save and build the file, much of the work has already
been done.

Until you explicitly initiate a build, Xcode does not commit
any of the output files to their standard location in the file system.
When you indicate that you are done editing, by invoking one of
the build commands, Xcode decides whether to keep or discard the
output files that it has generated in the background. If none of
the changes made subsequent to its generation affect the content
of a file, Xcode commits the file to its intended location in the file
system. Otherwise, Xcode discards its results and regenerates the
output file.

You can turn on predictive compilation by selecting “Use
Predictive Compilation” option in the Building pane of the Xcode
Preferences window.

Predictive compilation works only with GCC 3.3 or later and
native targets. All predictive compilation is done locally on your
computer, regardless of whether you have distributed builds enabled.
On slower machines, enabling predictive compilation may interfere
with Xcode performance during editing.

To conserve battery power, Xcode turns off predictive compilation
on laptop machines running under battery power.

[Next](Using%20Cross-Development%20in%20Xcode.md)[Previous](Linking.md)

