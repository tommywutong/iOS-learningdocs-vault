---
title: OpenGL Profiler User Guide
apple_id: TP40006475
resource_type: Guide
platform: Xcode Developer Tools
topic: Languages & Utilities
technology: OpenGL
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGLProfilerUserGuide/Strategies/Strategies.html
archived_at: '2026-07-15T07:37:04.530281Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Profiler User Guide](Introduction.md)


[Next](Controlling%20Profiling%20Programmatically.md)[Previous](Using%20Breakpoints.md)

# Identifying and Solving Performance Issues

This chapter describes a number of strategies that can help you track down performance issues and understand how OpenGL works with your application. Before you read this chapter, you should already be familiar with how to start and run a profiling session, and how to set breakpoints.

OpenGL is an evolving specification. As time goes on, programming practices that were acceptable in the past are replaced by techniques that work much better. There are several functions in the OpenGL specification that you should watch for when you profile your application. If you are using any of these OpenGL functions in your application, make sure that you really need to use them, and that you are using them correctly.

- Avoid `glBegin` because it signals that you are using immediate mode. Unless you are drawing a simple shape or creating a small prototype, immediate mode is typically not an optimal technique for using OpenGL.
- `glFinish` forces your application to wait until all OpenGL commands in the pipeline have executed on the graphics card.
- `glFlush` is typically not needed because flushing is usually handled by other calls, such as `CGLFlushDrawable`. The function `glFlush` flushes at the macro level, an expensive operation. Flushing calls provided by the OS X interfaces (AGL, CGL, Cocoa OpenGL classes) act at a microlevel to give finer control over flushing and, as a result, much better performance.
- `glTexImage` and related calls. Check to see if you are using this function to redefine the texture each frame. If so, change your code to define the texture outside frame rendering. If your data changes, you can instead use a data replacement technique, such as pixel buffer objects, or call `glTexSubImage` to specify the image again. Keep in mind that you can call `glTexSubImage` to specify the entire image again (maintaining the current texture parameters), and it will be a less expensive call than `glTexImage`. You should call `glTexImage` only if you must specify a larger image.
- Any form of `glGet` or `glIs`. Getting state values slows your application. Unless your application is a “middle ware” application, you shouldn’t need to retrieve state values. During development, however, it’s quite common to call `glGetError`. When your application is ready to go into production, make sure that your remove `glGetError` calls and any other state getting and checking functions. As an alternative during development, you can look for errors by setting OpenGL Profiler to break on errors.
- `glPushAttrib` or `glPopAttrib`. You should keep track of OpenGL state instead of using the server attribute stack.
- The function `glDrawPixels` is a convenience function that, under the hood, uses screen-aligned textured quads. If you use screen-aligned textured quads directly, you’ll save the overhead of calling `glDrawPixels`. Make sure that when you use textured quads that you also use appropriate texture filtering.
- If you are calling `glReadPixels`, you should also be using pixel buffer objects.
- `glProgramLocalParameter` and `glProgramEnvParameter` calls. These calls, defined by the [GL_ARB_vertex_program](http://oss.sgi.com/projects/ogl-sample/registry/ARB/vertex_program.txt) extension, load only one parameter at a time. It’s more efficient to use `glProgramLocalParameters` and `glProgramEnvParameters`, defined by the [GL_EXT_gpu_program_parameters](http://opengl.org/registry/specs/EXT/gpu_program_parameters.txt) extension, which loads multiple parameters.

You can get a quick view of what your application is doing by collecting a trace for a single frame. Although viewing the trace and statistics for one frame provides a narrow view of application behavior, you can use this strategy to narrow down problem areas in your application.

To collect a trace for a single frame:

1. Launch or attach to the application of interest.
2. Open the Statistics window.
3. Navigate in the application to the area where you suspect a problem.
4. Set a breakpoint on the function `CGLFlushDrawable`. If you are using a single-buffered rendering context, you might also need to set a breakpoint on the function `glFlush`.
5. When your application pauses, click Clear in the Statistics window.
6. Click Continue in the Breakpoints window. When your application pauses, make sure it rendered the frame completely. If not, your code likely calls more than one flush operation per frame.

   Then, check for the following in the Statistics window:

   - State management. Check to see if you are calling `glPopAttrib` calls. If possible you should instead track your own state. It’s not a good idea to set state on a per frame basis. It’s best to consolidate state changes and set them outside the frame.
   - Calls that take significantly more time than the others.
   - Any OpenGL calls that are listed in [Making Sure You Use Functions Correctly](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnbqfvjvomy).
7. Click the Continue button in the Breakpoints window to resume execution of your application.

To get the best performance, make sure your data is using an optimal data type and format combination. You won’t get the best performance otherwise.

Ideally, you’ll want to use:

`GL_BGRA`, `GL_UNSIGNED_INT_8_8_8_8_REV`

This is the fastest data type and format combination. If it isn’t fast, you may have a problem with your driver.

If that’s not possible, you can often get acceptable performance from the following. Just make sure to test these combinations on a device-by-device basis:

`GL_BGRA`, `GL_UNSIGNED_SHORT_1_5_5_5_REV`

`GL_YCBR_422_APPLE`, `GL_UNSIGNED_SHORT_8_8_REV_APPLE`

OpenGL Profiler does not know what the inbound data format is. So you need to check the point at which your data gets uploaded by OpenGL by performing this steps:

1. Select Collect Trace and Include Backtraces in the OpenGL Profiler window.
2. Set a breakpoint where your data is uploaded.
3. When your application breaks, click Call Stack in the Trace window.

The amount of data generated when collecting a trace can be overwhelming. Most of the time you’ll collect a trace for only one frame, which is typically enough to track down the most common issues. (See [Identifying Problem Areas in Your Application](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnbqfvjvona).) If you do need to collect more than a frame of data, you can create a custom shell script that operates on trace data so that you can get it into a more manageable state. When you want to apply a script, click the Filter button in the Trace window. OpenGL Profiler provides the trace data as input (`stdin`) to your script and writes the results from your scripting calls to `stdout`.

If a drawing call is slow and you suspect a shader is the cause, you may need to collect more than frame of data. You can then use a script to pare down the data to suspicious calls. [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnbqfvjvomq) shows a very simple script that sorts calls by function call time, with the slowest calls last. Your script would need to be customized so that it performs operations appropriate for the problem you are trying to isolate. After you use a script to identify suspicious calls, you can use the line number of the output to trace back to where the call actually took place.

__Listing 3-1__  A shell script for finding the slowest calls in a trace

```
#!/bin/tcsh -f
awk '{ print $3" "$0 }' | sort -n
```

To create a script:

1. Open an application, such as Xcode, that lets you create a plain text file.
2. Enter the appropriate script commands using any scripting language that accepts input from `stdin`.
3. Save the script with a `.filter` extension.

   You can save it to any location that you’d like.
4. For the first script that you create, select it in the Finder and choose File > Get Info.

   Make sure that the “Open with” pop-up menu is set to the application that you used for creating the script. This ensures that OpenGL Profiler will use this application to open any files with the `.filter` extension.

To filter trace data:

1. Open the Trace window.
2. Click Browse, navigate to the script you want to use, and select it.

   You can modify an existing script by clicking Open.
3. Click Filter, then provide a name for the output file.

You can quickly check for errors in your application by setting one or more error breakpoints. To use OpenGL Profiler to check for application errors:

1. Choose View > Breakpoints.
2. Select one or more of these options:

   - Break on error. Your application pauses when it encounters any type of error.
   - Break on VAR error. Your application pauses when there is a problem using the vertex array range extension.
   - Break on thread conflict. You can select this if your application is multithreaded.
   - Break on SW fallback. You application pauses when it uses the software renderer as a fallback. Although this condition is not strictly an error, it alerts you to situations for which the system does not have the appropriate hardware renderer to carry out a particular OpenGL call.
3. If you have not already done so, launch or attach your application.
4. Monitor the Breakpoints window for errors.

In OS X v10.5 and later, the OpenGL framework can offload processing onto a separate thread that runs on a different CPU core. You use the `CGLEnable` function to enable multithreaded execution programmatically using this code:

```c
#include <OpenGL/OpenGL.h>

CGLError err = 0;
CGLContextObj ctx = CGLGetCurrentContext();

// Enable the multi-threading
err =  CGLEnable( ctx, kCGLCEMPEngine);

if (err != kCGLNoError )
{
     // Multi-threaded execution is possibly not available
     // Insert your code to take appropriate action
}
```

For more details see Technical Note TN2085: _[Enabling multi-threaded execution of the OpenGL framework](https://developer.apple.com/library/archive/technotes/tn2085/_index.html#//apple_ref/doc/uid/DTS10004075)_.

After enabling multithreading, some applications see a dramatic increase in OpenGL performance; others might not. In general, the multithreaded OpenGL engine is a good option for applications that are CPU bound.

If your application enables the multithreaded OpenGL engine, it’s a good idea to check whether it actually improves performance. After you programmatically enable multithreading, evaluate its effect by following these steps:

1. Launch or attach to the application of interest.
2. In the main OpenGL Profiler window, check the frame rate at a point in your application that is repeatable. You’ll check this same point later.
3. Choose Views > Breakpoints.
4. Make sure the multithreaded control option is set to “App control.”
5. In the main OpenGL Profiler window, check the frame rate.
6. Set a breakpoint on a function.

   Although you can choose any function, typically you’d set a breakpoint on `CGLFlushDrawable` for a double-buffered rendering context or `glFlush` for a single-buffered rendering context.
7. When your application pauses, select the “Force off” option for multithreaded control.
8. Press Continue to resume execution of your application.
9. In the main OpenGL Profiler window, check the frame rate.

   Compare this frame rate to the rate you observed when using the multithreaded OpenGL engine.

Applications that can’t use the GPU for some reason (such as the graphics card does not support some of the OpenGL extensions that your code uses) use the software renderer as a fallback. If you notice a drop in the performance of your application, you may want to check whether the application is using the GPU as you expect.

Starting in OS X v10.5, you can set your application to break whenever it uses the software renderer as a fallback. (See [Checking for Application Errors, Thread Conflicts, and Software Fallbacks](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzvfvbuqnbqfvjvonq).) Prior to OS X v10.5, you can monitor the GPU use of your application whenever your application pauses at a breakpoint. The best breakpoints to check are:

- `CGLFlushDrawable`
- After `glUseProgramObjectARB`
- After `glBindProgramARB`
- Any `glDraw` or related command, including the following:

  - `glAccum`
  - `glBegin`
  - `glBlitFramebufferEXT`
  - `glBitmap`
  - `glClear`
  - `glCopyPixels`
  - `glDrawPixels`
  - `glReadPixels`
  - `glCopyTexSubImage*D`
  - `glCopyTexImage*D`
  - `glDrawArrays`
  - `glDrawElements`
  - `glDrawRangeElements`

When your application pauses at these breakpoints, check the values of `kCGLCPGPUFragmentProcessing` and `kCGLCPGPUVertexProcessing` shown in the Call Stack pane of the Breakpoints window. A value of `GL_TRUE` indicates that your application is using the GPU for the process associated with the constant.

If your application renders to a window, you can often identify the cause of performance issues by resizing the window. While your application renders to a window, resize it. After you shrink the window, if the execution time is significantly faster, then the issue might be related to low VRAM. If the execution time is faster proportional to the window size, then your application is fragment bound. If the execution time is the same, then your application either is vertex bound on the GPU or is CPU bound.

Many calls in OpenGL are used as sets, such as:

- `glBegin` and `glEnd`
- `glEnable` and `glDisable`

You can check the # of Calls column in the Statistics window to make sure that these (and similar sets) are always matched in your application. For example, if you find 5 `glBegin` calls but only 3 `glEnd` call, you should modify your code so that you have the same number of each. Unmatched calls typically are a symptom of unneeded code and always indicate imprecise code. Call sets should always match within a frame.

[Next](Controlling%20Profiling%20Programmatically.md)[Previous](Using%20Breakpoints.md)

