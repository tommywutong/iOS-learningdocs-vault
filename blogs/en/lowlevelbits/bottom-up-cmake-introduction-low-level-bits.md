---
title: Bottom-up CMake introduction - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/bottom-up-cmake-introduction/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d06ad91fee677543'
translated: false
---

> 原文：[Bottom-up CMake introduction - Low Level Bits 🇺🇦](https://lowlevelbits.org/bottom-up-cmake-introduction/)　·　Low Level Bits (Alex Denisov)

# Bottom-up CMake introduction

_Published on May 24, 2019_

If you want to learn CMake, but do not have time to go through all the resources on the internet, then this article is for you. I will cover essentials you’ll need to start:

- targets
- commands
- variables
- functions
- macros

In the next few minutes, we will reimplement some CMake’s builtin functionality using the CMake itself.

**Disclaimer:** there are several very inaccurate statements about CMake in this article. Most of them are here on purpose: the goal is to build an intuition of how CMake works, not to be 100% correct.

### What is CMake?

CMake is not a build system as many think of it. CMake is a _build system generator_. Basically, you can see it as a compiler that compiles CMake scripts into Makefiles. Or several other build systems including [Ninja](https://ninja-build.org) and Xcode, Eclipse, and Visual Studio projects.

![](https://lowlevelbits.org/img/bottom-up-cmake/cmake-compiler.png)

The typical workflow is as follows: you create a `CMakeLists.txt` (can be empty), you generate the build system, you build something. Here is the code:

```bash
> touch CMakeLists.txt
> cmake .
> make help
```

This is the bare minimum you need to start. Now let’s learn some CMake concepts.

### Targets

All the work in CMake is organized around **targets**. A **target** is something you can _build_ or _call_.

#### Target calls

Create a `CMakeLists.txt` with the following content:

```cmake
add_custom_target(hello-target
                  COMMAND cmake -E echo "Hello, CMake World")
```

And run the following commands:

```bash
> cmake .
< truncated >
-- Configuring done
-- Generating done

> make hello-target
Scanning dependencies of target hello-target
Hello, CMake World
Built target hello-target
```

Here, the `make` tells us that it has built the target `hello-target`, even though it just called `echo` command and did not produce any artifacts.

#### Build targets

Let’s fix that and actually build some simple program. Create the following files:

```c
// main.c

extern void hello_world();

int main() {
  hello_world();
  return 0;
}
```

```c
// hello.c
extern int printf(const char *, ...);

void hello_world() {
  printf("Hello, CMake world\n");
}
```

Replace the custom target COMMAND:

```cmake
add_custom_target(hello-target
                  COMMAND gcc main.c hello.c -o hello)
```

And re-run `make`:

```bash
> make hello-target
< truncated >
-- Configuring done
-- Generating done
Built target hello-target
```

As you can see `make` detected the change and reconfigured CMake. If everything is right, you should have the `hello` executable:

```bash
> ./hello
Hello, CMake world
```

Great success!!!

### Commands

In fact, you can describe the whole build process using the custom target as we did above. The problem is, however, that the command will re-run every time whenever you run `make hello-target`: the `hello` program will be re-compiled completely even when nothing has changed.

Let’s use separate **commands** to solve this problem. The new version of `CMakeLists.txt`:

```cmake
add_custom_command(OUTPUT hello.o
                   COMMAND gcc -c hello.c
                   DEPENDS hello.c)
add_custom_command(OUTPUT main.o
                   COMMAND gcc -c main.c
                   DEPENDS main.c)

add_custom_target(hello-target
                  COMMAND gcc main.o hello.o -o hello
                  DEPENDS main.o hello.o)
```

The important point here is the `DEPENDS`. This construct describes the build process in the form of a (direct acyclic) graph: A depends on B, B depends on C and D, and so forth. Then, a change of D or C means that B is changed, which means that A is also changed, and therefore, all the changed items should be re-created.

Now try the following: build the program, add some change to one of the files, re-run the build twice, you should see something like this:

```bash
> make hello-target
[ 50%] Generating hello.o
[100%] Generating main.o
[100%] Built target hello-target
# Add small change to hello.c
> make hello-target
[ 50%] Generating hello.o
[100%] Built target hello-target
> make hello-target
[100%] Built target hello-target
```

We’ve just got **incremental compilation**, yay!

### Variables

It is time to do some refactoring: I’m more of a `clang` person than `gcc`, and therefore I want an easier way to change the compiler. Let’s extract it into a separate variable.

Definition of a variable is as easy as `set (FOO bar)` call, that defines a variable `FOO` with value `bar`. The usage is also straightforward: `${FOO}` becomes `bar` when executed.

Here is how a better version of `CMakeLists.txt` looks like:

```cmake
set (C_COMPILER gcc)

add_custom_command(OUTPUT hello.o
                   COMMAND ${C_COMPILER} -c hello.c
                   DEPENDS hello.c)
add_custom_command(OUTPUT main.o
                   COMMAND ${C_COMPILER} -c main.c
                   DEPENDS main.c)

add_custom_target(hello-target
                  COMMAND ${C_COMPILER} main.o hello.o -o hello
                  DEPENDS main.o hello.o)
```

The variable definition can be recursive. Try to add the following code to the CMake script:

```cmake
set (NUMBERS 1)
message(${NUMBERS})
set (NUMBERS ${NUMBERS} 2)
message(${NUMBERS})
set (NUMBERS ${NUMBERS} 3)
message(${NUMBERS})
set (NUMBERS 0 ${NUMBERS})
message(${NUMBERS})
```

And re-run `cmake .` to see this in action:

```bash
> cmake .
1
12
123
0123
```

### Functions

In CMake, everything is a function!

```cmake
set (FOO bar)
```

`set` is a function that takes two arguments.

```cmake
if(CMAKE_SYSTEM_NAME STREQUAL Linux)
  # ...
else()
  # ...
endif()
```

`if`, `else`, and `endif` are functions.

`add_custom_target` and `add_custom_command` are also functions.

Let’s create our own function and hide all the intricacies of our CMake script:

```cmake
set (C_COMPILER gcc)

function(create_executable name)
  add_custom_command(OUTPUT hello.o
                     COMMAND ${C_COMPILER} -c hello.c
                     DEPENDS hello.c)
  add_custom_command(OUTPUT main.o
                     COMMAND ${C_COMPILER} -c main.c
                     DEPENDS main.c)

  add_custom_target(${name}
                    COMMAND ${C_COMPILER} main.o hello.o -o hello
                    DEPENDS main.o hello.o)
endfunction()

create_executable(hello-target)
```

_Fun fact: `function` and `endfunction` are also functions._

The function is now reusable, but quite useless since the source files are hardcoded. Let’s go a bit deeper and fix this issue.

### Macros

In CMake, everything is a function! Except for macros.

Macros are like functions, with one exception: they are inlined whenever they called. We can extract compilation into the macro:

```cmake
macro(compile source_file)
  get_filename_component(output_file ${source_file} NAME_WE)
  set (output_file ${output_file}.o)
  add_custom_command(OUTPUT ${output_file}
                     COMMAND ${C_COMPILER} -c ${source_file}
                     DEPENDS ${source_file})
endmacro()
```

The macro uses `get_filename_component` to cut the extension from the input source file and constructs the output file name: `main.c -> main.o`.

Now we can use this macro:

```cmake
function(create_executable name)
  compile(hello.c)
  set (output_files ${output_file})

  compile(main.c)
  set (output_files ${output_files} ${output_file})

  add_custom_target(${name}
                    COMMAND ${C_COMPILER} ${output_files} -o hello
                    DEPENDS ${output_files})
endfunction()
```

The code looks a bit cleaner now, but there is at least one part that may look confusing: `set (output_files ${output_file})`. Since the body of a macro is inlined, we can rewrite this function like this (just for illustration):

```cmake
function(create_executable name)
  get_filename_component(output_file hello.c NAME_WE)
  set (output_file ${output_file}.o)
  add_custom_command(OUTPUT ${output_file}
                     COMMAND ${C_COMPILER} -c hello.c
                     DEPENDS hello.c)
  set (output_files ${output_file})

  get_filename_component(output_file main.c NAME_WE)
  set (output_file ${output_file}.o)
  add_custom_command(OUTPUT ${output_file}
                     COMMAND ${C_COMPILER} -c main.c
                     DEPENDS main.c)
  set (output_files ${output_files} ${output_file})

  add_custom_target(${name}
                    COMMAND ${C_COMPILER} ${output_files} -o hello
                    DEPENDS ${output_files})
endfunction()
```

So basically, we reuse the variable `output_file`. We can use it to construct the list of object files for the custom target. I hope it is clearer now.

### Loops

It obviously follows (c) that we can use a loop to handle a variable amount of source files passed to this function:

```cmake
function(create_executable name)
  foreach(file ${ARGN})
    compile(${file})
    set (output_files ${output_files} ${output_file})
  endforeach()

  add_custom_target(${name}
                    COMMAND ${C_COMPILER} ${output_files} -o hello
                    DEPENDS ${output_files})
endfunction()

create_executable(hello-target main.c hello.c)
```

Here we iterate over passed source files (`main.c`, `hello.c`) stored in the `ARGN` variable, and accumulate all the intermediate files in `output_files`.

### Final touches

I added three more things to the final version:

- I added another variable `C_FLAGS` that stores some additional compile flags one may need
- the name of the executable passed as a separate argument
- extracted the linking phase into a separate command

```cmake
set (C_COMPILER gcc)
set (C_FLAGS -g -O0)

macro(compile source_file)
  get_filename_component(output_file ${source_file} NAME_WE)
  set (output_file ${output_file}.o)
  add_custom_command(OUTPUT ${output_file}
                     COMMAND ${C_COMPILER} ${C_FLAGS} -c ${source_file}
                     DEPENDS ${source_file})
endmacro()

function(create_executable name exe)
  foreach(file ${ARGN})
    compile(${file})
    set (output_files ${output_files} ${output_file})
  endforeach()

  add_custom_command(OUTPUT ${exe}
                     COMMAND ${C_COMPILER} ${output_files} -o ${exe}
                     DEPENDS ${output_files})

  add_custom_target(${name} DEPENDS ${exe})
endfunction()

create_executable(hello-target hello main.c hello.c)
```

Give it another try:

```bash
> cmake .
> make hello-target
> ./hello
Hello, CMake world!
```

### Conclusion

We’ve just replicated (limited) version of CMake’s [`add_executable`](https://cmake.org/cmake/help/latest/command/add_executable.html) functionality.

Here is the version you would use if you didn’t know how to build the thing on your own:

```cmake
set (CMAKE_C_COMPILER gcc)
set (CMAKE_C_FLAGS -g -O0)

add_executable(hello main.c hello.c)
```

### What’s next?

Go and learn about other CMake [functions](https://cmake.org/cmake/help/latest/manual/cmake-commands.7.html) (that are confusingly called _commands_), you are ready now!

I would highly recommend learning about the following concepts:

- [add_subdirectory](https://cmake.org/cmake/help/latest/command/add_subdirectory.html)
- [include](https://cmake.org/cmake/help/latest/command/include.html)
- [properties](https://cmake.org/cmake/help/latest/manual/cmake-properties.7.html)

    - [get_property](https://cmake.org/cmake/help/latest/command/get_property.html)
    - [set_property](https://cmake.org/cmake/help/latest/command/set_property.html)
- [All the rest](https://cmake.org/cmake/help/latest/index.html)
