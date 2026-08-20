---
title: Code Speed Performance Guidelines
apple_id: 10000150i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeSpeed/Articles/ImpedanceMismatch.html
archived_at: '2026-07-18T01:47:04.164583Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Speed Performance Guidelines](Introduction%20to%20Code%20Speed%20Performance%20Guidelines.md)


[Next](Perceived%20Responsiveness.md)[Previous](Check%20Your%20Algorithms.md)

# Impedance Mismatches

In electronics, an impedance mismatch refers to a mismatch between the output signal from one component and the input signal expected by another component. In programming, this term is used in a similar way to refer to a mismatch between data structures in your code.

Each library and framework typically defines its own data structures for managing information. When the framework exposes a function, it may also expose any custom data structures that are parameters or return values for that function. If you call that function in your code, you must pass it the data structure it is expecting to see. If you do not store a copy of that data structure in your own code, then you have to create it and populate it with information before making the function call.

Converting between system-defined data structures and any custom data structure formats used by your code wastes CPU time that could be spent doing other things. Before you write any code for your algorithms, carefully consider what data you need to operate on and design your data structures accordingly.

When you are getting ready to design your code and data structures, you should think carefully about how your code will interact with external code. If your algorithm calls for passing a particular data structure back and forth many times to an external library, you might want to design your algorithms to work directly with the data structures from that library.

As with any performance optimization, you should carefully consider whether matching the data structures of external frameworks is appropriate. Using the native data structure of an external library might give your code a slight speed boost in passing data back and forth, but if it slows down your algorithm it is a wasted gain. You should always measure the performance impact of any optimization you put in place and make sure it is an improvement rather than a regression.

Converting back and forth between integer and floating-point values can slow down performance, particularly on the G5 processor. On the G5, type conversions of this sort can cause bubbles in the instruction pipelines as the processor hits the L1 cache to convert the data. If your code currently performs these types of conversions, you should consider the following options instead:

- Avoid the conversions altogether by staying in one domain (either integer or floating-point).
- Use Velocity Engine (AltiVec), where type conversions are done in registers rather than in memory.
- Try compiling with the GCC `-fast` option. (Note that this option optimizes for the G5 processor by default. To optimize for G4 processors, you must also pass the `-mcpu=7450` option to GCC.)

One way to avoid type conversions altogether is to use a shadow variable. This technique is useful in situations where you would otherwise have to cast back and forth between types. Instead of casting, you create a duplicate variable of the needed type and use it in the same way as the other variable.

Listing 1 shows the use of a shadow variable in a simplified example. The original code would cast integer `i` to a `double` and then add it to `sum`. Rather than add integer `i` to `sum` during each loop iteration, the code maintains a shadow copy of `i` and adds that value to `sum`. The change resulted in code that was three times faster than the original version on a G5 processor.

__Listing 1__  Using shadow variables

```
double calculateDoublePrecisionSum(int numIterations)
{
    double sum = 0.0;
    int i;
    double i_fp; // shadow variable for i

    for (i = 0, i_fp = 0.0; i < numIterations; i++, i_fp++)
    {
        sum += i_fp;
    }

    return sum;
}
```


If your application is implemented using Cocoa, you can take advantage of the Core Foundation toll-free bridged types to improve performance of repetitive operations. Many methods in the Foundation Kit framework have equivalent functions in the Core Foundation framework. These equivalent functions can take either a Core Foundation type or a Foundation Kit object. Because function calls have a slight performance advantage over message dispatches, you might see a measurable gain by calling the Core Foundation function instead.

When substituting Core Foundation function calls for Foundation Kit methods, make sure that you handle any exceptional cases. Many Core Foundation functions are faster because they do not perform as much error checking as their Foundation Kit equivalents. Passing a null object to a Foundation Kit method may cause the method to return a null value back. Passing a null object to a Core Foundation function may cause a crash.

[Next](Perceived%20Responsiveness.md)[Previous](Check%20Your%20Algorithms.md)

