---
title: Xgrid Programming Guide
apple_id: TP40006246
resource_type: Guide
platform: macOS
topic: Performance
technology: XgridFoundation
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/MacOSXServer/Conceptual/Xgrid_Programming_Guide/GettingStarted/GettingStarted.html
archived_at: '2026-07-15T08:16:40.483664Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xgrid Programming Guide](Introduction.md)


[Next](Using%20the%20Xgrid%20Command-Line%20Client.md)[Previous](Xgrid%20Overview.md)

# Getting Started with Xgrid

Writing a client application for Xgrid involves significant planning prior to writing your code. This chapter describes some things to consider when planning a project for Xgrid and shows you how to get started.

The first task is to assess whether your job is suitable for parallel processing with Xgrid. If a job can be broken into a series of independent tasks which can be performed in any order, or with simple order dependencies, it is generally suitable. If complex interdependencies exist between one computational task and another, or the tasks must be performed in linear order, it is generally not suitable.

You can specify minimal task dependencies when you submit a job. For example, you can specify that task D may not begin until tasks A, B, and C are complete. More complex dependencies, however, are better suited to a multiprocessing language such as MPI than to Xgrid.

The size of the data set being operated on also matters. If a great deal of processing is done on a small data set, the job is better suited to Xgrid than if a small amount of processing is done on a large data set—transferring the data may take more time than is saved by dividing the processing among multiple computers.

It is the responsibility of the client to break the job up into independently executable tasks, and to assemble the collection of executable files, as well as input and output files or directories, into a job submission. You’ll find the details of a job submission later in this document, but know for now that breaking the job into executable tasks—with any necessary files and directories—is part of the process.

The next step in the planning process is to assess what type of Xgrid is needed to perform the job in a reasonable amount of time. Some types of jobs can be performed well by a network of loosely connected computers; other jobs require shared access to network file servers, or even dedicated clusters sharing FDDI access to RAID arrays for reasonable efficiency.

The two most important factors in determining the type of Xgrid you need are the size the of the data set being operated on and the amount of processing to be done on the data set. For example, if you are doing a great deal of processing on a relatively small data set, the agents can be loosely connected—by Ethernet, Airport, or even the Internet. If a great deal of data must be processed by a relatively short algorithm, the time spent transferring the data may be greater than the time saved by dividing up the processing, unless shared access to data—or very fast data connections—are available.

A common task for Xgrid is video processing. Consider three kinds of job: compressing a short video to several bandwidths for Internet distribution, applying a filter to a long video, and compressing a large video for DVD in three formats: standard television, widescreen, and high definition.

Compressing a short video to several bandwidths can be accomplished simply over Ethernet, and may be practical even with Airport networking. Transferring the video to the agents takes only seconds or a few minutes, while the compression may take many minutes or an hour. Thus the job scales well with an agent assigned to compressing each bandwidth. The returned data is compressed, making its transfer somewhat more efficient.

Applying a simple filter to a long video, however, may require dedicated hardware to benefit from parallel processing at all. In principal, it is easy to divide the job into a parallel set of tasks: simply divide the frames by the number of agents and set each agent to process a set of frames. It may require more time to transfer each frame to and from the agent than it does to apply the filter, however, thus negating any time saving unless the agents share rapid access to the data via shared FDDI access to a RAID or a similar technology.

Compressing a long video to three data-intensive formats falls between these two extremes. The processing may take several hours for each format, so the time saved by parceling out the task to multiple agents is significant (a separate agent for compressing the audio may also save significant time), but the data transfer time is also significant: it may take hours just to send three copies of the video over the same Ethernet backbone. In this case, even though time can probably be saved by using a loosely connected set of agents, fast Ethernet connection is a minimum requirement for reasonable efficiency, and FDDI or a dedicated cluster sharing a RAID will deliver proportionately faster results.

If you have not already done so, install the Developer Tools or Xcode Tools that came with your copy of Mac OS X and locate the Xgrid folder (in the `Developer/Examples/` folder). Locate the GridSample and GridMandelbrot sample projects.

Before you begin coding, you should use the `xgrid` command-line tool, then compile and run the GridSample application to get a feel for how Xgrid works. See [Using the Xgrid Command-Line Client](Using%20the%20Xgrid%20Command-Line%20Client.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpinedanjnknlte), and [Building and Running GridSample](Building%20and%20Running%20GridSample.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3denbwfvbuqnjnknltc).

When you are ready to begin coding, start by creating a collection of executable files and submitting them as a job using the `xgrid` command line client. When your job is submitting and running properly, continue your code development by modifying the GridSample code, overriding the job specification method and modifying the user interface. This process is the best way to develop and debug the functional part of your code, and it may be all you need to do. Modifying GridSample is explained in detail in [Overriding the Job Specification Function](Overriding%20the%20Job%20Specification%20Function.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3denbwfvbuqnrnknltc).

To integrate Xgrid capability into an existing application or to create an Xgrid client from scratch, use the Cocoa API for Xgrid: Xgrid Foundation. The process is described in [Writing a Cocoa Xgrid Client](Writing%20a%20Cocoa%20Xgrid%20Client.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3denbwfvbuqnznknltc). Even if this is your intended goal, you will probably save time and effort by using the `xgrid` command-line client and modifying the GridSample code as part of the development process, before creating or modifying your own application using Xgrid Foundation.

[Next](Using%20the%20Xgrid%20Command-Line%20Client.md)[Previous](Xgrid%20Overview.md)

