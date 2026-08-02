---
title: Metal Best Practices Guide
apple_id: TP40016642
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/Pipelines.html
archived_at: '2026-07-15T03:48:56.764538Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Best Practices Guide](index.md)



## Pipelines

__Best Practice:__ Build your render and compute pipelines asynchronously.

Having multiple render or compute pipelines allows your app to use different state configurations for specific tasks. Building these pipelines asynchronously maximizes performance and parallelism. Build all known pipelines up front and avoid lazy loading. Listing 14-1 shows how to build multiple render pipelines asynchronously.

__Listing 14-1__Building multiple render pipelines asynchronously

1. `const uint32_t pipelineCount;`
2. `dispatch_queue_t dispatch_queue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);`
4. `// Dispatch the render pipeline build`
5. `__block NSMutableArray<id<MTLRenderPipelineState>> *pipelineStates = [[NSMutableArray alloc] initWithCapacity:pipelineCount];`
7. `dispatch_group_t pipelineGroup = dispatch_group_create();`
8. `for(uint32_t pipelineIndex = 0; pipelineIndex < pipelineCount; pipelineIndex++)`
9. `{`
10. `id <MTLFunction> vertexFunction = [_defaultLibrary newFunctionWithName:vertexFunctionNames[pipelineIndex]];`
11. `id <MTLFunction> fragmentFunction = [_defaultLibrary newFunctionWithName:fragmentFunctionNames[pipelineIndex]];`
13. `MTLRenderPipelineDescriptor* pipelineDescriptor = [MTLRenderPipelineDescriptor new];`
14. `pipelineDescriptor.vertexFunction = vertexFunction;`
15. `pipelineDescriptor.fragmentFunction = fragmentFunction;`
16. `/* Configure additional descriptor properties */`
18. `dispatch_group_enter(pipelineGroup);`
19. `[_device newRenderPipelineStateWithDescriptor:pipelineDescriptor completionHandler: ^(id <MTLRenderPipelineState> newRenderPipeline, NSError *error )`
20. `{`
21. `// Add error handling if newRenderPipeline is nil`
22. `pipelineStates[pipelineIndex] = newRenderPipeline;`
23. `dispatch_group_leave(pipelineGroup);`
24. `}];`
25. `}`
27. `/* Do more work */`
29. `// Wait for build to complete`
30. `dispatch_group_wait(pipelineGroup, DISPATCH_TIME_FOREVER);`
32. `/* Use the render pipelines */`

[Functions and Libraries](FunctionsandLibraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmrufvjvomi)
