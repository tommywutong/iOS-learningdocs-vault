---
title: Audio Unit Validation Using the auval Tool
apple_id: DTS40007939
resource_type: Technical Note
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioUnit
published: '2008-09-08'
source_url: https://developer.apple.com/library/archive/technotes/tn2204/_index.html
archived_at: '2026-07-26T19:54:09.474263Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2204

# Audio Unit Validation Using the auval Tool

The `auval` command-line tool enables you to test the conformance of an audio unit to the behavior expected by applications that use Audio Unit Services.

__Important:__ The `auval` tool validates audio unit operational correctness and interface semantics. It does not assess audio unit implementation quality, nor does it test views (user interfaces).

[Usage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojthewugsbrfvjukq2ujfhu4mi)[The Validation Process](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojthewugsbrfvjukq2ujfhu4mq)[Debugging Options](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojthewugsbrfvjukq2ujfhu4my)[Testing for Memory Leaks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojthewugsbrfvjvkqstivbviskpjyzq)[Testing for Memory Smashers: Memory Scribble Test](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojthewugsbrfvjvkqstivbviskpjy2a)[Testing for Memory Smashers: Guard Malloc Test](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojthewugsbrfvjvkqstivbviskpjy2q)[Tips](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojthewugsbrfvjukq2ujfhu4ny)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydoojthewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Usage

You can run the `auval` tool from the command line as shown in listing 1.

__Listing 1__  Validating an audio unit

```
 [~] % auval -v TYPE SUBT MNFR
```

In listing 1, TYPE, SUBT, and MNFR represent four-character codes that uniquely identify an audio unit.

- TYPE - The component type, such as `aufx`
- SUBT - The component subtype, such as `hpas`
- MNFR - The manufacturer code, unique to a company. For example, the manufacturer code for Apple audio units is `appl`

For more information on audio unit identification, see [Audio Unit Programming Guide](../documentation/Music%20Audio/Audio%20Unit%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztenzyfvbuqmi).

Listing 2 shows the command to get a list of all audio units on a system that match a given component type.

__Listing 2__  Listing all audio units of a given type

```
 [~] % auval -s TYPE
```

To get a list of all installed audio units, enter the command shown in listing 3.

__Listing 3__  Listing all installed audio units

```
 [~] % auval -a
```

The `auval` tool has built-in help available. You access it as shown in listing 4.

__Listing 4__  Obtaining auval help

```
 [~] % auval -h
```

While executing, the `auval` tool may indicate one of two possible failure modes.

- ERROR - Indicates a condition that must be fixed
- WARNING - Indicates a condition that should be fixed

