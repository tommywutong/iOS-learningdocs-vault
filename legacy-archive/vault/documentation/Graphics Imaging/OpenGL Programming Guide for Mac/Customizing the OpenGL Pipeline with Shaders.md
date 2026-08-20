---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_shaders/opengl_shaders.html
archived_at: '2026-07-15T07:36:43.498582Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](Techniques%20for%20Scene%20Antialiasing.md)[Previous](Best%20Practices%20for%20Working%20with%20Texture%20Data.md)

# Customizing the OpenGL Pipeline with Shaders

OpenGL 1.x used fixed functions to deliver a useful graphics pipeline to application developers. To configure the various stages of the pipeline shown in Figure 12-1, applications called OpenGL functions to tweak the calculations that were performed for each vertex and fragment. Complex algorithms required multiple rendering passes and dozens of function calls to configure the calculations that the programmer desired. Extensions offered new configuration options, but did not change the complex nature of OpenGL programming.

__Figure 12-1__  OpenGL fixed-function pipeline

!

Starting with OpenGL 2.0, some stages of the OpenGL pipeline can be replaced with _shaders_. A shader is a program written in a special shading language. This program is compiled by OpenGL and uploaded directly into the graphics hardware. Figure 12-2 shows where your applications can hook into the pipeline with shaders.

__Figure 12-2__  OpenGL shader pipeline

!

Shaders offer a considerable number of advantages to your application:

- Shaders give you precise control over the operations that are performed to render your images.
- Shaders allow for algorithms to be written in a terse, expressive format. Rather than writing complex blocks of configuration calls to implement a mathematical operation, you write code that expresses the algorithm directly.
- Older graphics processors implemented the fixed-function pipeline in hardware or microcode, but now graphics processors are general-purpose computing devices. The fixed function pipeline is itself implemented as a shader.
- Shaders allow for longer and more complex algorithms to be implemented using a single rendering pass. Because you have extensive control over the pipeline, it is also easier to implement multipass algorithms without requiring the data to be read back from the GPU.
- Your application can switch between different shaders with a single function call. In contrast, configuring the fixed-function pipeline incurs significant function-call overhead.

If your application uses the fixed-function pipeline, a critical task is to replace those tasks with shaders.

If you are new to shaders, _OpenGL Shading Language_, by Randi J. Rost, is an excellent guide for those looking to learn more about writing shaders and integrating them into your application. The rest of this chapter provides some boilerplate code, briefly describe the extensions that implement shaders, and discusses tools that Apple provides to assist you in writing shaders.

OpenGL 2.0 offers vertex and fragment shaders, to take over the processing of those two stages of the graphics pipeline. These same capabilities are also offered by the [ARB_shader_objects](http://www.opengl.org/registry/specs/ARB/shader_objects.txt), [ARB_vertex_shader](http://www.opengl.org/registry/specs/ARB/vertex_shader.txt) and [ARB_fragment_shader](http://www.opengl.org/registry/specs/ARB/fragment_shader.txt)extensions. Vertex shading is available on all hardware running OS X v10.5 or later. Fragment shading is available on all hardware running OS X v10.6 and the majority of hardware running OS X v10.5.

Creating a shader program is an expensive operation compared to other OpenGL state changes. Listing 12-1 presents a typical strategy to load, compile, and verify a shader program.

__Listing 12-1__  Loading a Shader

```
/** Initialization-time for shader **/             GLuint shader, prog;             GLchar *shaderText = “... shader text ...”;              // Create ID for shader            shader = glCreateShader(GL_VERTEX_SHADER);             // Define shader text            glShaderSource(shaderText);             // Compile shader            glCompileShader(shader);             // Associate shader with program            glAttachShader(prog, shader);            // Link program            glLinkProgram(prog);                 // Validate program            glValidateProgram(prog);             // Check the status of the compile/link            glGetProgramiv(prog, GL_INFO_LOG_LENGTH, &logLen);            if(logLen > 0)            {                // Show any errors as appropriate                glGetProgramInfoLog(prog, logLen, &logLen, log);                fprintf(stderr, “Prog Info Log: %s\n”, log);        }       // Retrieve all uniform locations that are determined during link phase            for(i = 0; i < uniformCt; i++)            {                uniformLoc[i] = glGetUniformLocation(prog, uniformName);            }             // Retrieve all attrib locations that are determined during link phase            for(i = 0; i < attribCt; i++)            {                attribLoc[i] = glGetAttribLocation(prog, attribName);            }      /** Render stage for shaders **/     glUseProgram(prog);
```

This code loads the text source for a vertex shader, compiles it, and adds it to the program. A more complex example might also attach fragment and geometry shaders. The program is linked and validated for correctness. Finally, the program retrieves information about the inputs to the shader and stores then in its own arrays. When the application is ready to use the shader, it calls `glUseProgram` to make it the current shader.

For best performance, your application should create shaders when your application is initialized, and not inside the rendering loop. Inside your rendering loop, you can quickly switch in the appropriate shaders by calling `glUseProgram`. For best performance, use the vertex array object extension to also switch in the vertex pointers. See [Vertex Array Object](Best%20Practices%20for%20Working%20with%20Vertex%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgywvgvzy) for more information.

In addition to the standard shader, some Macs offer additional shading extensions to reveal advanced hardware capabilities. Not all of these extensions are available on all hardware, so you need to assess whether the features of each extension are worth implementing in your application.

The [EXT_transform_feedback](http://www.opengl.org/registry/specs/EXT/transform_feedback.txt) extension is available on all hardware running OS X v10.5 or later. With the feedback extension, you can capture the results of the vertex shader into a buffer object, which can be used as an input to future commands. This is similar to the pixel buffer object technique described in [Using Pixel Buffer Objects to Keep Data on the GPU](Best%20Practices%20for%20Working%20with%20Texture%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqg4wvgvztha), but more directly captures the results you desire.

The [EXT_gpu_shader4](http://www.opengl.org/registry/specs/EXT/gpu_shader4.txt) extension extends the OpenGL shading language to offer new operations, including:

- Full integer support.
- Built-in shader variable to reference the current vertex.
- Built-in shader variable to reference the current primitive. This makes it easier to use a shader to use the same static vertex data to render multiple primitives, using a shader and uniform variables to customize each instance of that primitive.
- Unfiltered texture fetches using integer coordinates.
- Querying the size of a texture within a shader.
- Offset texture lookups.
- Explicit gradient and LOD texture lookups.
- Depth Cubemaps.

The [EXT_geometry_shader4](http://www.opengl.org/registry/specs/EXT/geometry_shader4.txt) extension allows your create geometry shaders. A geometry shader accepts transformed vertices and can add or remove vertices before passing them down to the rasterizer. This allows the application to add or remove geometry based on the calculated values in the vertex. For example, given a triangle and its neighboring vertices, your application could emit additional vertices to better create a more accurate appearance of a curved surface.

The [EXT_bindable_uniform](http://www.opengl.org/registry/specs/EXT/bindable_uniform.txt) extension allows your application to allocate buffer objects and use them as the source for uniform data in your shaders. Instead of relying on a single block of uniform memory supplied by OpenGL, your application allocates buffer objects using the same API that it uses to implement vertex buffer objects ([Vertex Buffers](Best%20Practices%20for%20Working%20with%20Vertex%20Data.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgywvgvzr)). Instead of making a function call for each uniform variable you want to change, you can swap all of the uniform data by binding to a different uniform buffer.

[Next](Techniques%20for%20Scene%20Antialiasing.md)[Previous](Best%20Practices%20for%20Working%20with%20Texture%20Data.md)

