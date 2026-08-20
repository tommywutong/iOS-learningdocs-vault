---
title: Metal Programming Guide
apple_id: TP40014221
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Prog-Func/Prog-Func.html
archived_at: '2026-07-15T08:16:51.262585Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Programming Guide](About%20Metal%20and%20This%20Guide.md)


[Next](Graphics%20Rendering-%20Render%20Command%20Encoder.md)[Previous](Resource%20Objects-%20Buffers%20and%20Textures.md)

# Functions and Libraries

This chapter describes how to create a [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) object as a reference to a Metal shader or compute function and how to organize and access functions with a [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) object.

A [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) object represents a single function that is written in the Metal shading language and executed on the GPU as part of a graphics or compute pipeline. For details on the Metal shading language, see the _Metal Shading Language Guide_.

To pass data or state between the Metal runtime and a graphics or compute function written in the Metal shading language, you assign an argument index for textures, buffers, and samplers. The argument index identifies which texture, buffer, or sampler is being referenced by both the Metal runtime and Metal shading code.

For a rendering pass, you specify a `MTLFunction` object for use as a vertex or fragment shader in a [MTLRenderPipelineDescriptor](https://developer.apple.com/documentation/metal/mtlrenderpipelinedescriptor) object, as detailed in [Creating a Render Pipeline State](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgny). For a compute pass, you specify a `MTLFunction` object when creating a [MTLComputePipelineState](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate) object for a target device, as described in [Specify a Compute State and Resources for a Compute Command Encoder](Data-Parallel%20Compute%20Processing-%20Compute%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltgma).

A [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) object represents a repository of one or more [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) objects. A single `MTLFunction` object represents one Metal function that has been written with the shading language. In the Metal shading language source code, any function that uses a Metal function qualifier (`vertex`, `fragment`, or `kernel`) can be represented by a `MTLFunction` object in a library. A Metal function without one of these function qualifiers cannot be directly represented by a `MTLFunction` object, although it can called by another function within the shader.

The `MTLFunction` objects in a library can be created from either of these sources:

- Metal shading language code that was compiled into a binary _library_ format during the app build process.
- A text string containing Metal shading language source code that is compiled by the app at runtime.

For the best performance, compile your Metal shading language source code into a library file during your app's build process in Xcode, which avoids the costs of compiling function source during the runtime of your app. To create a [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) object from a library binary, call one of the following methods of [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice):

- [newDefaultLibrary](https://developer.apple.com/documentation/metal/mtldevice/1433380-newdefaultlibrary) retrieves a library built for the main bundle that contains all shader and compute functions in an app’s Xcode project.
- [newLibraryWithFile:error:](https://developer.apple.com/documentation/metal/mtldevice/1433416-newlibrarywithfile) takes the path to a library file and returns a `MTLLibrary` object that contains all the functions stored in that library file.
- [newLibraryWithData:error:](https://developer.apple.com/documentation/metal/mtldevice/1433391-makelibrary) takes a binary blob containing code for the functions in a library and returns a `MTLLibrary` object.

For more information about compiling Metal shading language source code during the build process, see [Creating Libraries During the App Build Process](Metal%20Tools.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqobnknltq).

To create a [MTLLibrary](https://developer.apple.com/documentation/metal/mtllibrary) from a string of Metal shading language source code that may contain several functions, call one of the following methods of [MTLDevice](https://developer.apple.com/documentation/metal/mtldevice). These methods compile the source code when the library is created. To specify the compiler options to use, set the properties in a [MTLCompileOptions](https://developer.apple.com/documentation/metal/mtlcompileoptions) object.

- [newLibraryWithSource:options:error:](https://developer.apple.com/documentation/metal/mtldevice/1433431-newlibrarywithsource) synchronously compiles source code from the input string to create `MTLFunction` objects and then returns a `MTLLibrary` object that contains them.
- [newLibraryWithSource:options:completionHandler:](https://developer.apple.com/documentation/metal/mtldevice/1433351-newlibrarywithsource) asynchronously compiles source code from the input string to create `MTLFunction` objects and then returns a `MTLLibrary` object that contains them. `completionHandler` is a block of code that is invoked when object creation is completed.

The [newFunctionWithName:](https://developer.apple.com/documentation/metal/mtllibrary/1515524-newfunctionwithname) method of `MTLLibrary` returns a `MTLFunction` object with the requested name. If the name of a function that uses a Metal shading language function qualifier is not found in the library, then `newFunctionWithName:` returns `nil`.

Listing 4-1 uses the [newLibraryWithFile:error:](https://developer.apple.com/documentation/metal/mtldevice/1433416-newlibrarywithfile) method of `MTLDevice` to locate a library file by its full path name and uses its contents to create a `MTLLibrary` object with one or more `MTLFunction` objects. Any errors from loading the file are returned in `error`. Then the `newFunctionWithName:` method of `MTLLibrary` creates a `MTLFunction` object that represents the function called `my_func` in the source code. The returned function object `myFunc` can now be used in an app.

__Listing 4-1__  Accessing a Function from a Library

```
NSError *errors;
id <MTLLibrary> library = [device newLibraryWithFile:@"myarchive.metallib"
                          error:&errors];
id <MTLFunction> myFunc = [library newFunctionWithName:@"my_func"];
```


Because the actual contents of a [MTLFunction](https://developer.apple.com/documentation/metal/mtlfunction) object are defined by a graphics shader or compute function that may be compiled before the `MTLFunction` object was created, its source code might not be directly available to the app. You can query the following `MTLFunction` properties at run time:

- [name](https://developer.apple.com/documentation/metal/mtlfunction/1515424-name), a string with the name of the function.
- [functionType](https://developer.apple.com/documentation/metal/mtlfunction/1516042-functiontype), which indicates whether the function is declared as a vertex, fragment, or compute function.
- [vertexAttributes](https://developer.apple.com/documentation/metal/mtlfunction/1515944-vertexattributes), an array of [MTLVertexAttribute](https://developer.apple.com/documentation/metal/mtlvertexattribute) objects that describe how vertex attribute data is organized in memory and how it is mapped to vertex function arguments. For more details, see [Vertex Descriptor for Data Organization](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltina).

`MTLFunction` does not provide access to function arguments. A reflection object (either [MTLRenderPipelineReflection](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection) or [MTLComputePipelineReflection](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection), depending upon the type of command encoder) that reveals details of shader or compute function arguments can be obtained during the creation of a pipeline state. For details on creating pipeline state and reflection objects, see [Creating a Render Pipeline State](Graphics%20Rendering-%20Render%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnznknltgny) or [Creating a Compute Pipeline State](Data-Parallel%20Compute%20Processing-%20Compute%20Command%20Encoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrrfvbuqnrnknltg). Avoid obtaining reflection data if it will not be used.

A reflection object contains an array of [MTLArgument](https://developer.apple.com/documentation/metal/mtlargument) objects for each type of function supported by the command encoder. For [MTLComputeCommandEncoder](https://developer.apple.com/documentation/metal/mtlcomputecommandencoder), [MTLComputePipelineReflection](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection) has one array of [MTLArgument](https://developer.apple.com/documentation/metal/mtlargument) objects in the [arguments](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection/1414909-arguments) property that correspond to the arguments of its compute function. For [MTLRenderCommandEncoder](https://developer.apple.com/documentation/metal/mtlrendercommandencoder), [MTLRenderPipelineReflection](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection) has two properties, [vertexArguments](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/1514686-vertexarguments) and [fragmentArguments](https://developer.apple.com/documentation/metal/mtlrenderpipelinereflection/1514701-fragmentarguments), that are arrays that correspond to the vertex function arguments and fragment function arguments, respectively.

Not all arguments of a function are present in a reflection object. A reflection object only contains arguments that have an associated resource, but not arguments declared with the `[[ stage_in ]]` qualifier or built-in `[[ vertex_id ]]` or `[[ attribute_id ]]` qualifier.

Listing 4-2 shows how you can obtain a reflection object (in this example, [MTLComputePipelineReflection](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection)) and then iterate through the [MTLArgument](https://developer.apple.com/documentation/metal/mtlargument) objects in its [arguments](https://developer.apple.com/documentation/metal/mtlcomputepipelinereflection/1414909-arguments) property.

__Listing 4-2__  Iteration Through Function Arguments

```
MTLComputePipelineReflection* reflection;
id <MTLComputePipelineState> computePS = [device
              newComputePipelineStateWithFunction:func
              options:MTLPipelineOptionArgumentInfo
              reflection:&reflection error:&error];
for (MTLArgument *arg in reflection.arguments) {
    //  process each MTLArgument
}
```

The [MTLArgument](https://developer.apple.com/documentation/metal/mtlargument) properties reveal the details of an argument to a shading language function.

- The [name](https://developer.apple.com/documentation/metal/mtlargument/1462031-name) property is simply the name of the argument.
- [active](https://developer.apple.com/documentation/metal/mtlargument/1461891-isactive) is a Boolean that indicates whether the argument can be ignored.
- [index](https://developer.apple.com/documentation/metal/mtlargument/1461883-index) is a zero-based position in its corresponding argument table. For example, for `[[ buffer(2) ]]`, `index` is 2.
- [access](https://developer.apple.com/documentation/metal/mtlargument/1462029-access) describes any access restrictions, for example, the read or write access qualifier.
- [type](https://developer.apple.com/documentation/metal/mtlargument/1461997-type) is indicated by the shading language qualifier, for example, `[[ buffer(n) ]]`, `[[ texture(n) ]]`, `[[ sampler(n) ]]`, or `[[ threadgroup(n) ]]`.

[type](https://developer.apple.com/documentation/metal/mtlargument/1461997-type) determines which other [MTLArgument](https://developer.apple.com/documentation/metal/mtlargument) properties are relevant.

- If `type` is [MTLArgumentTypeTexture](https://developer.apple.com/documentation/metal/mtlargumenttype/mtlargumenttypetexture), then the [textureType](https://developer.apple.com/documentation/metal/mtlargument/1461920-texturetype) property indicates the overall texture type (such as `texture1d_array`, `texture2d_ms`, and `texturecube` types in the shading language), and the [textureDataType](https://developer.apple.com/documentation/metal/mtlargument/1462049-texturedatatype) property indicates the component data type (such as `half`, `float`, `int`, or `uint`).
- If `type` is [MTLArgumentTypeThreadgroupMemory](https://developer.apple.com/documentation/metal/mtlargumenttype/mtlargumenttypethreadgroupmemory), the [threadgroupMemoryAlignment](https://developer.apple.com/documentation/metal/mtlargument/1462030-threadgroupmemoryalignment) and [threadgroupMemoryDataSize](https://developer.apple.com/documentation/metal/mtlargument/1461951-threadgroupmemorydatasize) properties are relevant.
- If `type` is [MTLArgumentTypeBuffer](https://developer.apple.com/documentation/metal/mtlargumenttype/mtlargumenttypebuffer), the [bufferAlignment](https://developer.apple.com/documentation/metal/mtlargument/1462007-bufferalignment), [bufferDataSize](https://developer.apple.com/documentation/metal/mtlargument/1461986-bufferdatasize), [bufferDataType](https://developer.apple.com/documentation/metal/mtlargument/1461885-bufferdatatype), and [bufferStructType](https://developer.apple.com/documentation/metal/mtlargument/1462041-bufferstructtype) properties are relevant.

If the buffer argument is a struct (that is, `bufferDataType` is [MTLDataTypeStruct](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypestruct)), the `bufferStructType` property contains a [MTLStructType](https://developer.apple.com/documentation/metal/mtlstructtype) that represents the struct, and `bufferDataSize` contains the size of the struct, in bytes. If the buffer argument is an array (or pointer to an array), then `bufferDataType` indicates the data type of an element, and `bufferDataSize` contains the size of one array element, in bytes.

Listing 4-3 drills down in a [MTLStructType](https://developer.apple.com/documentation/metal/mtlstructtype) object to examine the details of struct members, each represented by a [MTLStructMember](https://developer.apple.com/documentation/metal/mtlstructmember) object. A struct member may be a simple type, an array, or a nested struct. If the member is a nested struct, then call the [structType](https://developer.apple.com/documentation/metal/mtlstructmember/1462011-structtype) method of `MTLStructMember` to obtain a `MTLStructType` object that represents the struct and then recursively drill down to analyze it. If the member is an array, use the [arrayType](https://developer.apple.com/documentation/metal/mtlstructmember/1461887-arraytype) method of `MTLStructMember` to obtain a [MTLArrayType](https://developer.apple.com/documentation/metal/mtlarraytype) that represents it. Then examine its [elementType](https://developer.apple.com/documentation/metal/mtlarraytype/1462012-elementtype) property of `MTLArrayType`. If `elementType` is [MTLDataTypeStruct](https://developer.apple.com/documentation/metal/mtldatatype/mtldatatypestruct), call the [elementStructType](https://developer.apple.com/documentation/metal/mtlarraytype/1461901-elementstructtype) method to obtain the struct and continue to drill down into its members. If `elementType` is [MTLDataTypeArray](https://developer.apple.com/documentation/metal/mtldatatype/array), call the [elementArrayType](https://developer.apple.com/documentation/metal/mtlarraytype/1461963-elementarraytype) method to obtain the subarray and analyze it further.

__Listing 4-3__  Processing a Struct Argument

```
MTLStructType *structObj = [arg.bufferStructType];
for (MTLStructMember *member in structObj.members) {
    //  process each MTLStructMember
    if (member.dataType == MTLDataTypeStruct) {
       MTLStructType *nestedStruct = member.structType;
       // recursively drill down into the nested struct
    }
    else if (member.dataType == MTLDataTypeArray) {
       MTLStructType *memberArray = member.arrayType;
       // examine the elementType and drill down, if necessary
    }
    else {
       // member is neither struct nor array
       // analyze it; no need to drill down further
    }
}
```

[Next](Graphics%20Rendering-%20Render%20Command%20Encoder.md)[Previous](Resource%20Objects-%20Buffers%20and%20Textures.md)