[Back to Top](#)

## The Validation Process

Audio unit validation proceeds in multiple phases, with each phase given a `* *PASS` or `* *FAIL` grade. A passing grade for a phase indicates no errors. After running the `auval` tool you can look for the following strings in the output:

1. VALIDATING AUDIO UNIT

   - Tests whether the component type matches one of Apple's specified audio unit types.
   - Tests whether the component manufacturer code has at least one uppercase letter, as is required.
2. TESTING OPEN TIMES

   - Tests both the cold and warm time to open the audio unit. Opening time should be kept to a minimum because it impacts the launch time and, therefore, the usability of host applications.
3. VERIFYING DEFAULT SCOPE FORMATS

   - Verifies the exported audio data formats of input and output buses. The default format for an audio unit should have a sample rate of 44100Hz and a channel configuration that the audio unit in fact supports.
4. VERIFYING REQUIRED PROPERTIES

   - Verifies that the audio unit implements all required properties, some of which can vary according to the type of audio unit.
5. VERIFYING RECOMMENDED PROPERTIES

   - Warns if the audio unit does not implement a property that is recommended for that type of audio unit.
6. VERIFYING OPTIONAL PROPERTIES

   - Verifies optional, Apple-defined properties of an audio unit, according to its type. Reports only on properties that are implemented and checks that they are implemented correctly.
7. VERIFYING SPECIAL PROPERTIES

   - Verifies the Class Information (persistence) property, checking that the audio unit specifies an appropriate data format for persistence.
   - If the audio unit indicates that it has a view, verifies that the view can be found and opened.

     __Important:__ The `auval` tool does not display an audio unit's user interface or perform any UI verification
   - Verifies that factory presets, if implemented, are handled and reported correctly.
8. PUBLISHED PARAMETER INFO

   - Verifies any parameter information exported by an audio unit.
9. FORMAT TESTS

   - Verifies that the audio unit can be set to the channel configurations it indicates it supports.
   - Verifies that the audio unit cannot be set to channel configurations it does not indicate support for.
10. RENDER TESTS

    - Performs rendering tests at various numbers of maximum frames-per-slice. This test sets the `MaxFramesPerSlice` property between rendering calls to verify that the audio unit correctly responds.
    - Tests the audio unit's response to an `AudioUnitReset` function call, and tests the audio unit's connection semantics.
    - Test the setting of both atomic and ramped parameters during rendering.

      __Important:__ This test validates rendering using the audio unit's default channel configuration. If the audio unit supports mono-to-mono rendering, this test validates rendering using that configuration as well.

[Back to Top](#)

## Debugging Options

You can use the `auval` tool to test your audio unit for memory leaks and potential memory smashers. Apple recommends three memory tests. Each requires you to define some environment variables. For more information on Malloc environment variables, see _[Malloc Debug Environment Variables Release Notes](../releasenotes/Developer%20Tools/Malloc%20Debug%20Environment%20Variables%20Release%20Notes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytamrw)_.

### Testing for Memory Leaks

Audio units should not leak memory. This section describes how to test for memory leaks.

1. To test for memory leaks in an audio unit, set the following environment variable:

   `export MallocStackLogging=1`
2. Execute the `auval` tool using the `w` and `q` switches. The `w` switch prevents `auval` from terminating. The `q` switch suppresses diagnostic output. You will see output similar to that shown in listing 5.

   __Listing 5__  Preparing to test for memory leaks

   ```
   [~] % auval -v aufx bpas appl -w -q sh(6261) malloc: recording malloc stacks to disk using standard recorder sh(6261) malloc: stack logs being written into /tmp/stack-logs.6261.sh.8jZkMX arch(6262) malloc: recording malloc stacks to disk using standard recorder arch(6262) malloc: stack logs being written into /tmp/stack-logs.6262.arch.0SVUSw auvaltool(6262) malloc: recording malloc stacks to disk using standard recorder auvaltool(6262) malloc: stack logs deleted from /tmp/stack-logs.6262.arch.0SVUSw auvaltool(6262) malloc: stack logs being written into /tmp/stack-logs.6262.auvaltool.ahETKI    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *          AU Validation Tool          Version: 1.2.1b3            Copyright 2003-2007, Apple, Inc. All Rights Reserved.           Specify -h (-help) for command options   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  -------------------------------------------------- VALIDATING AUDIO UNIT: 'aufx' - 'bpas' - 'appl' -------------------------------------------------- AU VALIDATION SUCCEEDED.
   ```
3. With the `-w` switch, `auval` does not terminate. In another shell, you then execute the `leaks` command (using the pid (process identifier) of the `auval` process you are testing. In the example you see in listing 6, the pid is `13425`. The `-q` switch suppresses printout from `auval`.

   __Listing 6__  Testing for memory leaks

   ```
   [~] % leaks 13425 Process 13425: 2780 nodes malloced for 471 KB Process 13425: 0 leaks for 0 total leaked bytes.
   ```
4. If your audio unit has memory leaks, the `leaks` tool prints out a stack log for each leak it detects.

### Testing for Memory Smashers: Memory Scribble Test

Audio units should not attempt to use memory that is not theirs. This section and the next describe how to test for out-of-bounds memory usage.

1. To perform memory scribble test on an audio unit, define the following two environment variables:

   `export MallocScribble=1`

   `export MallocGuardEdges=1`
2. Execute the `auval` tool using the `q` switch. You'll see something like the output shown in listing 7.

   __Listing 7__  Performing a memory scribble test

   ```
   [~] % auval -v aufx bpas appl -q sh(1294) malloc: protecting edges sh(1294) malloc: enabling scribbling to detect mods to free blocks arch(1295) malloc: protecting edges arch(1295) malloc: enabling scribbling to detect mods to free blocks auvaltool(1295) malloc: protecting edges auvaltool(1295) malloc: enabling scribbling to detect mods to free blocks    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *          AU Validation Tool          Version: 1.2.1b3            Copyright 2003-2007, Apple, Inc. All Rights Reserved.           Specify -h (-help) for command options   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  -------------------------------------------------- VALIDATING AUDIO UNIT: 'aufx' - 'bpas' - 'appl' -------------------------------------------------- AU VALIDATION SUCCEEDED.
   ```

   In this case we don't need to specify the `-w` option. We're using the `-q` option to suppress `auval` printing.
3. If your audio unit writes to memory beyond its bounds, it will crash. The stack trace of the crash will be located to the position where the the problem exists. The objective here of course is not to crash!

### Testing for Memory Smashers: Guard Malloc Test

1. To perform a Guard Malloc test on an audio unit, define the following three environment variables:

   `export DYLD_FORCE_FLAT_NAMESPACE=1`

   `export DYLD_INSERT_LIBRARIES=/usr/lib/libgmalloc.dylib`

   `export MALLOC_VECTOR_SIZE=1`

   __Note:__ In Mac OS X versions prior to 10.5, the MALLOC_ALTIVEC_SIZE variable was used instead of the MALLOC_VECTOR_SIZE variable.
2. Execute the `auval` tool using the `q` switch. You'll see something like the output shown in listing 8.

   __Listing 8__  Performing a Guard Malloc test

   ```
   [~] % auval -v aufx bpas appl -q GuardMalloc: Allocations will be placed on 16 byte boundaries. GuardMalloc: - Some buffer overruns may not be noticed. GuardMalloc: - Applications using vector instructions (e.g., SSE or Altivec) should work. GuardMalloc: GuardMalloc version 18 GuardMalloc: Allocations will be placed on 16 byte boundaries. GuardMalloc: - Some buffer overruns may not be noticed. GuardMalloc: - Applications using vector instructions (e.g., SSE or Altivec) should work. GuardMalloc: GuardMalloc version 18 GuardMalloc: Allocations will be placed on 16 byte boundaries. GuardMalloc: - Some buffer overruns may not be noticed. GuardMalloc: - Applications using vector instructions (e.g., SSE or Altivec) should work. GuardMalloc: GuardMalloc version 18    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *          AU Validation Tool          Version: 1.2.1b3            Copyright 2003-2007, Apple, Inc. All Rights Reserved.           Specify -h (-help) for command options   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  -------------------------------------------------- VALIDATING AUDIO UNIT: 'aufx' - 'bpas' - 'appl' -------------------------------------------------- AU VALIDATION SUCCEEDED.
   ```
3. If your audio unit fails the Guard Malloc test, it will crash. The stack trace of the crash will be located to the position where the the problem exists. The objective here of course is not to crash!
[Back to Top](#)

## Tips

1. For convenience, you can define these sets of debugging options as aliases for your shell. For the standard Mac OS X Bash shell, enter the lines shown in listing 9 in the `.profile` file in your home directory. Once in that file, these aliases are available to each Bash session you open.

   __Listing 9__  Defining shell aliases for memory tests

   ```
   alias	leaktest="export export MallocStackLogging=1"  alias 	scribbletest="export MallocScribble=1; export MallocGuardEdges=1;"  alias 	guardtest="export DYLD_FORCE_FLAT_NAMESPACE=1; export DYLD_INSERT_LIBRARIES=/usr/lib/libgmalloc.dylib;export MALLOC_VECTOR_SIZE=1;"
   ```

   __Note:__ In Mac OS X versions prior to 10.5, the MALLOC_ALTIVEC_SIZE variable was used instead of the MALLOC_VECTOR_SIZE variable.

   You then set the environment variables by entering the alias names. For example, before testing for leaks, you would enter the following command:

   ```
   [~] % leaktest
   ```
2. You can also perform these memory tests in a gdb session. To do this, first launch gdb. Then before executing the `auval` tool, on the gdb command line define these environment variables using the gdb `set env` command, as shown in listing 10.

   __Listing 10__  Using gdb to perform audio unit memory tests

   ```
   (gdb) set env MallocScribble 1 (gdb) r  Starting program: /usr/bin/auval  malloc[13448]: enabling scribbling to detect mods to free blocks Reading symbols for shared libraries +............... done malloc[13448]: enabling scribbling to detect mods to free blocks    * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *          AU Validation Tool          Version: 1.1.0b9           Copyright 2003-4, Apple Computer, Inc.           Specify -h (-help) for command options   * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *  Program exited normally. (gdb)
   ```

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-08 |  |
| 2008-08-21 | New document that test the conformance of audio units to Audio Unit Services. |

