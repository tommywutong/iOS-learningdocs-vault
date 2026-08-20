---
title: Code Speed Performance Guidelines
apple_id: 10000150i
resource_type: Guide
platform: macOS
topic: Performance
technology: null
published: '2014-03-10'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/CodeSpeed/Articles/CheckAlgorithms.html
archived_at: '2026-07-18T01:46:46.077387Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Speed Performance Guidelines](Introduction%20to%20Code%20Speed%20Performance%20Guidelines.md)


[Next](Impedance%20Mismatches.md)[Previous](Diagnosing%20Slow%20Operations.md)

# Check Your Algorithms

Choosing the right algorithm for a task can have significant impacts on performance. If an algorithm doesn’t scale to the amount of data in the system, your application can appear slow and unresponsive. The following sections help you identify potential problems with your algorithms and things you can do to fix those problems.

While it is possible to choose the right algorithm right away, you’ll never know it’s the right one until you measure its performance under different load situations. You should always gather metrics for your code before you attempt to go back and tune any algorithms. Metrics tell you first and foremost _whether_ you have a performance problem. Only after you’ve determined there is a problem should you try to figure out the best way to fix it.

When you gather performance metrics, remember that the apparent speed of the operation is not the only measurement. Memory usage is another measurement to consider. If an operation allocates a lot of memory, it may not perform as well under low-memory conditions or when the system has to do a lot of paging. You should try running your application under these conditions and gather more data.

Sampling is one way to gather data for your application. Sampling tells you where your application is spending its time. For information on the available sampling tools, see [Finding Time-Consuming Operations](Diagnosing%20Slow%20Operations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrha3dsljzg4ztsoa).

Whenever you analyze sample data from your application, you should always try to differentiate between the cost of the function being called and the usage of that function. Suppose you sample your executable and determine that it is spending too much time in one particular function. This tells you something about the general location of a performance problem but does not tell you exactly where that problem lies. In this situation, there could be several possible reasons for time being spent in that function, including the following:

- The function could be poorly optimized.
- The parent function could be calling the child function more times than it really needs to. Thus, the parent function needs optimization.
- The thread may be blocked and the statistical sampling tool is seeing the function many times when in fact no code is actually executing.
- The function may be very fast but called at a regular interval that happens to match the sampling interval.

Keep in mind that even if a function has a high cost, it’s also possible that you can reduce its usage as well. Think about the design of your high-level algorithms and make sure that they are performing only those tasks that are absolutely required. Solving performance issues in your high-level algorithms can have a much greater impact than tuning individual functions. For example, eliminating a function call saves much more time than simply tuning that function.

The data mining features of Shark can help you view your data set in ways that might make it easier to see the real problems. Using the data mining features, you can remove symbols over which you have no control, such as those found in system libraries. Doing so applies the costs incurred by those symbols to the function that called them. This could point out places where your code is calling system routines too frequently. Reducing the number of system calls (or providing a different implementation) can significantly reduce the overall time spent in your own function.

For more information about Shark’s data mining features, see the Shark User Manual.

In operations involving anything other than small amounts of data, operations that involve quadratic or worse algorithms are generally a bad choice. Any time your algorithm speed scales at anything above a linear rate to the number of elements, you should reconsider the benefit of that algorithm.

When choosing an algorithm, it’s important to know the intended data set for that algorithm. If you’re dealing with a data set that contains anywhere from ten to ten million records, then it’s worth the time to code an algorithm with a linear or logarithmic performance. The effort to do so is worth the resulting performance gains. However, if you know you’ll always be dealing with a small number of records, the implementation time for a quadratic algorithm might make it more attractive than a more complex algorithm.

Whenever possible, avoid using the `system` function to execute strings in the local shell. The `system` function sends a string to the shell's command-line interpreter and is an expensive operation to perform from your own code. Depending on the features you need, it might be better to implement them directly in your code or see if there is a more direct way to get what you need. For example, you might see if the target program accepts socket-based connections or has an API to do what you need.

[Next](Impedance%20Mismatches.md)[Previous](Diagnosing%20Slow%20Operations.md)

