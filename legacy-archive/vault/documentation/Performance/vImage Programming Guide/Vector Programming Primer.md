---
title: vImage Programming Guide
apple_id: TP30001001
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: Accelerate
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/vImage/VectorProgrammingPrimer/VectorProgrammingPrimer.html
archived_at: '2026-07-27T06:57:05.638157Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [vImage Programming Guide](Introduction%20to%20vImage%20Programming%20Guide.md)


[Next](Document%20Revision%20History.md)[Previous](Glossary.md)

# Vector Programming Primer

Vector programming is the programming paradigm that vImage uses to gain a performance benefit. This appendix explains how vector programming is able to achieve such benefits over traditional scalar programming.

With vector programming, multiple data elements (such as numbers) can be operated upon as one single unit – a vector. A vector can be thought of as an array that contains several elements, but unlike the array from traditional (or scalar) programming, all of the elements of the vector can be operated upon in a single instruction (as opposed to operating upon one array element at a time, as in scalar programming).

To better understand the significance of using vectors, you need to know how scalar code is processed by the CPU. Typically, when you program in a programming language (for example, C), the compiler converts the programming statements found in your source code files to a series of assembly instructions that the CPU can understand. These instructions usually consist of adding, subtracting, or multiplying two numbers together and storing the result somewhere in memory. [Figure A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrrgmwvgvzs) shows how a compiler could handle scalar code.

__Figure A-1__  Scalar code compilation example

（原归档配图未能恢复：`C_way.jpg`）

As shown in [Figure A-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrrgmwvgvzs), to multiply each element of the array by 2, it is necessary to iterate through the array and multiply each individual element by 2. You can see the suggested assembly code produced in the figure to the right. (Note: This assembly code is intentionally inaccurate to more easily illustrate this concept).

Vector programming works similarly. The compiler converts programming statements into a series of assembly instructions for performing arithmetic. The main difference is that data can be stored in a new data type called a `vector`. [Figure A-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambrfvbuqmrrgmwvgvzt) shows the previous operation, but done using vectorized code.

__Figure A-2__  Vector code compilation example

（原归档配图获取待重试：`Vec_way.jpg`）

When using vectorized code, to achieve the same goal of multiplying all of the numbers in the vector by 2, special operators exist that allow you to do this in one single instruction. This example uses `vec_mul` as our vector multiplication operator. Vector operator names change from processor to processor. This operator multiplies all elements in the vector, by a number (here, 2). This differs from the scalar example that iterates through the array and multiplies each number by 2.

When examining the assembly code produced by the vector version, you’ll notice that the end result is the same, but with less assembly code than the scalar version.

This optimization may seem minor in this trivial example, but when considering the pixel-per-pixel operations frequently used in image processing routines (and the many layers of arithmetic involved), the performance gains can be significant.

Despite the efficiency of vector programming, in practice it can be difficult to implement. Aside from getting used to the new data types involved, you need to rewrite algorithms with data parallelism in mind. You also want to consider what types of vector processors you plan to support because the code and build process will most likely differ.

The vImage framework is built on top of vector programming routines for several different architectures, enabling it to abstract the nuances of hardware-specific vector programming. This not only saves you programming time but also allows you to deploy the software on various system architectures (including those without a vector processor, such as the G3 architecture) with the same code.

[Next](Document%20Revision%20History.md)[Previous](Glossary.md)
