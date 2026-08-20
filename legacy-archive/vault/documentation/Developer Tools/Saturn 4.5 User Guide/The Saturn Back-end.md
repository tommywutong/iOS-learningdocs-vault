---
title: Saturn 4.5 User Guide
apple_id: TP40005157
resource_type: Guide
platform: macOS
topic: Xcode
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/SaturnUserGuide/TheSaturnBack-end/TheSaturnBack-end.html
archived_at: '2026-07-15T07:25:26.166107Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Saturn 4.5 User Guide](Overview.md)


[Next](Document%20Revision%20History.md)[Previous](The%20Saturn%20Front-end.md)

# The Saturn Back-end

The Saturn back-end is a dynamic library that is _linked_ with the application under study. It is invoked by your application during function prologues and epilogues in order to produce the profile traces used by the Saturn front-end application.

After the back-end is linked with your application, it will automatically produce one or more Saturn profile files in the active each time your application is executed. The output file name format is: “{app name}`.`{thread #}`.sat`”. Because each execution of your application can create many different profile files, one for each thread, Saturn creates a new directory in your working directory and names it “`Saturn_profile_`{app name}`_`{run number}” to collect all of the separate profiles together. In this name, the run number starts at 0 and is incremented each time you run your program, if you take several profiles in succession.

Most of the time, this library will work for you with very little intervention. However, in case of problems or if you desire more precise control over your profiling then you may need to control it more directly. This chapter discusses some issues that may occur when linking the back-end to your application and some ways that you can control the back-end to get more control over how it profiles your application.

As mentioned in the [Overview](Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnjxfvbuqmjnknltc), there are two ways to use the back-end to generate the data files for the front-end:

- `-finstrument-functions`— Saturn typically takes advantage of the infrastructure that GCC provides through the `-finstrument-functions` option. This option works with both PowerPC _and_ Intel-based Macs. You can type this option right into your GCC command lines. With Xcode, you will need to enter it as a string into the “Other C Flags” line in your target’s build settings, because Xcode does not have pre-made setting that you can check for this option.

  When program source is compiled by GCC with this flag, GCC adds a __prologue__ function call at each routine entry point, in each module compiled. GCC also adds an __epilogue__ function call to each routine in every module, before the routine returns. The prologue and epilogue functions that Saturn attaches to your application emit an entry for a Saturn document file (`*.sat` format). These two functions are included in the Saturn back-end dynamic library called `libSaturn.dylib`. To link to the library, either add the file `/usr/lib/libSaturn.dylib` to your Xcode project (when adding this “framework,” you will need to use _Command-Shift-G_ in the _Open file..._ dialog in order to access the `/usr/lib` folder, which is otherwise hidden) or add `-lSaturn` to the link command in a makefile.
- `-pg`— This profiling option, which works on PowerPC-based Macs only, causes `gcc` to use its _gprof_ profiling technique. Saturn can read the resulting `gmon.out` files and display the profiling results in a manner similar to the command-line `gprof` tool.

  When using this method, you do not have to make any other modifications to your source code or compiler/linker options. The whole program will be instrumented with just the `-pg` option. You also do not have to link against any special libraries.

  Apple supplies libraries already compiled with the `-pg` option enabled, so they may be profiled when linked with your `-pg` binary. However, by default libraries without `-pg` are used. To select the profiling versions of the libraries, set the environment variable `DYLD_IMAGE_SUFFIX` to “`_profile`” before running your application.

So which option should you use? In general, the `-finstrument-functions` option is the better choice. While it can incur somewhat more overhead than the `-pg` one, it allows Saturn to record more types of information. To be precise, it captures more callstack timing information, which allows Saturn to display its full callstack graph. Without this information, Saturn can present only summary statistics. Moreover, if you are on an Intel-based Mac, this is the only option that you can use.

If you link with the Saturn dynamic library, you can set the following environment variables in your shell, before starting your application, in order to easily control several options:

- `SATURN_WORKING_DIR`— Set this to the path of the directory where you want to store the Saturn data files. Absolute paths are generally best; relative paths will be resolved relative to the current working directory of the shell that invokes the application being profiled.
- `PROFILE_SIZE_LIMIT`— This parameter, when supplied, forces the back-end to limit the size of the data files produced to a fixed limit, expressed here in bytes. If this limit is reached, profiling stops immediately. It is a good way to make sure that your application does not accidentally fill up your entire disk with profile data, a factor that is especially important if you are writing profile data to your Mac OS X startup disk.
- `PROFILE_TIME_LIMIT`— This parameter, when supplied, forces the back-end to limit the time that it records profiling information to a fixed time limit, expressed here in seconds. If this limit is reached, profiling stops immediately. This option is an easy way to terminate profiling early for long-running applications. (For more precise termination control, however, see [Programmatic Start/Stop Control](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tcnjxfvbuqnjnknltc), instead.) In addition, like the previous `PROFILE_SIZE_LIMIT` variable, it can be used to prevent your application from filling up your entire disk with profile data. However, because it provides no file size guarantees, `PROFILE_SIZE_LIMIT` is generally recommended over this.

By default, Saturn profiles your entire application, from beginning to end, in all threads of execution. However, in real programs you often only want to profile a subset of your application’s execution at any one time, in order to focus your analysis on one part of the application or another. To allow you to exercise this level of control, the Saturn back-end contains three other functions that you can use directly in your programs: `initSaturn()`, `startSaturn()`, and `stopSaturn()`. These functions control generation of output data in the back-end dynamic library, enabling profiling for a thread at each `startSaturn()` call and disabling it at each `stopSaturn()` call.

Normally, these functions are used in a fairly simple pattern. To explicitly initialize the Saturn back-end for tracing your program, add the call: `initSaturn(char *path)`. This acts much like the automatic initialization, but allows you to explicitly specify the name of your Saturn profile. Once tracing has been initialized, you can then start and stop tracing using pairs of `startSaturn` and `stopSaturn` calls.

If your program creates any child threads over the course of its execution, they inherit the profiling status of their parent, by default. Hence these explicit start and stop calls are also a good way to limit profiling to a limited number of threads of interest in a heavily multithreaded program.

This section gives a brief reference for the three routines you can use to control Saturn directly.

- __initSaturn__—

  `void initSaturn(char *path);`

  This must be called before any `startSaturn` or `stopSaturn` calls are made. It initializes Saturn with the following parameter:

  __path__— The path of the directory to write output files. This can be a full path or a path relative to the current working directory. A `NULL` or an empty string argument will cause the files to be written in the current working directory.
- __startSaturn__—

  `void startSaturn(void);`

  Begins Saturn profiling. Data for every function that is called after this will be stored in the appropriate data file for the thread that is executing the call.
- __stopSaturn__—

  `void stopSaturn(void);`

  Ends Saturn profiling. Data collection ceases for this thread until `startSaturn` is called again. There can be many `startSaturn/stopSaturn` function call pairs throughout an instrumented application, if you want to see many small segments of execution scattered in different areas.

Below is a basic example using these functions. It shows how you can use a single pair of `startSaturn` and `stopSaturn` calls to exclude initialization and shutdown code from your profile. This is a common practice with programs that spend minimal amounts of time in these routines, in order to avoid polluting the profile with the large number of relatively unimportant function calls often found there. Please note that there can be many `startSaturn/stopSaturn` function call pairs throughout an instrumented application, if you want to focus even further on small segments of execution scattered in different areas.

```c
#include <Saturn.h>
int main()
{
 // Initialize Saturn:
 // The output file will put in the current working directory.
  initSaturn ("");

 // Do work that you don't want to measure, like initialization
  . . . init code here . . .

  // Start the back-end.
  startSaturn ();

  // This portion of the program is measured
  . . . program core here . . .

  // Stop the back-end.
  stopSaturn ();

  // This isn't measured, again
  . . . shutdown core here . . .
}
```

[Next](Document%20Revision%20History.md)[Previous](The%20Saturn%20Front-end.md)

