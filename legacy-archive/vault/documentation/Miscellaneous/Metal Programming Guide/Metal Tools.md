---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Dev-Technique/Dev-Technique.html
archived_at: '2026-07-15T08:16:50.065309Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Metal%20Feature%20Set%20Tables.md)[Previous](Buffer%20and%20Texture%20Operations-%20Blit%20Command%20Encoder.md)

# Metal Tools

This chapter lists the tools available to help you customize and improve your development workflow.

Compiling shader language source files and building a library (`.metallib` file) during the app build process achieves better app performance than compiling shader source code at runtime. You can build a library within Xcode or by using command line utilities.

Any shader source files that are in your project are automatically used to generate the default library, which you can access from Metal framework code with the [newDefaultLibrary](https://developer.apple.com/documentation/metal/mtldevice/1433380-newdefaultlibrary) method of [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice).

[Figure 8-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqobnknltm) shows the command line utilities that form the compiler toolchain for Metal shader source code. When you include `.metal` files in your project, Xcode invokes these tools to build a library file that you can access in your app at run time.

To compile shader source into a library without using Xcode:

1. Use the `metal` tool to compile each `.metal` file into a single `.air` file, which stores an intermediate representation (IR) of shader language code.
2. Optionally, use the `metal-ar` tool to archive several `.air` files together into a single `.metalar` file. (`metal-ar` is similar to the Unix `ar`.)
3. Use the `metallib` tool to build a Metal `.metallib` library file from IR `.air` files or from archive `.metalar` files.

__Figure 8-1__  Building a Library File with Command Line Utilities

!!

[Listing 8-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqobnknlti) shows the minimum number of commands needed for compiling and building a `.metal` file into a `.metallib` file.

__Listing 8-1__  Building a Library File with Command Line Utilities

```
xcrun -sdk macosx metal MyLibrary.metal -o MyLibrary.air
xcrun -sdk macosx metallib MyLibrary.air -o MyLibrary.metallib
```

To access the resulting library in framework code, call the [newLibraryWithFile:error:](https://developer.apple.com/documentation/metal/mtldevice/1433416-newlibrarywithfile) method, as shown in [Listing 8-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqobnknltk).

__Listing 8-2__  Accessing a Library File within Your App

```
NSError *libraryError = NULL;
NSString *libraryFile = [[NSBundle mainBundle] pathForResource:@"MyLibrary" ofType:@"metallib"];
id <MTLLibrary> myLibrary = [_device newLibraryWithFile:libraryFile error:&libraryError];
if (!myLibrary) {
    NSLog(@"Library error: %@", libraryError);
}
```


When a Metal app is running from Xcode, the default scheme settings reduce performance. Xcode detects whether the Metal API is used in the source code and automatically enables the GPU Frame Capture and Metal API Validation settings, as seen in Figure 8-2. When GPU Frame Capture is enabled, the debug layer is activated. When Metal API Validation is enabled, each call is validated, which affects performance further. For both settings, CPU performance is more affected than GPU performance. Unless you disable these settings, app performance may noticeably improve when the app is run outside of Xcode.

__Figure 8-2__  Xcode Scheme Editor Settings for a Metal App

!!

Use the tips in the following sections to gain more useful diagnostic information when debugging and profiling your Metal app.

For Metal shading language source code file names, you must use the `.metal` file name extension to ensure that the development tools (Xcode and the GPU frame debugger) recognize the source files when debugging or profiling.

To perform frame capture in Xcode, enable debug and call the [insertDebugCaptureBoundary](https://developer.apple.com/documentation/metal/mtlcommandqueue/1508692-insertdebugcaptureboundary) method of [MTLCommandQueue](https://developer.apple.com/documentation/metal/mtlcommandqueue) to inform Xcode. The [presentDrawable:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1443029-present) and [presentDrawable:atTime:](https://developer.apple.com/documentation/metal/mtlcommandbuffer/1442989-present) methods of [MTLCommandBuffer](https://developer.apple.com/documentation/metal/mtlcommandbuffer) similarly inform Xcode about frame capture, so call [insertDebugCaptureBoundary](https://developer.apple.com/documentation/metal/mtlcommandqueue/1508692-insertdebugcaptureboundary) only if those methods are not present. Refer to [Debugging Metal and OpenGL ES](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/debugging_with_xcode/chapters/special_debugging_workflows.html#//apple_ref/doc/uid/TP40015022-CH9-SW24) for further information.

Many Metal framework objects—such as command buffers, pipeline states, and resources—support a [label](https://developer.apple.com/documentation/metal/mtlresource/1515814-label) property. You can use this property to assign a name for each object that is meaningful in the context of your application’s design. These labels appear in the Xcode Frame Capture debugging interface, allowing you to more easily identify objects.

Similarly, the [insertDebugSignpost:](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458034-insertdebugsignpost), [pushDebugGroup:](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458041-pushdebuggroup), and [popDebugGroup](https://developer.apple.com/documentation/metal/mtlcommandencoder/1458040-popdebuggroup) methods allow you to insert debug strings into a command buffer and to push or pop string labels used to identify groups of encoded commands.

To profile an app in Instruments, run the Metal System Trace tool. Refer to [Metal System Trace Profiling Template](https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/ProfilingTemplates.html#//apple_ref/doc/uid/TP40004652-CH19-SW13) for further information.

[Next](Metal%20Feature%20Set%20Tables.md)[Previous](Buffer%20and%20Texture%20Operations-%20Blit%20Command%20Encoder.md)

