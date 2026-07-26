---
title: 'Friday Q&A 2010-04-02: OpenCL Basics'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2010-04-02-opencl-basics.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:76ff9fa3ad0b07a2'
translated: false
---

> 原文：[Friday Q&A 2010-04-02: OpenCL Basics](https://www.mikeash.com/pyblog/friday-qa-2010-04-02-opencl-basics.html)　·　mikeash.com Friday Q&A

Posted at 2010-04-02 11:28 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2010-04-09: Comparison of Objective-C Enumeration Techniques](https://www.mikeash.com/pyblog/friday-qa-2010-04-09-comparison-of-objective-c-enumeration-techniques.html)  
Previous article: [And Again](https://www.mikeash.com/pyblog/and-again.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [opencl](https://www.mikeash.com/pyblog/?tag=opencl)

Friday Q&A 2010-04-02: OpenCL Basics

by [Mike Ash](https://www.mikeash.com/)

**SMUGOpenCL**  
 I made heavy use of Chris Liscio's [SMUGOpenCL](https://bitbucket.org/liscio/smugopencl/wiki/Home) library, which provides some nice Objective-C wrappers for basic OpenCL functionality.

**What is OpenCL?**  
 OpenCL is a natural outgrowth of the move toward doing general-purpose computation on graphics cards using OpenGL. The graphics card is actually the most powerful number cruncher in many PCs, and taking advantage of its power for non-graphics computations has been an emerging trend in recent years. My [GPULife](http://www.mikeash.com/software/gpulife/) screensaver is an example of using OpenGL to do non-graphics computations, in this particular case computing the Game of Life.

OpenGL, while providing enough power to do general-purpose computations with the GLSL shader language, is awkward for non-graphical purposes. GLSL is still heavily graphics-oriented, and lacks things which many non-graphics computations need, like the ability to do random memory access for writing. Working around these limitations is possible, but is hard to do and can greatly hurt efficiency.

Not all graphics cards are capable of GLSL, and CPU emulation can be slow. A truely adaptable program will run computations on the GPU when possible and on the CPU as a fallback, ideally with vectorized, parallelized CPU code, but OpenGL doesn't make this easy.

OpenCL does make it easy. OpenCL allows you to program your GPU using normal C, with all the pointer craziness and random memory access that implies. Of course your performance will be better with more structured accesses, just like with anything, but for when you really need random accesses, OpenCL allows it. OpenCL can also target both GPUs and CPUs, and when you need to fall back to CPUs, OpenCL will do its best to automatically vectorize and parallelize your code. OpenCL is structured so that it can do a much better job at these tasks than your normal compiler in many cases. Since you can use essentially the same code for both CPU and GPU, this means that you can maintain less code, run on any hardware, and still take full advantage of beefy GPUs when they're available.

**Overview**  
 OpenCL is a library that you access at runtime. You give programs to OpenCL, which transforms them into _kernels_, which are functions that you can then call using OpenCL.

Unlike normal C programming, you don't compile OpenCL kernels ahead of time. Instead, you feed the raw textual source to OpenCL, which compiles them at runtime. This is necessary because you can't know in advance just what sort of hardware you're going to target. And in the case where you're targeting CPUs, this still allows OpenCL to make specializations based on the specific CPU's vector capabilities and number of cores.

These kernels are written in plain C with some basic extensions. When compiled, they can't be directly accessed as C functions. Instead, you set arguments and make calls using OpenCL functions, which then manage the execution of the kernels.

**A Frequency Counter**  
 To illustrate the use of OpenCL, I built a byte frequency counter. This just loads a file and counts the number of times each byte value occurs, and prints out the result. This is not the most useful program in the world, but it's a decent illustration of how to use OpenCL.

**Code**  
 As usual, I'll be presenting excerpts here, but the full code is available from my public subversion repository:

`    svn co http://mikeash.com/svn/OpenCLFreqCount/`

Or just click on the URL above to browse it.

**Plain C Implementation**  
 I first wrote a non-OpenCL implementation of the frequency counter. This is useful to understand the problem, and also for debugging, to ensure that the OpenCL version produces the correct output. The function is simple: it takes an `NSData` and returns an `NSData` containing an array of `uint32_t`s representing the frequency counts. The computation is straightforward:

```
    static NSData *SimpleFreqCount(NSData *inData)
    {
        NSMutableData *freqCount = [NSMutableData dataWithLength: 256 * sizeof(uint32_t)];
        uint32_t *freqs = [freqCount mutableBytes];
        
        const unsigned char *ptr = [inData bytes];
        NSUInteger len = [inData length];
        for(NSUInteger i = 0; i < len; i++)
            freqs[ptr[i]]++;
        
        return freqCount;
    }
```

An OpenCL kernel gets invoked multiple times in parallel by OpenCL with the same parameters. The kernel can differentiate between these different instances by examining its work-item ID. These work-item IDs can get complex, but in the simplest case, each call to the kernel has one ID which you can fetch by calling

.

Because the kernels can execute in parallel, there are the standard problems with concurrent data access. To avoid clashes, I decided to write the frequency count in two stages.

The first stage will go through the input data in blocks of 256 bytes and compute a _local_ frequency count of the bytes just in that block. This local count will be stored into a large array which contains one local frequency count per block. The second stage will then go through and add all of the local counts together into one global count.

**OpenCL Kernel Code**  
 Here's what the start of the `freqcount` kernel, the first stage kernel, looks like:

```
    __kernel void freqcount(const unsigned char *input, unsigned short *output)
    {
```

This should be pretty familiar to any C programmer. The only strange part is the

keyword. This is an OpenCL-specific keyword which indicates that this function is a

, which is to say that it can be accessed from the outside program. It's also possible to write functions that can only be accessed by other OpenCL functions.

Next, the kernel gets its work-item ID:

```
        const uint index = get_global_id(0);
```

It uses this to compute a starting place in the array. Since we're working with 256-byte blocks, the starting index is the work-item ID multiplied by 256:

```
        const uint start = index * 256;
```

Then I simply loop through

, getting the value of each byte, and incrementing the value in the corresponding spot in

:

```
        for(uint i = 0; i < 256; i++)
        {
            uint value = input[start + i];
            output[start + value]++;
        }
    }
```

The

kernel is the second stage. It uses a fixed number of work items, 256, one for each entry in the frequency count. Each work item then loops through all of the local count arrays to compute a final total. This is what the kernel looks like:

```
__kernel void freqsum(const unsigned int count, unsigned short *freqs, unsigned int *totals)
{
    const uint index = get_global_id(0);
    for(uint i = 0; i < count; i++)
        totals[index] += freqs[index + i * 256];
}
```

Building the kernels was easy in this case, calling them is a bit more work. The first thing I do is pad the incoming data to a multiple of 256, so that it plays nice with the kernel's chunking:

```
    static NSData *CLFreqCount(NSData *inData)
    {
        NSMutableData *data = [NSMutableData dataWithData: inData];
        
        // pad data to multiple of 256
        NSUInteger dataLength = [data length];
        NSUInteger paddedLength = dataLength + 255 - (dataLength + 255) % 256;
        NSUInteger pad = paddedLength - dataLength;
        [data setLength: paddedLength];
```

(This will change the final frequency count, of course, so the amount of padding is kept in the

variable so that it can be subtracted off at the end.)

Next I create buffers to hold the local counts and the final count. The local counts array is twice as large as the incoming data, because it needs two bytes for each byte value for each 256-byte block. The final count array is just enough to hold 256 32-bit integers:

```
        // create large output area
        NSMutableData *largeOutput = [NSMutableData dataWithLength: paddedLength * 2];
        // and the final totals area
        NSMutableData *freqCount = [NSMutableData dataWithLength: 256 * sizeof(uint32_t)];
```

Now it's time to set up OpenCL. I'll be doing everything through SMUGOpenCL, so you won't see any OpenCL calls here. If you want to see how the OpenCL calls work under the hood, you can look at the SMUGOpenCL source directly.

The first thing to do is to set up a context in which the kernels can be executed:

```
        SMUGOpenCLContext *context = [[SMUGOpenCLContext alloc] initCPUContext];
```

Note that you can substitute

instead to execute code on the GPU. It's your choice, not the system's, and it will fail if your GPU can't handle OpenCL, so you need to handle this carefully. For this simple example, I just always use a CPU context.

Next, I load the OpenCL program into the context, and fetch the two kernels out of the program. The `CLFreqCountSourceString` function just returns an `NSString` containing the code to the two kernels:

```
        SMUGOpenCLProgram *program = [[SMUGOpenCLProgram alloc] initWithContext: context sourceString: CLFreqCountSourceString()];
        SMUGOpenCLKernel *freqCountKernel = [program kernelNamed: @"freqcount"];
        SMUGOpenCLKernel *freqSumKernel = [program kernelNamed: @"freqsum"];
```

I need to pass the buffers I created as arguments, but I can't pass them directly. Instead, I need to turn them into

objects. SMUGOpenCL makes this really easy:

```
        cl_mem dataCL = [data getOpenCLBufferForReadingInContext: context];
        cl_mem largeOutputCL = [largeOutput getOpenCLBufferForWritingInContext: context];
        cl_mem freqCountCL = [freqCount getOpenCLBufferForWritingInContext: context];
```

Next, I set the arguments for both kernels. This is a little tedious. In addition to the buffers, I also need to pass a block count in to the sum kernel, which I compute by just dividing the padded data length by 256:

```
        cl_int err;
        err = [freqCountKernel setArgument: 0 withSize: sizeof(dataCL) data: &dataCL;];
        if(err)
            ERROR("OpenCL error: %lld", (long long)err);
        err = [freqCountKernel setArgument: 1 withSize: sizeof(largeOutputCL) data: &largeOutputCL;];
        if(err)
            ERROR("OpenCL error: %lld", (long long)err);
        
        cl_uint sumCount = paddedLength / 256;
        err = [freqSumKernel setArgument: 0 withSize: sizeof(sumCount) data: &sumCount;];
        if(err)
            ERROR("OpenCL error: %lld", (long long)err);
        err = [freqSumKernel setArgument: 1 withSize: sizeof(largeOutputCL) data: &largeOutputCL;];
        if(err)
            ERROR("OpenCL error: %lld", (long long)err);
        err = [freqSumKernel setArgument: 2 withSize: sizeof(freqCountCL) data: &freqCountCL;];
        if(err)
            ERROR("OpenCL error: %lld", (long long)err);
```

Now it's finally time to run the kernels. In addition to the kernel to run, the context also wants a global and local work size. The global work size is just the number of work items to run, and is essentially the maximum number that

can return. The local work size is something I honestly don't quite understand, and I just use a SMUGOpenCL method to get a good size. The sizes are passed as arrays because some fancy stuff can be done (presumably for multi-dimensional data and such) by passing multiple values, but I only need one:

```
        size_t globalSizeCount[] = { paddedLength / 256 };
        size_t localSizeCount[] = { [context workgroupSizeForKernel: freqCountKernel] };
        [context enqueueKernel: freqCountKernel
            withWorkDimensions: 1
                globalWorkSize: globalSizeCount
                 localWorkSize: localSizeCount];
        
        size_t globalSizeSum[] = { 256 };
        size_t localSizeSum[] = { [context workgroupSizeForKernel: freqSumKernel] };
        [context enqueueKernel: freqSumKernel
            withWorkDimensions: 1
                globalWorkSize: globalSizeSum
                 localWorkSize: localSizeSum];
```

Now the kernels are running. Enqueueing the kernels just makes them eligible to run, but doesn't guarantee that they're finished, because they can run concurrent with your normal code. This could be useful for setting up computations and then doing something else while they crunch. Since the results here are needed right away, I just force the context to block until computation is complete:

```
        [context finish];
```

Now the results are sitting in

, except that they're incorrect due to padding. To fix this, I do a quick fix-up of the frequency count for zero:

```
        uint32_t *freqs = [freqCount mutableBytes];
        // compensate for the padding
        freqs[0] -= pad;
```

And finally, release allocated objects and return:

```
        [program release];
        [context release];
        
        return freqCount;
    }
```

And that's it! You can run the included test program to compute a frequency count on a file, and it produces identical results to the simple reference function.

**Conclusion**  
 OpenCL isn't too complicated to get started with, and SMUGOpenCL makes it especially easy. Performance might be trickier. With a CPU context, OpenCL was significantly slower than the non-OpenCL code for a single pass through the data. With some loops to force it to do more work, and reduce the overhead of OpenCL setup, the OpenCL version pulled ahead a bit. My Mac Pro's video card doesn't do OpenCL, so I didn't test GPU speed, but I'm going to guess that these kernels are not well adapted to the GPU. How to wrest the maximum speed out of OpenCL is beyond the scope of today's post. OpenCL is an exciting new technology, and much easier to get started with than doing general-purpose computation with OpenGL, and I hope that I've shown you enough to start experimenting on your own.

That's it for this week. Come back in another seven days for the next edition of Friday Q&A. Until then, keep sending your ideas for posts. Friday Q&A is driven by reader suggestions, so if you have a topic that you'd like to see covered here, [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
