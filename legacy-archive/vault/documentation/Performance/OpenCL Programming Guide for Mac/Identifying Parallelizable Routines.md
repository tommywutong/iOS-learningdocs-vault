---
title: OpenCL Programming Guide for Mac
apple_id: TP40008312
resource_type: Guide
platform: macOS
topic: Performance
technology: OpenCL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Performance/Conceptual/OpenCL_MacProgGuide/IdentifyingParallelizableRoutines/IdentifyingParallelizableRoutines.html
archived_at: '2026-07-18T01:48:59.631126Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenCL Programming Guide for Mac](About%20OpenCL%20for%20OS%20X.md)


[Next](How%20the%20Kernel%20Interacts%20With%20Data%20in%20OS%20X%20OpenCL.md)[Previous](OpenCL%20On%20OS%20X%20Basics.md)

# Identifying Parallelizable Routines

This chapter provides a very basic introduction to how to design a program so that it can be implemented as an OpenCL kernel and called from an OpenCL host. For specifics about design patterns that may positively or negatively affect application performance, see [Tuning Performance On the GPU](Tuning%20Performance%20On%20the%20GPU.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmrsfvjvony) and [Improving Performance On the CPU](Improving%20Performance%20On%20the%20CPU.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqmjrgmwvgvzx).

The first step in using OpenCL to improve your application’s performance is to identify what portions of your application are appropriate for parallelization. Whereas in a general application you can spawn a separate thread for a task as long as the functions in the thread are re-entrant and you’re careful about how you synchronize data access, to achieve the level of parallelism for which OpenCL is ideal, it is much more important for the work items to be independent of each other. Although work items in the same workgroup can share local data, they execute synchronously and so no work item’s calculations depend on the result from another work item. Parallelization works only when the tasks that you run in parallel do not depend on each other.

For example, assume that you are writing a simple application that keeps track of the grades for students in a class. This application consists of two main tasks:

1. Compute the final grade for each student, assuming the final grade for each student is the average of all the grades that student received.
2. Obtain a class average by averaging the final grades of all students.

You cannot perform these two tasks in parallel because they are not independent of each other: to calculate the class average, you must first calculate the final grade for each student.

Although you cannot perform task 1 and task 2 simultaneously, there is still an opportunity for parallelization here.

The pseudocode in [Listing 4-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqojnknltg) proceeds through each student in the class, one by one, calculating the average of each student’s grades and caching it in the student object. Although this example computes each grade average one at a time, there’s no reason that the grade averages for all the students couldn’t be calculated at the same time. Because the grades of one student do not affect the grades of another, you can calculate the final grade for each student independently and at the same time instead of looping through the same set of instructions for each student, one at a time. This is the idea behind data parallelism.

__Listing 4-1__  Pseudocode that computes the final grade for each student

```

// Assume 'class' is a collection of 'student' objects.
foreach(student in class)
{
    // Assume getGrades() returns a collection of integer grades.
    grades = student.getGrades();

    sum = 0;
    count = 0;

    // Iterate through each grade, adding it to sum.
    foreach(grade in grades)
    {
        sum += grade;
        count++;
    }

    // Cache the average grade in the student object.
    student.averageGrade = sum / count;
}
```

Data parallelism consists of taking a single task (in this case, calculating a student’s average grade), and repeating it over multiple sets of data. No students’ grades affect another student’s grades. This means that you can calculate each student’s average in parallel.

To express this programmatically: first separate your task (calculating the final grade of a student) from your data (the list of students in the class). [Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqojnknlte) shows how you can isolate the final-grading task.

__Listing 4-2__  The isolated grade average task

```
task calculateAverageGradeForStudent( student )
{
    // Assume getGrades() returns a collection of integer grades.
    grades = student.getGrades();

    sum = 0;
    count = 0;

    // Iterate through each grade, adding it to sum.
    foreach(grade in grades)
    {
        sum += grade;
        count++;
    }

    // Store the average grade in the student object.
    student.averageGrade = sum / count;
}
```

Now that you have the task isolated, you need to apply it to the individual students in the class in parallel. Because OpenCL has native support for parallel computing, you can rewrite the task shown in [Listing 4-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjsfvbuqojnknlte) as an OpenCL kernel function. Using the OpenCL framework API, you can enqueue this kernel to run on a device where each compute unit on the device can apply an instance of the kernel (that is, a work item) to a different set of data.

The challenge in parallelizing your application is to identify the tasks that you can distribute across multiple compute units. Sometimes, as in this example, the identification is relatively trivial and requires few algorithmic changes. Other times, it might require designing a new algorithm from scratch that lends itself more readily to parallelization. Although there is no universal rule for parallelizing your application, there are a few tips you can keep in mind:

- Pay attention to loops.

  Often the opportunities for parallelization lie within a subroutine that is repeated over a range of results.
- Nested loops might be restructured as multi-dimensional parallel tasks.
- Find as many tasks as possible that do not depend on each other.

  Finding a group of routines that do not share memory or depend on each other’s results is usually a good indicator that you can perform them in parallel. If you have enough such tasks, you can consider writing a task-parallel OpenCL program.
- Due to the overhead of setting up a context and transferring data over a PCI bus, you must be processing a fairly large data set before you see any benefits from using OpenCL to process data in parallel. The exact point at which you start to see benefits depends on the OpenCL implementation and the hardware being used, so you will have to experiment to see how fast you can get your algorithm to execute. In general, a high ratio of computation to data access and lots of mathematical computations are good for OpenCL programs.

[Next](How%20the%20Kernel%20Interacts%20With%20Data%20in%20OS%20X%20OpenCL.md)[Previous](OpenCL%20On%20OS%20X%20Basics.md)

