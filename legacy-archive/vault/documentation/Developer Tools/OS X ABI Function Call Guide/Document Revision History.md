---
title: OS X ABI Function Call Guide
apple_id: TP40002521
resource_type: Guide
platform: macOS
topic: General
technology: null
published: '2010-11-17'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/LowLevelABI/995-Revision-2.3/history.html
archived_at: '2026-07-15T07:25:16.133498Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X ABI Function Call Guide](Introduction%20to%20OS%20X%20ABI%20Function%20Call%20Guide.md)


[Previous](x86-64%20Function%20Calling%20Conventions.md)

# Document Revision History

This table describes the changes to _OS X ABI Function Call Guide_.

| __Date__ | __Notes__ |
| 2010-11-17 | Updated links to the System V Application Binary Interface document. |
| 2009-02-04 | Made content corrections. |
| 2009-01-06 | Made minor content changes. |
|  | Corrected IA-32 function-result–return details. |
| 2007-04-04 | Added details about the OS X x86-64 environment. |
|  | Added cross-reference to System V x86-64 ABI document in [x86-64 Function Calling Conventions](x86-64%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tamzvfvjvomi). |
| 2006-11-07 | Clarified parameter-passing and floating-point operation details. |
|  | Clarified how parameters are passed in the parameter area in the PPC32 environment in [Stack Structure](32-bit%20PowerPC%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvomjz). |
|  | Clarified how arrays and structures are placed in the parameter area in the PPC64 environment in [Stack Structure](64-bit%20PowerPC%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinzrfvjvomjs). |
|  | Indicated how floating point operations are performed in the IA-32 environment in [IA-32 Function Calling Conventions](IA-32%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojsfvjvona). |
|  | Clarified how structures are returned in the IA-32 environment in [Returning Results](IA-32%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojsfvjvoni). |
| 2006-04-04 | Corrected description of natural alignment in the PPC and PPC64 architectures, and clarified stack-alignment details in the IA32 architecture. |
|  | Corrected the data types that yield better performance when using natural alignment in [32-bit PowerPC Function Calling Conventions](32-bit%20PowerPC%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimzyfvjvomrq) and [64-bit PowerPC Function Calling Conventions](64-bit%20PowerPC%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdinzrfvjvomju). |
|  | Specified that function callers are responsible for aligning the stack at 16-byte boundaries at the point of function calls in [IA-32 Function Calling Conventions](IA-32%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojsfvjvona). |
| 2006-01-10 | Specified when called functions remove parameters from the stack upon return in the OS X IA-32 ABI. |
|  | Updated [Passing Arguments](IA-32%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojsfvjvomy) and [Returning Results](IA-32%20Function%20Calling%20Conventions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojsfvjvoni) to describe how compiler-generated parameters are handled by called functions. |
| 2005-12-06 | Changed the alignment values and red zone limits for 64-bit programs to their correct values. |
| 2005-11-09 | New document that describes the function-calling conventions used in the architectures supported by OS X. Replaces information previously published in "PowerPC Runtime Architecture Guide." |

[Previous](x86-64%20Function%20Calling%20Conventions.md)

